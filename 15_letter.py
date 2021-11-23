f=open("15_letter.txt", "r+")
a=f.read(15)
print "First 15 letters: ",a
f=open("15_letter.txt", "wb")
f.write( "Hey hello this is my second assignment.");
f.close()
