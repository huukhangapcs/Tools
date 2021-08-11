import subprocess
import glob

files = glob.glob("*.mp4")
for file in files:
    wav_file = file.replace(".mp4",".wav")
    command = "ffmpeg -i %s -ab 160k -ac 2 -ar 44100 -vn %s" % (file,wav_file)
    subprocess.call(command, shell=True)

