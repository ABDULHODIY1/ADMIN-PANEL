from pytube import YouTube
YouTube('https://youtu.be/RpdfCHbLz-c').streams.first().download()
# yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
# yt.streams
#
# filter(progressive=True, file_extension='mp4')