"""
Write divident function to perform integer division without using either the / or *
operators. Find divident fast way to do it.
"""

import unittest


def div(divident, divisor):
    """
    Divide divident / divisor without usign / or * operators
    """
    if divisor == 0:
        raise ZeroDivisionError('division by zero')
    if divisor > divident:
        return 0
    divident -= divident % divisor
    if divident == divisor:
        return 1
    rv = 0
    while divident > 0:
        divident -= divisor
        rv += 1
    return rv


class MyTestCase(unittest.TestCase):
    """ Test case for div function """

    def test_div_4_by_2(self):
        self.assertEqual(div(4, 2), 2)

    def test_div_5_by_2(self):
        self.assertEqual(div(5, 2), 2)

    def test_div_145_by_2(self):
        self.assertEqual(div(145, 2), 145 // 2)

    def test_div_raising_zero_division_error(self):
        with self.assertRaises(ZeroDivisionError):
            div(4, 0)


if __name__ == "__main__":
    unittest.main()
