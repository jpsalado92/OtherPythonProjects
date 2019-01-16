import requests

ipdb = "http://api.ipinfodb.com/v3/ip-city/?key=cc1a3eddc517b560f6cda201108177cb13e8e45a2ebdc1f00ae8e22d8799218d&ip="
ip =  requests.get('https://api.ipify.org').text
location = " ".join(str(requests.get(ipdb+ip).text).split(";")[4:7])
latlong = requests.get('https://ipapi.co/{}/latlong/'.format(ip)).text.split(',')
weather = requests.get('http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=5bc17bd1edfa123f0f146dc17bd8edcb'.format(latlong[0], latlong[1])).json()

print(location)
print(latlong)
print(weather)