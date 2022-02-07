import os


def read_text_file(filePath):
    fileContent = open(filePath, 'r')
    print(fileContent.read())


directory = 'C:\\Users\\HP Notebook\\Documents\\sampleFolder'
os.chdir(directory)
for file in os.listdir():
    if file.endswith('.txt'):
        read_text_file(file)
