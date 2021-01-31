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
    1. Is advisable to use macchanger for your anonymity:
          ===================================================
          $ sudo macchager --mac=00:11:22:33:44:55 wlp1s0
          ===================================================
          used:  sudo macchager --mac=<mac false custom> <interface>

    2. Executing the script evil:
          $ sudo python maymool.py
          -----------------------------------------------------
          Note: maymool have don't the argument of '--help'
