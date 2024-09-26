import os, shutil
path = r'/Users/delaram/Documents/FALL2024/'

# shows us all the files within path
file_names = os.listdir(path)

folder_names = ['csv files','image files', 'text files', 'pdf files']
for folder in folder_names:
    folder_path = os.path.join(path, folder)
    if not os.path.exists(folder_path):
        print(f"Creating folder: {folder_path}")
        os.makedirs(folder_path)

for file in file_names:

    file_path = os.path.join(path, file)

    # Move CSV files
    if file.endswith(".csv") and not os.path.exists(os.path.join(path, "csv files", file)):
        shutil.move(file_path, os.path.join(path, "csv files", file))

    # Move PNG files
    elif file.endswith(".png") and not os.path.exists(os.path.join(path, "image files", file)):
        shutil.move(file_path, os.path.join(path, "image files", file))

    # Move TXT files
    elif file.endswith(".txt") and not os.path.exists(os.path.join(path, "text files", file)):
        shutil.move(file_path, os.path.join(path, "text files", file))

    # Move PDF files
    elif file.endswith(".pdf") and not os.path.exists(os.path.join(path, "pdf files", file)):
        shutil.move(file_path, os.path.join(path, "pdf files", file))

    # Handle files that do not match any extension
    else:
        print(f"File not moved: {file}")

# Remove empty folders 
for folder in folder_names:
    folder_path = os.path.join(path, folder)
    # check if the folder is empty and remove it if it is
    if len(os.listdir(folder_path)) == 0:
        os.rmdir(folder_path)
        print(f"removed empty folder: {folder_path}")