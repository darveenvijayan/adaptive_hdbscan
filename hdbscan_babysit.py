print('Start')
import numpy as np
import hdbscan

def test():
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

    clusterer = hdbscan.HDBSCAN(min_cluster_size=5, gen_min_span_tree=True)
    print(clusterer.fit(test_data))
    print(clusterer.minimum_spanning_tree_.to_numpy())


if __name__=="__main__":
    test()


print('Done')
