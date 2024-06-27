import pandas as pd
import matplotlib.pyplot as plt


plt.style.use('ggplot')

plt.rcParams['figure.figsize'] = (10, 5)

bikes = pd.read_csv('bikes.csv')
bikes['Berri 1'].plot()
berri_bikes = bikes[['Berri 1']].copy()
berri_bikes[:5]