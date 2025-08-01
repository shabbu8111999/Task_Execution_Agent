import os


def scan_directory(folder_path):
    files = []
    for root, dirs, filenames in os.walk(folder_path):
        for f in filenames:
            full_path = os.path.join(root, f)
            files.append(full_path)
    return files


def delete_files_by_extension(folder_path, extension = ".log"):
    deleted = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(extension):
                path = os.path.join(root, file)
                os.remove(path)
                deleted.append(path)
    return deleted
