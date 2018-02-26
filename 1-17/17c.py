import xmlrpclib

url = 'http://www.pythonchallenge.com/pc/phonebook.php'
server = xmlrpclib.Server(url)
print server.phone('Leopold')