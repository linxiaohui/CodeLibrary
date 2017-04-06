'''
上一关中, evil4.jpg 显示 Bert is evil! go back!
'''

url="http://www.pythonchallenge.com/pc/phonebook.php"

import xmlrpc.client
  
server=xmlrpc.client.Server(url)
print(server.phone("Bert"))
