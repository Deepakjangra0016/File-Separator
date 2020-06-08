import os, shutil

Dict_extensions = {
    'Audio_extension' : ('.mp3', '.m4a', '.wav', '.flac'),
    'Video_extension' : ('.mp4', '.mkv', '.MKV', '.flv', '.mpeg'),
    'Document_extension' : ('.doc', '.docx'),
    'PDF_extension' : ('.pdf'),
    'Excel_extension' : ('.xls', '.xlsx'),
    'Text_extension' : ('.txt')
}

folderpath = input('Enter Folder path to seperate files : ')

def file_finder (folder_path, file_extension):
    files = []
    for file in os.listdir(folder_path):
        for extension in file_extension:
            if file.endswith(extension):
                files.append(file)
    return files

for extension_type, extension_tuple in Dict_extensions.items():
    print(f"{extension_type.split('_')[0]} files = {len(file_finder(folderpath,extension_tuple))} ")
    if len(file_finder(folderpath,extension_tuple)) > 0:
        folder_name = extension_type.split('_')[0] + 'Files'
        folder_path = os.path.join(folderpath, folder_name)
        os.mkdir(folder_path)
    for item in (file_finder(folderpath, extension_tuple)):
        item_path = os.path.join(folderpath,item)
        item_new_path = os.path.join(folder_path,item)
        shutil.move(item_path,item_new_path)