# MayMool
Ataque Man in the Middle dentro de una red local. 👨‍💻
###### Attack Man In The Middle in the network local 👨‍💻
Automatizador de ataque Man in the Middle.
https://ibb.co/PrgR98V
https://ibb.co/QmP51nf
### Pre-Requisitos 📋

Names          | Method of install
---------------|-------
nmap           | [https://nmap.org/ or 'sudo apt install nmap'](https://nmap.org/)
xterm          | [apt install xterm](https://pkgs.org/search/?q=xterm)
mitm6          | [https://github.com/fox-it/mitm6](https://github.com/fox-it/mitm6)
python all     | [https://www.python.org/ or 'sudo apt install python'](https://www.python.org/)
ettercap       | [https://www.ettercap-project.org/downloads.htm or 'sudo apt install ettercap'](https://www.ettercap-project.org/downloads.html)
macchanger     | ['sudo apt install macchanger'](https://github.com/alobbs/macchanger)
### Ejecutar 🚬
##### Privacidad :
    1. Is advisable to use macchanger for your anonymity:
          ===================================================
          $ sudo macchager --mac=00:11:22:33:44:55 wlp1s0
          ===================================================
          used:  sudo macchager --mac=<mac false custom> <interface>


##### Ejecución:
    2. Executing the script evil:
          $ sudo python maymool.py
          -----------------------------------------------------
          Note: maymool have don't the argument of '--help'
- Lo primero que hará es configurar las tablas ARP para tener control de rediccionamiento que se le envía en la red.
![CHECKING TABLES...](https://funkyimg.com/i/3at2M.png)
- Acontinuación, te pedirá que ingreses la interfaz de red a trabajar.
![INTERFACE](https://funkyimg.com/i/3at3k.png)
- Luego te preguntara si deseas escanear objetivos con nmap (el archivo se exporta como scan-red.log) y introducimos la ip local del sistema (command: ifconfig),ip victima y el gateway(ip del router o modem)
![NMAP SCAN](https://funkyimg.com/i/3at2Q.png)}
- Si observamos el archivo generado 'scan-red.log', se encuentra los dispositivos conectados a la red, sus hostname, MAC,OS,etc.
![SCAN-RED.log](https://funkyimg.com/i/3at3x.png)
- MayMool en acción: En la ventana del terminal principal, mostrara el contenido encriptado con el que se consiguio ettercap. En la ventana de xterm, tendremos en primer plano la ip victima y esperando a que la vicitima habra algún contenido
![MayMool In Accion](https://funkyimg.com/i/3at3Z.png)
- El contenido mostrado con mitm6 , se mostrara de la siguiente manera: 
![mitm6 window](https://funkyimg.com/i/3at47.png)

            Primera parte: página/servicio/servidor o ip
            Segunda parte: Tipo de mensaje que llega hacia la victima.
