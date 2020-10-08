import requests
import json

def get_repos(user):
    response = requests.get("https://api.github.com/users/" + user + "/repos")
    repoJson = response.text
    repos = json.loads(repoJson)
    fin = []
    for item in repos:
        fin.append(item['name'])
    return fin

def get_commits(user, repo):
    response = requests.get("https://api.github.com/repos/"+ user + "/" + repo + "/commits")
    repos = json.loads(response.text)
    fin = []
    cnt = 0
    for item in repos:
        cnt += 1
    return cnt
def get_repo_and_commits(user):
    repos = get_repos(user)
    fin = []
    for repo in repos:
        num = get_commits(user, repo)
        fin.append([repo, num])
        print("In repo: " + repo + " there are " + str(num) + " commits ")
    return fin

print(get_commits("richkempinski", 'csp'))
print(get_commits("richkempinski", 'helloworld'))
print(get_commits("richkempinski", 'hellogitworld'))