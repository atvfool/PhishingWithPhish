import requests
import os
import random
import string
import json
import uuid

## the characters for the random characters
chars = string.ascii_letters + string.digits + "!@#$%^&*()"
## for email addresses, add whatever you see fit
domains = ["@gmail.com", "@yahoo.com", "@outlook.com", "@aol.com"]
random.seed = (os.urandom(1024))

## The url of where the form data is to be sent
url = ''

## Load the names list
names = json.loads(open('names.json').read())

for name in names:
    name_extra = ''.join(random.choice(string.digits) for i in range(3)) ## Gets 3 random digits to append to the name to make is seem more believe able

    username = name.lower() + name_extra + ''.join(random.choice(domains)) ## tacks on the random domain
    password = ''.join(random.choice(chars) for i in range(8)) ## fake password
    newuid = "{" + str(uuid.uuid4()) + "}" ## some phishing forms request a uuid so heres the code for that

	## Need to shape the data for how the site is expecting the data. will be different from site to site
    data = [{'Value':username, "ControlSource":"1"},
    {"Value":password, "ControlSource":"2"},
    {"ControlSource":"3"},
    {"ControlSource":"4"},
    {"ControlSource":"5"},
    {"ControlSource":"6"},
    {"Value":"No", "ControlSource":"7"},
    {"surveyId":newuid},]

    requests.post(url, allow_redirects=False, data=json.dumps(data)) ## Posts the data as json

    print 'sending username %s and password %s' % (username, password) ## Just here to know the it's still running

print 'Completed!!!'
