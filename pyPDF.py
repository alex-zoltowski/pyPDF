#!/usr/bin/python
import os
from fpdf import FPDF
from sys import argv
from PIL import Image

if len(argv) != 2:
    exit('Please provide only the path to the folder!')

path = argv[1]

if not os.path.isdir(path):
    exit('Path not valid')

if not path.endswith('/'):
    path += '/'

pdf = FPDF()

for f in os.listdir(path):
    if f.endswith('.jpg'):
        pdf.add_page()
        image = Image.open(path + f)
        width, height = image.size
        pdf.image(path + f, 0, 0)

pdf.output(path + 'pdf.pdf', 'F')
