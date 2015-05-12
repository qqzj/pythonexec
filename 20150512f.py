#!/usr/bin/env python
#-*- coding: utf-8 -*-
import Image
im = Image.open('C:/Users/Administrator/Desktop/BACKUP/4dd02d54dc2823a.png');
print im.format
print im.size
print im.mode
im.thumbnail((200, 100))
im.save('thumb.jpg', 'JPEG')