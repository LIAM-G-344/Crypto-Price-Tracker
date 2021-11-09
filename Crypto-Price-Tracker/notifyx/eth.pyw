import requests
import json
from time import sleep
from win10toast import ToastNotifier
from datetime import datetime

#add a config file to change the crypto coin type

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
