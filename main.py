# main.py
# nwgat.ninja MailNinja
# https://nwgat.ninja/mailboxninja

import machine
import urequests
import time

# MailNinja Notification

sleep(2)
response = urequests.get('http://yourmachine:9000/hooks/mailninja?token=42') # if you run webhook on a local machine
#response = urequests.get('http://192.168.4.2:9000/hooks/mailninja?token=42') # if your connected to esp8266 via its AP
response = urequests.get('http://hook.yourdomain.com/hooks/mailninja?token=42')

# put the device to sleep (uncomment when your done testing)
#machine.deepsleep()
