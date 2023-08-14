import torch
import json
import h5py
import random
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageShow
import networkx as nx
import os



def draw_single_box(pic, box, color='red', draw_info=None):
    draw = ImageDraw.Draw(pic)
    x1,y1,x2,y2 = int(box[0]), int(box[1]), int(box[2]), int(box[3])
    draw.rectangle(((x1, y1), (x2, y2)), outline=color)
    if draw_info:
        draw.rectangle(((x1, y1), (x1+50, y1+10)), fill=color)
        info = draw_info
        draw.text((x1, y1), info)
        
def print_list(name, input_list, scores=None):
    for i, item in enumerate(input_list):
        if scores == None:
            print(name + ' ' + str(i) + ': ' + str(item))
        else:
            print(name + ' ' + str(i) + ': ' + str(item) + '; score: ' + str(scores[i]))

def save_list_to_file(name, input_list,filename, scores=None):
    with open(f'outputs/sg_visualazation_results/{filename}_{name}.txt', 'w') as f:
        for i, item in enumerate(input_list):
            if scores == None:
                f.write(name + ' ' + str(i) + ': ' + str(item) + '\n')
            else:
                f.write(name + ' ' + str(i) + ': ' + str(item) + '; score: ' + str(scores[i]) + '\n')

def test_image(img_path):
    cwd = os.getcwd()
    print(cwd)
    img = Image.open(img_path)

    
def draw_image(img_path, boxes, box_labels, rel_labels, box_scores=None, rel_scores=None):
    cwd = os.getcwd()
    img = Image.open(os.path.join(cwd,img_path),'r')
    size = get_size(img.size)
    pic = img.resize(size)
    num_obj = len(boxes)
    for i in range(num_obj):
        info = str(i) + '_' + box_labels[i]
        draw_single_box(pic, boxes[i], draw_info=info)
    file_name = img_path.split('/')[-1]
    # pic.save(f'outputs/sg_visualazation_results/{file_name}')
    # print('*' * 50)
    # print_list('box_labels', box_labels, box_scores)
    # print('*' * 50)
    # print_list('rel_labels', rel_labels, rel_scores)
    # text_file_name = file_name.split('.')[0]
    # save_list_to_file('box_labels', box_labels, text_file_name, box_scores)
    # save_list_to_file('rel_labels', rel_labels, text_file_name, rel_scores)

    return file_name,pic

def get_size(image_size):
    min_size = 600
    max_size = 1000
    w, h = image_size
    size = min_size
    if max_size is not None:
        min_original_size = float(min((w, h)))
        max_original_size = float(max((w, h)))
        if max_original_size / min_original_size * size > max_size:
            size = int(round(max_size * min_original_size / max_original_size))
    if (w <= h and w == size) or (h <= w and h == size):
        return (w, h)
    if w < h:
        ow = size
        oh = int(size * h / w)
    else:
        oh = size
        ow = int(size * w / h)
    return (ow, oh)

def visualize_scene_graph(image_idx, box_topk, rel_topk,custom_prediction,custom_data_info):
    ind_to_classes = custom_data_info['ind_to_classes']
    ind_to_predicates = custom_data_info['ind_to_predicates']

    image_path = custom_data_info['idx_to_files'][image_idx]

    boxes = custom_prediction[str(image_idx)]['bbox'][:box_topk]
    box_labels = custom_prediction[str(image_idx)]['bbox_labels'][:box_topk]
    box_scores = custom_prediction[str(image_idx)]['bbox_scores'][:box_topk]
    all_rel_labels = custom_prediction[str(image_idx)]['rel_labels']
    all_rel_scores = custom_prediction[str(image_idx)]['rel_scores']
    all_rel_pairs = custom_prediction[str(image_idx)]['rel_pairs']

    for i in range(len(box_labels)):
        box_labels[i] = ind_to_classes[box_labels[i]]

    rel_labels = []
    rel_scores = []
    edges = []
    for i in range(len(all_rel_pairs)):
       
        if all_rel_pairs[i][0] < box_topk and all_rel_pairs[i][1] < box_topk:
            rel_scores.append(all_rel_scores[i])
            label = str(all_rel_pairs[i][0]) + '_' + box_labels[all_rel_pairs[i][0]] + ' => ' + ind_to_predicates[all_rel_labels[i]] + ' => ' + str(all_rel_pairs[i][1]) + '_' + box_labels[all_rel_pairs[i][1]]
            rel_labels.append(label)
            source = str(all_rel_pairs[i][0]) + '_' + box_labels[all_rel_pairs[i][0]]
            target = str(all_rel_pairs[i][1]) + '_' + box_labels[all_rel_pairs[i][1]]
            relation = ind_to_predicates[all_rel_labels[i]]
            score = all_rel_scores[i]
            edges.append((source, target, {'relation': relation, 'score': score}))

    edges = edges[:rel_topk]
    rel_labels = rel_labels[:rel_topk]
    rel_scores = rel_scores[:rel_topk]   

    file_name,pic = draw_image(image_path, boxes, box_labels, rel_labels, box_scores=box_scores, rel_scores=rel_scores)
    # Create a 1x2 grid of subplots
    fig, axarr = plt.subplots(1, 2, figsize=(10, 5))

    G = nx.DiGraph()

    for edge in edges:
        G.add_edge(edge[0], edge[1], relation=edge[2]['relation'], score=edge[2]['score'])

    # Display the image on the left subplot
    axarr[0].imshow(pic)
    axarr[0].axis('off')  # Hide the axes for the image

    pos = nx.spring_layout(G)
    edge_labels = {(u, v): d['relation'] for u, v, d in G.edges(data=True)}

    # Draw nodes
    nx.draw_networkx_nodes(G, pos)

    # Draw edges
    nx.draw_networkx_edges(G, pos)

    # Draw node labels
    nx.draw_networkx_labels(G, pos)

    # Draw edge labels with relations
    

    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    # Display the networkx graph on the right subplot
    nx.draw(G, with_labels=True, ax=axarr[1], node_size=700)

    # Show the combined plots
    plt.tight_layout()
    plt.show()
    print('------------------------------')
    for edge,score in zip(rel_labels,rel_scores):
        print(edge, score)

 