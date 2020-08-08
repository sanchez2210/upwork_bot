def query_formatter(query, type):
	'''
	Inputs: query, '+' or '%20'
	Output: A url friendly query
	'''

	if type == '+':
		url_friendly_query =  query.replace(' ', '+')

	elif type == '%20':
		url_friendly_query =  query.replace(' ' , ' %20')


	return url_friendly_query

	

def attrs_exist(element, attr):
	if element.attrs.get(attr):
		return element.attrs.get(attr)

	else:
		return None