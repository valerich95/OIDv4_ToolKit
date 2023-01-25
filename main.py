# ---------------
# Date: 7/19/2018
# Place: Biella/Torino
# Author: EscVM & TArt
# Project: OID v4
# ---------------

"""
OID v4 Downloader
Download specific classes of the huge online dataset Open Image Dataset.
Licensed under the MIT License (see LICENSE for details)
------------------------------------------------------------
Usage:
refer to README.md file
"""
from sys import exit
from textwrap import dedent
from modules.parser import *
from modules.utils import *
from modules.downloader import *
from modules.show import *
from modules.csv_downloader import *
from modules.bounding_boxes import *
from modules.image_level import *

def find(ch,st): 
    indexes=[]
    index1=0
    while(True):
        if ch in st[index1:]:
            index2=st[index1:].index(ch)
            indexes.append(index1+index2)
            index1=index2+index1+1
        
        else:
            break
    return(indexes)

ROOT_DIR = ''
DEFAULT_OID_DIR = os.path.join(ROOT_DIR, 'OID')

if __name__ == '__main__':

    args = parser_arguments()
    indexes=find(",",args.classes[0])
    classes=[]
    for ind in range(len(indexes)):
        if ind==0:
            classes.append(args.classes[0][:indexes[ind]])
        elif ind==len(indexes)-1:
            classes.append(args.classes[0][indexes[ind-1]+2:indexes[ind]])
            classes.append(args.classes[0][indexes[ind]+2:len(args.classes[0])])
        else:
            classes.append(args.classes[0][indexes[ind-1]+2:indexes[ind]])                      
    args.classes = classes
    print(args.classes)
    if args.command == 'downloader_ill':
        image_level(args, DEFAULT_OID_DIR)
    else:
        bounding_boxes_images(args, DEFAULT_OID_DIR)
