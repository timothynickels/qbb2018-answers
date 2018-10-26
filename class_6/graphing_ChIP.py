#!/usr/bin/env python3

"""
Usage: ./graphing_ChIP.py ctcf_gained.bed ctcf_lost.bed Mus_musculus.GRCm38.94_features.bed
"""

import sys
import matplotlib.pyplot as plt
import numpy as np

gain = open(sys.argv[1])
loss = open(sys.argv[2])
features = open(sys.argv[3])

features_Gained = {}
features_Lost = {}
for line in features:
    fieldsF=line.rstrip("\r\n").split("\t")
    gain.seek(0)
    loss.seek(0)
    for i, line in enumerate (gain):
        fieldsG=line.rstrip("\r\n").split("\t")
        if ((int(fieldsG[1]) <= int(fieldsF[2])) & (int(fieldsG[1]) >= int(fieldsF[1]))) | \
        (((int(fieldsG[2]) <= int(fieldsF[2])) & int(fieldsG[2]) >= int(fieldsF[1]))):
            if (fieldsF[3]) in features_Gained:
                features_Gained[fieldsF[3]] += 1
            else:
                features_Gained[fieldsF[3]] = 1
    for j, line in enumerate (loss):
        fieldsL=line.rstrip("\r\n").split("\t")
        if ((int(fieldsL[1]) <= int(fieldsF[2])) & (int(fieldsL[1]) >= int(fieldsF[1]))) | \
        (((int(fieldsL[2]) <= int(fieldsF[2])) & int(fieldsL[2]) >= int(fieldsF[1]))):           
            if (fieldsF[3]) in features_Lost:
                features_Lost[fieldsF[3]] += 1
            else:
                features_Lost[fieldsF[3]] = 1

numOtherGain = numGain = i+1
numOtherLoss = numLoss = j+1
for value in features_Gained:
    numOtherGain = numOtherGain - features_Gained[value]
for value in features_Lost: 
    numOtherLoss = numOtherLoss - features_Lost[value]
features_Gained['other'] = numOtherGain
features_Lost['other'] = numOtherLoss
panelLeftX = []
panelLeftY = []
for key in features_Gained:
    panelLeftX.append("Gain in " + key)
    panelLeftY.append(features_Gained[key])
for key in features_Lost: 
    panelLeftX.append("Loss in " + key)
    panelLeftY.append(features_Lost[key])
    
fig, axes = plt.subplots(1,2,figsize=(30,15))
fig.suptitle("CTCF ChIP Summary", fontsize=35)
axes[0].set_ylabel("Number")
axes[0].bar(panelLeftX, panelLeftY)
axes[0].tick_params('x', rotation=20)
axes[1].set_xlabel("Type")
axes[1].set_ylabel("Number")
axes[1].bar(['Peaks Gained', 'Peaks Lost'], [numGain, numLoss])
fig.savefig("CTCF_ChIP_Summary.png")
plt.close(fig)