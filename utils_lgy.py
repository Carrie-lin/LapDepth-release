import os
import json
from collections import OrderedDict
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import trimesh
import torch
import time
import math
from plyfile import PlyData, PlyElement
import torch.nn.functional as F

## to see the distribution of an array



## to judge if the folder already exist 
## if not, make one
def judge_exist_and_mkdir(file_path):    
    isExists=os.path.exists(file_path)
    if not isExists:
        os.makedirs(file_path)


## write obj files
def write_obj_file(filename, V, F=None, C=None, vid_start=1):
    with open(filename, 'w') as f:
        if C is not None:
            for Vi, Ci in zip(V, C):
                f.write(f"v {Vi[0]} {Vi[1]} {Vi[2]} {Ci[0]} {Ci[1]} {Ci[2]}\n")
        else:
            for Vi in V:
                f.write(f"v {Vi[0]} {Vi[1]} {Vi[2]}\n")
                
        if F is not None:
            for Fi in F:
                f.write(f"f {Fi[0]+vid_start} {Fi[1]+vid_start} {Fi[2]+vid_start}\n")


## draw colored points to obj: red means positive and blue means negtive
## if need to clip the value, set a positive value for threshold
def draw_colored_points_to_obj(filename, vertices, scalars_for_color,threshold=None):
    print(f"draw colored points to obj file :{filename}")
    print('v min:',min(scalars_for_color))
    print('v max:',max(scalars_for_color))
    assert len(vertices.shape) == 2
    assert vertices.shape[-1] == 3
    if threshold:
        norm = matplotlib.colors.Normalize(vmin=-threshold, vmax=threshold, clip=True)
    else:
        norm = matplotlib.colors.Normalize(vmin=min(scalars_for_color), vmax=max(scalars_for_color), clip=True)
    mapper = cm.ScalarMappable(norm=norm, cmap=cm.jet)
    colors = [(r, g, b) for r, g, b, a in mapper.to_rgba(scalars_for_color)]
    write_obj_file(filename, vertices.reshape(-1, 3), C=colors)