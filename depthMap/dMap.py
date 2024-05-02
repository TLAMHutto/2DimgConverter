import subprocess
import os
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from ipywidgets import FloatSlider
from ipywidgets import GridspecLayout
from prompt_toolkit.formatted_text import PygmentsTokens

import os, contextlib
with open(os.devnull, 'w') as devnull:
    with contextlib.redirect_stdout(devnull):
        import numpy as np
        subprocess.check_call(['pip', 'install', 'numpy-stl'])
        from stl import mesh
        import cv2


print('App running successfully...')

