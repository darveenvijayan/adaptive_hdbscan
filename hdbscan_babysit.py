
import timeit
import time
import numpy as np
import hdbscan
import sklearn.datasets as datasets
import resource 

def prim():
    """ CREATE DATA """
    data, _ = datasets.make_moons(n_samples=2000, noise=0.15)

    """ RUN ALGO """
    clusterer = hdbscan.HDBSCAN(min_cluster_size=5, gen_min_span_tree=False)
    clusterer.fit(data, algo='prim')
    # print('look at _hdbscan_generic')

    memMb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0/1024.0
    # print(memMb,'MB')


def boruvka():
    """ CREATE DATA """
    data, _ = datasets.make_moons(n_samples=2000, noise=0.15)

    """ RUN ALGO """
    clusterer = hdbscan.HDBSCAN(min_cluster_size=5, gen_min_span_tree=False)
    clusterer.fit(data, algo='boruvka')
    # print('look at _hdbscan_generic')
    
    memMb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0/1024.0
    # print(memMb,'MB')

if __name__=="__main__":


    print('[ PRIMS ALGO ] ')
    execution_time = timeit.timeit(prim, number=100)
    print('prims',execution_time)


    print('[ BORUVKAS ALGO ] ')
    execution_time = timeit.timeit(boruvka, number=100)
    print('boruvkas',execution_time)


