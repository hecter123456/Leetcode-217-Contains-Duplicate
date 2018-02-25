import unittest

class unitest(unittest.TestCase):
    def testNone(self):
        Input = []
        Output = False
        self.assertEqual(Solution().containsDuplicate(Input),Output)
    def testSample(self):
        Input = [1,2,3,1]
        Output = True
        self.assertEqual(Solution().containsDuplicate(Input),Output)
    def testFalseSample(self):
        Input = [1,2,3]
        Output = False
        self.assertEqual(Solution().containsDuplicate(Input),Output)

class Solution():
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))

if __name__ == '__main__':
    unittest.main()
