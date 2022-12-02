from sys import *
from os import *

def Script_Task(No):
    if((No%2)==0):
        print("{} is Even Number".format(argv[1]))
    else:
        print("{} is Odd Number".format(argv[1]))


def main():
    print("---------------Automations---------------")
    
    print("Automation Script started with name : ",argv[0])

    if(len(argv)!=2):
        print("Error: Insufficient arguments")
        print("Use -h for help and -u for usage of the script")
        exit()

    if((argv[1]=="-h" or argv[1]=="-H")):
        print("Help: This script is used to perform __________")
        exit()

    elif ((argv[1]== "-u") or (argv[1]== "-U")):
        print("Usage : Provide _________ number of arguments as")
        print("First Arugment as : __________")
        print("Second Arugment as : __________")
        exit()

    else:
        Script_Task(int(argv[1]))

if __name__=="__main__":
    main()