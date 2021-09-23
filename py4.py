
import requests
import xmltodict

url = "https://www.w3schools.com/xml/simple.xml"
response = requests.get(url)
data = xmltodict.parse(response.content)
# print(data)
for food in data['breakfast_menu']['food']:
    print("Name : ",food['name']," , Price : ",food['price'])

