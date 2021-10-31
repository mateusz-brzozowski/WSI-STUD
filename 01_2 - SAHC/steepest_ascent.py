from cec2017.functions import f1, f2, f3
from plot import create_plot
from autograd import grad
import numpy as np

def booth(x):
    return (x[0] + 2*x[1] - 7)**2 + (2*x[0] + x[1] - 5)**2

def steepest_ascent(function, x, beta):
    dx = x.copy()
    points = [dx]
    while not stop(function, points):
        grad_fct = grad(function)
        dx -= beta*grad_fct(dx)
        points.append(dx.copy())
    return points

def stop(function, points):
    if len(points) > 1000:
        return True
    dx = 0.001
    if (function(points[-1]) <= function(points[-1] + [dx, 0]) and
        function(points[-1]) <= function(points[-1] + [-dx, 0]) and
        function(points[-1]) <= function(points[-1] + [0, dx]) and
        function(points[-1]) <= function(points[-1] + [0, -dx])):
        return True
    return False

def draw_steepest_ascent(function, beta):
    UPPER_BOUND = 100
    DIMENSIONALITY = 2
    x = np.random.uniform(-UPPER_BOUND, UPPER_BOUND, size=DIMENSIONALITY)
    print(x)
    points = steepest_ascent(function, x, beta)
    print(points[-1])
    create_plot(function, points)

def main():
    # draw_steepest_ascent(f1, 0.00000001)
    # draw_steepest_ascent(f2, 0.1)
    # draw_steepest_ascent(f3, 0.00003)
    draw_steepest_ascent(booth,0.5)



if __name__ == "__main__":
    main()
