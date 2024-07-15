import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0','lang' : 'eng'}

response = requests.get(url,headers=header)

soup = BeautifulSoup(response.content , 'html.parser')


top_movies = soup.find_all('li',class_='ipc-metadata-list-summary-item sc-10233bc-0 iherUv cli-parent')
print(len(top_movies))

for movie in top_movies:
    print('Movie Title',movie.find('div',class_='ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 iALATN cli-title').a.text.split('.')[1])
    print('Rank ',movie.find('div',class_='ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 iALATN cli-title').a.text.split('.')[0])