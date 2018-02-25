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
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] = -1
            else:
                dic[i] = 1
        for key,value in dic.items():
            if dic[key] == -1:
                return True
        return False

if __name__ == '__main__':
    unittest.main()
