import unittest
def more_than_five(val: int) -> bool:
    """
    Check if value > 5
    :param val: value to check.
    :return: True if value > 5, else - False
    """
    return False
class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(more_than_five(6))
        self.assertFalse(more_than_five(4))
