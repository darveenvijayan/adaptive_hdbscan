
import timeit
import time
import numpy as np
import hdbscan
import sklearn.datasets as data

def test():
    print('==================== Start ====================')
    # test_data = np.array([[-0.57164688, -0.97735768],
    #             [-1.10797067, -1.03454204],
    #             [ 0.7402006 ,  0.56931596],
    #             [ 0.73285504,  0.84136899],
    #             [ 1.01393778,  1.12031321],
    #             [ 0.92635625,  1.04848789],
    #             [-1.05198656, -0.8509797 ],
    #             [ 0.81312495,  0.69898712],
    #             [-0.72161448, -1.24689847],
    #             [-1.33428595, -0.92862354]])

    moons, _ = data.make_moons(n_samples=225, noise=0.05)
    blobs, _ = data.make_blobs(n_samples=225, centers=[(-0.75,2.25), (1.0, 2.0)], cluster_std=0.4)
    test_data = np.vstack([moons, blobs])

    clusterer = hdbscan.HDBSCAN(min_cluster_size=5, gen_min_span_tree=False)
    clusterer.fit(test_data)

    print('==================== End ====================')

def test2():
    print('==================== Start ====================')
    # blobs, _ = data.make_blobs(n_samples=50, centers=[(-2,4), (2, 4)], cluster_std=0.3)
    # blobs2, _ = data.make_moons(n_samples=50, noise=0.05)
    # test_data = np.vstack([blobs, blobs2])

    test_data = np.load('clusterable_data.npy')

    clusterer = hdbscan.HDBSCAN(min_cluster_size=10, gen_min_span_tree=False)
    clusterer.fit(test_data)
    print('==================== End ====================')

if __name__=="__main__":

    

    # start = time.time()
    # time.sleep(1)
    # test()
    # end = time.time()
    # print((end - start)*1000,'ms')
    # print((end - start),'s')
    # print(1/(end - start),'fps')



    # for i in range(100):
    execution_time = timeit.timeit(test, number=100)
    print('test',execution_time)
    # execution_time = timeit.timeit(test2, number=100)
    # print('test2',execution_time)



    # boruvka, n_samples=100, 100x = 0.22222486598184332
    # prim,    n_samples=100, 100x = 0.20724696799879894

    # boruvka, n_samples=200, 100x = 0.3396061599778477
    # prim,    n_samples=200, 100x = 0.326383864012314

    # boruvka, n_samples=400, 100x = 0.6332883120048791
    # prim,    n_samples=400, 100x = 0.5759929250052664

    # boruvka, n_samples=450, 100x = 0.6704638260125648
    # prim,    n_samples=450, 100x = 0.6547297410143074

    #-----------------------------------------------------------------------

    # boruvka, n_samples=500, 100x = 0.7017132840119302
    # prim,    n_samples=500, 100x = 0.7069316999986768

    # boruvka, n_samples=600, 100x = 0.8466894229932223
    # prim,    n_samples=600, 100x = 0.9055061409890186

    # boruvka, n_samples=1000, 100x = 1.3225931390188634
    # prim,    n_samples=1000, 100x = 1.584193285991205

    # boruvka, n_samples=2000, 100x = 2.646664101019269
    # prim,    n_samples=2000, 100x = 3.8432789770013187

    # boruvka, n_samples=4000, 100x = 5.566422673990019
    # prim,    n_samples=4000, 100x = 10.935613119974732