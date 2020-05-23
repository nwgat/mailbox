# boot.py
# nwgat.ninja
# https://nwgat.ninja/mailboxninja

import network
import main
import esp

# disable debug
esp.osdebug(None)

# connect wifi
sta_if = network.WLAN(network.STA_IF)
sta_if.connect("your_ssid", "yourwifipassword")
