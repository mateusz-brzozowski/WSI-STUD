from cec2017.functions import f1, f2, f3
from plot import create_plot
from autograd import grad
import numpy as np

def booth(x):
    return (x[0] + 2*x[1] - 7)**2 + (2*x[0] + x[1] - 5)**2

def steepest_ascent(function, x, beta, n):
    dx = x.copy()
    points = []
    for _ in range(n):
        grad_fct = grad(function)
        dx -= beta*grad_fct(dx)
        points.append(dx.copy())
    return points

def main():
    UPPER_BOUND = 200
    DIMENSIONALITY = 2
    x = np.random.uniform(-UPPER_BOUND, UPPER_BOUND, size=DIMENSIONALITY)
    print("1-st point: ", x)
    # points = steepest_ascent(f1, x, 0.00000001, 40)
    # points = steepest_ascent(f2, x, 0.5, 400)
    # points = steepest_ascent(f3, x, 0.00005, 40)
    points = steepest_ascent(booth, x, 0.05, 40)
    create_plot(booth, points)


if __name__ == "__main__":
    main()
