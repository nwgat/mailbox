# wifi.py
# nwgat.ninja
# https://nwgat.ninja/mailboxninja

import network

# setup wifi mode
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# static ip (uncomment to enable)
#wlan.ifconfig(('192.168.1.8', '255.255.255.0', '192.168.1.1', '1.1.1.1'))

# connect
wlan.connect('yournetwork', 'password')