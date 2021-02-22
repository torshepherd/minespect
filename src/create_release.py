"""
Code adapted from https://stackoverflow.com/questions/10480440/zip-folder-with-subfolder-in-python.

All credit to cjbarth
"""

# importing required modules 
from zipfile import ZipFile, ZIP_DEFLATED
import os
from animation import *

PATH_TO_DOWNLOADS = os.path.join(os.path.dirname(PATH_TO_SRC), 'downloads')
PATH_TO_RESOURCEPACK_ZIP = os.path.join(PATH_TO_DOWNLOADS, 'resourcepack.zip')
PATH_TO_DATAPACK_ZIP = os.path.join(PATH_TO_DOWNLOADS, 'datapack.zip')

def get_shield_url(label, message, color='brightgreen'):
    formatted_label = label.replace(' ', '%20')
    formatted_message = message.replace(' ', '%20')
    return 'https://img.shields.io/badge/{}-{}-{}'.format(formatted_label, formatted_message, color)
    
def zip_dir(src_path, archive_path):    
    with open(os.path.join(PATH_TO_LOG, 'release.log'), 'a+') as releaselog:
        print('\n\nWriting {}'.format(archive_path), file=releaselog)
        with ZipFile(archive_path, 'w', ZIP_DEFLATED) as archive_file:
            total_num_files = 0
            num_zipped = 0
            for dirpath, dirnames, filenames in os.walk(src_path):
                for filename in filenames:
                    total_num_files += 1
            for dirpath, dirnames, filenames in os.walk(src_path):
                for filename in filenames:
                    file_path = os.path.join(dirpath, filename)
                    archive_file_path = os.path.relpath(file_path, src_path)
                    archive_file.write(file_path, archive_file_path)
                    print('Writing {} to {}'.format(filename, archive_file_path), file=releaselog)
                    num_zipped += 1
                    frac = num_zipped / total_num_files
                    print_progress(frac, empty_char=' ', fill_char='\u001b[32m▧\u001b[0m')
            print()
            
def main():
    # build all animations specified 
    create_all_animations()
    
    # clear out downloads/
    print('Done creating animations, clearing out downloads...')
    try:
        os.remove(PATH_TO_RESOURCEPACK_ZIP)
    except:
        pass
    try:
        os.remove(PATH_TO_DATAPACK_ZIP)
    except:
        pass
    try:
        os.remove(os.path.join(PATH_TO_LOG, 'release.log'))
    except:
        pass
    
    # path to folder which needs to be zipped 
    print('Zipping resource pack...')
    zip_dir(PATH_TO_RESOURCEPACK, PATH_TO_RESOURCEPACK_ZIP)
    print('Zipping data pack...')
    zip_dir(PATH_TO_DATAPACK, PATH_TO_DATAPACK_ZIP)

if __name__ == "__main__": 
    main()
    # print(get_all_file_paths(PATH_TO_DATAPACK))
