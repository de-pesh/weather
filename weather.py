import requests
from bs4 import BeautifulSoup as b
try:
    HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
    city = "kathmandu"
    city = input("Enter city to get weather data : ")
    query = "https://www.google.com/search?q=weather+" + city
    html = requests.get(query, headers=HEADERS)
    soup = b(html.content, "html.parser")
    t = soup.find(id = "wob_tm")
    temp = t.getText()
    w = soup.find(id="wob_ws")
    wind = w.getText()
    print("\nIt is ", temp, " degree celcius at ", city)
    print("The speed of wind at ", city , "is ", wind)
except:
    print("We could'nt recognize this city")
