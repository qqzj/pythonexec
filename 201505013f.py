# -*- coding: utf-8 -*-
import time
print time.strftime('%Y-%m-%d %H:%M:%S')
import Image
im = Image.open('C:/Users/Administrator/Desktop/BACKUP/4dd02d54dc2823a.png')
w,h = im.size
print w,h
im.thumbnail((50, 50))
im.save('C:/Users/Administrator/Desktop/demo.png')