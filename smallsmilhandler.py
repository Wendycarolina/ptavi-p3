#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):
    
    def __init__ (self):
        self.width = ""
        self.height = ""
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
    
    def startElement(self, name, attrs):
        lista = []
        if name == 'root-layout':
            self.width = attrs.get('width', "")
            self.height = attrs.get('height', "")
            self.backgroundcolor = attrs.get('background-color', "")
            dicc_root = {'width': self.width, 'height': self.height, 'backgroundcolor': self.backgroundcolor}
            print(dicc_root)
            lista.append(dicc_root)
        elif name == 'region':
            self.id = attrs.get('id', "")
            self.top = attrs.get('top',"")
            self.bottom = attrs.get('bottom', "")
            self.left = attrs.get('left', "")
            self.right = attrs.get('right', "")
            dicc_region = {'id': self.id, 'top': self.top, 'bottom': self.bottom, 'left': self.left, 'right': self.right}
            print(dicc_region)
            lista.append(dicc_region)
        elif name == 'img':
            self.src = attrs.get('src', "")
            self.region = attrs.get('region', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")
            dicc_img = {'src': self.src, 'region': self.region, 'begin': self.begin, 'dur': self.dur}
            print(dicc_img)
            lista.append(dicc_img)
        elif name == 'audio':
            self.src = attrs.get('src', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur',"")
            dicc_audio = {'src': self.src, 'begin': self.begin, 'dur': self.dur}
            print(dicc_audio)
            lista.append(dicc_audio)
        elif name == 'textstream':
            self.src = attrs.get('src',"")
            self.region = attrs.get('region', "")
            dicc_text = {'src': self.src, 'region': self.region}
            print(dicc_text)
            lista.append(dicc_text)
        
        
        print(lista)

if __name__ == "__main__":
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
