
import timeit
import time
import numpy as np
import hdbscan
import sklearn.datasets as datasets
import resource 

def prim():
    total_mem = 0
    total_time = 0
    for i in range(100):

        """ CREATE DATA """
        data, _ = datasets.make_moons(n_samples=2000, noise=0.15)

        """ RUN ALGO """
        start_time = time.time()
        clusterer = hdbscan.HDBSCAN(min_cluster_size=5, gen_min_span_tree=False)
        clusterer.fit(data, algo='prim')


        total_time+= time.time()-start_time
        total_mem += resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0/1024.0

    print('total iteration : ', i+1)
    print('Memory used : ', total_mem/(i+1),'kB')
    print('Total time taken : ',total_time/(i+1),'seconds')


def boruvka():
    total_mem = 0
    total_time = 0
    for i in range(100):

        """ CREATE DATA """
        data, _ = datasets.make_moons(n_samples=2000, noise=0.15)

        """ RUN ALGO """
        start_time = time.time()
        clusterer = hdbscan.HDBSCAN(min_cluster_size=5, gen_min_span_tree=False)
        clusterer.fit(data, algo='boruvka')


        total_time+= time.time()-start_time
        total_mem += resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0/1024.0

    print('total iteration : ', i+1)
    print('Memory used : ', total_mem/(i+1),'kB')
    print('Total time taken : ',total_time/(i+1),'seconds')

if __name__=="__main__":

    
    print('[ PRIMS ALGO ] ')
    prim()
    print()
    print()


    print('[ BORUVKAS ALGO ] ')
    boruvka()


    # print('[ PRIMS ALGO ] ')
    # execution_time = timeit.timeit(prim, number=100)
    # print('prims',execution_time)


    # print('[ BORUVKAS ALGO ] ')
    # execution_time = timeit.timeit(boruvka, number=100)
    # print('boruvkas',execution_time)
