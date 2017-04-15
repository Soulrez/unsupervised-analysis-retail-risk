import numpy as np
from numpy import linalg
from numpy.linalg import norm
from scipy.spatial.distance import squareform, pdist
import sklearn
from sklearn.manifold import TSNE
from sklearn.datasets import load_digits
from sklearn.preprocessing import scale
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.manifold.t_sne import (_joint_probabilities,
                                    _kl_divergence)
from sklearn.utils.extmath import _ravel
import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects
import matplotlib
from os import listdir
from os.path import isfile, join

# Random state.
RS = 20150101
#points = np.empty([2,2])
def scatter(x):
    f = plt.figure(figsize=(10, 10))
    sc = plt.scatter(x[:,0], x[:,1],c=x[:,1],cmap=plt.cm.get_cmap("jet", 10))
    plt.savefig('tsne-generated.png', dpi=120)

def get_points(filename):
    with open('data/safeway/'+filename) as f:
        data = [map(float, i.split(',')) for i in f]
        data_transform = TSNE(random_state=RS).fit_transform(data)
        #global points
        #if filename=='xaa':
            #print('Before:' + str(len(points)))
            #points = data_transform
            #print('After:' + str(len(points)))
        #else:
            #print('Before:' + str(len(points)))
            #points = np.concatenate([points,data_transform])
            #print('After:' + str(len(points)))
        #print points
        scatter(data_transform)

if __name__ == '__main__':
    files = ["report.csv"]
    for filename in files:
        get_points(filename)
    #global points
    #scatter(points)
