# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 03:08:23 2022

@author: kalt9
"""

import pandas as pd
import scipy.stats
from scipy.stats import ttest_ind 

diabetes = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Datasets/Diabetes/DB1_Diabetes/diabetic_data.csv')

diabetes.info()

# 1) Difference between sex and the # of days in hospital?
male = diabetes[diabetes['gender']=='Male']
female = diabetes[diabetes['gender']=='Female']

ttest1 = ttest_ind(male['time_in_hospital'], female['time_in_hospital'])
print(ttest1)

# p-value = 1.4217299655114968e-21. p-value < 0.05, indicating there is a
# statistical significant difference between sex and the # of days spent in a hospital.
 
# 2) Difference between race (Caucasian:African American) and the # of days in a hospital?
Caucasian = diabetes[diabetes['race']=='Caucasian']
AfricanAmerican = diabetes[diabetes['race']=='AfricanAmerican']

ttest2 = ttest_ind(Caucasian['time_in_hospital'], AfricanAmerican['time_in_hospital'])
print(ttest2)

# p-value = 4.178330085585203e-07, which is < 0.05, indicating a significant difference
# beween race and the # of days spent in a hospital.

# 3) Difference between race (Asian:African American) and the # of lab procedures performed?
Asian = diabetes[diabetes['race']=='Asian']
AfricanAmerican = diabetes[diabetes['race']=='AfricanAmerican']

ttest3 = ttest_ind(Asian['num_lab_procedures'], AfricanAmerican['num_lab_procedures'])
print(ttest3)

# p-value = 6.948907528800307e-05 which is < 0.05, indicating a significant difference
# between race and the # of lab procedures performed.




