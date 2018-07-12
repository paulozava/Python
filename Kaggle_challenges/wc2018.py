import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

matches = pd.read_csv('results.csv')
matches =  matches.replace({'Germany DR': 'Germany', 'China': 'China PR'})
matches['date'] = pd.to_datetime(matches['date'])

matches['date','home_team','away_team','home_score','away_score']
matches['date' : 'away_score']

