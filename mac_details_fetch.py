import requests
import json

f = open('key.txt', 'r')
content = f.read()

url = "https://mac-address-lookup1.p.rapidapi.com/static_rapid/mac_lookup/"

mac_address = input("Enter the MAC address: ")

querystring = {"query":mac_address}

headers = {
    'x-rapidapi-host': "mac-address-lookup1.p.rapidapi.com",
    'x-rapidapi-key': content # replace with your rapid api key API key
    }

response = requests.request("GET", url, headers=headers, params=querystring)
data = json.loads(response.text)
if data['result'] == [] :
    print("No data found")
else:
    print(data['result'][0]['name']) # print the name of the company of the mac address
