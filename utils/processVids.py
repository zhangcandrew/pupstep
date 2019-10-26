import os
from scipy.io import wavfile
from defaults import DOWNLOAD_PATH, VIDEO_FILE_PATHS, PROCESSED_VIDEOS_PATH, SOUND_FILES_PATH

def processVids():
    vidsAsArray = []
    if not os.path.exists(SOUND_FILES_PATH):  
        os.makedirs(SOUND_FILES_PATH)
    
    for filename in VIDEO_FILE_PATHS[0]:
        if not os.path.exists(os.path.join(SOUND_FILES_PATH, os.path.splitext(os.path.basename(filename))[0]+'.wav')): 
            os.system('ffmpeg -i \'{}\' -acodec pcm_s16le -ar 16000 \'{}.wav\''.format(filename, os.path.join(SOUND_FILES_PATH, os.path.splitext(os.path.basename(filename))[0] ))) 

    for root, _, filen in os.walk(SOUND_FILES_PATH):
        for soundfile in filen:
            fs, data = wavfile.read(os.path.join(root, soundfile))
            vidsAsArray.append(data)
   
    for item in vidsAsArray:
        print(item.shape)
    return vidsAsArray

print(processVids())
