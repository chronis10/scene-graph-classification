### Create environment
```
conda create -n sgg-classification python=3.7
conda activate sgg-classification
```
## CUDA install 
Ubuntu 20.04/ WSL 2.0

Important: CUDA 11.1 needs gcc 9

Use this link for multiple gcc versions: https://phoenixnap.com/kb/install-gcc-ubuntu

```
wget https://developer.download.nvidia.com/compute/cuda/11.1.0/local_installers/cuda_11.1.0_455.23.05_linux.run
sudo sh cuda_11.1.0_455.23.05_linux.run 
```
### Fix CUDA Home

Run every time before start expirements if you already have a symlink with different CUDA version
```
export CUDA_HOME="/usr/local/cuda-11.1" 
```

## Pytorch install 
```
pip install torch==1.10.0+cu111 torchvision==0.11.0+cu111 torchaudio==0.10.0 -f https://download.pytorch.org/whl/torch_stable.html
```

### Check if torch and CUDA works
```
import torch
torch.cuda.is_available()
```
If True continue else Good Luck with CUDA !!!

### Install rest environment dependencies
```
pip install ipython
pip install ipykernel notebook jupyter
pip install scipy
pip install h5py
pip install cython

pip install ninja yacs matplotlib tqdm opencv-python overrides

pip install torch-scatter -f https://data.pyg.org/whl/torch-1.10.0+cu111.html
pip install torch-sparse==0.6.12 -f https://data.pyg.org/whl/torch-1.10.0+cu111.html
pip install torch-geometric==2.0.0

pip install -q git+https://github.com/snap-stanford/deepsnap.git
```

## Pycotools
```
git clone https://github.com/cocodataset/cocoapi.git
cd cocoapi/PythonAPI
python setup.py build_ext install
```

## Scene-Graph Generation Model
```
git clone https://github.com/Yvonne0413/SceneGraph.git
cd SceneGraph
python setup.py build develop
```
## Scene-Graph Generation Model (not Used)
```
git clone https://github.com/KaihuaTang/Scene-Graph-Benchmark.pytorch.git
cd Scene-Graph-Benchmark.pytorch
python setup.py build develop
```
## Apex
```
git clone https://github.com/NVIDIA/apex.git
cd apex
python setup.py install --cuda_ext --cpp_ext
```
## Img2SceneGraph
```
git clone https://github.com/gyhandy/Img2SceneGraph.git
```
## Graph AE
```
git clone https://github.com/Pangyk/Graph_AE.git
```

