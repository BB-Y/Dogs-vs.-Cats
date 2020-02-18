import torch
import os

def cuda():
    return 1 if torch.cuda.is_availble() else 0

def imagelist(path):
    list = []
    for each_file in os.listdir(path):
         list.append(os.path.join(path,each_file))
    return list