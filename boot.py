# boot.py
# nwgat.ninja
# https://nwgat.ninja/mailboxninja
import network
import main

# connect wifi
sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_if.connect("your_ssid", "yourwifipassword")
#sta_if.ifconfig(config=('192.168.1.4', '255.255.255.0', '192.168.1.1', '1.1.1.1')) # static ip
