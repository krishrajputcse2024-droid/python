st = "hey how are you"

f = open("myfile.txt", "a")
data = f.write(st)
print(data)
f.close()