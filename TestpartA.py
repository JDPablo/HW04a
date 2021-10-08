import unittest

from partA import getRepos

class TestGetRepos(unittest.TestCase):
    def testJD(self): 
        self.assertIsNotNone(getRepos('JDPablo'))

    def testTom(self): 
        self.assertIsNotNone(getRepos('BlackRoseRipp'))

    def testJoan(self): 
        self.assertIsNotNone(getRepos('joantubungbanua'))

    def testKnownInvalid(self): 
        self.assertIsNone(getRepos('invalidacccccc'))

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()