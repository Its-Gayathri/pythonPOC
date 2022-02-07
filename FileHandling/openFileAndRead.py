file = open("C:\\Users\\HP Notebook\\Documents\\sample.txt", "r")
for each in file:
    print(each)

# using file.read()
file = open("C:\\Users\\HP Notebook\\Documents\\sample.txt", "r")
print('using file.read')
print(file.read())

# reading first 6 characters
file = open("C:\\Users\\HP Notebook\\Documents\\sample.txt", "r")
print('reading first 6 characters')
print(file.read(6))

# Reading first and last line
file = open("C:\\Users\\HP Notebook\\Documents\\sample.txt", "r")
print('First Line:')
print(file.readline())
print('Last Line:')
for last_line in file:
    pass
print(last_line)