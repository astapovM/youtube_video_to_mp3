from pytube import YouTube
import time

path_for_music = '/home/infected/Рабочий стол/music from youtube'
while True:
    video = input('Введите ссылку на видео для конвертации в мп3 формат >>> ')

    if "https://www.youtube" not in video:
        print("Введите правильную ссылку на видео")
    else:
        start = time.time()
        yt = YouTube(video)
        print(yt.title)
        print(yt.thumbnail_url)
        print(yt.streams.filter(only_audio=True))
        stream = yt.streams.get_by_itag(140)
        stream.download(output_path=path_for_music, filename=f'{yt.title}.mp3')

        print('[INFO] COMPLETE!')
        end = time.time() - start
        print(end)
        break
