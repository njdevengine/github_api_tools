from github import Github

# First create a Github instance:

# using username and password
g = Github("YOUR USERNAME", "YOUR PASS")

# or using an access token
g = Github("YOUR API KEY")

#print your own repos
for repo in g.get_user().get_repos():
    print(repo.name)
    
#get all possible repo arguments
print(dir(repo))

#get all possible github functions
for i in (dir(g)):
    print(i)
    
#perform a search and return repositories
search = g.search_repositories(query="YOUR QUERY HERE")

#get repos from search and gazers for each
for i in search:
#     print(i.html_url)
    print("REPO")
    print(i.html_url)
    print("gazers")
    for x in i.get_stargazers_with_dates():
        print(x.user.html_url)
    print("**************")

#get common gazers from two repos
def analyze(repo1,repo2):
    gazers_1 = []
    repo_1 = g.get_repo(repo1)
    for x in repo_1.get_stargazers_with_dates():
        gazers_1.append(x.user.html_url)
    gazers_2 = []
    repo_2 = g.get_repo(repo2)
    for x in repo_2.get_stargazers_with_dates():
        gazers_2.append(x.user.html_url)
    for i in list(set(gazers_1).intersection(gazers_2)):
        try:
            print(i,g.get_user(str(i.split("/")[-1])).get_repos()[0].get_commits()[0].raw_data["commit"]["author"]["email"])
        except:
            print(i,"no repos")
        
#format is username/reponame as it appears in url for a given repo
analyze("username1/repo1","username2/repo2")

#raw commit json
patch = repo.get_commits()[0].raw_data

#get email
g.get_user("USERNAME GOES HERE").get_repos()[0].get_commits()[0].raw_data["commit"]["author"]["email"]
#get name
g.get_user("USERNAME GOES HERE").get_repos()[0].get_commits()[0].raw_data["commit"]["author"]["email"]

#get gazers from one repo
def analyze_one(repo1):
    gazers_1 = []
    repo_1 = g.get_repo(repo1)
    for x in repo_1.get_stargazers_with_dates():
        gazers_1.append(x.user.html_url)
    for i in list(set(gazers_1)):
        try:
            print(i,g.get_user(str(i.split("/")[-1])).get_repos()[0].get_commits()[0].raw_data["commit"]["author"]["email"])
        except:
            print(i,"no repo")
            
analyze("username1/repo1")
