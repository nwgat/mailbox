# main.py
# nwgat.ninja
# https://nwgat.ninja/mailboxninja

import urequests
import machine

# MailNinja Notification
hook = urequests.get('http://yourserver:9292/hooks/mailninja?token=42')

# show network status
status = urequests.get("http://yourserver.com:9292")
print ('--------------------')
print ('Network Status:', (status.content))
print ('--------------------')

# Power Saving mode (RST + GND to wake up with a reed door sensor)
#machine.deepsleep()
