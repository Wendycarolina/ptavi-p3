#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):
    
    def __init__ (self):
        self.width = ""
        self.heigth = ""
        self.backgroundcolor = ""
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.left = ""
        self.right = ""
        self.src = ""
        self.region = ""
        self.begin = ""
        self.dur = ""
        self.inRoot = 0
        self.inRegion = 0
        self.inImg = 0
        self.inAudio = 0
        self.inTextstream = 0
    
    def startElement(self, name, attrs):
        if name == 'root-layout':
            self.width = attrs.get('width', "")
            self.height = attr.get('height', "")
            self.backgroundcolor = attr.get('background-color', "")
            self.inRoot = 1
            
        elif name == 'region':
            self.id = attrs.get('id', "")
            self.top = attrs.get('top',"")
            self.bottom = attrs.get('bottom', "")
            self.left = attr.get('left', "")
            self.right = attr.get('right', "")
            self.inRegion = 1
        elif name == 'img':
            self.src = attrs.get('src', "")
            self.region = attrs.get('region', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")
            self.inImg = 1
        elif name == 'audio':
            self.src = attrs.get('src', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur',"")
            self.inAudio = 1
        elif name == 'textstream':
            self.src = attrs.get('src',"")
            self.region = attrs.get('region', "")
            self.inTextstream = 1

        dicc_root = {'width': self.width, 'height': self.height, 'backgroundcolor': self.backgroundcolor}
        dicc_region = {'id': self.id, 'top': self.top, 'bottom': self.bottom, 'left': self.left, 'right': self.right}
        dicc_img = {'src': self.src, 'region': self.region, 'begin': self.begin, 'dur': self.dur}
        dicc_audio = {'src': self.src, 'begin': self.begin, 'dur': self.dur}
        dicc_text = {'src': self.src, 'region': self.region}
        print(dicc_root)
        print(dicc_region)
        print(dicc_img)
        print(dicc_audio)
        print(dicc_text)
"""     def endElement(self, name):
        if name == 'root-layout':
            self.root-layout = ""
            self.inRoot = 0
        elif name == 'region':
            self.region = ""
            self.inRegion = 0
        elif name == 'img':
            self.img = ""
            self.inImg = 0
        elif name == 'audio':
            self.audio = ""
            self.inAudio = 0
        elif name == 'textstream':
            self.textstream = ""
            self.inTextstream = 0
 def characters(self, char):
        if self.inRoot:
            self.root-layout += 
        if self.inRegion:
            self.Region += 
        if self.inImg:
            self.img += char
        if self.inAudio:
            self.audio += 
        if self.inTextstream:
            self.textstream += 

    def get_tags(self):
"""

if __name__ == "__main__":
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))












 
            

