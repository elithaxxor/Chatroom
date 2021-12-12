## UDP SERVER.PY
import os, sys, traceback, cv2, imutils, socket, time,datetime, base64
import threading, wave, pickle, struct, threading, queue
import numpy as np
#import pyaudio
'''

ATTEMMPT TO ESTABLISH SYN SYN-ACK CONNECTION VIA TCP, THEN SHIFT TO UDP FOR DATA TRANSFER 
pip install PyAudio
see (socket.opt)# https://notes.shichao.io/unp/ch7/

cb2.imencode os used to read an image from memory buffer. 
cv2.imcode, cv2.imenencode 


## q = queue.Queue(maxsize=10)
Constructor for a FIFO queue. maxsize is an integer that sets the upperbound limit on the number of items that can be placed in the queue. Insertion will block once this size has been reached, until queue items are consumed. If maxsize is less than or equal to zero, the queue size is infinite.

start udp listening 
'''

q = queue.Queue(maxsize=10)
Queue.qsize()
Queue.empty()
Queue.full()
print('Empty Queue? ',Queue.empty())
print('Empty full? ',Queue.full())
print('queue Size? ',Queue.qsize())





BUFF_SIZE = 65536 # play with buffer
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFF_SIZE)
host_name = socket.gethostbyname()
host_ip = socket.gethostbyname(host_name)
port = 4921
host_addr = ((host_ip, port))
server_info = f'[+] --[{host_ip}:{port}]-- '
print('X' *50)
print(f'[+] Server Listening [{time.time()}]]\n [{server_info}]')
vid = cv2.VideoCapture(1)
if vid.isOpened():
    print(f'[+] Stream Recv\'d  [{time.time()}]]\n [{server_info}]')

def make_vid():
    WIDTH=500
    while(vid.isoOpened):
        try:
            _, frame = vid.read()
            frame = imutils.resize(frame, width=WIDTH)
            q.put(frame)
        except exception as e:
            print(f'[-] -- [Error in make_vid function] -- [-] \n[{traceback.exc()}] \n [{sys.exc.info()[2]}]')
        print('[-] Chat Closed ')
        time.sleep(.0001)
        Brea
        vid.release()


def b64_encoder():
    encoded = cv2.namedWindow('[+] [B64-ENCODER STARTED] ')
    print('Encoded_value', Encoded )
    return encoded

def Queue_Info():
    Queue.qsize()
    Queue.empty()
    Queue.full()
    print('Empty Queue? ',Queue.empty())
    print('Empty full? ',Queue.full())
    print('queue Size? ',Queue.qsize())





def send_vid():
    def make_vid():
        def encypt_256():
            pass
        def decrytp_256():
            pass
    WIDTH = 500
    while(vid.isOpened()):
        try:
            _, frame = vid.read()
            frame = imutiles.reseize(frame, width=WIDTH)
            if frame:
                Queue_Info()
            q.put(frame)
        except Exception
    
    fps,st,frames2count,cnt=(0,0,20,0)
    cv2.namedWindow('[+] [OUTBOUND-FRAME] ')
    cv2.moveWindow('[+]) [OUTBOUND-FRAME ]', 400,30)
    while True: ##may need to remove while here
        msg, client_addr = server.socket.recvfrom(BUFF_SIZE)
        print(f'[+] [INBOUND CONNECTION] {time.ctime()} [+],]\n\tt', client_address)
        print(msg).decode('utf-8')
        WIDHT=500
        while True:
            frame = q.get()
            encoded, buffer = cv2.imencode('.jepg',frame,[cv2.IMWRITE_JPEG_QUALITY, 80])
            message = base64.base64.encode(buffer)
            print('encoded message')

















