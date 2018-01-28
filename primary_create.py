
from __future__ import print_function
import httplib2
import os
import config as cfg

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/admin-directory_v1-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/admin.directory.user'
CLIENT_SECRET_FILE = cfg.primaryauth
APPLICATION_NAME = cfg.googleappname

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    
    Note: This section of code is a modified copy of Google's own Python API
    example As such please determine the appropriate license being used
    """
    working_dir = os.getcwd()
    credential_dir = os.path.join(working_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'googleprimary.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main(employee):

	credentials = get_credentials()
	http = credentials.authorize(httplib2.Http())
	service = discovery.build('admin', 'directory_v1', http=http)
	                
	userinfo = {'primaryEmail': employee.primaryemail(),
        'name': { 'givenName': employee.firstname, 'familyName': employee.lastname },
        'password': employee.password(),
        'orgUnitPath': cfg.primaryorgpath,}

	service.users().insert(body=userinfo).execute()

if __name__ == '__main__':
    main()
