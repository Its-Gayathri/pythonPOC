file = open('C:\\Users\\HP Notebook\\Documents\\sample1.txt', 'w+')
file.write('this is first line\n')
file.write('this is 2nd line\n')
file.seek(0)
print(file.read())
file.close()

# Appending
file = open('C:\\Users\\HP Notebook\\Documents\\sample1.txt', 'a+')
file.write('this is 3rd line\n')
file.seek(0)
print(file.read())
file.close()
