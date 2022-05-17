

class OpenFile:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_val, exc_tb)
        if self.file:
            self.file.close()
        return True


with OpenFile('temp.txt', 'r') as file:
    print('Start reading file')
    print(file.read())


# Розширити атрибути класу та добавити перевірку на помилки при закритті файлу
