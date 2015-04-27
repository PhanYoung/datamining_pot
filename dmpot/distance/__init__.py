# -*- coding: utf-8 -*-
"""
The :mod:`mlpot.distance` module gathers popular distance calculating
algorithms.
"""
from __future__ import absolute_import

from numpy.linalg import norm

from .vector_dist_ import cosine
from .vector_dist_ import pearson
from .vector_dist_ import euclid

from .sequense_dist_ import editdist
from .sequense_dist_ import norm_editdist
from .sequense_dist_ import lcs
from .sequense_dist_ import lcs_sim

from .set_sim_ import jaccard
from .set_sim_ import dice
from .set_sim_ import cover_sim

__all__ = ['cosine',
           'pearson',
           'editdist',
           'norm_editdist',
           'lcs',
           'lcs_sim',
           'jaccard',
           'dice',
           'cover_sim',
           'euclid']