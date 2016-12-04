# This is /etc/network/interfaces file I use on raspbian

auto lo
iface lo inet loopback

auto eth0
allow-hotplug eth0
iface eth0 inet manual

# Ethernet interface works as a router, using the wireless network
iface eth0 inet static
address 192.168.69.1
netmask 255.255.255.0
network 192.168.69.0
broadcast 192.168.69.255
gateway 192.168.69.1

auto wlan0
allow-hotplug wlan0
iface wlan0 inet dhcp
wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
post-down killall -q wpa_supplicant
iface default inet dhcp
