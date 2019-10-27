import os

DOWNLOAD_PATH = '/home/andy/GitProjects/pupstep/dogsounds/unprocessed'
API_KEY=str(open('API_KEY.txt', 'r').read())
VIDEO_FILE_PATHS = [[os.path.join(root, name) for name in files] for root, _, files in os.walk(DOWNLOAD_PATH)]
PROCESSED_VIDEOS_PATH = '/home/andy/GitProjects/pupstep/dogsounds/processed/wavvideos'
SOUND_FILES_PATH = '/home/andy/GitProjects/pupstep/dogsounds/processed/soundfiles/'
