#!/usr/bin/env python3

"""
pdf2svg dur1c.pdf dur1c.svg
pdf2svg dur1d.pdf dur1d.svg
pdf2svg dur1e.pdf dur1e.svg
pdf2svg dur1f.pdf dur1f.svg
pdf2svg dur1g.pdf dur1g.svg
pdf2svg dur2a.pdf dur2a.svg
pdf2svg dur2b.pdf dur2b.svg
pdf2svg dur2c.pdf dur2c.svg
pdf2svg dur2d.pdf dur2d.svg
pdf2svg dur2e.pdf dur2e.svg
pdf2svg dur2f.pdf dur2f.svg
pdf2svg dur2g.pdf dur2g.svg
pdf2svg mol0f.pdf mol0f.svg
pdf2svg mol0g.pdf mol0g.svg
pdf2svg mol1a.pdf mol1a.svg
pdf2svg mol1b.pdf mol1b.svg
pdf2svg mol1c.pdf mol1c.svg
pdf2svg mol1d.pdf mol1d.svg
pdf2svg mol1e.pdf mol1e.svg
pdf2svg mol1f.pdf mol1f.svg
pdf2svg mol1g.pdf mol1g.svg
pdf2svg mol2a.pdf mol2a.svg
pdf2svg mol2b.pdf mol2b.svg
pdf2svg mol2c.pdf mol2c.svg

inkscape -w 1024 dur1c.svg -b white -o dur1c.png
inkscape -w 1024 dur1d.svg -b white -o dur1d.png
inkscape -w 1024 dur1e.svg -b white -o dur1e.png
inkscape -w 1024 dur1f.svg -b white -o dur1f.png
inkscape -w 1024 dur1g.svg -b white -o dur1g.png
inkscape -w 1024 dur2a.svg -b white -o dur2a.png
inkscape -w 1024 dur2b.svg -b white -o dur2b.png
inkscape -w 1024 dur2c.svg -b white -o dur2c.png
inkscape -w 1024 dur2d.svg -b white -o dur2d.png
inkscape -w 1024 dur2e.svg -b white -o dur2e.png
inkscape -w 1024 dur2f.svg -b white -o dur2f.png
inkscape -w 1024 dur2g.svg -b white -o dur2g.png
inkscape -w 1024 mol0f.svg -b white -o mol0f.png
inkscape -w 1024 mol0g.svg -b white -o mol0g.png
inkscape -w 1024 mol1a.svg -b white -o mol1a.png
inkscape -w 1024 mol1b.svg -b white -o mol1b.png
inkscape -w 1024 mol1c.svg -b white -o mol1c.png
inkscape -w 1024 mol1d.svg -b white -o mol1d.png
inkscape -w 1024 mol1e.svg -b white -o mol1e.png
inkscape -w 1024 mol1f.svg -b white -o mol1f.png
inkscape -w 1024 mol1g.svg -b white -o mol1g.png
inkscape -w 1024 mol2a.svg -b white -o mol2a.png
inkscape -w 1024 mol2b.svg -b white -o mol2b.png
inkscape -w 1024 mol2c.svg -b white -o mol2c.png

"""

import datetime as DT
import pathlib as PL
import random as RND
import matplotlib.pyplot as PLT

output_file = 'results.csv'

p = PL.Path('./notes').glob('**/*.png')
files = [x for x in p if x.is_file() \
         and 'dur' in str(x) \
         ]
# print(files)

def ShowImage(img_path):
    img = PLT.imread(img_path)
    PLT.imshow(img, cmap = 'gray')

    PLT.draw()
    PLT.waitforbuttonpress(0) # this will wait for indefinite time
    PLT.close()

def TimeNote():
    fi = RND.choice(files)
    tic = DT.datetime.now()
    ShowImage(fi)
    dt = DT.datetime.now() - tic
    return [tic, fi.stem, dt.total_seconds()]

while True:
    results = TimeNote()
    with open(output_file, "a") as fi:
        fi.write(";".join(map(str, results))+"\n")
