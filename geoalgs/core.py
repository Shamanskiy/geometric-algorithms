from math import isclose
import numpy as np

MY_ABS_TOL = 1e-6
MY_REL_TOL = 1e-9

class Point2D:

    def __init__(self, x = 0, y = 0):
        self.coords = np.array([x,y])

    def __repr__(self):
        return f'({self.coords[0]},{self.coords[1]})'

    def __eq__(self,other):
        return isclose(self.coords[0],other.coords[0],rel_tol=MY_REL_TOL,abs_tol=MY_ABS_TOL) \
            and isclose(self.coords[1],other.coords[1],rel_tol=MY_REL_TOL,abs_tol=MY_ABS_TOL)

    def __lt__(self, other):
        return self.coords[0] < other.coords[0] or \
            (isclose(self.coords[0],other.coords[0],rel_tol=MY_REL_TOL,abs_tol=MY_ABS_TOL) \
                and self.coords[1] < other.coords[1])

    def x(self):
        return self.coords[0]

    def y(self):
        return self.coords[1]