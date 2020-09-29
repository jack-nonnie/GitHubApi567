from unittest import TestCase
from HW4ASSW567.HelloGitHub import helloGithub


class Test(TestCase):
    def test1(self):
        self.assertEqual(helloGithub("richkempinski")[0], ['csp', 32])
    def test2(self):
        self.assertEqual(helloGithub("richkempinski")[1], ['hellogitworld', 32])
    def test3(self):
        self.assertEqual(helloGithub("richkempinski")[3], ['Mocks', 32])
    def test4(self):
        self.assertEqual(len(helloGithub("richkempinski")), 9)
