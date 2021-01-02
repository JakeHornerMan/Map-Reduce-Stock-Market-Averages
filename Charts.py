# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 19:53:04 2020

@author: Horner
"""

import matplotlib.pyplot as plt
import pandas as pd

#barChart= pd.read_csv('PythonProject/output/IbmTotalVolume_ReducerOutput.txt')
#year = barChart['date']
#totalvol = barChart['total_vol']
#plt.bar(year, totalvol)
#plt.savefig('PythonProject/output/IBMbar.png')

#barChart= pd.read_csv('PythonProject/output/MicrosoftTotalVolume_ReducerOutput.txt')
#year = barChart['date']
#totalvol = barChart['total_vol']
#plt.bar(year, totalvol)
#plt.savefig('PythonProject/output/Microsoftbar.png')

#barChart= pd.read_csv('PythonProject/output/IntelTotalVolume_ReducerOutput.txt')
#year = barChart['date']
#totalvol = barChart['total_vol']
#plt.bar(year, totalvol)
#plt.savefig('PythonProject/output/Intelbar.png')

#barChart= pd.read_csv('PythonProject/output/AppleTotalVolume_ReducerOutput.txt')
#year = barChart['date']
#totalvol = barChart['total_vol']
#plt.bar(year, totalvol)
#plt.savefig('PythonProject/output/Applebar.png')

#barChart= pd.read_csv('PythonProject/output/GoogleTotalVolume_ReducerOutput.txt')
#year = barChart['date']
#totalvol = barChart['total_vol']
#plt.bar(year, totalvol)
#plt.savefig('PythonProject/output/Googlebar.png')

#lineplot = pd.read_csv('PythonProject/output/AppleAvg_ReducerOutput.txt')
#year = lineplot['date']
#avgopen = lineplot['avg_open']
#plt.plot(year, avgopen)
#plt.savefig('PythonProject/output/Appleline.png')

#lineplot = pd.read_csv('PythonProject/output/IbmAvg_ReducerOutput.txt')
#year = lineplot['date']
#avgopen = lineplot['avg_open']
#plt.plot(year, avgopen)
#plt.savefig('PythonProject/output/IBMline.png')

#lineplot = pd.read_csv('PythonProject/output/MicrosoftAvg_ReducerOutput.txt')
#year = lineplot['date']
#avgopen = lineplot['avg_open']
#plt.plot(year, avgopen)
#plt.savefig('PythonProject/output/Microsoftline.png')

#lineplot = pd.read_csv('PythonProject/output/GoogleAvg_ReducerOutput.txt')
#year = lineplot['date']
#avgopen = lineplot['avg_open']
#plt.plot(year, avgopen)
#plt.savefig('PythonProject/output/Googleine.png')

lineplot = pd.read_csv('PythonProject/output/IntelAvg_ReducerOutput.txt')
year = lineplot['date']
avgopen = lineplot['avg_open']
plt.plot(year, avgopen)
plt.savefig('PythonProject/output/Intelline.png')
