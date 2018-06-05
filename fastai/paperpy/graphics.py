import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patheffects as patheffects

def show_img(im, figsize=None, ax=None):
    if not ax: fig,ax = plt.subplots(figsize=figsize)
    ax.imshow(im)
    #ax.set_xticks(np.linspace(0, 224, 8))
    #ax.set_yticks(np.linspace(0, 224, 8))
    #ax.grid()
    #ax.set_yticklabels([])
    #ax.set_xticklabels([])
    return ax

def draw_outline(o, lw):
    o.set_path_effects([patheffects.Stroke(
        linewidth=lw, foreground='white'), patheffects.Normal()])

def draw_text(ax, xy, txt, sz=14, color='white'):
    text = ax.text(*xy, txt,
        verticalalignment='top', color=color, fontsize=sz, weight='bold')
    draw_outline(text, 1)

def plotImageAndTitleArrays(imgs, titles, grid=(1,12)):
    for i in range(len(imgs)):
        imgs[i] = imgs[i]/np.max(imgs[i])
    fig, axes = plt.subplots(*grid, figsize=(12, 8))
    for i,ax in enumerate(axes.flat):
        ax = show_img(imgs[i],ax=ax)
        draw_text(ax, (0,0), titles[i])
    plt.tight_layout()