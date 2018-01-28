#Please use this file to configure options for your specific implementation

#Our two Google email domains are listed here
domains = {
	'primary': '@example1.com',
	'secondary': '@example2.com'
	}

#Names of our Oauth files
googleappname = 'Example App Name'

primaryauth = 'primary_secret.json'
primaryorgpath = '/Example/Example'

secondarauth = 'secondary_secret.json'
schoologyauth = 'schoology_config.yml'

#Password generator... not configured, please implement one!
def passwordgenerator(firstname, lastname):
	password = "%s%s" % (firstname, lastname)
	return password

