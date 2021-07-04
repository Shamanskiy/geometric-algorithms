import unittest

import core
import convexhull

class TestConvexHull(unittest.TestCase):

    def test_PointsMakeRightTurn_True(self):
        A = core.Point2D(0,0)
        B = core.Point2D(0,1)
        C = core.Point2D(1,0)
        self.assertTrue(convexhull.points_make_a_right_turn(A,B,C))

    def test_PointsMakeRightTurn_False(self):
        A = core.Point2D(0,0)
        B = core.Point2D(1,0)
        C = core.Point2D(0,1)
        self.assertFalse(convexhull.points_make_a_right_turn(A,B,C))

    def test_PointsMakeRightTurn_Colinear(self):
        A = core.Point2D(0,0)
        B = core.Point2D(0,1)
        C = core.Point2D(0,2)
        self.assertFalse(convexhull.points_make_a_right_turn(A,B,C))

    def test_PointsMakeRightTurn_Coinciding(self):
        A = core.Point2D(0,0)
        B = core.Point2D(0,0)
        C = core.Point2D(0,2)
        self.assertFalse(convexhull.points_make_a_right_turn(A,B,C))

    def test_ConvexHull_trivial(self):
        input_points = [
            core.Point2D(-1,0),
            core.Point2D(1,0),
            core.Point2D(0,-1),
            core.Point2D(0,1),
            core.Point2D(-0.5,0)
        ]
        ground_truth = [
            core.Point2D(-1,0), 
            core.Point2D(0,1),
            core.Point2D(1,0),
            core.Point2D(0,-1)
        ]

        convex_hull = convexhull.convex_hull_2D(input_points)
        self.assertEqual(ground_truth,convex_hull)

if __name__ == '__main__':
    unittest.main()