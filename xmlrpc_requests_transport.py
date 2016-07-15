try:
    import xmlrpclib as xmlrpc
except ImportError:
    import xmlrpc.client as xmlrpc
import requests

class XRequests(xmlrpc.Transport):
	"""
	Transport object to be used with XMLRPC from the Python standard lib
	"""
	# Header dictionary. See Requests documentation for specific information
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) '
	                         'Chrome/41.0.2228.0 Safari/537.36', 'Content-Type': 'text/xml'}
	# Create the object where session data is stored
	session = requests.Session()
	# Set options required for Requests to work
	transport = 'http'
	verify = True

	def request(self, host, url, xml_body, verbose):
		"""
		Submit the request to the server.  Pass response to parse_response, return response to XML-RPC lib.
		Args:
			Host = IP or domain name with port number attached if avaible
			url = Location of resource on server
			xml_body = XML request to send
			verbose = A boolean flag which is passed from ServerProxy call
		"""
		
		if self.transport == 'https':
			# Create URL from the provided data
			url_long = '{}://{}{}'.format('https', host, url)
			if verbose == True:
				print('Full URL: ' + url_long)
			r = self.session.post(url_long, data=xml_body, headers=self.headers, verify=self.verify)

		elif self.transport == 'http':
			# Create URL from the provided data
			url_long = '{}://{}{}'.format('http', host, url)
			if verbose == True:
				print('Full URL: ' + url_long)
			r = self.session.post(url_long, data=xml_body, headers=self.headers)

		return self.parse_response(r)

	def parse_response(self, resp):
	    """
	    Parse the xmlrpc response.
	    """
	    p, u = self.getparser()
	    p.feed(resp.text)
	    p.close()
	    return u.close()

	def set_options(self, transport: str = 'http', verify: bool = True):
		"""
		Limitations in the ServerProxy implimenatation does not allow HTTP or HTTPS
		to be passed to the Requests module.
		Args:
			transport = Specify a transport type. HTTP or HTTPS
			verify = Verify is an option for Requests' HTTPS method to choose to check SSL certificates
		"""
		self.transport = transport.lower()
		self.verify = verify
