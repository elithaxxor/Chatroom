## UDP SERVER.PY
import os, sys, traceback, cv2, imutils, socket, time,datetime, base64
import threading, wave, pickle, struct, threading, queue
import numpy as np


'''
Client Side- UDP Streamer / text room 

Set params for UDP -00 
'''
BREAK = False
# play with buffer

BUFF_SIZE = 65536
port = 4921


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFF_SIZE)
client_name = socket.gethostbyname()
client_ip = socket.gethostbyname(host_name)
client_addr = ((host_ip, port))
server_info = f'[+] --[{host_ip}:{port}]-- '
print(f'[+] Server Listening [{time.time()}]]\n [{server_info}]')
intro=b'[+].. [Client] Looking to Connect. \n [CLIENT-IP]--[{client_addr}]'

client_socket.sendto(intro,(host_ip, port))


