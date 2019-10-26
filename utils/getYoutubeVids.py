import requests
import json
from pytube import YouTube
import os

DOWNLOAD_PATH = '/home/andy/GitProjects/pupstep/dogsounds/'

def getVids():
    params = {
            'key': 'AIzaSyBaAZ9j2f6n1qv-RMoB-jEOAeRsqv5Ycjw', 
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
    for vidID in vidlist:
        YouTube(requestUrl+vidID).streams.filter(progressive=True, file_extension='mp4').first().download(output_path=DOWNLOAD_PATH)
        print('Successfully downloaded vid') 


def chopUpVids(mp4Filepaths):
    for vidFilepath in mp4Filepaths:
        print('process func here')



VideoIDList = getVids()
# downloadVids(VideoIDList)
vidFilePaths = [[os.path.join(root, name) for name in files] for root, _, files in os.walk(DOWNLOAD_PATH)]
print(vidFilePaths[0])


