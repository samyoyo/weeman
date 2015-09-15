#!/usr/bin/env python2
##
## weeman - http server for phishing.
##
## Written by Hypsurus <hypsurus@mail.ru>
##

import sys
from core.misc import printt

try:
    from bs4 import BeautifulSoup as bs
except ImportError:
    printt(1, "Please install beautifulsoup 4 to continue ...")

def tests_pyver():
    if sys.version[:3] == "2.7" or "2" in sys.version[:3]:
        pass # All good
    elif "3" in sys.version[:3]:
        printt(1,"Weeman has no support for Python 3.")
    else:
        printt(1, "Your Python version is very old ..")

def tests_platform():
    if "linux" in sys.platform:
        printt(3, "Running Weeman on linux ... (All good)")
    elif "darwin" in sys.platform:
        printt(3, "Running Weeman on \'Mac\' (Not tested)")
    elif "win" in sys.platform:
        printt(3, "Running Weeman on \'Windows\' (Not tested)")
    else:
        printt(3, "If \'Weeman\' runs sucsessfuly on your platform %s\nPlease let me (@Hypsurus) know!" %sys.platform)

def main():
    tests_pyver()
    tests_platform()
    from core.shell import shell
    shell()

if __name__ == '__main__':
    main()
