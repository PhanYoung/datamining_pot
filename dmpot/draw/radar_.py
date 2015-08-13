# -*- coding: utf-8 -*-

"""
Example of creating a radar chart (a.k.a. a spider or star chart) [1]_.

Although this example allows a frame of either 'circle' or 'polygon', polygon
frames don't have proper gridlines (the lines are circles instead of polygons).
It's possible to get a polygon grid by setting GRIDLINE_INTERPOLATION_STEPS in
matplotlib.axis to the desired number of vertices, but the orientation of the
polygon is not aligned with the radial axes.

.. [1] http://en.wikipedia.org/wiki/Radar_chart
"""
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.spines import Spine
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection
import json
from colors_ import make_colors

def radar_factory(num_vars, frame='polygon'):
    """Create a radar chart with `num_vars` axes.

    This function creates a RadarAxes projection and registers it.

    Parameters
    ----------
    num_vars : int
        Number of variables for radar chart.
    frame : {'circle' | 'polygon'}
        Shape of frame surrounding axes.

    """
    # calculate evenly-spaced axis angles
    theta = 2*np.pi * np.linspace(0, 1-1./num_vars, num_vars)
    # rotate theta such that the first axis is at the top
    theta += np.pi/2

    def draw_poly_patch(self):
        verts = unit_poly_verts(theta)
        return plt.Polygon(verts, closed=True, edgecolor='k')

    def draw_circle_patch(self):
        # unit circle centered on (0.5, 0.5)
        return plt.Circle((0.5, 0.5), 0.5)

    patch_dict = {'polygon': draw_poly_patch, 'circle': draw_circle_patch}
    if frame not in patch_dict:
        raise ValueError('unknown value for `frame`: %s' % frame)

    class RadarAxes(PolarAxes):

        name = 'radar'
        # use 1 line segment to connect specified points
        RESOLUTION = 1
        # define draw_frame method
        draw_patch = patch_dict[frame]

        def fill(self, *args, **kwargs):
            """Override fill so that line is closed by default"""
            closed = kwargs.pop('closed', True)
            return super(RadarAxes, self).fill(closed=closed, *args, **kwargs)

        def plot(self, *args, **kwargs):
            """Override plot so that line is closed by default"""
            lines = super(RadarAxes, self).plot(*args, **kwargs)
            for line in lines:
                self._close_line(line)

        def _close_line(self, line):
            x, y = line.get_data()
            # FIXME: markers at x[0], y[0] get doubled-up
            if x[0] != x[-1]:
                x = np.concatenate((x, [x[0]]))
                y = np.concatenate((y, [y[0]]))
                line.set_data(x, y)

        def set_varlabels(self, labels):
            self.set_thetagrids(theta * 180/np.pi, labels)

        def _gen_axes_patch(self):
            return self.draw_patch()

        def _gen_axes_spines(self):
            if frame == 'circle':
                return PolarAxes._gen_axes_spines(self)
            # The following is a hack to get the spines (i.e. the axes frame)
            # to draw correctly for a polygon frame.

            # spine_type must be 'left', 'right', 'top', 'bottom', or `circle`.
            spine_type = 'circle'
            verts = unit_poly_verts(theta)
            # close off polygon by repeating first vertex
            verts.append(verts[0])
            path = Path(verts)

            spine = Spine(self, spine_type, path)
            spine.set_transform(self.transAxes)
            return {'polar': spine}

    register_projection(RadarAxes)
    return theta


def unit_poly_verts(theta):
    """Return vertices of polygon for subplot axes.

    This polygon is circumscribed by a unit circle centered at (0.5, 0.5)
    """
    x0, y0, r = [0.5] * 3
    verts = [(r*np.cos(t) + x0, r*np.sin(t) + y0) for t in theta]
    return verts






def draw_radar(data, spoke_labels=None, grids=[0.2, 0.4, 0.6, 0.8], 
               auto_scale=False, color='b'):
    
    N = len(data)
    theta = radar_factory(N, frame='polygon')
    fig = plt.figure()
    fig.subplots_adjust(wspace=0.05, hspace=0.50, top=0.95, bottom=0.1)
    
    ax = fig.add_subplot(111, projection='radar')
    if not auto_scale:
        plt.axhspan(0, 1, 0, 1, visible=False)
    plt.rgrids(grids)
    ax.plot(theta, data, color=color)
    ax.fill(theta, data, facecolor=color, alpha=0.25)
    if not spoke_labels:
        spoke_labels = [''] * N
    ax.set_varlabels(spoke_labels)
  #  plt.show()
    
    
def draw_radar_set(datas, n_cols, n_rows=None, titles=None, colors=None, 
                   auto_scale=False, grids=[0.2, 0.4, 0.6, 0.8],
                   spoke_labels=None, figsize=(12, 26), pic_title=None,
                   save_path=None):
    datas = np.array(datas)
    
    n_datas, n_indice = datas.shape
    
    if not n_rows:
        n_rows = (len(datas) + n_cols - 1) / n_cols + 1
        
    if not colors:    
        colors = make_colors(n_datas)
        
    if not titles:
        titles = [str(i) for i in xrange(1, n_datas+1)]
    
    if not spoke_labels:
        spoke_labels = [''] * n_indice
        
       
    fig = plt.figure(figsize=figsize)
    fig.subplots_adjust(wspace=0, hspace=0.5, top=0.95, bottom=0.1)
    theta = radar_factory(n_indice, frame='polygon')
    

    def draw_all(datas, title="COMBINE"):
        ax = fig.add_subplot(n_rows, n_cols, 1, projection='radar')
        if not auto_scale:
            plt.axhspan(0, 1, 0, 1, visible=False)
        plt.rgrids(grids)
        ax.set_title(title, weight='bold', size='medium', position=(0.5, 1.08),
                     horizontalalignment='center', verticalalignment='center')
        for d, color in zip(datas, colors):
            ax.plot(theta, d, color=color)
            ax.fill(theta, d, facecolor=color, alpha=0.25)
        ax.set_varlabels(spoke_labels)       
                
    def draw_sub(data, pos, title, color):
        ax = fig.add_subplot(n_rows, n_cols, pos, projection='radar')
        if not auto_scale:
            plt.axhspan(0, 1, 0, 1, visible=False)
        plt.rgrids(grids)
        ax.set_title(title, weight='bold', size='medium', position=(0.5, 1.08),
                     horizontalalignment='center', verticalalignment='center')
        ax.plot(theta, data, color=color)
        ax.fill(theta, data, facecolor=color, alpha=0.25)
        ax.set_varlabels(spoke_labels)
    
    if pic_title:   
        plt.figtext(0.5, 1.01, pic_title,
                    ha='center', color='black', weight='bold', size='large')
    
    draw_all(datas)
    for i, (d, c, t) in enumerate(zip(datas, colors, titles)):
        draw_sub(d, i+2, t, c)
        

    if save_path:
        plt.savefig(save_path)
    
        
