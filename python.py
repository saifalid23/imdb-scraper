from bs4 import BeautifulSoup
import http
import requests, openpyxl

excel = openpyxl.Workbook()
print(excel.sheetnames)
sheet = excel.active
sheet.title = 'top 250 of imdb'
print(excel.sheetnames)
sheet.append(['Movie rank','Movie name','year Of Release','Rating'])


try:
    source =  requests.get('https://www.imdb.com/chart/top/')
    source.raise_for_status()

    soup = BeautifulSoup(source.text,'html.parser')
    # print(soup)

    movies = soup.find('tbody',class_="lister-list").find_all('tr')
    # print(len(movies))

    for movie in movies:


        rank = movie.find('td',class_="titleColumn").get_text(strip=True).split('.')[0]
        # rank = 
        name = movie.find('td',class_="titleColumn").a.text

        year = movie.find('td',class_='titleColumn').span.text.strip('()')

        rating = movie.find('td',class_="ratingColumn imdbRating").strong.text
        print(rank ,name ,year, rating)
        sheet.append([rank ,name ,year, rating])
        
        # break

except Exception as e:
    print(e)

excel.save('IMDB Movies Ratings.xlsx')
