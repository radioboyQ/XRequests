# XRequests
A transport class for Python's XMLRPC Client which maintains sessions.

## Example usage
This example is for local Dukowiki
```python
>>> from xmlrpc_requests_transport import XRequests
>>> url = 'http://localhost/lib/exe/xmlrpc.php'
>>> s = xmlrpc.client.ServerProxy(url,transport=XRequests(), verbose=True)
>>> # Unauthenticated RPC calls
>>> s.dokuwiki.getTitle()
Full URL: http://localhost/lib/exe/xmlrpc.php
"Scott's Personal Wiki"
>>> # Since this is a Dokuwiki, it returns True when a session authenticated
>>> s.dokuwiki.login(username, password)
Full URL: http://localhost/lib/exe/xmlrpc.php
True
>>> # This method requires an authenticated session
>>> s.dokuwiki.getVersion()
Full URL: http://localhost/lib/exe/xmlrpc.php
'Release 2016-06-26a "Elenor of Tsort"'
>>>
```

## Installation instructions
[Python Requests](http://docs.python-requests.org/en/master/ "Requests: HTTP for Humans") must be in Python's path.  
[xmlrpc_requests_transport.py](../blob/master/xmlrpc_requests_transport.py) must also be in Python's path. The same directory is fine.

## Qwerks of XML-RPC
Python's XML-RPC library has a lot of qwerks about it.   
For starts, you can not use a custom transport when connecting to HTTPS.

### Work arounds
Since the XML-RCP lib won't let us use a custom transport with anything except HTTP, this presents a weird problem.   
A function called `set_options` is used to set 'HTTPS' and if 'Requests' should verify the SSL certificate.
```python
>>> # Create ServerProxy with options set
>>> s = xmlrpc.client.ServerProxy(url,transport=XRequests().set_options(transport='https', verify=False),  verbose=True)
>>> s.dokuwiki.search('python')


### Insparation
https://gist.github.com/chrisguitarguy/2354951
