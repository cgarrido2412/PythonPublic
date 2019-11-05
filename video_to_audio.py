#pip install moviepy
import moviepy.editor as mp
video = mp.VideoFileClip("SampleVideo.mp4")
video.audio.write_audiofile("SampleAudio.mp3")
