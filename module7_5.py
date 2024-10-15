import os
import time

print(os.getcwd())
# print(os.walk(top))
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        filepath = os.path.join(r'C:\Users\Fox\Desktop\ProjectsPhyton\Urban\pythonProject1\Module 7')
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime('%d.%m.%Y %H:%M', time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(file)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, '
              f'Родительская директория: {parent_dir}')
