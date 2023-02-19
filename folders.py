import os
import argparse

 

dlpath = "C:\\Users\\GSoukup\\Downloads"

os.chdir(dlpath)

 

parser = argparse.ArgumentParser(description='Processes the folder name from CLI. (i.e: W380923)',add_help=True, epilog='The actual script helps you create daily folders.\nIf you do NOT provide a folder name with -n optional NAME argument than you are asked to provide one. \n If you are using -n flag you can instantly provide the folder name.\n \n After creating folders, you can always decide to delete them if you have mistaken.\n')

parser.add_argument('-n',default='-', help="This is the foldername.")

args = parser.parse_args()

 

directory = args.n

 

print(f'The following argument given: {directory}\n')

 

"""

def makeDirs(name):

    name = input('Please provide a folder name:')

    os.mkdir()

 

"""

# Creating folder

parentDir = os.getcwd()

if directory == "-":

    directory = input('Please provide a folder name.\n')

 

path = os.path.join(parentDir,directory)

 

# Creating subfolders

issues,pstrmps,potig,remedy = "issues","pstrmps","potig","remedy"

 

pathissues = os.path.join(path,issues)

pathpstrmps = os.path.join(path,pstrmps)

pathpotig = os.path.join(path,potig)

pathremedy = os.path.join(path,remedy)

 

# Already existing?

if os.path.exists(path):

    os.rmdir(pathissues)

    os.rmdir(pathpstrmps)

    os.rmdir(pathpotig)

    os.rmdir(pathremedy)

    os.rmdir(path)

    print(f"\nEmpty folder ({directory}) deleted with the same name at the following path: {path}\n")

    input("Please approve.\n\n")

 

print(f"Current folder path:\n {path}\n")

 

# Making folders

os.mkdir(path)

print(f"Folder is created > '{directory}' at '{parentDir}'\n\n")

 

os.mkdir(pathissues)

print(f"Folder is created > '{issues}' at ''{path}'\n")

 

os.mkdir(pathpstrmps)

print(f"Folder is created > '{pstrmps}' at '{path}'\n")

 

os.mkdir(pathpotig)

print(f"Folder is created > '{potig}' at '{path}'\n")

 

os.mkdir(pathremedy)

print(f"Folder is created > '{remedy}' at '{path}'\n")

 

# Deleting subfolder, folders

wannaDel = input("\nPlease input you want to delete the new folder or not. y/n \n")

 

print(f"\nAnswered: '{wannaDel}' which is {type(wannaDel)}\n")

 

if wannaDel == "y":

    os.rmdir(pathissues)

    print(f"Folder '{pathissues}' is deleted.\n")

    os.rmdir(pathpstrmps)

    print(f"Folder '{pathpstrmps}' is deleted.\n")

    os.rmdir(pathpotig)

    print(f"Folder '{pathpotig}' is deleted.\n")

    os.rmdir(pathremedy)

    print(f"Folder '{pathremedy}' is deleted.\n")

    os.rmdir(path)

    print(f"Folder '{path}' is deleted.\n")

else:

    print("Folder(s) is/are NOT deleted.\n")
