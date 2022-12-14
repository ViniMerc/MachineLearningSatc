# -*- coding: utf-8 -*-
"""Machine Learning 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dc1Fgk3wGK55sZMXFL7Ma3GTEa6Dc5ny
"""

import pandas as pd
import numpy as np

dataset = pd.read_csv('titanic.csv',index_col=False)

dataset.head()

dataset.shape

dataset.describe

dataset.info()

dataset.index

dataset.columns

dataset = dataset.drop(['Name', 'Ticket','SibSp', 'Parch', 'Cabin'], axis=1)
#dataset.drop(['Name', 'Ticket','SibSp', 'Parch', 'Cabin'], axis=1, inplace=True)

dataset

from sklearn import preprocessing

scaler = preprocessing.StandardScaler() #modelo de padronização scalonalizador

fare = dataset['Fare'].values

fare

fare_scaled = scaler.fit_transform(fare.reshape(-1,1))

fare_scaled

dataset['Fare'] = fare_scaled

dataset.head()

scaler = preprocessing.MinMaxScaler()

fare_scaled = scaler.fit_transform(fare.reshape(-1,1))

dataset['Fare'] = fare_scaled

dataset.head()

encoder = preprocessing.OrdinalEncoder()

sex = dataset['Sex'].values

sex_encoder = encoder.fit_transform(sex.reshape(-1,1))

dataset['Sex_encoded'] = sex_encoder

dataset.head()

one_hot_encoder = preprocessing.OneHotEncoder()

sex_one_hot_encoder = one_hot_encoder.fit_transform(dataset['Sex'].values.reshape(-1,1))

one_hot_encoder.get_feature_names(['Sex'])

sex_one_hot_encoder_values = sex_one_hot_encoder.toarray()

sex_one_hot_encoder_values.shape

dataset[one_hot_encoder.get_feature_names(['Sex'])] = sex_one_hot_encoder_values

dataset

dataset.isnull().sum()

dataset["Age"].fillna(dataset['Age'].mean(), inplace = True)

dataset.isnull().sum()

dataset.dropna(axis=0,inplace=True)

# Commented out IPython magic to ensure Python compatibility.
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline

sns.boxplot(x = dataset['Fare'])

hi_filter = dataset['Fare'].quantile(0.99)

lo_filter = dataset['Fare'].quantile(0.1)

dataset = dataset[(dataset['Fare']>lo_filter) & (dataset['Fare']<hi_filter)]

