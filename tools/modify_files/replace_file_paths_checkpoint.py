import json
import os 
import shutil

current_dir = os.getcwd()


parent_dir = os.path.dirname(os.path.dirname(os.getcwd()))

move_directory = os.path.join(parent_dir, 'SceneGraph/maskrcnn_benchmark/utils')

if os.path.isfile(os.path.join(move_directory,"checkpoint.py")):
    if not os.path.isfile(os.path.join(move_directory,"checkpoint.py.bak")):
        os.rename(os.path.join(move_directory,"checkpoint.py"), os.path.join(move_directory,"checkpoint.py.bak"))
    else:
        os.remove(os.path.join(move_directory,"checkpoint.py"))
        
if os.path.isfile(os.path.join(move_directory,"checkpoint.py")):
    os.remove(os.path.join(move_directory,"checkpoint.py"))

shutil.copyfile(os.path.join(current_dir,"checkpoint.py"), os.path.join(move_directory,"checkpoint.py"))

