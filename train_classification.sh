#!/bin/bash
cd Graph_AE
python train_classifier.py \
--d ag \
--n_skip 0 \
--batch 40 \
--e 300 \
--lr 1e-4 \
--n_train 280 \
--n_test 120 \
--c_rate 0.85 \
--model_dir '../outputs/graphae_model/'
