from pytube import YouTube

# En cas de problemes installer le pytube ou autre
# module directement dans le /usr/bin/"version python"
# /usr/bin/python3.9 -m pip install git+https://github.com/pytube/pytube

# url = "https://www.youtube.com/watch?v=9bZkp7q19f0"
BASE_YOUTUBE_URL = "https://www.youtube.com"


def get_video_from_url():
    url = input("Entrer l'URL de la video a telecharger : \n")
    #verifier que url commence par "https://www.youtube.com"
    # if url[:len(BASE_YOUTUBE_URL)]== BASE_YOUTUBE_URL:
    #ou encore
    if url.lower().startswith(BASE_YOUTUBE_URL):
        return url
    print("ERREUR : Vous devez entrer une URL Youtube valide")
    return get_video_from_url() #recursive


def on_download_progress(stream, chunk, bytes_remaining):
    bytes_download = stream.filesize - bytes_remaining
    percent = bytes_download * 100 / stream.filesize
    print(f"Progression du telechargement {int(percent)} %")


def get_video_stream_itag_from_user(streams):
    index =1
    print()
    print("CHOIX DES RESOLUTIONS")
    for stream in streams:#.fmt_streams:
        print(f"{index} - {stream.resolution}")# - {stream.itag}
        index += 1
    while True:
        resol_num = input("CHoisissez la resolution : \n")
        if resol_num == "":
            print("ERREUR : Vous devez rentrer un nombre")
        else:
            try:
                resol_num_int = int(resol_num)
            except:
                print("ERREUR : Vous devez rentrer un nombre")
            else:
                if not 1 <= resol_num_int <= len(streams):
                    print(f"Vous devez entrer un nombre entre 1 et {len(streams)}")
                else:
                    break
    itag = streams[resol_num_int-1].itag
    return itag


# url = "https://www.youtube.com/watch?v=sVPYIRF9RCQ&t=1s"
url = get_video_from_url()

youtube_video = YouTube(url)

youtube_video.register_on_progress_callback(on_download_progress)


print("TITRE : " + youtube_video.title)
print("Nb Vues : " + str(youtube_video.views))

streams = youtube_video.streams.filter(progressive=True, file_extension='mp4')
itag = get_video_stream_itag_from_user(streams)
print("Itag : ", itag)

stream = youtube_video.streams.get_by_itag(itag)
# ou encore 
# stream = youtube_video.streams.get_highest_resolution()
print("stream video : ", stream)
print("Telchargement...")
stream.download()
print("OK")


