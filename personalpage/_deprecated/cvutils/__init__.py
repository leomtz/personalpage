# Tool to handle CVs
# Created by Leonardo Ignacio Martínez Sandoval
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'

# openpyxl helps to work with MSExcel databases
import openpyxl as opx

from . import itemclasses
from . import primaryclasses