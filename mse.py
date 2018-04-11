# -*- coding: utf-8 -*-
"""
Created on Thu Apr 05 19:07:55 2018

@author: sg1014023
"""
X_test =[ 1, 2, 3, 4,5];
Y_test =[ 2, 4, 5, 6,7];
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(X_test,Y_test)
