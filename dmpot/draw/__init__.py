# -*- coding: utf-8 -*-

from matplotlib.pyplot import hist
from .histogram_ import split_hist
from .histogram_ import bins_hist
from .histogram_ import desc_distribute

__all__ = ['hist',
           'bins_hist',
           'split_hist',
           'desc_distribute']