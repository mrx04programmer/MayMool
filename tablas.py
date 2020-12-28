#_*_ coding: utf8 _*_
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
def check():
	print R+""" [!] Debes ejecutar el programa en el usuario root"""
	print B+""" 

       .__                   __   .__                           
  ____ |  |__   ____   ____ |  | _|__| ____    ____             
_/ ___\|  |  \_/ __ \_/ ___\|  |/ /  |/    \  / ___\            
\  \___|   Y  \  ___/\  \___|    <|  |   |  \/ /_/  >           
 \___  >___|  /\___  >\___  >__|_ \__|___|  /\___  / /\  /\  /\ 
     \/     \/     \/     \/     \/       \//_____/  \/  \/  \/ 
                                        
"""
os.system("clear")
check()
time.sleep(2)
print(B+"[*]"+GRs+" Configurando IP forward")
os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
time.sleep(1)
print(B+"[*]"+GRs+" Configurando tablas...")
time.sleep(1)
os.system("iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080")
os.system("iptables -t nat -A PREROUTING -p tcp --destination-port 443 -j REDIRECT --to-port 8080")
os.system("iptables -t nat -A PREROUTING -p tcp --destination-port 123 -j REDIRECT --to-port 123")
time.sleep(2)
print(B+"[*] "+W+"IPTABLES complete.")