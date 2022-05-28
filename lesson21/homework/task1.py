class OpenFile:
    counter = 0

    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        OpenFile.counter += 1
        print('Start reading file')
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            print(f'Closing context, number of contexts is {self.counter}')
        self.file.close()


# with OpenFile('test.txt', 'r') as file:
#     print(file.read())

# Розширити атрибути класу та добавити перевірку на помилки при закритті файлу
