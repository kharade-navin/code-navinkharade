import re
import os
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os as os
import json

### Set wd
path="C:/BMI"
os.chdir(path)

# Read JSON data into python
import json
with open('BMI.json', 'r') as datafile:
    data = json.load(datafile)

BMI_df = pd.DataFrame(data)
BMI_df.shape
BMI_df

BMI_df["BMI"] = (BMI_df["WeightKg"]/(BMI_df["HeightCm"]/100)**2).round(2)

# create a list of conditions
conditions = [
    (BMI_df["BMI"] < 18.4),
    (BMI_df["BMI"] >= 18.5) & (BMI_df["BMI"] < 25),
    (BMI_df["BMI"] >= 25) & (BMI_df["BMI"] < 30),
    (BMI_df["BMI"] >= 30) & (BMI_df["BMI"] < 35),
    (BMI_df["BMI"] >= 35) & (BMI_df["BMI"] < 40),
    (BMI_df["BMI"] >= 40)    
    ]

# create a list of the values we want to assign for each condition
values1 = ['Underweight', 'Normal weight', 'Overweight','Moderately obese', 'Severely obese','Very severely obese']
values2 = ['Malnutrition risk', 'Low risk', 'Enhanced risk','Medium risk', 'High risk','Very high risk']

BMI_df['BMI_Category'] = np.select(conditions, values1)
BMI_df['Health_risk']  = np.select(conditions, values2)
BMI_df

Count_Overweight = len(BMI_df[(BMI_df["BMI"] >= 25) & (BMI_df["BMI"] < 30)])
Count_Overweight

BMI_df.to_json(r'BMI_Results.json',orient='records', lines=True)
