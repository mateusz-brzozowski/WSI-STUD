import matplotlib.pyplot as plt
import numpy as np


def draw_plot(function, bounds, plot_step):
    x_arr = y_arr = np.arange(-bounds, bounds, plot_step)
    X, Y = np.meshgrid(x_arr, y_arr)
    Z = np.empty(X.shape)

    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            Z[i, j] = function(np.array([X[i, j], Y[i, j]]))

    plt.contour(X, Y, Z, 20)


def draw_arrows(points, scale):
    for i in range(len(points)-1):
        delta = points[i+1] - points[i]
        plt.arrow(
            points[i][0], points[i][1],
            delta[0], delta[1],
            head_width=scale * 0.05, head_length=scale * 0.01,
            fc='k', ec='k')


def create_plot(fun, points):
    MAX_POINT = np.amax(points)
    PLOT_STEP = MAX_POINT / 100

    draw_plot(fun, MAX_POINT, PLOT_STEP)
    draw_arrows(points, MAX_POINT)

    plt.show()
