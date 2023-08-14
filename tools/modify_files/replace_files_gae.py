import json
import os 
import shutil

current_dir = os.getcwd()

parent_dir = os.path.dirname(os.path.dirname(os.getcwd()))

move_directory = os.path.join(parent_dir, 'Graph_AE/utils/')

if os.path.isfile(os.path.join(move_directory,"train_utils.py")):
    if not os.path.isfile(os.path.join(move_directory,"train_utils.py.bak")):
        os.rename(os.path.join(move_directory,"train_utils.py"), os.path.join(move_directory,"train_utils.py.bak"))
    else:
        os.remove(os.path.join(move_directory,"train_utils.py"))
        
if os.path.isfile(os.path.join(move_directory,"train_utils.py")):
    os.remove(os.path.join(move_directory,"train_utils.py"))

shutil.copyfile(os.path.join(current_dir,"train_utils.py"), os.path.join(move_directory,"train_utils.py"))

move_directory = os.path.join(parent_dir, 'Graph_AE/')

if os.path.isfile(os.path.join(move_directory,"train_classifier.py")):
    if not os.path.isfile(os.path.join(move_directory,"train_classifier.py.bak")):
        os.rename(os.path.join(move_directory,"train_classifier.py"), os.path.join(move_directory,"train_classifier.py.bak"))
    else:
        os.remove(os.path.join(move_directory,"train_classifier.py"))
        
if os.path.isfile(os.path.join(move_directory,"train_classifier.py")):
    os.remove(os.path.join(move_directory,"train_classifier.py"))

shutil.copyfile(os.path.join(current_dir,"train_classifier.py"), os.path.join(move_directory,"train_classifier.py"))

