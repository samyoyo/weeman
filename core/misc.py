##
## misc.py - usefull functions
##

import sys
import time

def printt(s, msg):
    if s == 1:
        print("\033[01;31m[%s] Error: %s\033[00m" %(time.strftime("%H:%M:%S"),msg))
        sys.exit(1)
    elif s == 2:
        print("\033[01;32m[%s] %s\033[00m" %(time.strftime("%H:%M:%S"),msg))
    elif s == 3: 
        print("\033[01;01m[%s] %s\033[00m" %(time.strftime("%H:%M:%S"),msg))
    else:
        print("\033[01;01m[%s] %s\033[00m" %(time.strftime("%H:%M:%S"),msg))

def print_help():
    print("\t\033[01;32mshow   : show default settings.")
    print("\tset    : set settings (set port 80).")
    print("\trun    : start the server.")
    print("\tclear  : clear screen.")
    print("\thelp   : show help.")
    print("\tquit   : bye bye.\033[00m")

def isroot():
    if os.getuid() !=0:
        printt(1,"Please run weeman as root.")


