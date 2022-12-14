import os


# check if the 'data' folder already exists, otherwise create it
files_folders = os.listdir()

if 'data' not in files_folders:
    print("Creating 'data' folder")
    os.mkdir('data')


# create the sub-folders
os.makedirs("data/brand", exist_ok=True)
os.makedirs("data/license", exist_ok=True)