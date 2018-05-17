'''
Created on 17 May 2018

@author: mark
'''
import xml.sax,re, urllib2


class AlbumHandler(xml.sax.ContentHandler):
    def startDocument(self):
        print "starting document \n"
        self.artists = {}
        self.lastartist=''
        self.currentTag=''
        self.found = False
    def startElement(self,tag,attributes):
        print "found element %s \n" % tag
        self.currentTag = tag
        if tag == 'album':
            self.artists[self.lastartist].append(attributes.get('id'))
    def characters(self,data):
        if not re.search('^\s*$',data):
            print "found data : %s \n" % data
            if self.currentTag == 'artist':
                self.artists[data] = []
                self.lastartist = data
    def endDocument(self):
        print(self.artists.__repr__())
req = urllib2.urlopen('https://www.ledge.co.za/img/album.xml')
xml.sax.parseString(req.read(),AlbumHandler())