#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys


if __name__ == "__main__":
    try:
        fich = open(sys.argv[1], 'r')
        parser = make_parser()
        cHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(fich)
        lista = cHandler.get_tags()
        print(lista)
    except IOError:
        sys.exit("Usage: python karaoke.py file.smil")
    except IndexError:
        sys.exit("Usage: python karaoke.py file.smil")
