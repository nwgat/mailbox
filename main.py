# main.py
# nwgat.ninja
# https://nwgat.ninja/mailboxninja

import machine
import urequests
import time

# MailNinja Notification
response = urequests.get('http://sub.yourdomain.com:9292/hooks/mailninja?token=42')

# Power Saving mode (RST + GND to wake up with a reed door sensor)
time.sleep(5)
machine.deepsleep()
