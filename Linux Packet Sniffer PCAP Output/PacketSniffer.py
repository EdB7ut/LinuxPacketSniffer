# Edward Brutski
# 10/22/2022
# CYB 333, Professor Heurmann
# Course Project Option 2

import socket
from struct import pack
import time

class PCAPFile:
	def __init__(self, filename):
		self.fp = open(filename, 'wb')
		header = pack('!IHHiIII', 0xa1b2c3d4, 2, 4, 0, 0, 65535, 1)
		print(header)
		self.fp.write(header)
		
	def write(self, data):
		seconds, mseconds = [int(part) for part in str(time.time()).split('.')]
		length = len(data)
		message = pack('!IIII', seconds, mseconds, length, length)
		self.fp.write(message)
		self.fp.write(data)
		
	def close(self):
        	self.fp.close

conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
pcap = PCAPFile('packets.pcap')
while True:
    raw_data, addr = conn.recvfrom(65535)
    pcap.write(raw_data)
pcap.close()
