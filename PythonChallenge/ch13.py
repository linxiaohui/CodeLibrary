# *-* coding:UTF-8 *-*

url="http://www.pythonchallenge.com/pc/phonebook.php"

import xmlrpc.client
  
server=xmlrpc.client.Server(url)
print(server.phone("Bert"))
