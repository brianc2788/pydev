'''
arp-mitm-detect.py
------------------
"Detects" man-in-the-middle ARP-
spoofing by checking to see if
the hw address your packets are
being sent to (e.g. your router)
has changed. If it has, there is
a chance an attacker is forwarding
your packets to/from your device
and your access point.

Note; this script is untested.

Authored by: brianc2788@gmail.com
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
