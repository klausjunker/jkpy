# https://analyticsindiamag.com/hands-on-tutorial-on-mean-shift-clustering-algorithm/
# kleine Fehler angepasst: neuer paketort für make_blobs, variablen falsch
import numpy as np
import pandas as pd
from sklearn.cluster import MeanShift
#from sklearn.datasets.samples_generator import make_blobs (alte Versionen!)
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
coordinates = [[2, 2, 3], [6, 7, 8], [5, 10, 13]]
X, _ = make_blobs(n_samples = 120, centers = coordinates,cluster_std = 0.60)
data_fig = plt.figure(figsize=(12, 10))  
ax = data_fig.add_subplot(111, projection ='3d')  
ax.scatter(X[:, 0], X[:, 1], X[:, 2], marker ='o',color ='green')  
plt.show()
from sklearn.cluster import  estimate_bandwidth
bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=500)
msc = MeanShift(bandwidth=bandwidth, bin_seeding=True)
msc.fit(X)
cluster_centers = msc.cluster_centers_
labels = msc.labels_
print(f"labels: {labels}")
labels_unique= np.unique(labels)
print(f"unique labels: {labels_unique}")
n_clusters = len(labels_unique)
print(f"anzahl cluster: {n_clusters}")
print(n_clusters)
msc_fig = plt.figure(figsize=(12, 10))
ax = msc_fig.add_subplot(111, projection ='3d')
ax.scatter(X[:, 0], X[:, 1], X[:, 2], marker ='o',color ='yellow')
ax.scatter(cluster_centers[:, 0], cluster_centers[:, 1],
           cluster_centers[:, 2], marker ='o', color ='green',
          s = 300, linewidth = 5, zorder = 10)
plt.title('Estimated number of clusters: %d' % n_clusters)  
plt.show()
print("ende demo mean-shift-3D")
