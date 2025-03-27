import cv2
import os
import ffmpeg
from tempfile import NamedTemporaryFile

import ffmpeg.stream
import ffmpeg.video

def convert_to_mov(input_file: str, output_file: str = None):
    # if there is no output file specified, create a temp file then return contents
    if output_file == None:
        with NamedTemporaryFile("rb+", suffix=".mov") as tmp:
            convert_to_mov(input_file, tmp)
            contents = tmp.read()
        return contents
    (
        ffmpeg
        .input(input_file)
        .output(output_file, vcodec='copy', acodec='copy', format='mov')
        .run()
    )

def get_thumbnail_from_mov(input_file: str, output_file: str = None):
    # if there is no output file specified, create a temp file and then return contents
    if output_file == None:
        with NamedTemporaryFile("rb+", suffix=".heic") as tmp:
            get_thumbnail_from_mov(input_file, tmp)
            contents = tmp.read()
        return contents
    (
        ffmpeg
        .input(input_file, ss=0)
        .output(output_file, vframes=1, format='heic')
        .run()
    )

def get_thumbnail_from_contents(contents: bytes, output_file: str = None):
    with NamedTemporaryFile("rb+", suffix=".heic") as inp_file:
        inp_file.write(contents)
        contents = get_thumbnail_from_mov(inp_file, output_file)
    return contents

def create_caml(video_path: str, output_file: str, update_label=lambda x: None):
    cam = cv2.VideoCapture(video_path)
    assets_path = os.path.join(output_file, "assets")
    try:
        # creating a folder named data
        if not os.path.exists(assets_path): 
            os.makedirs(assets_path) 
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
        frame_count = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))
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
	      <animation type="CAKeyframeAnimation" calculationMode="linear" keyPath="contents" beginTime="1e-100" duration="{duration}" removedOnCompletion="0" repeatCount="inf" repeatDuration="0" speed="1" timeOffset="0">
		<values>\n""")
        while(True):
            # reading from frame 
            ret,frame = cam.read() 
        
            if ret: 
                # if video is still left continue creating images 
                name = 'assets/' + str(currentframe) + '.jpg'
                if update_label:
                    update_label('Creating...' + name)
                else:
                    print ('Creating...' + name)
        
                # writing the extracted images
                cv2.imwrite(os.path.join(output_file, name), frame)
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
      <LKState name="Sleep PortraitUp Light">
	<elements/>
      </LKState>
      <LKState name="Lock PortraitUp Light">
	<elements/>
      </LKState>
      <LKState name="Home PortraitUp Light">
	<elements/>
      </LKState>
      <LKState name="Sleep LandscapeLeft Light" basedOn="Sleep PortraitUp Light">
	<elements/>
      </LKState>
      <LKState name="Lock LandscapeLeft Light">
	<elements/>
      </LKState>
      <LKState name="Home LandscapeLeft Light" basedOn="Home PortraitUp Light">
	<elements/>
      </LKState>
      <LKState name="Sleep PortraitDown Light" basedOn="Sleep PortraitUp Light">
	<elements/>
      </LKState>
      <LKState name="Lock PortraitDown Light">
	<elements/>
      </LKState>
      <LKState name="Home PortraitDown Light" basedOn="Home PortraitUp Light">
	<elements/>
      </LKState>
      <LKState name="Sleep LandscapeRight Light" basedOn="Sleep PortraitUp Light">
	<elements/>
      </LKState>
      <LKState name="Lock LandscapeRight Light">
	<elements/>
      </LKState>
      <LKState name="Home LandscapeRight Light" basedOn="Home PortraitUp Light">
	<elements/>
      </LKState>
      <LKState name="Sleep PortraitUp Dark" basedOn="Sleep PortraitUp Light">
	<elements/>
      </LKState>
      <LKState name="Lock PortraitUp Dark">
	<elements/>
      </LKState>
      <LKState name="Home PortraitUp Dark" basedOn="Home PortraitUp Light">
	<elements/>
      </LKState>
      <LKState name="Sleep LandscapeLeft Dark" basedOn="Sleep PortraitUp Light">
	<elements/>
      </LKState>
      <LKState name="Lock LandscapeLeft Dark">
	<elements/>
      </LKState>
      <LKState name="Home LandscapeLeft Dark" basedOn="Home PortraitUp Light">
	<elements/>
      </LKState>
      <LKState name="Sleep PortraitDown Dark" basedOn="Sleep PortraitUp Light">
	<elements/>
      </LKState>
      <LKState name="Lock PortraitDown Dark">
	<elements/>
      </LKState>
      <LKState name="Home PortraitDown Dark" basedOn="Home PortraitUp Light">
	<elements/>
      </LKState>
      <LKState name="Sleep LandscapeRight Dark" basedOn="Sleep PortraitUp Light">
	<elements/>
      </LKState>
      <LKState name="Lock LandscapeRight Dark">
	<elements/>
      </LKState>
      <LKState name="Home LandscapeRight Dark" basedOn="Home PortraitUp Light">
	<elements/>
      </LKState>
    </states>
    <stateTransitions>
      <LKStateTransition fromState="*" toState="Sleep PortraitUp Light">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="Sleep PortraitUp Light" toState="*">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="*" toState="Lock PortraitUp Light">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="Lock PortraitUp Light" toState="*">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="*" toState="Home PortraitUp Light">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="Home PortraitUp Light" toState="*">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="*" toState="Sleep LandscapeLeft Light">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="Sleep LandscapeLeft Light" toState="*">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="*" toState="Lock LandscapeLeft Light">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="Lock LandscapeLeft Light" toState="*">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="*" toState="Home LandscapeLeft Light">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="Home LandscapeLeft Light" toState="*">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="*" toState="Sleep PortraitDown Light">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="Sleep PortraitDown Light" toState="*">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="*" toState="Lock PortraitDown Light">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="Lock PortraitDown Light" toState="*">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="*" toState="Home PortraitDown Light">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="Home PortraitDown Light" toState="*">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="*" toState="Sleep LandscapeRight Light">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="Sleep LandscapeRight Light" toState="*">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="*" toState="Lock LandscapeRight Light">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="Lock LandscapeRight Light" toState="*">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="*" toState="Home LandscapeRight Light">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="Home LandscapeRight Light" toState="*">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="*" toState="Sleep PortraitUp Dark">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="Sleep PortraitUp Dark" toState="*">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="*" toState="Lock PortraitUp Dark">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="Lock PortraitUp Dark" toState="*">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="*" toState="Home PortraitUp Dark">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="Home PortraitUp Dark" toState="*">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="*" toState="Sleep LandscapeLeft Dark">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="Sleep LandscapeLeft Dark" toState="*">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="*" toState="Lock LandscapeLeft Dark">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="Lock LandscapeLeft Dark" toState="*">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="*" toState="Home LandscapeLeft Dark">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="Home LandscapeLeft Dark" toState="*">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="*" toState="Sleep PortraitDown Dark">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="Sleep PortraitDown Dark" toState="*">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="*" toState="Lock PortraitDown Dark">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="Lock PortraitDown Dark" toState="*">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="*" toState="Home PortraitDown Dark">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="Home PortraitDown Dark" toState="*">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="*" toState="Sleep LandscapeRight Dark">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="Sleep LandscapeRight Dark" toState="*">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="*" toState="Lock LandscapeRight Dark">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="Lock LandscapeRight Dark" toState="*">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="*" toState="Home LandscapeRight Dark">
	<elements/>
      </LKStateTransition>
      <LKStateTransition fromState="Home LandscapeRight Dark" toState="*">
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