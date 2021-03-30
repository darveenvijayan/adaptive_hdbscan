
import timeit
import time
import numpy as np
import hdbscan
import sklearn.datasets as data

def test():
    print('==================== Start ====================')
    test_data = np.array([[-0.57164688, -0.97735768],
                [-1.10797067, -1.03454204],
                [ 0.7402006 ,  0.56931596],
                [ 0.73285504,  0.84136899],
                [ 1.01393778,  1.12031321],
                [ 0.92635625,  1.04848789],
                [-1.05198656, -0.8509797 ],
                [ 0.81312495,  0.69898712],
                [-0.72161448, -1.24689847],
                [-1.33428595, -0.92862354]])

    # moons, _ = data.make_moons(n_samples=50, noise=0.05)
    # blobs, _ = data.make_blobs(n_samples=50, centers=[(-0.75,2.25), (1.0, 2.0)], cluster_std=0.4)
    # test_data = np.vstack([moons, blobs])

    clusterer = hdbscan.HDBSCAN(min_cluster_size=5, gen_min_span_tree=False)
    clusterer.fit(test_data)
    # print(clusterer.minimum_spanning_tree_.to_numpy())
    print('==================== End ====================')

def test2():
    blobs, _ = data.make_blobs(n_samples=50, centers=[(-2,4), (2, 4)], cluster_std=0.3)
    blobs2, _ = data.make_moons(n_samples=50, noise=0.05)
    test_data = np.vstack([blobs, blobs2])

    clusterer = hdbscan.hdbscan(test_data, min_cluster_size=5, gen_min_span_tree=True)

    # print(clusterer)

if __name__=="__main__":

    

    start = time.time()
    test()
    end = time.time()
    print((end - start)*1000,'ms')
    # for i in range(100):
    # execution_time = timeit.timeit(test, number=100)
    # print('test',execution_time)
    # execution_time = timeit.timeit(test2, number=100)
    # print('test2',execution_time)


