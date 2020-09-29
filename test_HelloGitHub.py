from unittest import TestCase
from HelloGitHub import helloGithub


class Test(TestCase):
    def test1(self):
        self.assertEqual(helloGithub("richkempinski")[0], ['csp', 32])
    def test2(self):
        temp = helloGithub("richkempinski")
        commit = 0
        for i in range(len(temp)):
            if(temp[i][0] == 'hellogitworld'):
                commit = temp[i][1]
        self.assertEqual(commit, 32)
    def test3(self):
        self.assertEqual(helloGithub("richkempinski")[3], ['Mocks', 32])
    def test4(self):
        self.assertEqual(len(helloGithub("richkempinski")), 9)
    def test5(self):
        temp = helloGithub("richkempinski")
        commitCnt = 0
        for i in range(len(temp)):
            if (temp[i][1] == 32):
                commitCnt +=1
        self.assertEqual(commitCnt, 9)
