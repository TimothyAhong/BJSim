import os
print os.getcwd()
f = open("test.txt","a")
f2 = open("test2.txt","a")

f.write("line1\n")
f.write("line2\n")
f2.write("lino1\n")
f2.write("lino2\n")
f.close()
f2.close()
