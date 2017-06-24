import requests

EMAIL =    'huge'
PASSWORD = 'file'
URL = 'http://www.pythonchallenge.com/pc/return/good.html'

session = requests.session()

login_data = dict(username=EMAIL, password=PASSWORD)
r = session.post(URL, data=login_data)
print r.content
