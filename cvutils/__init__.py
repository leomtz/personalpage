# Tool to handle CVs
# Created by Leonardo Ignacio Martínez Sandoval
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'

# openpyxl helps to work with MSExcel databases
import openpyxl as opx

# We import the following to create plots
import numpy as npy
import matplotlib.pyplot as plt

from cvutils.primaryclasses import *
from cvutils.itemclasses import * 