# boot.py
# nwgat.ninja
# https://nwgat.ninja/mailboxninja

import network
import main

# connect wifi
sta_if = network.WLAN(network.STA_IF)
sta_if.connect("your_ssid", "yourwifipassword")
