# -*- coding: utf-8 -*-

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from dmpot import distance
from dmpot import draw


from dmpot import ml
from dmpot import feature

from dmpot import draw
import numpy as np


print distance.lcs_sim('abce', 'abecf')
from dmpot import evaluate