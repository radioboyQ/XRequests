from xmlrpc_requests_transport import XRequests
import xmlrpc.client

username = 'radioboy'
password = 'password'
url = 'http://localhost/lib/exe/xmlrpc.php'

s = xmlrpc.client.ServerProxy(url,transport=XRequests().set_options(transport='https', verify=False),  verbose=True)

# Make XML calls. Any session data is autmatically stored
print(s.dokuwiki.login(username, password))
print(s.wiki.getRPCVersionSupported())
print(s.dokuwiki.getTime())
