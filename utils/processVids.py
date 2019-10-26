import os
from scipy.io import wavfile
from defaults import DOWNLOAD_PATH, VIDEO_FILE_PATHS, PROCESSED_VIDEOS_PATH, SOUND_FILES_PATH

def processVids():
    vidsAsArray = []
    for filename in VIDEO_FILE_PATHS[0]:
        if not os.path.exists(SOUND_FILES_PATH):
            os.makedirs(SOUND_FILES_PATH)
            os.system('ffmpeg -i {} -acodec pcm_s16le -ar 16000 {}.wav'.format(filename, os.path.join(os.basename(SOUND_FILES_PATH, os.path.basename(filename))))) 
        print(filename)
        fs, data = wavfile.read(filename)
        vidsAsArray.append(data)
    return vidsAsArray

print(processVids())
