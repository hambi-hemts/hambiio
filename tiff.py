#!/usr/bin/python
# -*- coding: latin-1 -*-

from PIL import Image
import numpy 
import string
import os, sys
import glob

PyVersion = sys.version_info[0] 

def get_pixel_size(tifimage):
    """ 
    Returns: u'Image Pixel Size = 1.861 nm'
    
    Usage:
        from PIL import Image
        tifimage = Image.open(f)
    """
    item_4_1 = list(tifimage.tag.items())[4][1]
    lines = list(tifimage.tag.items())[4][1].split('\r\n')
    
    entry = None
    
    for line in lines:
        if 'Image Pixel Size' in line:
            line.encode('utf-8')
            entry = line
            break
            
    if PyVersion == 2:
        entry = entry.split('=')[1].encode('utf-8')
        ### changelog: changed the code for the number extraction, such that Pixel Size = 14.97 nm is correctly read in:
        #old line:
        #all_not_digits = string.ascii_letters + '.' + ' ' + 'µ'
        #new line:
        all_not_digits = string.ascii_letters + ' ' + 'µ'
        number = float(entry.translate(None, all_not_digits))
        dim    = entry.translate(None, string.digits + '.' + ' ')
    elif PyVersion == 3:
        entry  = str(entry.split('=')[1])
        ### changelog: changed the code for the number extraction, such that Pixel Size = 14.97 nm is correctly read in:
        #old line:
        #number = float(''.join(i for i in entry if i.isdigit()))
        #new line:
        number = float(''.join(i for i in entry if (i.isdigit() or i == '.')))
        dim    = ''.join(i for i in entry if i.isalpha())
    
    if dim == 'nm':
        number = number * 1e-9 
    elif dim == 'pm':
        number = number * 1e-12
    elif dim == 'µm':
        number = number * 1e-6
    elif dim == 'mm':
        number = number * 1e-3
    
    return number
def scale_me(tiffile):
    """ 
    
    Usage:
        im = im.convert('RGB')
        imarray = numpy.array(im)

        x, y = scale_me(f)
        mpl.imshow(imarray, cmap = 'Reds', extent = [0, x, 0, y])
    """ 
    
    im = Image.open(tiffile)
    imarray = numpy.array(im)
    x, y = imarray.shape
    pixelsize = get_pixel_size(im)
    
    return y * pixelsize, x * pixelsize