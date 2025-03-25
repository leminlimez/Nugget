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