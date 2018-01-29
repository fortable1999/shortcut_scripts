import sys
import socket
import http.client

key = sys.argv[-1]
conn = http.client.HTTPConnection('kvs.ouroborothon.com')
conn.request("GET", '/%s/' % key)
response = conn.getresponse()
data = response.read()
data_str = data.decode()
print(data_str)

