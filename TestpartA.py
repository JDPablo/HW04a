import unittest
from unittest.mock import patch

import partA
from partA import getRepos

githubID1 = 'JDPablo'
githubID2 = 'BlackRoseRipp'
githubID3 = 'joantubungbanua'
repo = 'hw04a'

class TestGetRepos(unittest.TestCase):
    @patch('partA.getRepos')
    def testJD(self, mock_getRepos):
        mock_getRepos.returnValue = [repo]
        repos = partA.getRepos('JDPablo')
        self.assertIsNotNone(repos, list)

    @patch('partA.getRepos')
    def testTom(self, mock_getRepos):
        mock_getRepos.returnValue = [repo]
        repos = partA.getRepos('BlackRoseRipp')
        self.assertIsNotNone(repos, list)

    @patch('partA.getRepos')
    def testJoan(self, mock_getRepos):
        mock_getRepos.returnValue = [repo]
        repos = partA.getRepos('joantubungbanua')
        self.assertIsNotNone(repos, list)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()