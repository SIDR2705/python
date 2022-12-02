import os

def Delete_File(FileName):
	if(os.path.exists(FileName)):
		size=os.path.getsize(FileName)
		if(size==0):
			os.remove(FileName)
		else:
			print("Are you sure to delete file ? Y/N ")
			option=input()
			if(option=="y" or option == "Y"):
				os.remove(FileName)
			else:
				print("File deletion process stopped.")


	else:
		print("File is no existing")
		return

def main():
	print("Enter the file name :")
	Name=input()

	Delete_File(Name)

if __name__=="__main__":
	main()
