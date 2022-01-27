with open('C:\\Users\\HP Notebook\\Documents\\sample.txt', 'r') as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)