#!/usr/bin/python
# -*- coding: utf-8 -*-

afstand = float( input( 'Geef een afstand (in km) in: ' ) )

verbruik = round( afstand * 4.5 / 100, 2 )

print('{} liter'.format( verbruik ) )