# %%
"""
# 训练集篇
1. 一个机器学习任务包括：数据的收集 -> 数据集的处理 -> 模型构建 -> 训练
2. 在torch中，Dataset形成从idx到input tensor的映射，DataLoader(Dataset)可以自动化完成batch data的读取和epoch之后的shuffle等
3. 训练集收集后应该先用bash/shell/awk进行相应简单的处理，然后再构建Dataset模块和generate_dataset函数
"""

# %%
import torch
from torch.utils.data import *
from PIL import Image 
import os
import numpy as np

# %%
"""
Dataset不区分train_data和test_data
"""

# %%
class MalwareData(Dataset):
    def __init__(self, images, labels):
        self.images = images # images: the path of the image path list
        self.labels = labels # labels: the corresponding lable of the image 
    
    def __len__(self):
        return len(self.images)
    
    def __getitem__(self, idx):
        img_path = self.images[idx]
        label = self.labels[idx]
        
        img = Image.open(img_path)
        img = img.resize((224, 224))
        img_mat = np.asarray(img, dtype=np.float32)
        img_mat = np.reshape(img_mat, (1, 224, 224)) # can be replaced with unsqueeze
        img_mat = np.repeat(img_mat, 3, axis=0) # (3, 224, 224)
        img_tensor = torch.from_numpy(img_mat)
        
        return img_tensor, label

# %%
def generate_dataset(dataset_path):
    # generate Dataset according to dataset_path(which should be preprocessed by bash/shell)
    # path: the path of the dataset, divided by label as name of the folder
    images = []
    labels = []
    
    for label in os.listdir(dataset_path):
        label_path = os.path.join(dataset_path, label)
        for fname in os.listdir(label_path):
            fpath = os.path.join(label_path, fname)
            images.append(fpath)
            labels.append(label)
            
    return MalwareData(images, labels)
