import requests as req
import time
while True:
    time.sleep(60)
    try :
        r = req.head("https://admin-panel-kitabi.ahmeddk13.repl.co")
        rr = req.get("https://kotobati.ahmeddk13.repl.co/")
    except Exception :
        print("Error")
