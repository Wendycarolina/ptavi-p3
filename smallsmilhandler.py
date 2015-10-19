#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):
    def __init__(self):
        self.etiqueta = ['root-layout', 'region', 'img',
                         'audio', 'textstream']
        self.atributo = {'root-layout': ['width', 'height',
                         'background-color'],
                         'region': ['id', 'top', 'bottom', 'left', 'right'],
                         'img': ['src', 'region', 'begin', 'dur'],
                         'audio': ['src', 'begin', 'dur'],
                         'textstream': ['src', 'region']}
        self.lista = []

    def startElement(self, name, attrs):
        dicc = {}
        if name in self.etiqueta:
            dicc['name'] = name
            for i in self.atributo[name]:
                dicc[i] = attrs.get(i, "")
            self.lista.append(dicc)

    def get_tags(self):
        return self.lista


if __name__ == "__main__":
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print(cHandler.get_tags())
