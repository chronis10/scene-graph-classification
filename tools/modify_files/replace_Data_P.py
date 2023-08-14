import json
import os 
import shutil

current_dir = os.getcwd()

parent_dir = os.path.dirname(os.path.dirname(os.getcwd()))

move_directory = os.path.join(parent_dir, 'Img2SceneGraph')

if os.path.isfile(os.path.join(move_directory,"Data_P.py")):
    if not os.path.isfile(os.path.join(move_directory,"Data_P.py.bak")):
        os.rename(os.path.join(move_directory,"Data_P.py"), os.path.join(move_directory,"Data_P.py.bak"))
    else:
        os.remove(os.path.join(move_directory,"Data_P.py"))
        
if os.path.isfile(os.path.join(move_directory,"Data_P.py")):
    os.remove(os.path.join(move_directory,"Data_P.py"))

shutil.copyfile(os.path.join(current_dir,"Data_P.py"), os.path.join(move_directory,"Data_P.py"))
