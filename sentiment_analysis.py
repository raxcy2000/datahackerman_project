import pandas as pd
import numpy as np
import json
import os 

from data_ingestion.ingest import get_data
from parameters.params import combined_data_file_path
from sklearn.model_selection import train_test_split
from autogluon.text import TextPredictor

import warnings
warnings.filterwarnings('ignore')
np.random.seed(42)

data = get_data(combined_data_file_path)
print(data.head(2))

data.rename(columns = {'author.properties.friends': 'friends',
                        'author.properties.status_count': 'status_count',
                        'author.properties.verified': 'verified', 
                        'content.body': 'text', 
                        'location.country': 'country',
                        'properties.platform': 'platform', 
                        'properties.sentiment': 'sentiment', 
                        'location.latitude': 'latitude',
                        'location.longitude': 'longitude'},
                        inplace=True)

df = data[['text', 'sentiment']]
print(df.head())

df = df.dropna(axis=0)


train_data, test_data = train_test_split(
    df[0:50], test_size=0.1, random_state=42
)

predictor = TextPredictor(label='sentiment', eval_metric='acc', path='artefacts/model')
predictor.fit(train_data, time_limit=240)

print("end")