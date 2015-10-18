#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys
import json
from urllib.request import urlretrieve

class KaraokeLocal():
    def __init__(self, fich):
        parser = make_parser()
        cHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(fich)
        self.lista = cHandler.get_tags()

    def __str__(self):
        elemento = ''
        for dicc in self.lista:
            elemento += dicc['name']
            for i in dicc:
                if dicc[i] and i != 'name':
                    elemento += "\t" + i + '="' + dicc[i] + '"'
            elemento +='\n'
        return elemento
    def to_json(self, fich):
        if fich != 'karaoke.json':
            archivo = open('karaoke.json','w')
            contenido = json.dumps(self.lista)
            archivo.write(contenido)
       
    def do_local(self):
         for dicc in self.lista:
            for etiqueta in dicc:
                if dicc[etiqueta].find('http://') == 0:
                    url = dicc[etiqueta]
                    elemento = url[url.rfind('/') + 1:]
                    urlretrieve(url, elemento)
                    modifica = dicc[etiqueta].split('/')[-1]
                    dicc[etiqueta] = modifica
                    
        
if __name__ == "__main__":
    try:
        fich = open(sys.argv[1], 'r')
 
    except IOError:
        sys.exit("Usage: python karaoke.py file.smil")
    except IndexError:
        sys.exit("Usage: python karaoke.py file.smil")

    karaoke = KaraokeLocal(fich)
    print(karaoke)
    karaoke.to_json(fich)
    karaoke.do_local()
    karaoke.to_json(fich)
    print(karaoke)
