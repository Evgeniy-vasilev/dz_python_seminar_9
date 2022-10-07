# Загрузчик видео с YouTube (в видео и аудио версиях)

# Привет! Смог добраться до дз только в пятницу. Пока разобрался только так...
import pytube

url = input('Введите url: ')
yt = pytube.YouTube(url)
path = input('Введите путь к папке для скачивания: ')
print()

print(yt.thumbnail_url)
print(yt.title)
print()

for i in yt.streams.filter(file_extension='mp4'):
    print(i)

it = int(input('Введите itag для скачивания: '))
stream = yt.streams.get_by_itag(it)
stream.download(path)

print('Скачивание завершено!')
