##
## config.py - config variables
## 
## Written by @Hypsurus
##

import os
import sys

__author__ = "Hypsurus <hypsurus@mail.ru>"
__version__ = "1.3"
__codename__ = "ArmWork"

def history_getkey(key):
    try:
        history = open("history.log", "r").readlines()
    except Exception as e:
        return 0
    if history == None:
        return 0
    for line in history:
        if line.startswith("\n") or line.startswith("#"):
            pass
        (skey,value) = line.split(" = ")
        if skey == key:
            return str(value[:-1])
    return 0

url = history_getkey("url") or "http://localhost"
port = int(history_getkey("port")) or int(8080)
action_url = history_getkey("action_url") or "http://localhost/login"
user_agent = history_getkey("user_agent") or "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36"


