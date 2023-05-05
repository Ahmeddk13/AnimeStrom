import requests as req
import time
while True:
    time.sleep(3)
    try :
        r = req.get("https://admin-panel-kitabi.ahmeddk13.repl.co")
        rr = req.get("https://kotobati.ahmeddk13.repl.co/")
    except Exception :
        print("Error")
