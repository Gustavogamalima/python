import requests

try:
    response = requests.get('http://pudim.com.br/')
except requests.RequestException:
    print('Pudding website is currently not accessible.')
else:
    print('Successfully accessing the Pudding website!')
