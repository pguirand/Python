from pytube import YouTube
import ffmpeg, os


def on_download_progress(stream, chunk, bytes_remaining):
    bytes_download = stream.filesize - bytes_remaining
    percent = bytes_download * 100 / stream.filesize
    print(f"Progression du telechargement {int(percent)} %")


def download_video(url):
    youtube_video = YouTube(url)
    youtube_video.register_on_progress_callback(on_download_progress)


    # print("TITRE : " + youtube_video.title)
    # print("Nb Vues : " + str(youtube_video.views))

    #Combiner video et audio flux
    #Flux video 
    streams = youtube_video.streams.filter(progressive=False, file_extension='mp4', type='video').order_by('resolution').desc()
    video_stream = streams[0] # video avec la meilleure resolution

    #Flux audio
    streams = youtube_video.streams.filter(progressive=False, file_extension='mp4', type='audio').order_by('abr').desc()
    audio_stream = streams[0]

    # print("Video Stream :", video_stream)
    # print("Audio Stream :", audio_stream)


    print(f"Telchargement - {youtube_video.title} ...")
    video_stream.download("video")
    # print("OK")

    # print("Telchargement Audio ...")
    audio_stream.download("audio")
    # print("OK")

    audio_filename = os.path.join("audio", video_stream.default_filename)
    video_filename = os.path.join("video", video_stream.default_filename)
    output_filename = video_stream.default_filename

    # print("Combinaison de Fichiers ...")
    ffmpeg.output(ffmpeg.input(audio_filename), ffmpeg.input(video_filename), output_filename, vcodec="copy", acodec="copy", 
    loglevel="quiet").run(overwrite_output=True)
    print('OK')

    #supprimer les repertoires videos et audios apres utilisation

    os.remove(audio_filename)
    os.remove(video_filename)
    os.rmdir("audio")
    os.rmdir("video")
    

