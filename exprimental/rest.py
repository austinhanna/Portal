UID = "me"
OAUTH_TOKEN="107065847491-3m9juj5th2cmack2ea50956neq7mvu93.apps.googleusercontent.com"
APP_SECRET_KEY = "4mn7paw00WD89InVAEsmBlys"
CLIENT_ID = "107065847491-3m9juj5th2cmack2ea50956neq7mvu93.apps.googleusercontent.com"

import requests
url = "https://www.googleapis.com/fitness/v1/users/me/dataSources"

headers = { 'content-type': 'application/json',
            'Authorization': 'Bearer %s' % OAUTH_TOKEN }
r = requests.get(url, headers=headers)

print(r.status_code)
print(r.content)
