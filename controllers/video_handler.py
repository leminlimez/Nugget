import cv2
import os
import ffmpeg
from tempfile import mkdtemp, NamedTemporaryFile
from shutil import rmtree

ignore_pb_frame_limit = False

def set_ignore_frame_limit(value: bool):
    global ignore_pb_frame_limit
    ignore_pb_frame_limit = value

def convert_to_mov(input_file: str, output_file: str = None):
    # if there is no output file specified, create a temp file then return contents
    if output_file == None:
        tmpdir = mkdtemp()
        tmp = os.path.join(tmpdir, "vid.mov")
        convert_to_mov(input_file, tmp)
        with open(tmp, "rb") as tmpfile:
            contents = tmpfile.read()
        rmtree(tmpdir)
        return contents
    inp = ffmpeg.input(input_file)
    out = ffmpeg.output(inp, output_file, f='mov', vcodec='copy', acodec='copy')
    ffmpeg.run(out)

def get_thumbnail_from_mov(input_file: str, output_file: str = None):
    # if there is no output file specified, create a temp file and then return contents
    if output_file == None:
        tmpdir = mkdtemp()
        tmp = os.path.join(tmpdir, "thumb.png")
        get_thumbnail_from_mov(input_file, tmp)
        with open(tmp, "rb") as tmpfile:
            contents = tmpfile.read()
        rmtree(tmpdir)
        return contents

    inp = ffmpeg.input(input_file, ss=0)
    out = ffmpeg.output(inp, output_file, vframes=1)
    ffmpeg.run(out)

def get_thumbnail_from_contents(contents: bytes, output_file: str = None):
    with NamedTemporaryFile("rb+", suffix=".mov") as inp_file:
        inp_file.write(contents)
        contents = get_thumbnail_from_mov(inp_file.name, output_file)
    return contents

def create_caml(video_path: str, output_file: str, auto_reverses: bool, update_label=lambda x: None):
    cam = cv2.VideoCapture(video_path)
    assets_path = os.path.join(output_file, "assets")
    frame_count = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))
    FRAME_LIMIT = 400
    reverse = 0
    if auto_reverses:
        reverse = 1
    if not ignore_pb_frame_limit and frame_count > FRAME_LIMIT:
        raise Exception(f"Videos must be under {FRAME_LIMIT} fps to loop. Either reduce the frame rate or make it shorter.")
    try:
        # creating a folder named data
        if not os.path.exists(assets_path): 
            os.makedirs(assets_path, exist_ok=True) 
    # if not created then raise error
    except OSError:
        print ('Error: Creating directory of data')
    
    # frame
    currentframe = 0
    width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    with open(os.path.join(output_file, "main.caml"), "w") as caml:
        # write caml header
        fps = cam.get(cv2.CAP_PROP_FPS)
        duration = frame_count / fps
        caml.write(f"""<?xml version="1.0" encoding="UTF-8"?>

<caml xmlns="http://www.apple.com/CoreAnimation/1.0">
  <CALayer allowsEdgeAntialiasing="1" allowsGroupOpacity="1" bounds="0 0 {width} {height}" contentsFormat="RGBA8" cornerCurve="circular" hidden="0" name="_FLOATING" position="{int(width/2)} {int(height/2)}">
    <sublayers>
      <CATransformLayer allowsEdgeAntialiasing="1" allowsGroupOpacity="1" allowsHitTesting="1" bounds="0 0 {width} {height}" contentsFormat="RGBA8" cornerCurve="circular" name="Chip" position="{int(width/2)} {int(height/2)}">
	<sublayers>
	  <CALayer allowsEdgeAntialiasing="1" allowsGroupOpacity="1" bounds="0 0 {width} {height}" contentsFormat="RGBA8" cornerCurve="circular" name="CALayer1" position="{int(width/2)} {int(height/2)}">
	    <contents type="CGImage" src="assets/0.jpg"/>
	    <animations>
	      <animation type="CAKeyframeAnimation" calculationMode="linear" keyPath="contents" beginTime="1e-100" duration="{duration}" removedOnCompletion="0" repeatCount="inf" repeatDuration="0" speed="1" timeOffset="0" autoreverses="{reverse}">
		<values>\n""")
        while(True):
            # reading from frame 
            ret,frame = cam.read() 
        
            if ret: 
                # if video is still left continue creating images 
                name = 'assets/' + str(currentframe) + '.jpg'
                if update_label:
                    update_label('Creating...' + name)
                print('Creating...' + name)
        
                # writing the extracted images
                cv2.imwrite(os.path.join(output_file.removeprefix(u"\\\\?\\"), name), frame)
                caml.write(f"\t\t\t<CGImage src=\"{name}\"/>\n")
        
                # increasing counter so that it will
                # show how many frames are created
                currentframe += 1
            else:
                break
        caml.write("""		</values>
	      </animation>
	    </animations>
	  </CALayer>
	</sublayers>
      </CATransformLayer>
    </sublayers>
    <states>
      <LKState name="Locked">
	<elements/>
      </LKState>
      <LKState name="Unlock">
	<elements/>
      </LKState>
      <LKState name="Sleep">
	<elements/>
      </LKState>
    </states>
    <stateTransitions>
      <LKStateTransition fromState="*" toState="Unlock">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="Unlock" toState="*">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="*" toState="Locked">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="Locked" toState="*">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="*" toState="Sleep">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="Sleep" toState="*">
	<elements/>
      </LKStateTransition>
    </stateTransitions>
  </CALayer>
</caml>
""")
    
    # Release all space and windows once done
    cam.release()
    cv2.destroyAllWindows()

    # Write the other caml
    with open(os.path.join(output_file, "index.xml"), "w") as index:
        index.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>assetManifest</key>
	<string>assetManifest.caml</string>
	<key>documentHeight</key>
	<real>{height}</real>
	<key>documentResizesToView</key>
	<true/>
	<key>documentWidth</key>
	<real>{width}</real>
	<key>dynamicGuidesEnabled</key>
	<true/>
	<key>geometryFlipped</key>
	<false/>
	<key>guidesEnabled</key>
	<true/>
	<key>interactiveMouseEventsEnabled</key>
	<true/>
	<key>interactiveShowsCursor</key>
	<true/>
	<key>interactiveTouchEventsEnabled</key>
	<false/>
	<key>loopEnd</key>
	<real>0.0</real>
	<key>loopStart</key>
	<real>0.0</real>
	<key>loopingEnabled</key>
	<false/>
	<key>multitouchDisablesMouse</key>
	<false/>
	<key>multitouchEnabled</key>
	<false/>
	<key>presentationMouseEventsEnabled</key>
	<true/>
	<key>presentationShowsCursor</key>
	<true/>
	<key>presentationTouchEventsEnabled</key>
	<false/>
	<key>rootDocument</key>
	<string>main.caml</string>
	<key>savesWindowFrame</key>
	<false/>
	<key>scalesToFitInPlayer</key>
	<true/>
	<key>showsTouches</key>
	<true/>
	<key>snappingEnabled</key>
	<true/>
	<key>timelineMarkers</key>
	<string>[(null)]</string>
	<key>touchesColor</key>
	<string>1 1 0 0.8</string>
	<key>unitsInPixelsInPlayer</key>
	<true/>
</dict>
</plist>
""")