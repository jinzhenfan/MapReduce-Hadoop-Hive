# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 00:48:04 2013

@author: jinzhen
"""
import numpy as np
import csv

beta_hat=beta_hat = np.empty(6)


with open('outfile.txt','w') as out:

    output = csv.writer(out, delimiter='\n')
    output.writerow(beta_hat)

out.closed