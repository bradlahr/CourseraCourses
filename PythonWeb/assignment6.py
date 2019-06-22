import urllib.request, urllib.parse, urllib.error
#import xml.etree.ElementTree as ET
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
if len(address) < 1: exit

print('Retrieving', address)
uh = urllib.request.urlopen(address, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')

print(data.decode())

info = json.loads(data)
print('User count:', len(info["comments"]))


sum = 0
for nodes in info["comments"]:
    #print(nodes["count"])
    sum += int(nodes["count"])

print("Sum = ", sum)


