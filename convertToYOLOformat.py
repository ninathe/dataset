import xml.etree.ElementTree as ET
import os, random
# from os import getcwd

sets=[('2019', 'train'), ('2019', 'val'), ('2019', 'test')]
classes = ["Other", "Can", "Plastic", "PlasticBottle"]

def convert_annotation(year, sett, image_id, wd):
    in_file = open('Annotations/%s.xml'%(image_id))
    tree=ET.parse(in_file)
    root = tree.getroot()
    os.rename('%s/images/%s.jpg'%(wd, image_id), '%s/coco/images/%s%s/COCO_%s%s_%s.jpg'%(wd, sett, year, sett, year, image_id))


    size = root.find('size')
    width = int(size.find('width').text)
    height = int(size.find('height').text)
    list_file = open('coco/labels/%s%s/COCO_%s%s_%s.txt'%(sett, year, sett, year, image_id), 'w')

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        objwidth = int(xmlbox.find('xmax').text) - int(xmlbox.find('xmin').text)
        objheight = int(xmlbox.find('ymax').text) - int(xmlbox.find('ymin').text)
        x_center = int(xmlbox.find('xmin').text) + 1/2*objwidth
        y_center = int(xmlbox.find('ymin').text) + 1/2*objheight
        box = [cls_id, x_center/width, y_center/height, objwidth/width, objheight/height]
        list_file.write(" ".join([str(a) for a in box]))
        list_file.write('\n')
    list_file.close()


wd = os.getcwd()
dirname = './Annotations'
files = [f[:-4] for f in os.listdir(dirname) if f[-4:].lower() == '.xml']
dirname = './Annotations'

# random divide  
trainval = random.sample(files, len(files)//2)
test = [f for f in files if f not in trainval]

# random divide 
train = random.sample(trainval, len(trainval)//2)
val = [f for f in trainval if f not in train]

for file in val:
    convert_annotation("2018", "val", file, wd)
for t in train:
    convert_annotation("2018", "train", t, wd)


    
    