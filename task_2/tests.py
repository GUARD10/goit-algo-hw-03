import math
import unittest

from task_2.koch_algo import koch


class FakeTurtle:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.angle = 0.0
        self.path = []

    def forward(self, dist):
        rad = math.radians(self.angle)
        self.x += dist * math.cos(rad)
        self.y += dist * math.sin(rad)
        self.path.append((round(self.x, 5), round(self.y, 5)))

    def left(self, deg):
        self.angle += deg

    def right(self, deg):
        self.angle -= deg


class TestKoch(unittest.TestCase):

    def test_level_0(self):
        t = FakeTurtle()
        koch(t, 9, 0)
        self.assertEqual(len(t.path), 1)
        self.assertAlmostEqual(t.path[0][0], 9.0)
        self.assertAlmostEqual(t.path[0][1], 0.0)

    def test_level_1(self):
        t = FakeTurtle()
        koch(t, 9, 1)
        self.assertEqual(len(t.path), 4)

        expected = [
            (3.0, 0.0),
            (4.5, 2.59808),
            (6.0, 0.0),
            (9.0, 0.0)
        ]

        for i, (ex, ey) in enumerate(expected):
            x, y = t.path[i]
            self.assertAlmostEqual(x, ex, places=4)
            self.assertAlmostEqual(y, ey, places=4)

    def test_level_2_segment_count(self):
        t = FakeTurtle()
        koch(t, 9, 2)
        self.assertEqual(len(t.path), 16)

    def test_angle_reset(self):
        t = FakeTurtle()
        koch(t, 9, 1)
        self.assertEqual(t.angle, 0.0)


if __name__ == "__main__":
    unittest.main()
