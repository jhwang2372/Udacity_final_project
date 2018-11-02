import csv
import numpy as np
import pandas as pd

pp = np.load('prob.npy')
pp = pp.reshape(12500,1)

ind = np.arange(1,12501, 1)
ind = ind.reshape(12500, 1)

pd_data = pd.DataFrame({"ID" : np.arange(12500)+1, "label" : 1.0})
for i, p in enumerate(pp):
    pd_data.at[i, 'label'] = p

#pd_data = pd.DataFrame(pp, columns =['label'])
pd_data.to_csv('submission.csv', index=0)

