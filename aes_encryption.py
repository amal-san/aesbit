

file = open("1.png", "rb")  

byt = file.read()

print(type(byt))





for i in range(40):
	file2 = open("2.txt", "wb")

	file2.write(byt)


file2.close()	








class File():

	def __init__(self, name, extension,size):
		self.name = name
		self.extension = extension
		self.size = size


