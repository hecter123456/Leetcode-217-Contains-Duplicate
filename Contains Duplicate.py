import unittest

class unitest(unittest.TestCase):
    def testNone(self):
        Input = []
        Output = False
        self.assertEqual(Solution().containsDuplicate(Input),Output)

class Solution():
    def containsDuplicate(self, nums):
        if nums == []:
            return False

if __name__ == '__main__':
    unittest.main()
