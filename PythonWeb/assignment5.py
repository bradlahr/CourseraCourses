import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    #parms = dict()
    #parms['address'] = address
    #url = urllib.parse.urlencode(address)
    print('Retrieving', address)
    uh = urllib.request.urlopen(address, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    #print(data.decode())
    tree = ET.fromstring(data)

    results = tree.findall('.//count')

    #print(results)
    countstring = 0
    for nodes in results:
        countstring += int(nodes.text)
        
    print('Sum:', countstring)
