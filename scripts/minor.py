#imported libraries

from rapidconnect import RapidConnect    #to use a rapid api
import pprint       #pretty print a json
import requests     #access apis
import datetime     #get current date and time
import statistics   #calculate mean
#%%
#entry

def take_location():
    place=input('please enter your location: ')
    crop=input('please enter the crop of your choice: ')

#%%
#show weather info of the place
def get_weather(place):
    def api_for_weather(place):
        result=requests.get('http://api.openweathermap.org/data/2.5/weather?q='+place+'&appid=26215a2614573c7ce3405f3338415d10')
        data=result.json()
        return data
    
    def print_temp_details(data):
        values={
                'temperature':str(data['main']['temp']-273.15)+' Celcius',
                'latitude':str(data['coord']['lat']),
                'longitude':str(data['coord']['lon']),
                'humidity':str(data['main']['humidity'])+' %',
                'pressure':str(data['main']['pressure'])+' hPa',
                'wind-speed':str(data['wind']['speed']*1.60934)+' kmph',
                'wind-direction':str(data['wind']['deg'])+' degrees',
                'visibility':str(data['visibility'])+' metres',
                }
        
        for key in values:
            print(key+' : '+values[key])
        
    def calculate_coord(data):
        coord=[data['coord']['lat'],data['coord']['lon']]
        return coord
    
    
    data=api_for_weather(place)
    print_temp_details(data)
    coord=calculate_coord(data)
#    print('coordinates of {0}: {1}'.format(place,coord))
    return coord    

#%%
#get the current geological conditions of the place within a pd of +-1mths
def get_soil_info(place,coord):
    def api_for_geocon(place):
        now = datetime.datetime.now()
        start_date=str(now.year)+'-'+str(now.month-1)+'-'+str(now.day)
        end_date=str(now.year)+'-'+str(now.month+1)+'-'+str(now.day)
    #    result=requests.get('https://api.weatherbit.io/v2.0/history/agweather?lat='+str(coord[0])+'&lon='+str(coord[1])+'&start_date='+start_date+'&end_date='+end_date+'&key=283a77fe5cbe46718430e4d5418be6c1')
        result=requests.get('https://api.weatherbit.io/v2.0/forecast/agweather?lat='+str(coord[0])+'&lon='+str(coord[1])+'&key=3d6dc8552cb74208866db831e6cc7724')
        data=result.json()
        return data
    
    def cal_mean(data):
        mean_vals=[]
        summ_vals_dict={}
        keywords=['bulk_soil_density','skin_temp_avg','precip','specific_humidity','pres_avg','soilt_0_10cm','soilm_0_10cm','wind_10m_spd_avg']
        for k in keywords:
            summ=0
            for i in range(0,9):
                summ+=data['data'][i][k]
            summ_vals_dict[k]=summ
        for key in summ_vals_dict:
            summ_vals_dict[key]=(summ_vals_dict[key])/9
    
        return summ_vals_dict
    
    
    daaa=api_for_geocon(place)
    ppp=cal_mean(daaa)
    return ppp

#%%
#    geocoding
def geocoding(place):
    coord=[]
    result=requests.get('https://api.opencagedata.com/geocode/v1/json?q='+place+'&key=217e890a4fed4cc780a83c8cce2abf14')
    data=result.json()
    coord.append(data['results'][0]['geometry']['lat'])
    coord.append(data['results'][0]['geometry']['lng'])
    return (coord)


    #%%

#logout
#
#change the
#redeem ke side mein call me
#call me pe click pe same kaam as on redeem
#call me pe login compulsory

#%%
#import pprint
#print('WELCOME TO THE WEATHER INFORMER\n\n')
#s=input('please enter the city you wan tto know the weather of: ')
#print('what would you like ot know about the city\'s weather \n')
#print('1. WIND \n 2. ATMOSPHERE INFO \n 3. ASTRONOMY')
#choice= input('\n please enter the number mentioned before the above options as per your requirement')
#
#if choice=='1':
#    choicetext='wind'
#elif choice=='2':
#    choicetext='atmosphere'
#else:
#    choicetext='astronomy'
#
#from rapidconnect import RapidConnect
#rapid = RapidConnect("default-application_5b73eddbe4b02799e7f62c4e", "0de0badd-30ac-408c-9e0c-e2a4e51dbfc6")
#
#result = rapid.call('YahooWeatherAPI', 'getWeatherForecast', { 
#	'location': s ,
##    'filter': choicetext
#})
#
#final=[]
#d=result['query']['results']['channel']['item']['forecast']
#keywords=['day','high','low']
#
#for i in range(0,7):
#    if i==0:
#        e=[]
#        e.append(d[i]['day'])
#        for j in keywords:
#            e.append(d[i][j])
#        date=e[1].split(' ')
#        date.pop()
#        date=' '.join(date)
#        e[1]=date
#        final.append(e)
#    else:
#        e=[]
#        for j in keywords:
#            e.append(d[i][j])
#        date=e[0].split(' ')
#        date.pop()
#        date=' '.join(date)
#        e[0]=date
#        final.append(e)
#        
#print(final)
#
#for i in final:

#%%