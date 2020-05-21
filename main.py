# main.py
# nwgat.ninja
# https://nwgat.ninja/mailboxninja

import machine
import urequests
import time

# MailNinja Notification

response = urequests.get('http://hook.yourdomain.com/hooks/mailninja?token=42')
response = urequests.get('http://yourmachine:9000/hooks/mailninja?token=42') # if you run webhook on a local machine
#response = urequests.get('http://192.168.4.2:9000/hooks/mailninja?token=42') # if your connected to esp8266 via its AP

#  sleep, keep it higher when you test and to 2 when your ready
sleep(2)

# put the device to sleep (uncomment when your done testing)
#machine.deepsleep()
