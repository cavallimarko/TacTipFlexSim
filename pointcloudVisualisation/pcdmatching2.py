from functools import partial
import matplotlib.pyplot as plt
from pycpd import RigidRegistration
import numpy as np
from mpl_toolkits.mplot3d import Axes3D



def visualize(iteration, error, X, Y, ax):
    plt.cla()
    ax.scatter(X[:, 0],  X[:, 1], X[:, 2], color='red', label='Target')
    ax.scatter(Y[:, 0],  Y[:, 1], Y[:, 2], color='blue', label='Source')
    ax.text2D(0.87, 0.92, 'Iteration: {:d}\nQ: {:06.4f}'.format(
        iteration, error), horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize='x-large')
    ax.legend(loc='upper left', fontsize='x-large')
    plt.draw()
    plt.pause(0.1)
    #print(error)


def main():
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits import mplot3d

    # actual code to load,slice and display the point cloud

    data_path = "PointClouds/"
    filename = "MeasurementLRot10.0.txt"
    point_cloud = np.loadtxt(data_path + filename)
    mean_Z = np.mean(point_cloud, axis=0)[2]
    # spatial_query=point_cloud[abs( point_cloud[:,2]-mean_Z)<1000]
    point_cloud[point_cloud[:, 2] < 0, 2] = 150
    spatial_query = point_cloud
    xyz = spatial_query[:, :3]
    xyz=xyz[xyz[:,2] <150]
    filename1 = "MeasurementLRot20.0.txt"
    point_cloud1 = np.loadtxt(data_path + filename1)
    mean_Z1 = np.mean(point_cloud1, axis=0)[2]
    # spatial_query=point_cloud[abs( point_cloud[:,2]-mean_Z)<1000]
    point_cloud1[point_cloud1[:, 2] < 0, 2] = 150
    spatial_query1 = point_cloud1
    xyz1 = spatial_query1[:, :3]
    xyz1=xyz1[xyz1[:,2] <150]
    X = xyz
    # synthetic data, equaivalent to X + 1
    Y = xyz1

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    callback = partial(visualize, ax=ax)

    reg = RigidRegistration(**{'X': X, 'Y': Y})
    reg.register(callback)
    plt.show()


if __name__ == '__main__':
    main()