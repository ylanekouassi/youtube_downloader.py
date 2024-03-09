#YOUTUBE DOWNLOADER

import pytube

url = input("Enter your URL: ")
yt = pytube.YouTube(url) #need a url as a parameter

stream = yt.streams.get_highest_resolution()
stream.download()