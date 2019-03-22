#DECLARE name : ARRAY[0:6] OF STRING
name = [0,0,0,0,0,0]

no_names = 0
fh = open("File.py")
line = fh.readline()
while line != "":
    name[no_names] = line
    no_names = no_names + 1
    line = fh.readline()

print("There are ", no_names , "names.")

for index in range(0,no_names):
    print(name[index])