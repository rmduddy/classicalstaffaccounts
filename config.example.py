#Please use this file to configure options for your specific implementation

#Our two Google email domains are listed here
domains = {
	'primary': '@example1.com',
	'secondary': '@example2.com'
	}

#Names of our Oauth files
primaryauth = 'primary_secret.json'
secondarauth = 'secondary_secret.json'
schoologyauth = 'schoology_config.yml'

#Password generator... not configured, please implement one!
def passwordgenerator(firstname, lastname):
	password = "%s%s" % (firstname, lastname)
	return password

