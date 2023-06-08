import sys,os
import socket
from datetime import datetime
import time

ver ="\033[1;31m"
os.system('clear')
print(f'\033[1;36m*'*70)
print(f"{ver}::::CARREGANDO::::")
print(f"{ver}[                        ]0%")
time.sleep(1)
print(f"{ver}[=====                   ]25%")
time.sleep(1)
print(f"{ver}[========                ]35%")
time.sleep(2)
print(f"{ver}[===========             ]50%")
time.sleep(1)
print(f"{ver}[===============         ]75%")
time.sleep(2)
print(f"{ver}[====================    ]95%")
time.sleep(1)
print(f"{ver}[========================]100%")
os.system("clear")
print(f"""\033[1;31m
    █▀▀ █▀▀ █▀▀█ █▀▀▄ ░░ █▀▀ █▀▀ █▀▀
    ▀▀█ █░░ █▄▄█ █░░█ ▀▀ ▀▀█ █▀▀ █░░
    ▀▀▀ ▀▀▀ ▀░░▀ ▀░░▀ ░░ ▀▀▀ ▀▀▀ ▀▀▀""")
time.sleep(2)
print("""\033[1;31m
      .....
                        .....
           OK.                           00
           .0k          .....           x0:
            :0o         .....          cOo
             d0;           ..         '0k
              O0.                    .O0
              .00                    O0.
               ;xo..              ..lx;
              ..oNd                dWo..
                .' .              . ,.
                .,'..   .    .   ..',.
                  .,'.  .    .  .';.
                   ....'..  .......
                    .. .      . ..
                     ....    . ..
                     .....  . ...
                      .,.... ''
                       .,''.,'.
                       ..,.,..
                       .'','''
                       ...... .
                     .. .    ' .
                   .....      ....
                   ...         ..""")

print(f'\033[1;36m*'*70)
ip = input(f'\033[1;32mSCAN PORTS IP-HOST----> \033[1;34m ')
print('=' * 50)
print(f'\033[1;33mSCAN IP >>> ' + ip)
print(f'\033[1;36mSCANNING STARTED AT: ' + str(datetime.now()))
print('SCANEANDO REDE AQUARDE...')
print('=' * 50)
portas = [17,18,22,23,67,68,69,80,111,123,135,136,137,138,139,161,162,1900,3389,5353,5900,1433,443]
for port in portas:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.1)
    result= s.connect_ex((ip, port))
    if result == 0:
        print('[+] PORT OPEN ==>',[port])
        print('-'*50)
    else:
        print('[-] PORT CLOSE==>',[port],end='\r')



