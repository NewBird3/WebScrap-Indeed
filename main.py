import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
    url = 'https://in.indeed.com/jobs?q=Python+Developer&l=Pune%2C+Maharashtra&start={page}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_ = 'job_seen_beacon')
    for item in divs:
        title = item.find('a').text.strip()
        company = item.find('span', class_='companyName').text.strip()
        try:
            salary = item.find('span', class_ = 'salary-snippet').text.strip()
        except:
            salary = ''
        summary = item.find('div', class_='job-snippet').text.strip().replace('\n', '')

        job = {
            'title': title,
            'company' : company,
            'salary' : salary,
            'summary' : summary,
        }
        joblist.append(job)
    return

joblist = []

for i in range(0,40,10):
        print(f'Getting page, {i}')
        c = extract(0)
        transform(c)

df = pd.DataFrame(joblist)
print(df.head())
df.to_csv('jobs.csv')




