#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys
import json
from urllib.request import urlretrieve


if __name__ == "__main__":
    try:
        fich = open(sys.argv[1], 'r')
        parser = make_parser()
        cHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(fich)
        lista = cHandler.get_tags()
        archivo = open('karaoke.json','w')
        line = json.dumps(lista)
        archivo.write(line)

        for dicc in lista:
            for etiqueta in dicc:
                if dicc[etiqueta].find('http://') == 0:
                    url = dicc[etiqueta]
                    elemento = url[url.rfind('/') + 1:]
                    urlretrieve(url, elemento)
                    modifica = dicc[etiqueta].split('/')[-1]
                    dicc[etiqueta] = modifica
                    

        for dicc in lista:
            print(dicc['name']),
            for i in dicc:
                if dicc[i] and i != 'name':
                    print("\t" + i + '="' + dicc[i] + '"')
    except IOError:
        sys.exit("Usage: python karaoke.py file.smil")
    except IndexError:
        sys.exit("Usage: python karaoke.py file.smil")
