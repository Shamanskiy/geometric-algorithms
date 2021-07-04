import unittest

import core

class TestPoint(unittest.TestCase):

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

if __name__ == '__main__':
    unittest.main()