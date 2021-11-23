data = data2 = ""
with open('file1.txt') as f:
    data = f.readline()
with open('file2.txt') as f:
    data2 = f.readline()
data += "\n"
data += data2
with open ('file3.txt', 'w') as f:
    f.write(data)
