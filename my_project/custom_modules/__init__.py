import os


# check if the 'data' folder already exists, otherwise create it
files_folders = os.listdir()

if 'data' not in files_folders:
    print("Creating 'data' folder")
    os.mkdir('data')
else:
    print("The 'data' folder already exists")


# create the sub-folders
os.makedirs("data/brand", exist_ok=True)