# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 14:11:31 2020

@author: Horner
"""

import pandas as pd
#import numpy as np

#import dataset
appleStock = pd.read_csv('aapl.us.txt')
#find values of between 1990 and 2001
#appleStock=appleStock[1344:3870]
appleStock = appleStock.iloc[0:]
appleStock.to_csv('appleStock.txt', header=False)

#import dataset
ibmStock = pd.read_csv('ibm.us.txt')
#find values of between 1990 and 2001
#ibmStock=ibmStock[7037:9563]
ibmStock = ibmStock.iloc[0:]
ibmStock.to_csv('ibmStock.txt', header=False)

#import dataset
intelStock = pd.read_csv('intc.us.txt')
#find values of between 1990 and 2001
#intelStock=intelStock[4534:7060]
intelStock = intelStock.iloc[0:]
intelStock.to_csv('intelStock.txt', header=False)

microsoftStock = pd.read_csv('msft.us.txt')
#find values of between 1990 and 2001
#microsoftStock=microsoftStock[962:3487]
microsoftStock = microsoftStock.iloc[0:]
microsoftStock.to_csv('microsoftStock.txt', header=False)

googleStock = pd.read_csv('googl.us.txt')
#find values of between 1990 and 2001
#gooleStock=gooleStock[962:3487]
googleStock = googleStock.iloc[0:]
googleStock.to_csv('googleStock.txt', header=False)