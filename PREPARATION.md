# Paths and files fixes

## Make dirs

```
mkdir outputs
mkdir datasets
mkdir checkpoints
```

## Action Genome image paths

```
cd tools
./fix_ag_imgs_paths.py
```

## Modify Scene Graph Benchmark files

### VG (Manual actions)
Modify the following part from the 
```
tools/modify_files/paths_catalog.py
```
 with your full path of ...../scene-classification/datasets/vg

{
    "VG_stanford_filtered": {
        "img_dir": "/mnt/c/Users/chron/Desktop/scene-classification/datasets/vg/VG_100K",
        "roidb_file": "/mnt/c/Users/chron/Desktop/scene-classification/datasets/vg/VG-SGG.h5",
        "dict_file": "/mnt/c/Users/chron/Desktop/scene-classification/datasets/vg/VG-SGG-dicts.json",
        "image_file": "/mnt/c/Users/chron/Desktop/scene-classification/datasets/vg/image_data.json"
    },
    "VG_stanford_filtered_with_attribute": {
        "img_dir": "/mnt/c/Users/chron/Desktop/scene-classification/datasets/vg/VG_100K_backup",
        "roidb_file": "/mnt/c/Users/chron/Desktop/scene-classification/datasets/vg/VG-SGG-with-attri.h5",
        "dict_file": "/mnt/c/Users/chron/Desktop/scene-classification/datasets/vg/VG-SGG-dicts-with-attri.json",
        "image_file": "/mnt/c/Users/chron/Desktop/scene-classification/datasets/vg/image_data.json"
}


```
cd tools/modify_files
python3 replace_file_paths_catalog.py
```


### Modify checkpoints paths

```
cd tools/modify_files
python3 replace_file_paths_checkpoint.py
```

## Modify Img2SceneGraph

```
cd tools/modify_files
python3 replace_Data_P.py
```

## Modify GAE

```
cd tools/modify_files
python3 replace_files_gae.py
```
