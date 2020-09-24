import requests
from bs4 import BeautifulSoup as BS


url='https://sinoptik.ua/погода-алнаши'

def get_html(url):
    r=requests.get(url)
    return r.text

def tomorrow_url(html):
    soup=BS(html,'html.parser')
    nd=soup.find('div',id='bd2').find('a').get('href')
    return 'https:'+str(nd)

def get_next_day(html):
    soup=BS(html,'html.parser')
    next_day=soup.find('div',id='bd2')
    minus=next_day.find('div',class_='min').find('span').text
    plus=next_day.find('div',class_='max').find('span').text
    return 'от '+minus+' до '+plus

def description_tomorrow(html):
    soup=BS(html,'html.parser')
    dis=soup.find('div',id='bd2c').find('div',class_='description').text
    return dis

temp_next_day=get_next_day(get_html(url))
day=(description_tomorrow(get_html(tomorrow_url(get_html(url)))))

