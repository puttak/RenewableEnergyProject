# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 00:06:12 2018

@author: Dmob
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import turtle
import time
import random
import os
import dbm
import pickle
import copy
from collections import namedtuple
import re



def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result
    
    
factorial(5)