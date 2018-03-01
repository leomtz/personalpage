# openpyxl helps to work with MSExcel databases
import openpyxl as opx

# We import the following to create plots
import numpy as npy
import matplotlib.pyplot as plt

from cvutils.primaryclasses import *
from cvutils.itemclasses import * 

# The test
def test():
    cv = cv_from_xlsx(r'data/CV.xlsx')
    print("Success")
    return cv
