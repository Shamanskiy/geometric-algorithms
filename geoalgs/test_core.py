import unittest

import core

class TestPoint2D(unittest.TestCase):

    def test_Point2D_default(self):
        A = core.Point2D()
        B = core.Point2D(0,0)
        self.assertEqual(A,B)

    def test_Point2D_NotEqual(self):
        A = core.Point2D(0.0,0.0)
        B = core.Point2D(1.0,2.0)
        self.assertNotEqual(A,B)

    def test_Point2D_Equal(self):
        A = core.Point2D(0.0,0.0)
        B = core.Point2D(0.0,0.0)
        self.assertEqual(A,B)
    
    def test_Point2D_CloseAbs(self):
        A = core.Point2D(0.0,0.0)
        B = core.Point2D(0.0,1e-7)
        self.assertEqual(A,B)

    def test_Point2D_FarAbs(self):
        A = core.Point2D(0.0,0.0)
        B = core.Point2D(0.0,1e-5)
        self.assertNotEqual(A,B)

    def test_Point2D_CloseRel(self):
        A = core.Point2D(1e9,0.0)
        B = core.Point2D(1e9 + 0.99,0.0)
        self.assertEqual(A,B)

    def test_Point2D_CloseRelBoundary(self):
        A = core.Point2D(1e9,0.0)
        B = core.Point2D(1e9 + 1.0,0.0)
        self.assertEqual(A,B)


    def test_Point2D_FarRel(self):
        A = core.Point2D(1e9,0.0)
        B = core.Point2D(1e9 + 1.01,0.0)
        self.assertNotEqual(A,B)

    def test_Point2D_repr(self):
        point = core.Point2D(1,2)
        self.assertEqual(point.__repr__(),'(1,2)')

    def test_Point2D_comparison1(self):
        A = core.Point2D(0.0,0.0)
        B = core.Point2D(1.0,0.0)
        self.assertLess(A,B)

    def test_Point2D_comparison2(self):
        A = core.Point2D(0.0,0.0)
        B = core.Point2D(0.0,1.0)
        self.assertLess(A,B)

    def test_Point2D_comparison1(self):
        A = core.Point2D(0.0,0.0)
        B = core.Point2D(0.0,0.0)
        self.assertFalse(A < B)

    def test_Point2D_sort(self):
        points = [
            core.Point2D(2,0), 
            core.Point2D(1,1),
            core.Point2D(1,0),
            core.Point2D(0,0)
        ]
        ground_truth = [
            core.Point2D(0,0), 
            core.Point2D(1,0),
            core.Point2D(1,1),
            core.Point2D(2,0)
        ]
        sorted_points = sorted(points)
        self.assertEqual(ground_truth,sorted_points)

if __name__ == '__main__':
    unittest.main()