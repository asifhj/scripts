from HTMLParser import HTMLParser
import sys
# create a subclass and override the handler methods

class MyHTMLParser(HTMLParser):
    data_counter = 0 
    event=""
    counter = 0
    t = ""
    def handle_starttag(self, tag, attrs):
	if tag=="tr":
		t = "tr"
	        #print "Encountered a start tag:", tag
		print ""

    def handle_endtag(self, tag):
	if tag=="tr":
	        #print "Encountered an end tag :", tag
		#print ""
		self.event = ""
    def handle_data(self, data):
	if data.strip()!="":		
		self.event = self.event + ", " + str(data.strip().replace("\n", "").replace("\n", "").replace("  ",""))
		self.counter = self.counter + 1
		
	if self.counter == 7: 
		print self.event + "\n" 		
		self.counter = 0			
		

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
with open('2.html', 'r') as content_file:
    html_doc = content_file.read()
parser.feed(html_doc)
