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

    for repo1 in reposURL:
        repos.append(repo1['name'])

    for repo2 in repos:
        commitsURL = commitsAPILink + f'{githubID}/{repo2}/commits'
        jsonFile = json.loads((requests.get(url = commitsURL)).text)
        output.append(f'Repo: {repo2}\nCommits: {len(jsonFile)}\n')

    return output

def main():
    idInput = input("Please enter the Github ID of the account you'd like to see the repos of: ")
    for repo in getRepos(idInput):
        print(repo)

if __name__ == '__main__':
    main()
