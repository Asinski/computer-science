import os


def search_file(path, name):
    for i in os.listdir(path):
        if i == name:
            print("Путь к файлу:", path)
        elif os.path.isdir(fr"{path}\\{i}"):
            search_file(fr"{path}\\{i}", name)


path = input()
name = input()
search_file(path, name)