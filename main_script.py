# In[0]: IMPORT AND FUNCTIONS
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import FeatureUnion
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer  
from sklearn.preprocessing import OneHotEncoder      
from sklearn.model_selection import KFold   
from statistics import mean
import joblib 

# In[1]: STEP 1. LOOK AT THE BIG PICTURE (DONE)
# In[2]: STEP 2. GET THE DATA (DONE). LOAD DATA


