# Demo für dbscan mit schöner visualisierung mithilfe pandas
# Quelle: https://www.youtube.com/watch?v=Q7iWANbkFxk

import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure # neu
from pandas import DataFrame #neu für visualisierung 
#from sklearn import metrics
#from sklearn.preprocessing import StandardScaler

# Generate sample data
X, _ = make_blobs(n_samples=500, centers=3, n_features=2   , random_state=20)
# n_features=Dimension _ = labels egal da uninformed learning!

#visualisierung
df =  DataFrame(dict(x=X[:,0], y=X[:,1])) 
fig, ax = plt.subplots(figsize=(8,8))
df.plot(ax=ax , kind='scatter' , x='x' , y='y')
plt.show()


# Compute DBSCAN
db = DBSCAN(eps=1, min_samples=5).fit(X)
labels = db.labels_  # liste von labels von dbscan erzeugt!
print(len(set(labels)))   # anzahl von labels

#core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
#core_samples_mask[db.core_sample_indices_] = True

#visualisierung
df =  DataFrame(dict(x=X[:,0], y=X[:,1],label=labels)) 
fig, ax = plt.subplots(figsize=(8,8))
colors= {-1:'red', 0:'blue', 1:'orange', 2:'green', 3:'skyblue'}
grouped=df.groupby('label')
for key, group in grouped:
    group.plot(ax=ax , kind='scatter' , x='x' , y='y', label=key,color=colors[key])
plt.show()

