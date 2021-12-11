#!/usr/bin/env python

import httplib
import socket
import re
import csv

def is_website_online(host):
    """ Esta funcion chequea para un dominio si responde el dns
        si socket info devuelve algo entonces el dns funciona.
    """
    try:
        socket.gethostbyname(host)
    except socket.gaierror:
        return False
    else:
        return True


def is_page_available(host, path="/"):
    """  Esta funcion recupera el codigo de estado de un sitio web.
         si no puede acceder al dominio entonces devuelve falso.
    """
    try:
        conn = httplib.HTTPConnection(host)
        conn.request("HEAD", path)
        if re.match("^[23]\d\d$", str(conn.getresponse().status)):
            return True
    except StandardError:
        return None


with open('lista_url.csv', 'r') as File:
    reader = csv.reader(File)
    for row in reader:
        onLine = is_page_available(row[0])
        print('El sitio ' + str(row[0]) + ' está online? ----> ' + str(onLine))


      
     
