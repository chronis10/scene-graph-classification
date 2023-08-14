#!/bin/bash
# This script generates the graphs for the SceneGraph project
cwd=$(pwd)

cd SceneGraph
CUDA_VISIBLE_DEVICES=0 python -m torch.distributed.launch \
--master_port 10027 --nproc_per_node=1 tools/relation_test_net.py \
--config-file "configs/e2e_relation_X_101_32_8_FPN_1x.yaml" \
MODEL.ROI_RELATION_HEAD.USE_GT_BOX False \
MODEL.ROI_RELATION_HEAD.USE_GT_OBJECT_LABEL False \
MODEL.ROI_RELATION_HEAD.PREDICTOR CausalAnalysisPredictor \
MODEL.ROI_RELATION_HEAD.CAUSAL.EFFECT_TYPE TDE \
MODEL.ROI_RELATION_HEAD.CAUSAL.FUSION_TYPE sum \
MODEL.ROI_RELATION_HEAD.CAUSAL.CONTEXT_LAYER motifs \
MODEL.WEIGHT "$cwd/checkpoints/upload_causal_motif_sgdet/model_0028000.pth" \
TEST.IMS_PER_BATCH 1 \
DTYPE "float16" \
GLOVE_DIR "$cwd/datasets/glove" \
MODEL.PRETRAINED_DETECTOR_CKPT "$cwd/checkpoints/upload_causal_motif_sgdet" \
OUTPUT_DIR "$cwd/outputs/upload_causal_motif_sgdet" \
TEST.CUSTUM_EVAL True \
TEST.CUSTUM_PATH  "$cwd/datasets/ActionGenome/frames_bicls" \
DETECTED_SGG_DIR "$cwd/datasets/ActionGenome/anno_frames_bicls"