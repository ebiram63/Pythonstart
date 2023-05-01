import requests

"""
body = requests.get('https://tahlildadeh.com/')

print(body.status_code)
print(body.headers)

"""

mydata = {
    'name' : 'ebi63',
    'password' : 'Ebi123456'

}
# h = useragent
body = requests.post('https://tahlildadeh.',data=mydata)
#body = requests.post('https://tahlildadeh.',header = h)

