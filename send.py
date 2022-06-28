import machine
import network
import socket
import time
import random

pin = machine.Pin(2, machine.Pin.OUT)

UDP_PORT = 5005
# enable station interface and connect to WiFi access point
nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.connect('network_name', 'password')
# now use sockets as usual
nic.ifconfig(('192.168.0.24', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
ip = nic.ifconfig()[0]
print(ip)

print("This is Tx Node")

Power = 0.1
UDP_IP = "192.168.0.30"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.bind(('192.168.0.35', UDP_PORT))

while True:
    Water = random.randint(0, 1)
    Water = bool(Water)
    PowerStr = ("Power Consumption: " + str(Power) + " kWh")
    WaterStr = ("Water Running: " + str(Water))

    s.sendto(str.encode(PowerStr), (UDP_IP, UDP_PORT))
    s.sendto(str.encode(WaterStr), (UDP_IP, UDP_PORT))

    pin.value(1)
    time.sleep(1)
    pin.value(0)




