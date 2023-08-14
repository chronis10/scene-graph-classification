import json
import os 
import shutil

current_dir = os.getcwd()


parent_dir = os.path.dirname(os.path.dirname(os.getcwd()))

move_directory = os.path.join(parent_dir, 'SceneGraph/maskrcnn_benchmark/config')

if os.path.isfile(os.path.join(move_directory,"paths_catalog.py")):
    if not os.path.isfile(os.path.join(move_directory,"paths_catalog.py.bak")):
        os.rename(os.path.join(move_directory,"paths_catalog.py"), os.path.join(move_directory,"paths_catalog.py.bak"))
    else:
        os.remove(os.path.join(move_directory,"paths_catalog.py"))
        
if os.path.isfile(os.path.join(move_directory,"paths_catalog.py")):
    os.remove(os.path.join(move_directory,"paths_catalog.py"))

shutil.copyfile(os.path.join(current_dir,"paths_catalog.py"), os.path.join(move_directory,"paths_catalog.py"))
