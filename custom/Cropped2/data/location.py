import os
# from os import getcwd


wd = os.getcwd()
dirname = './images/val2018'
files = [f[:] for f in os.listdir(dirname) if f[-4:].lower() == '.jpg']
list_file = open('valLocations.txt', 'w')
for f in files:
    list_file.write("/home/nina/custom/images/val2018/%s"%(f))
    list_file.write('\n')

dirname = './images/train2018'
files = [f[:] for f in os.listdir(dirname) if f[-4:].lower() == '.jpg']
list_file = open('trainLocations.txt', 'w')
for f in files:
    list_file.write("/home/nina/custom/images/train2018/%s"%(f))
    list_file.write('\n')

