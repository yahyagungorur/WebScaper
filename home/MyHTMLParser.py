from html.parser import HTMLParser
import re

class MyHTMLParser(HTMLParser):

    # Initializing lists
    def __init__(self):
        HTMLParser.__init__(self)
        self.lsStartTags = list()
        self.lsEndTags = list()
        self.IsData = list()
        self.i = 0
        self.h1 = list()
        self.fuctionname = ""

    # HTML Parser Methods
    def handle_starttag(self, startTag, attrs):
        if (startTag == "h1"):
            self.lsStartTags.append(startTag)
            self.i += 1

    def handle_endtag(self, endTag):
        if (endTag == "h1"):
            self.lsEndTags.append(endTag)
            self.i -= 1

    def handle_data(self, data):
        if (re.search("[{}:%#!]", data) == None):
            if self.fuctionname == "GetPrice":
                if (self.i):
                    self.IsData.append(data)
                    self.h1.append(data)
                elif (data.find("TL") != -1 or data.isdigit() or re.sub(r'\W', "", data).replace("TL", "").isdigit()):
                    self.IsData.append(data)

            else:
                self.IsData.append(data)
