import requests
import json
from pytube import YouTube
import os
from defaults import API_KEY, DOWNLOAD_PATH


def getVids():
    params = {
            'key': API_KEY.strip(), 
            'part': 'snippet',
            'q': 'dog+barking+compilation',
            }
    url = 'https://www.googleapis.com/youtube/v3/search'
    response = requests.get(url, params)
    jsonResponseVids = json.loads(response.text)
    videoIDs = [video['id']['videoId'] for video in jsonResponseVids['items']]
    return videoIDs


def downloadVids(vidlist):
    requestUrl = 'https://youtu.be/'
    
    if not os.path.exists(DOWNLOAD_PATH):
        os.mkdir(DOWNLOAD_PATH)

    for vidID in vidlist:
        YouTube(requestUrl+vidID).streams.filter(progressive=True, file_extension='mp4').first().download(output_path=DOWNLOAD_PATH)
        print('Successfully downloaded vid') 


VideoIDList = getVids()
downloadVids(VideoIDList)
VIDEO_FILE_PATHS = [[os.path.join(root, name) for name in files] for root, _, files in os.walk(DOWNLOAD_PATH)]

print('Finished downloading 5 vids at path ', DOWNLOAD_PATH)

