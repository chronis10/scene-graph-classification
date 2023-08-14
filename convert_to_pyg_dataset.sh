#!/bin/bash

cd Img2SceneGraph
python Data_P.py \
--out_dir ../outputs/img2scenegraph_output \
--root ../datasets/ActionGenome/anno_frames_bicls \
--name ag \
--method a \
--para 0.1 \
--dim 500 \
--max_nodes 100 \
--min_nodes 3 \
--max_edges 100 \
--min_edges 2  