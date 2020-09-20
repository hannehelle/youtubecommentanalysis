import time
from utilits import get_video_id
from create_data import all_data
from write_xls import write_xls

start = time.time()
print("Программа начала работу, ", start)
video_link = input("Введите ссылку:")
video_id = get_video_id(video_link)
data = all_data(video_id)
write_xls(video_id, data)
end = time.time()
print("Время работы всей программы: ", end - start)