from xml.dom.minidom import DocumentType

# Python code to convert video to audio
import moviepy.editor as mp

# Insert Local Video File Path
clip = mp.VideoFileClip(r"Video File")

# Insert Local Audio File Path
clip.audio.write_audiofile(r"Audio File")

