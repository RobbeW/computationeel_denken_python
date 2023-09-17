#!/usr/bin/python
# -*- coding: utf-8 -*-

getal = int( input( 'Geef een getal in: ' ) )

honderdtallen = ( getal // 100 ) % 10

print('\n{}'.format( honderdtallen ) )