import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (10, 5)

complaints = pd.read_csv('311-service-requests.csv')
complaints[:5]['Complaint Type']
