import json
import requests

def getRepos(githubID):
    reposAPILink = "https://api.github.com/users/"
    commitsAPILink = "https://api.github.com/repos/"
    repos = []
    output = []
    reposURL = reposAPILink + f'{githubID}/' + 'repos'
    reposURL = requests.get(url = reposURL)
    reposURL = json.loads(reposURL.text)

    for repo in reposURL:
        repos.append(repo['name'])

    for repo in repos:
        commitsURL = commitsAPILink + f'{githubID}/{repo}/commits'
        jsonFile = json.loads(requests.get(url = commitsURL).text)
        output.append(f'Repo: {repo}\nCommits: {len(jsonFile)}\n')

    return output

def main():
    user = input("Enter user's Github ID: ")
    for repo in getRepos(user):
        print(repo)

if __name__ == '__main__':
    main()
