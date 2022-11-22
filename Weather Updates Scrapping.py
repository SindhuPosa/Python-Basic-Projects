from bs4 import BeautifulSoup as bs
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/107.0.0.0 Safari/537.36'}
def weather(city):
    city=city.replace(" ","+")
    res=requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
    print('Getting the weather...')
    soup=bs(res.text,'html.parser')
    location=soup.select('#wob_loc')[0].getText().strip()
    time=soup.select('#wob_dts')[0].getText().strip()
    info=soup.select('#wob_dc')[0].getText().strip()
    weather=soup.select('#wob_tm')[0].getText().strip()
    print(location)
    print(time)
    print(info)
    print(weather+"°C")
city=input("Enter the name of the city-- ")
city=city+" weather"
weather(city)
