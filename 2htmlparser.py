import HTMLParser
from xml.etree import ElementTree
class NaiveHTMLParser(HTMLParser):
    """
    Python 3.x HTMLParser extension with ElementTree support.
    @see https://github.com/marmelo/python-htmlparser
    """

    def __init__(self):
        self.root = None
        self.tree = []
        HTMLParser.__init__(self)

    def feed(self, data):
        HTMLParser.feed(self, data)
        return self.root

    def handle_starttag(self, tag, attrs):
        if len(self.tree) == 0:
            element = ElementTree.Element(tag, dict(self.__filter_attrs(attrs)))
            self.tree.append(element)
            self.root = element
        else:
            element = ElementTree.SubElement(self.tree[-1], tag, dict(self.__filter_attrs(attrs)))
            self.tree.append(element)

    def handle_endtag(self, tag):
        self.tree.pop()

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)
        pass

    def handle_data(self, data):
        if self.tree:
            self.tree[-1].text = data

    def get_root_element(self):
        return self.root

    def __filter_attrs(self, attrs):
        return filter(lambda x: x[0] and x[1], attrs) if attrs else []

html=""
with open('2.html', 'r') as content_file:
    html = content_file.read()
h = HTMLParser()
parser = NaiveHTMLParser(h)
root = parser.feed(html)
parser.close()

# root is an xml.etree.Element and supports the ElementTree API
# (e.g. you may use its limited support for XPath expressions)

# get title
#print(root.find('head/title').text)

# get all anchors
for a in root.findall('table'):
    print(a)
