

from sys import prefix
import requests
from bs4 import BeautifulSoup
from requests import status_codes
def extract(page) :
    headers= {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
    url = f"https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=Data%20Analyst&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=0DQT0data%20analyst0DQT0&pDate=I&sequence={page}&startPage=1"
    r= requests.get(url,headers)
    soup = BeautifulSoup(r.content,"html.parser")
    return soup

def transform(soup):
    divs= soup.find_all("li",class_= "clearfix job-bx wht-shd-bx")
    for item in divs:
        company= item.find("h3").text.strip()
        location= item.find("span").text.strip()
        skills= item.find("span",class_ = "srp-skills").text.strip()
        experience= item.find("li").text.replace("card_travel","").strip()
        job= { "company": company,
        "location": location,
        "skills": skills,
        "experience": experience
        }
        joblist.append(job)
    return


joblist= []  
for i in range(1,50) : 
    c= extract(i)
    transform(c)
print(len(joblist))

import pandas as pd
df= pd.DataFrame(joblist)
#print(df.head())
df.to_csv("jobs.csv")