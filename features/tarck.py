from bs4 import BeautifulSoup
import requests

# dis = 'urinary'
# source = requests.get(f"https://www.nhsinform.scot/search?q={dis}&locpt=&ds=&tab=inform").text
# soup = BeautifulSoup(source, 'lxml')

# disease = soup.ol.a['href']

# source1 = requests.get(f"https://www.nhsinform.scot{disease}").text
# soup = BeautifulSoup(source1, 'lxml')

# dis_info = soup.find('div', class_="editor").p.text

# print(dis_info)

source=requests.get(f"https://www.practo.com/search?results_type=doctor&q=%5B%7B%22word%22%3A%22Dermatologist%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22subspeciality%22%7D%5D&city=Bangalore").text
soup=BeautifulSoup(source,'lxml')

print(soup.prettify())