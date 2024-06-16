import bs4 as bs
import requests
import pickle

html = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies#S&P_500_component_stocks')
soup = bs.BeautifulSoup(html.text)

tickers = []

table = soup.find('table', {'class': 'wikitable sortable'})
rows = table.find_all('tr')[1:]
for row in rows:
    ticker = row.find_all('td')[0].text
    tickers.append(ticker[:-1])

with open('tickers.pickle', 'wb') as f:
    pickle.dump(tickers, f)

with open('tickers.pickle', 'rb') as f:
    tickers = pickle.load(f)

print(tickers)