import time


def read_file_timed(file):
    """Возвращает содержимое файла и измеряет требуемое время."""
    start_time = time.time()
    try:
        f = open(file, 'rb')
    except FileNotFoundError:
        print(f'[Errno 2] No such file or directory: {file}')
    else:
        finish_time = time.time()
        result = finish_time - start_time
        print(f'Time required for {file} = {result}')
        f.close()
    finally:
        print('Финал')

video_data = read_file_timed('myfile1.bin')  # 155 MB
# Time required for video.mp4 = 0.06553506851196289

# попытка считать отсутствующий файл
video_data = read_file_timed('file_not_exist.mp4')  # 155 MB
# FileNotFoundError: [Errno 2] No such file or directory: 'video2.mp4'