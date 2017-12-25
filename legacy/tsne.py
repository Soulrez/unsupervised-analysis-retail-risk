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

#points = np.empty([2,2])
def scatter(x,state):
    f = plt.figure(figsize=(5, 5))

    # Calculate the L2 norm for coloring purposes
    x1,y1 = x[:,0], x[:,1]
    l2 = []
    for i in range(0,len(x)):
        l2.append(np.sqrt(x1[i]**2 + y1[i]**2))

    sc = plt.scatter(x[:,0], x[:,1],c=np.asarray(l2),cmap=plt.cm.get_cmap("jet", 10))
    #sc = plt.scatter(x[:,0], x[:,1],c=np.linalg.norm(x[:,0]-x[:,1]),cmap=plt.cm.get_cmap("jet", 10))
    plt.axis('off')
    plt.savefig('plots/tsne-'+state+'.png', dpi=600)

def get_points(filename):
    with open('data/safeway/'+filename) as f:
        data = [map(float, i.split(',')) for i in f]
        
        # Perplexity Hyperparameters
        pe = [2,5,30,50,100]
        # Iteration Hyperparameters
        it = [200,600,1200,10000]
        for i in pe:
        	for j in it:
        		data_transform = TSNE(perplexity=i,n_iter=j).fit_transform(data)
        		scatter(data_transform,str(i)+'-'+str(j))
        
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
        
if __name__ == '__main__':
    files = ["report.csv"]
    for filename in files:
        get_points(filename)
    #global points
    #scatter(points)
