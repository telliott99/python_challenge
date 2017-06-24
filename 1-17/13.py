import xmlrpclib

url = 'http://www.pythonchallenge.com/pc/phonebook.php'
server = xmlrpclib.Server(url)

#print server.system.listMethods()

'''
['phone', 'system.listMethods', 'system.methodHelp', 'system.methodSignature', 'system.multicall', 'system.getCapabilities']
>
'''

# result = server.phone()
# error: needs parameter(s)

# print server.system.methodSignature('phone')
''' 
> python 13.py 
[['string', 'string']]
>
'''

#print server.phone('evil')

'''
> python 13.py 
He is not the evil
> 
'''

print server.phone('Bert')
'''
> python 13.py 
555-ITALY
>
'''

