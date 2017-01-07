# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 23:37:19 2013

@author: jinzhen
"""
def trunc(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    if f>0 or f==0:
        return ('%.*f' % (n + 1, f))[:-1]
    else:
        return ('%.*f' % (n + 1, f-0.1))[:-1]
print trunc(-10.9034,1)