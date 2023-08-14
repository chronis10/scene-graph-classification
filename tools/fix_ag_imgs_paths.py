import json
import os 

current_dir = os.getcwd()


parent_dir = os.path.dirname(os.getcwd())
json_path = os.path.join(parent_dir, 'datasets/ActionGenome/anno_frames_bicls/custom_data_info.json')


with open(json_path, 'r') as f:
    data = json.load(f)

idx_to_files = data['idx_to_files']

new_idx_to_files = []
for fl in idx_to_files:
    filename = fl.split('/')[-1]
    new_idx_to_files.append(f"datasets/ActionGenome/frames_bicls/{filename}")


data['idx_to_files'] = new_idx_to_files

with open(json_path, 'w') as f:
    json.dump(data, f, indent=4)
