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

#view raw data keys    
#[print(i) for i in list(searches[0][0].raw_data.keys())][0]

repo_names = []
repo_owners = []
star_count = []
links = []
subs = []
langs = []
descs = []

for i in range(len(searches)):
    for n in range(len(searches[i])):
        repo_names.append(searches[i][n].raw_data["name"])
        repo_owners.append(searches[i][n].raw_data["owner"]["login"])
        star_count.append(searches[i][n].raw_data["stargazers_count"])
        links.append(searches[i][n].raw_data["html_url"])
        subs.append(searches[i][n].raw_data["subscribers_count"])
        langs.append(searches[i][n].raw_data["language"])
        descs.append(searches[i][n].raw_data["description"])
        
df = pd.DataFrame({"Repo Name":repo_names,"Description":descs,"Owner":repo_owners,"Stars":star_count,"Subscribers":subs,"Language":langs,"Link":links})

#alternatively using github trends API https://github.com/huchenme/github-trending-api
#sample trends url
#https://ghapi.huchen.dev/repositories?language=javascript&since=weekly&spoken_language_code=english
import requests
import json

weekly_url = "https://ghapi.huchen.dev/repositories?&since=weekly&spoken_language_code=english"
today_url = "https://ghapi.huchen.dev/repositories?&since=today&spoken_language_code=english"

def get_trends(link,filename):
    with requests.Session() as s:
        url = link
        r = s.get(url)
    data = r.json()
    
    repo_names = []
    repo_owners = []
    star_count = []
    links = []
    langs = []
    descs = []

    for i in range(len(data)):
        repo_names.append(data[i]["name"])
        descs.append(data[i]["description"])
        repo_owners.append(data[i]["author"])
        star_count.append(data[i]["currentPeriodStars"])
        links.append(data[i]["url"]+"/"+data[i]["name"])
        try:
            langs.append(data[i]["language"])
        except:
            langs.append("")

    trends = pd.DataFrame({"Repo Name":repo_names,"Description":descs,"Owner":repo_owners,"Stars":star_count,"Language":langs,"Link":links}).sort_values(by="Stars",ascending=False)
    trends.to_csv(filename+".csv",index=False)
    
get_trends(weekly_url,"weekly_trends")
get_trends(today_url,"today_trends")

week = pd.read_csv("weekly_trends.csv")
day = pd.read_csv("today_trends.csv")
