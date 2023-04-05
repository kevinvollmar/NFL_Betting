
import pandas as pd
import os
import urllib.request
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnnotationBbox
import csv

df = pd.read_csv('https://raw.githubusercontent.com/kevinvollmar/NFL_Betting/main/spreadspoke_scores.csv?token=GHSAT0AAAAAACACUSHOJG7FN3BTH7PICRXCZASCWPA')

#avg = df.mean()

#print(df.describe())

x = df['team_home']
y = df['score_home'].mean()

plt.bar(x, y, color = 'g', label = 'Avg')
plt.xlabel('Teams')
plt.ylabel('Avg Score')
plt.title('Avg Scores for Each Team')
plt.legend()
plt.show()