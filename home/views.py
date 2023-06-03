from django.shortcuts import render , HttpResponse 
import json
import urllib.request
from datetime import datetime, timedelta , date 
from home import apikeys

# Create your views here.
def home(request):
   



      

   if request.method =='POST':
      city=request.POST['city']
      print(city)
      
      

      

      

    
      
      
      # geocoder api
      req_url='https://api.openweathermap.org/geo/1.0/direct?q='+city+'&appid='+apikeys.weatherapikey
      url=req_url.replace(" ","_")
      location_codes=urllib.request.urlopen(url).read()
      location_cord=json.loads(location_codes)
      
      lati=str(location_cord[0]['lat'])
      longi=str(location_cord[0]['lon'])
      print(lati,longi)
     

    
# weather api
      response=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?lat='+lati+'&lon='+longi+'&appid=92956e6e0fee0ffafec6d1637eb73a8c').read()
      response_data=json.loads(response)
   #   to get the date:
      date_now=date.today()
   #to get the temp in celius
      kelvin=response_data['main']['temp']
      celsius = kelvin - 273.15

      


      
      weather_data={
         "country":str(response_data['sys']['country']),
         "temperature":str(celsius)+'°C',

         "sky":str(response_data['weather'][0]['description']),
         "Windspeed":str(response_data['wind']['speed']),
         "Humidity":str(response_data['main']['humidity']),
         
         "date":str(date_now)


          

      }

      

   else:
      city=''
      weather_data={}
      
   



   

   return render(request, 'index.html',{'city':city,'data':weather_data})



