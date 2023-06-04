import json, requests
def main():
    intro ()  
#requesting user input to pull request from url  
    try:
      city = str(input("Please provide city name, exp.   Vermont  "))
  
      zipcde = int(input("Please provide zipcode, exp. 12345  "))  
      base_url = "https://api.openweathermap.org/data/2.5/weather"

      appid = "10b06e71194c26fdbb9cee8146f97770"
#appid = "906b6939735602a519447e37a839d229"
# trial and error testing
#city = "Detroit"
#cty = (city)  
      zcd = (zipcde)
      cty = (city)

#users input being sent off and returned with responses
      url = f'{base_url}?q={city}zz={zcd}&units=imperial&APPID={appid}'
      url = f"{base_url}?q=  {cty}&units=imperial&APPID={appid}"  
      print(url)

      print()

      response = requests.get(url)
      unformated_data =response.json()

      temp = unformated_data['main']["temp"]
      print(f"The current temperature is: {temp} degrees")

      temp_max = unformated_data['main']['temp_max']
      print(f"The max temperature is: {temp_max} degrees")
      main()
# Determining if users input was valid
    except:
      print ("Sorry there was an issue with your request, please refer to the  examples and try again. ")
# Error solution temp check user if they like to try again
    tempchk = input("If you would like to try again input 1, if not input 2.")
# Users response determine if system quits or trys again
    if int(tempchk)== (1):  
      print()
      main()
    else:
      quit
      

#Intro defined below to inform users of systems service and encourages participation 
def intro():
  print("Hello this program will provide you with the current temp of an  area by providing us with either a zip code or city.")

  print("     Give it a go!")
main()







  