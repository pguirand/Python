from pytube import YouTube
import ffmpeg, os

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


url = "https://www.youtube.com/watch?v=sVPYIRF9RCQ&t=1s"
# url = get_video_from_url()

youtube_video = YouTube(url)

youtube_video.register_on_progress_callback(on_download_progress)


print("TITRE : " + youtube_video.title)
print("Nb Vues : " + str(youtube_video.views))

#Combiner video et audio flux
#Flux video 
streams = youtube_video.streams.filter(progressive=False, file_extension='mp4', type='video').order_by('resolution').desc()
video_stream = streams[0] # video avec la meilleure resolution

#Flux audio
streams = youtube_video.streams.filter(progressive=False, file_extension='mp4', type='audio').order_by('abr').desc()
audio_stream = streams[0]

print("Video Stream :", video_stream)
print("Audio Stream :", audio_stream)


print("Telchargement Video ...")
video_stream.download("video")
print("OK")

print("Telchargement Audio ...")
audio_stream.download("audio")
print("OK")

audio_filename = os.path.join("audio", video_stream.default_filename)
video_filename = os.path.join("video", video_stream.default_filename)
output_filename = video_stream.default_filename

print("Combinaison de Fichiers ...")
ffmpeg.output(ffmpeg.input(audio_filename), ffmpeg.input(video_filename), output_filename, vcodec="copy", acodec="copy", 
loglevel="quiet").run(overwrite_output=True)
print('OK')

