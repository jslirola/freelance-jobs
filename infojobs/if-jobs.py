#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import re
from bs4 import BeautifulSoup

# Remove HTML tags
def removeTags(data):
    rData = data.get_text()
    review_text = BeautifulSoup(rData)
    return review_text.get_text()

# Return category slug
def getChoice(option):
	slug = ["/","/informatica","/diseno-multimedia","/comunicacion-y-letras","/administracion-y-empresas","/profesionales","/sanidad-y-cuidados"]
	if option<1 or option>7: option = 1
	return slug[option-1]

# Show menu
print ("""
OFERTAS DE EMPLEO - INFOJOBS FREELANCE

    1. Cualquiera
    2. Informática
    3. Diseño multimedia
    4. Comunicación y letras
    5. Administración y empresas
    6. Profesionales
    7. Sanidad y cuidados
    """)

opt = getChoice(int(input("Seleccione una categoría [1-7]: ")))

# Concatenate URL base with category and to do request
url = 'https://freelance.infojobs.net/proyectos'+opt
resp = urllib.request.urlopen(url)
respData = resp.read()

parsed_html = BeautifulSoup(respData,'html.parser')
jobs = parsed_html.select("ul#resultdata > li")

# Iterate jobs with clear format
for item in jobs:
	print(removeTags(item.a.span)+" "+removeTags(item.select("li.date span")[0]))
	print("https://freelance.infojobs.net"+item.a.get('href'))
	print(removeTags(item.p))
	print("--------------------------------------------------------------------")

resp.close()