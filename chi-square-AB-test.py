# Python chi-square A/B test

# Tested in python 2.7.6, numpy 1.9.0, scipy-0.14.0

import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

df=pd.read_csv("AB-test.csv")

# Will print this out
#  version  not-converted  converted
#0       A          18000      32000
#1       B          20000      30000


df = df.set_index('version')


#will clean out the label like this:

#         not-converted  converted
#version                          
#A                18000      32000
#B                20000      30000


observed = df.values

# Transform a Pandas dataframe into numpy array

#[[18000 32000]
# [20000 30000]]

result = chi2_contingency(observed)

# Give the results of

# (169.60955008488963, 9.0042014755951057e-39, 1, array([[ 19000.,  31000.],[ 19000.,  31000.]]))
# (Chi2, p-value,degree of freedom, The expected frequencies, based on the marginal sums of the table.)

chisq, p = result[:2]

print 'chisq = {}, p-value = {}'.format(chisq, p)
