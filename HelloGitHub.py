from github import Github
def helloGithub(userName):
    git = Github()
    user = git.get_user(userName)
    print(user.name)
    ret = []
    for repo in user.get_repos():
        cnt = repo.get_commits().__sizeof__()
        print("Repo: " + repo.name + " has " + str(cnt) + " commits")
        ret.append([repo.name, cnt])
    return ret




print(helloGithub("richkempinski"))


