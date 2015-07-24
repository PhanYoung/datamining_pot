# -*- coding: utf-8 -*-

_COLORS = ['blue', 'red',  'yellow', 'green', 'olive', 
           'magenta', 'cyan', 'purple', 'gray', 'black', 
           'orange', 'maroon', 'lime']

def make_colors(n):
    if n <= len(_COLORS):
        return _COLORS[ : n]
