import unittest
import requests
import mock
import json
from HW4ASSW567.HelloGitHub2 import get_repos, get_commits

class faker:
    def __init__(self, json_data):
        self.json_data = json_data
    def json(self):
        return self.json_data


diction = {
    "https://api.github.com/users/richkempinski/repos" : "repo.json",
    "https://api.github.com/repos/richkempinski/csp/commits": "csp.json",
    "https://api.github.com/repos/richkempinski/helloworld/commits": "helloworld.json",
    "https://api.github.com/repos/richkempinski/hellogitworld/commits": "hellogitworld.json",
}
def mockResponse(*args):
    if(args[0] in diction):
        with open(diction[args[0]]) as f:
            return faker(json.load(f))
    return faker(None)

class Test(unittest.TestCase):
    @mock.patch('requests.get', side_effect = mockResponse)
    def test_get_repo(self, mockrep):
        self.assertEqual(get_repos("richkempinski"), ['csp', 'hellogitworld', 'helloworld', 'Mocks', 'Project1', 'richkempinski.github.io', 'threads-of-life', 'try_nbdev', 'try_nbdev2'])

    @mock.patch('requests.get', side_effect=mockResponse)
    def test_get_commit1(self, mockrep):
        self.assertEqual(get_commits("richkempinski", 'csp'), 2)

    @mock.patch('requests.get', side_effect=mockResponse)
    def test_get_commit2(self, mockrep):
        self.assertEqual(get_commits("richkempinski", 'helloworld'), 6)

    @mock.patch('requests.get', side_effect=mockResponse)
    def test_get_commit1(self, mockrep):
        self.assertEqual(get_commits("richkempinski", 'hellogitworld'), 30)



if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

