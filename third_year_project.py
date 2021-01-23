# -*- coding: utf-8 -*-
"""Third Year Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ofkm3JsNxb0MfKMG-lTXivQkgLLdUA0D
"""

from DataPreprocessing import FileExtraction, CSVManager
from ModelTrain import Training

import os

import numpy as np

# change directory
os.chdir(r"D:\Third Year Project\CFIE-FRSE-master\output")

directory = os.getcwd()

csvManager = CSVManager("output.csv", directory)

# dp = FileExtraction(directory)

training = Training(csvManager.get_corpus(), csvManager.get_y())

'''
train the model on the corpus, 
and then evaluate with combination of 
the numerical features (make a formula)
'''

# 10000 0.010 random forest
# 10000 -0.138 decision tree

# TODO:
    # Add bag of words