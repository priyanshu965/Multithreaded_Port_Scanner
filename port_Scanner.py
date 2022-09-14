import argparse
from ast import arg, arguments, parse
from dataclasses import make_dataclass
from inspect import ArgSpec
import threading
import socket   
import time
from tracemalloc import start
from xmlrpc.client import ProtocolError

open_port = []

def prepare_args():
    op = argparse.ArgumentParser(description="Advance Port Scanner", usage= "%(prog)s 192.168.120.155")
    op.add_argument(metavar="IPv4",dest="ip",help="Target")
    op.add_argument("-s", "--start", dest="start", type=int, help="Starting POint", default=1)
    op.add_argument("-e", "--end", dest="end", type=int, help="Ending Port", default=65535)
    op.add_argument("-t", "--thread", dest="thread", type=int, help="Number Of Threads", default=500)
    op.add_argument("-v", "--verbose", dest="verbose", action="store_true", help="Verbose Mode")
    args = op.parse_args()
    return args

def prepare_port(start:int, end:int):
    for port in range(start,end+1):
        yield port

def scan_port():
    while True:
        try:
            s=socket.socket()
            s.settimeout(1)
            port = next(ports)
            s.connect((arguments.ip,port))
            open_port.append(port)
            if arguments.verbose:
                print(f"\r{open_port}",end="")
        except (ConnectionRefusedError, socket.timeout):
            continue
        except StopIteration:
            break

def prepare_threads(threads:int):
    thread_list = []
    for _ in range(threads+1):
        thread_list.append(threading.Thread(target=scan_port))
    
    for thread in thread_list:
        thread.start()

if __name__ == "__main__":
    start_time = time.time()
    arguments = prepare_args()
    ports = prepare_port(arguments.start,arguments.end)
    prepare_threads(arguments.thread)
    print(f"Open Ports:{open_port}")
    end_time = time.time()
    print(f"Time taken:{round(end_time-start_time,2)}")
