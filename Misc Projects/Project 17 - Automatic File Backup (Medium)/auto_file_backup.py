import os
import shutil
import datetime
import schedule
import time

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f'Folder copied to {dest_dir}')
    except FileExistsError:
        print(f'Folder already exists in {dest}')


source_dir = os.path.dirname(os.path.realpath(__file__))
destination_dir = '/home/luiz/Documents/python_projects/Backups'

schedule.every().day.at('16:24').do(lambda: copy_folder_to_directory(source_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)