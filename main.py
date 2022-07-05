import requests
from bs4 import BeautifulSoup
from proxy_config import login, password, proxy

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
}

proxies = {
    'https': f'http://{login}:{password}@{proxy}'
}


def get_data(url):
  # response = requests.get(url=url, headers=headers, proxies=proxies)
  # print(response)

  # with open(file='index.html', mode='w') as file:
  #   file.write(response.text)

  with open(file='index.html') as file:
    src = file.read()

  soup = BeautifulSoup(src, 'lxml')
  table = soup.find('table', id='ro5xgenergy')

  data_th = table.find('thead').find_all('tr')[-1].find_all('th')

  for dth in data_th:
    dth = dth.text.strip()
    print(dth)



def main():
  get_data(url='https://www.bls.gov/regions/midwest/data/AverageEnergyPrices_SelectedAreas_Table.htm')

if __name__ == '__main__':
  main()

