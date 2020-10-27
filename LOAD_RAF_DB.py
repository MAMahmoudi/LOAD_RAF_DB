import os
import sys

import pandas as pd
import cv2

# I converted label.lst to labeel.csv because csv is eazy to use

file = pd.read_csv('./labels.csv')
print(len(file))

# Put your images in a directory Images

Images_Path = './Images/'

# We create directories for classes
try:
    os.makedirs('Classes')
    os.makedirs('Classes/1')
    os.makedirs('Classes/2')
    os.makedirs('Classes/3')
    os.makedirs('Classes/4')
    os.makedirs('Classes/5')
    os.makedirs('Classes/6')
    os.makedirs('Classes/7')
except FileExistsError:
    print("Directory  already exists")

for i in range(1, 15339):
    print(i)
    classe = file['classe'][i]
    Image = file['Image'][i]
    print('File name', Image)
    print('classe', classe)
    Original_Image = cv2.imread(sys.path[0] + Images_Path + Image)
    print(Images_Path + Image)
    cv2.imwrite(sys.path[0] + '/Classes/' + classe.astype(str) + '/' + Image, Original_Image)
