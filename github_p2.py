#pip install PyGithub
#https://pygithub.readthedocs.io/en/latest/introduction.html
import pandas as pd
from github import Github
g = Github("YOUR API KEY")

####https://docs.github.com/en/github/searching-for-information-on-github/searching-for-repositories
#    search = g.search_repositories("language:python followers:>=100 stars:>=500 created:>=2020-08-01", "stars", "desc").get_page(i)
searches = []
for i in range(0,11):
    search = g.search_repositories("followers:>=100 stars:>=500 created:>=2020-08-01", "stars", "desc").get_page(i)
    searches.append(search)
    
#remove empty searches
while([] in searches) : 
    searches.remove([]) 
