import requests

EMAIL =    'QlpoOTFBWSZTWUGvgg0AAAEBgALAAgAgACGaaDNNBzxdyRThQkEGvgg0'
PASSWORD = 'QlpoOTFBWSZTWZQkfA4AAACBAAMkIAAhmmgzTRM8XckU4UJCUJHwOA=='
URL = 'http://www.pythonchallenge.com/pc/return/good.html'

session = requests.session()

login_data = dict(username=EMAIL, password=PASSWORD)
r = session.post(URL, data=login_data)
print r.content

#req = session.get('https://leaderboards.guildwars2.com/en/na/achievements/guild/Darkhaven%20Elite')

#print req.content