
# These tools do the actual work (scan, delete, rename files).


from langchain.tools import tool
import os


@tool
def scan_directory(folder_path: str) -> str:
    """ Scan a Folder and return a list of all files and sub-directories """
    if not os.path.exists(folder_path):
        return f"Folder Not Found :( {folder_path}"
    

    result = []
    for root, dirs, files in os.walk(folder_path):
        for d in dirs:
            result.append(f"DIR: {os.path.join(root, d)}")
        for f in files:
            result.append(f"FILE: {os.path.join(root, f)}")
    return "\n".join(result)


@tool
def delete_log_files(folder_path: str) -> str:
    """Delete all .log files from a folder and return list of deleted files."""
    deleted = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".log"):
                full_path = os.path.join(root, file)
                os.remove(full_path)
                deleted.append(full_path)
    return "Deleted:\n" + "\n".join(deleted) if deleted else "No .log files found."



@tool
def rename_drafts_to_final(folder_path: str) -> str:
    """Rename all files with 'draft' in name to 'final' in a given folder."""
    renamed = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if "draft" in file:
                old_path = os.path.join(root, file)
                new_file = file.replace("draft", "final")
                new_path = os.path.join(root, new_file)
                os.rename(old_path, new_path)
                renamed.append(f"{old_path} -> {new_path}")
    return "Renamed:\n" + "\n".join(renamed) if renamed else "No draft files to rename."