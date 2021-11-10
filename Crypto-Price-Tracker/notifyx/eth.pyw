import requests
import json
from time import sleep
from win10toast import ToastNotifier
from datetime import datetime

#Crypto-Price-Tracker
#Copyright (C) 2021  LIAM-G-344
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see https://github.com/LIAM-G-344/Crypto-Price-Tracker/blob/main/LICENSE.

fi_loc = __file__

print(fi_loc)

def getCryptoPrice():
    URL = "https://www.bitstamp.net/api/v2/ticker/ethusd/"
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)["last"])
        return priceFloat
    except requests.ConnectionError:
        print("Error querying Bitstamp API")

while True:
    toaster = ToastNotifier()
    now = datetime.now()
    current_time = now.strftime("Current Time: %H:%M")
    toaster.show_toast("Current Market Price: $" + str(getCryptoPrice()) + "/Ethereum",
                    current_time,
                   icon_path = "C:\Program Files\custom.ico" ,
                    duration=10)
    sleep(300)
