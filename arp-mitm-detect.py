'''
arp-mitm-detect.py
------------------
With a LOT of help...
from:
Ethical Hacking- A Hands-on Introduction...
by Daniel Graham

http://www.github.com/user5260/pyscripts/arp-mitm-detect.py

[Description]
Detects if you are being MITM'ed. No logging.

I.e., detects if your packets are being routed
by an attacker.
I.e., detects if you're host's IP tables
are being tampered with via MITM IP
forwarding/arping.

[Instructions/Usage]
Run this script if you are connected
via wi-fi.

No news is good news; if the script
exits without any output, it hasn't
detected any potential ARP tampering.
'''
from scapy.all import sniff

IP_MAC_Map = {}

def processPacket(packet):
	src_IP = packet['ARP'].psrc
	src_MAC = packet['Ether'].src
	if src_MAC in IP_MAC_Map.keys():
		if IP_MAC_Map[src_MAC] != src_IP:
			try:
				old_IP = IP_MAC_Map[src_MAC]
			except:
				old_IP = 'unknown'
			message = ("\n Possible ARP attack detected \n "
						+ "It is possible that the machine with IP address \n "
						+ str(old_IP) + " is pretending to be " + str(src_IP)
						+ '\n')
			return message
		else:
			IP_MAC_Map[src_MAC] = src_IP
	sniff(count=0, filter="arp", store = 0, prn = processPacket)
