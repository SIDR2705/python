import os

def CreateFile(FileName):

	if(os.path.exists(FileName)):
		print("File Already Exsist")
		return
	else:
		fd=open(FileName,"w")

def main():
	print("Enter the file name to create :")
	argv[1]=input()

	CreateFile(Name)

if __name__=="__main__":
	main()