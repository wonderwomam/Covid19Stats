import datetime    #for reading present data
import time
import requests    #for getting covid data from web
from plyer import notification  #to get notifications

#let there be no data initially

covidData= None

try:
 covidData=requests.get("https://corona-rest-api.herokuapp.com/Api/pakistan")

except: #if data isnt fetched bcz of lack of internet
 print("check your Internet Connection!!")

 #if data is fetched
if (covidData != None):
        # converting data into JSON format
        data = covidData.json()['Success']

        # repeating the loop for multiple times
        while (True):
            notification.notify(
                # title of the notification,
                title="COVID19 PK Stats on {}".format(datetime.date.today()),
                # the body of the notification
                message="Total cases : {totalcases}\nToday cases : {todaycases}\nToday deaths :{todaydeaths}\nTotal active :{active}".format(
                    totalcases=data['cases'],
                    todaycases=data['todayCases'],
                    todaydeaths=data['todayDeaths'],
                    active=data["active"]
                    ),

                # creating icon for the notification
                # we need to download a icon of ico file format
                app_icon= 'F:\\Paomedia-Small-N-Flat-Beer.ico',
                # the notification stays for 50sec
                timeout=50
            )
            # sleep for 4 hrs => 60*60*4 sec
            # notification repeats after every 4hrs
            time.sleep(60 * 60 * 4)







