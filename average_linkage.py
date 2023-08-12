# import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

# Prepare data and labels
dataset = np.array([[1,1],
                [1.5,1.5],
                [5,5],
                [3,4],
                [4,4],
                [3,3.5]
                ])

labels = ['A','B','C','D','E','F']

def average_linkage(data):
    
    average_clustering = linkage(data, method="average", metric="euclidean", optimal_ordering=True)
    
    # plot dendogram
    fig = plt.figure(figsize=(8, 4))
    plt.title('Average Linkage Hierarchical Clustering Dendrogram')
    plt.xlabel('index')
    plt.ylabel('distance')
    dendrogram(average_clustering,
               labels = labels,  # rotates the x axis labels
               leaf_font_size=8.,  # font size for the x axis labels
              )
    plt.show()
    
    
average_linkage(dataset)


