st = "hey how are you"

f = open("myfile.txt", "w")
data = f.write(st)
print(data)
f.close()