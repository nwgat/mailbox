# boot.py
# nwgat.ninja
# https://nwgat.ninja/mailboxninja
import network
import main

# wifi
sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_if.scan()
sta_if.connect("your_ssid", "yourwifipassword")
sta_if.isconnected()
