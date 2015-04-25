# -*- coding: utf-8 -*-
"""
The :mod:`mlpot.distance` module gathers popular distance calculating
algorithms.
"""
from __future__ import absolute_import, unicode_literals
from .vector_dist_ import cosine
from .vector_dist_ import pearson
from .str_dist_ import edit_dist

__all__ = ['cosine',
           'pearson',
           'edit_dist'
            ]