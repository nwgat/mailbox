# main.py
# nwgat.ninja
# https://nwgat.ninja/mailboxninja

import urequests, machine
from config import *

# MailNinja Notification
hook = urequests.get((webhook))

# show network status
status = urequests.get((webhook_server))
print ('--------------------')
print ('Internet Status:', (status.text))
print ('--------------------')

# Power Saving mode (RST + GND to wake up with a reed door sensor)
#machine.deepsleep()