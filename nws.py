
import requests
from bs4 import BeautifulSoup
nws_page=requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
# print(nws_page.content)
# scrap for page's ordered content
nws_soup=BeautifulSoup(nws_page.content,'html.parser')
# print(nws_soup.prettify)
# scrap for seven days weather forecast content div
seven_days=nws_soup.find(id="seven-day-forecast-body")
# print(seven_days)
# scrap for the days' weather content from specific weather div
forecast_days=seven_days.find_all(class_="tombstone-container")
# print(forecast_days)
# scrap for specific time/day's weather using respective indices (scrap overnight weather data)

overnight=forecast_days[0]
print(overnight.prettify)
# scrap for specific overnight weather data
#get_text() function removes tags
period=overnight.find(class_="period-name").get_text()
temp=overnight.find(class_="temp").get_text()
desc=overnight.find(class_="short-desc").get_text()
# print(period)
# print(temp)
# print(desc)
# scrap for Thursday's weather data
thur=forecast_days[1]
# print(thur)
# scrap for specific Thursday weather data
period1=thur.find(class_="period-name").get_text()
temp1=thur.find(class_="temp").get_text()
desc1=thur.find(class_="short-desc").get_text()
# print(period1)
# print(temp1)
# print(desc1)