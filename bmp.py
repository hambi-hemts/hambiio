#!/usr/bin/python
# -*- coding: latin-1 -*-

import numpy
import string
from PIL import Image
import os, sys
import glob

PyVersion = sys.version_info[0] 

def get_pixel_size_bmp_ssc(image_name, imarray):
    """ 
    Usage: 
    
        im = Image.open(image_name)
        imarray = numpy.array(im)
        px = get_pixel_size_bmp_ssc(image_name, imarray)
        im = im.convert('RGB')
        x, y = scale_me_bmp(image_name) 
        print x,y
        imshow(imarray, cmap = 'Greys', extent = [0, x,
                                                  0, y])
    Returns: u'FoV = 1.861 nm'
    
    Usage:
        from PIL import Image
        tifimage = Image.open(f)
    """

    filename = image_name.strip('bmp') + str('ssc')
    with open(filename) as fp:
        for line in fp:
            if 'FoV' in line:
                #line.encode('latin1')
                #[int(s) for s in str.split() if s.isdigit()]
                entry = line
                #entry.split
                #print entry
                break
    if PyVersion == 2:
        entry  = entry.split('=')[1]
        all_not_digits = string.letters + ' ' + 'µ'
        number = float(entry.translate(None, all_not_digits))
        dim    = entry.translate(None, string.digits + '.' + ' ')
        
    elif PyVersion == 3:
        entry  = str(entry.split('=')[1])
        number = float(''.join(i for i in entry if i.isdigit()))
        dim    = ''.join(i for i in entry if i.isalpha())
    
    
    if dim == 'nm':
        number = number * 1e-9 
    elif dim == 'µm':
        number = number * 1e-6
    elif dim == 'mm':
        number = number * 1e-3
    return number # number * 1E-3 / imarray.shape[0]
    
def scale_me_bmp(image_name):
    """ 
    Usage: 
    
        im = Image.open(image_name)
        imarray = numpy.array(im)
        px = get_pixel_size_bmp_ssc(image_name, imarray)
        im = im.convert('RGB')
        x, y = scale_me_bmp(image_name) 
        print x,y
        imshow(imarray, cmap = 'Greys', extent = [0, x,
                                                  0, y])
    Returns: u'FoV = 1.861 nm'
    
    Usage:
        from PIL import Image
        tifimage = Image.open(f)
    """

    filename = image_name.strip('bmp') + str('ssc')
    with open(filename) as fp:
        for line in fp:
            if 'FoV' in line:
                #line.encode('latin1')
                #[int(s) for s in str.split() if s.isdigit()]
                entry = line
                #entry.split
                #print entry
                break
    
    if PyVersion == 2:
        entry  = entry.split('=')[1]
        all_not_digits = string.letters + ' ' + 'µ'
        number = float(entry.translate(None, all_not_digits))
        dim    = entry.translate(None, string.digits + '.' + ' ')
        
    elif PyVersion == 3:
        entry  = str(entry.split('=')[1])
        number = float(''.join(i for i in entry if (i.isdigit() or i == '.')))
        dim    = ''.join(i for i in entry if i.isalpha())
    """
    entry  = entry.split('=')[1]
    all_not_digits = string.letters + ' ' + 'µ'
    number = float(entry.translate(None, all_not_digits))
    dim    = entry.translate(None, string.digits + '.' + ' ')"""
    
    """
    if dim == 'nm':
        number = number * 1e-9 
    elif dim == 'µm':
        number = number * 1e-6
    elif dim == 'mm':
        number = number * 1e-3""" 
    
    return number * 1E-3, number * 1E-3