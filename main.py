import json, requests

print("Hello this program will provide you with the    current temp of an area by providing us with either a zip code or city.")

print("     Give it a go!")



city = str(input("Please provide city name, exp.   Vermont  "))
  
zipcde = int(input("Please provide zipcode, exp. 12345  "))  
base_url = "https://api.openweathermap.org/data/2.5/weather"

#appid = "10b06e71194c26fdbb9cee8146f97770"
appid = "906b6939735602a519447e37a839d229"
#city = "Detroit"
#cty = (city)  
#zcd = (zipcde)
cty = (city)


#url = f'{base_url}?q={city}zz={zcd}&units=imperial&APPID={appid}'
url = f"{base_url}?q={cty}&units=imperial&APPID={appid}"  
print(url)
print()

response = requests.get(url)
unformated_data =response.json()

temp = unformated_data['main']["temp"]
print(f"The current temperature is: {temp}")

temp_max = unformated_data['main']['temp_max']
print(f"The max temperature is: {temp_max}")







  