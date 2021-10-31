import matplotlib.pyplot as plt
import numpy as np


def draw_plot(function, bounds, plot_step):
    x_arr = np.arange(-bounds, bounds, plot_step)
    y_arr = np.arange(-bounds, bounds, plot_step)
    X, Y = np.meshgrid(x_arr, y_arr)
    Z = np.empty(X.shape)

    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            Z[i, j] = function(np.array([X[i, j], Y[i, j]]))

    plt.contour(X, Y, Z, 20)


def draw_arrows(points, scale):
    for i in range(1, len(points)-1):
        dx = points[i+1] - points[i]
        plt.arrow(
            points[i][0], points[i][1],
            dx[0], dx[1],
            head_width=scale * 0.05, head_length=scale * 0.01,
            fc='k', ec='k')


def create_plot(function, points):
    point_array = []
    for point in points:
        x_array = []
        for x in point:
            x_array.append(abs(x))
        point_array.append(max(x_array))
    UPPER_BOUND = max(point_array) * 1.2
    PLOT_STEP = UPPER_BOUND / 100

    draw_plot(function, UPPER_BOUND, PLOT_STEP)
    draw_arrows(points, UPPER_BOUND)

    plt.show()
