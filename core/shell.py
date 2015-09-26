##
## shell.py - the weeman main shell
##
## Written by @Hypsurus 
##


import sys
import os
from core.complete import complete
from core.complete import array 
from core.config import __version__
from core.config import __codename__
from core.misc import printt
from core.misc import print_help
from core.config import url
from core.config import action_url
from core.config import port
from core.config import user_agent
from core.httpd import weeman

def print_startup():
    #print("\033[H\033[J") # Clear the screen
    print("\033[01;31m")
    print(open("core/logo.txt", "r").read())
    print("\033[00m")
    print("\033[01;33m\t    ..:: Weeman %s (%s) ::..\033[00m" %(__version__, __codename__)) 
    print("\033[01;34m\t-------------------------------------\033[00m")
    print("\t\'There are plenty of fish in the sea\'")
    print("\033[01;34m\t-------------------------------------\n\033[00m")
 
def shell():
    global url
    global port
    global action_url
    global user_agent

    print_startup()
    complete(array)

    if os.path.exists("history.log"):
        if  os.stat("history.log").st_size == 0:
            history = open("history.log", "w")
        else:
            history = open("history.log", "a")
    else:
        history = open("history.log", "w")

    while True:
        try:
            an = raw_input(" (weeman ) : ")
            prompt = an.split()
            if not prompt:
                print("Error: What? try help.")
            elif prompt[0] == ";" or prompt[0] == "clear":
                print("\033[H\033[J")
            elif prompt[0] == "q" or prompt[0] == "quit":
                printt(2,"bye bye!")
                break;
            elif prompt[0] == "help" or prompt[0] == "?":
                print_help()
            elif prompt[0] == "show":
                l = 11 + len(url)
                sys.stdout.write("\033[01;32m\t")
                print("-" * l)
                print("\turl        : %s " %url)
                print("\tport       : %d " %(port))
                print("\taction_url : %s " %(action_url))
                print("\tuser_agent : %s " %(user_agent))
                sys.stdout.write("\t\033[00m")
                print("-" * l)
            elif prompt[0] == "set":
                if prompt[1] == "port":
                    port = int(prompt[2])
                    history.write("port = %s\n" %port)
                if prompt[1] == "url":
                    url = str(prompt[2])
                    history.write("url = %s\n" %url)
                if prompt[1] == "action_url":
                    action_url = str(prompt[2])
                    history.write("action_url = %s\n" %action_url)
                if prompt[1] == "user_agent":
                    prompt.pop(0)
                    u = str()
                    for x in prompt:
                        u+=" "+x
                    user_agent = str(u.replace("user_agent", ""))
                    history.write("user_agent = %s\n" %user_agent)
            elif prompt[0] == "run" or prompt[0] == "r":
                s = weeman(url,port)
                s.clone()
                s.serve()
            elif prompt[0] == "banner" or prompt[0] == "b":
                print_startup()
            else:
                print("Error: \'%s\' What? try help." %prompt[0])

        except KeyboardInterrupt:
            s = weeman(url,port)
            s.cleanup()
            print("\nInterrupt ...")
        except Exception as e:
            printt(3, "Error: Weeman recived error! (%s)" %(str(e)))
