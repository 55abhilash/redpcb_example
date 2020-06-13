#!/usr/bin/python3

import os
from gerber import load_layer
from gerber.render import RenderSettings, theme
from gerber.render.cairo_backend import GerberCairoContext

#GERBER_MAIN = os.path.abspath(os.path.join(os.path.dirname(__file__), 'gerbers'))

## Load All Layers
#Top View Layers
copper = load_layer('gerber_files/copper.GTL')
soldermask = load_layer('gerber_files/soldermask.GTS')
legend = load_layer('gerber_files/silkscreen.GTO')
drill = load_layer('gerber_files/ncdrill.DRD')

#Bottom View Layers
copper_btm = load_layer('gerber_files/bottom_copper.GBL')
soldermask_btm = load_layer('gerber_files/bottom_mask.GBS')

## Color Settings
mask_settings = RenderSettings(color=theme.COLORS['red soldermask'], alpha=0.5, invert=True)
legend_settings = RenderSettings(color=theme.COLORS['white'], alpha=0.8)

## Rendering 
#Top View
cont = GerberCairoContext()
cont.render_layer(copper)
cont.render_layer(soldermask, settings=mask_settings)
cont.render_layer(legend, settings=legend_settings)
cont.render_layer(drill)

cont.dump('gen_images/redpcb.png')

#Clear cont
cont.clear()

#Bottom View
cont.render_layer(copper_btm)
cont.render_layer(soldermask_btm, settings=mask_settings)

cont.dump('gen_images/redpcb_bottom.png')
