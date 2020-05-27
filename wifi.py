# wifi.py
# nwgat.ninja
# https://nwgat.ninja/mailboxninja

import network
from config import *

# set wifi mode
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# static ip (uncomment to enable)
#wlan.ifconfig(('192.168.1.20', '255.255.255.0', '192.168.1.1', '1.1.1.1'))

# connect
wlan.connect((ssid), (ssid_pw))
