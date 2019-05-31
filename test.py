import xml.etree.ElementTree as ET
import os, random
# from os import getcwd

dirname = './Annotations'
files = [f[:-4] for f in os.listdir(dirname) if f[-4:].lower() == '.xml']
imgdir = './custom/Images'
    
for file in files:
    try:
        fh = open('%s/%s.jpg'%(imgdir,file), 'r')
        # Store configuration file values
    except FileNotFoundError:
        print(file)