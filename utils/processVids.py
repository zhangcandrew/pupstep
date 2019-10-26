import os
from scipy.io import wavfile
from defaults import DOWNLOAD_PATH
from getYoutubeVideos import VIDEO_FILE_PATHS

def processVids():
    vidsAsArray = []
    for file in VIDEO_FILE_PATH:
        fs, data = wavfile.read(file)
        vidsAsArray.append(data)
    return vidsAsArray

print(processVids())

