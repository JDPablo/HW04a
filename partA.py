import json
import requests

def getRepos(githubID):
    output = []
    githubIDURL = 'https://api.github.com/users/{}/repos'.format(githubID)
    githubInfo = requests.get(githubIDURL)
    reposInfo = json.loads(githubInfo.text)
    output.append('User: {}'.format(githubID))

    try:
        reposInfo[0]['name']
    except (TypeError, KeyError, IndexError):
        return 'error encountered while getting repos'

    try:
        for repo in reposInfo:
            repoName = repo['name']
            repoURL = 'https://api.github.com/repos/{}/{}/commits'.format(githubID, repoName)
            repoInfo = requests.get(repoURL)
            repoData = json.loads(repoInfo.text)
            output.append('Repo: {}\nCommits: {}'.format(repoName, len(repoData)))
    except (TypeError, KeyError, IndexError):
        return 'error encountered while getting commits'
    return output

def main():
    idInput = input("Please enter the Github ID of the account you'd like to see the repos of: ")
    for userInput in getRepos(idInput):
        print(userInput)

if __name__ == '__main__':
    main()
