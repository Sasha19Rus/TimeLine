import requests
from bs4 import BeautifulSoup as BS

base_url = ('https://www.google.com/search?q=rehc+ljkkfhf&oq=rehc+&aqs=chrome.0.69i59j69i57j0i10i131i433l5j69i60.1344j1j9&sourceid=chrome&ie=UTF-8')
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/102.0.0.0 Safari/537.36',
    'accept': '*/*'
}

def parse(url=base_url):
    session = requests.Session()
    response = session.get(url, headers=HEADERS)
    soup = BS(response.content, 'html.parser')
    items = soup.find_all('div', class_='b1hJbf')

    channel_events = ''
    for channel in items:
        channel_events = channel.find('span', class_='DFlfde SwHCTb').text

    return channel_events

#print(parser(url=base_url))
