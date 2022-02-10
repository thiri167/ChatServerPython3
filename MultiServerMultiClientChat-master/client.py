#Multi Server Multi Client Chat Application
#FE Front End Server
#BE Back End Server

from socket import *
import threading 
import sys
from Crypto.Cipher import AES

server=raw_input('Please enter IP address to connect ') #IP Address of the FE Server
# send an empty message only during the beginning of connection

#Encrypting the messages before sent to the Server
def do_encrypt(message):
	obj = AES.new('key1234567890123', AES.MODE_CBC, '1234567890123456')
	ciphertext = obj.encrypt(message)
    	return ciphertext
#Decryption of messages by the client
def do_decrypt(ciphertext):
	obj2 = AES.new('key1234567890123', AES.MODE_CBC, '1234567890123456')
	message = obj2.decrypt(ciphertext)
	return message

data = ''
data = data.ljust(16,'^')

Port = 4002 #Port number of the Front End Server
socket1 = socket(AF_INET, SOCK_DGRAM)
socket1.sendto(data, (server, Port))
print "----------------Chat Begins---------------------"
def transmit():
	while 1:
		data = raw_input("You:")
		data2 = data.upper()
		data3 = data2.ljust(16, '^')
		data4 = do_encrypt(data3)
		socket1.sendto(data4, (server, Port))
		if data == "EXIT" or data == "exit":
			print "\n Exiting chat"
			print "----------------------------------------------"
			second.exit()
			socket1.close()
       			break

def get(): 
	while 1: 
		new_data, address = socket1.recvfrom(2048)
		new_data = new_data.split(':')
		if len(new_data[1]) == 16:
			new_data2 = do_decrypt(new_data[1])
			new_data3 = new_data2.split('^')
			print "\n", new_data3[0]
			if new_data3[0] ==  "EXIT" or new_data3[0] == "exit":
				print "\n Exiting chat"
                        	print "----------------------------------------------"
                        	first.exit()
                        	socket1.close()
                       		break
		else:
			continue

first = threading.Thread(target=transmit)
second = threading.Thread(target=get)

first.start()
second.start()
first.join()
second.join()
sys.exit()
