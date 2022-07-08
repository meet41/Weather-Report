import requests
city = input("Enter your City Name : ")
print(city)
print("Weather Report for City : "+city)
url='https://wttr.in/{}'.format(city)
res=requests.get(url)
print(res.text)
