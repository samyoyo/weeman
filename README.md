Weeman - http server for phishing
=================================

About
=====

I wrote this as a tool to test network security (the users),
Usually we will run Weeman with dns spoof attack (MITM).

Weeman will do the following steps:
------------------------------------

* Weeman will Create fake html page (from the website)
* Weeman will Wait for clients
* Weeman will Grab the POST data.(user,password,cookies)
* Weeman Will try to login the client to the original site :smiley:


![Weeman](https://pbs.twimg.com/media/COftz7qVAAELhct.jpg)

Requirements
============

* Python 2.7
* Python BeautifulSoup 4

Install BeautifulSoup
---------------------

* Archlinux - sudo pacman -S python2-beautifulsoup4
* For another OS: - sudo pip install beautifulsoup4
* Tested only on linux.

Usage
======

`set` - set value

`show` - show variabels

`run` - run the server

Run server:
-----------

> set url http://localhost

> set action_url http://localhost/sendlogin

> set port 2020

> set user_agent My User Agent

> run


Get Weeman
=============
                git clone git://github.com/Hypsurus/weeman
  
Copyright 2015 (C) Hypsurus <hypsurus@mail.ru>.

License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>.
