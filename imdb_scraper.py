import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0','lang' : 'eng'}

response = requests.get(url,headers=header)

soup = BeautifulSoup(response.content , 'html.parser')


top_movies = soup.find_all('li',class_='ipc-metadata-list-summary-item sc-10233bc-0 iherUv cli-parent')
print(len(top_movies))
filename='top_movies.csv'
with open(filename,mode='w',newline='',encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['Movie Title','Rank','Year','Length','Rate'])
    for movie in top_movies:
      Title=movie.find('div',class_='ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 iALATN cli-title').a.h3.text.split('.')[1]
      Rank =movie.find('div',class_='ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 iALATN cli-title').a.h3.text.split('.')[0]
      Year=movie.find('div',class_='sc-b189961a-7 feoqjK cli-title-metadata').span.text
      Length=movie.find('div',class_='sc-b189961a-7 feoqjK cli-title-metadata').span.text
      Rate =movie.find('div',class_='sc-e2dbc1a3-0 ajrIH sc-b189961a-2 fkPBP cli-ratings-container').span.text
      writer.writerow([Title,Rank,Year,Length,Rate])

print('data has been saved successfully as ',filename)






