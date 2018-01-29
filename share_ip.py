import sys
import socket
import http.client

key = sys.argv[-1]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))
ip = s.getsockname()[0]
s.close()

print(ip)
conn = http.client.HTTPConnection("kvs.ouroborothon.com")
conn.request("POST", "/%s/" % key, ip)
response = conn.getresponse()
print(response.status, response.reason)
data = response.read()
print(data)
conn.close()
