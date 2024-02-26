#!/usr/bin/python

print "Resultados de MySQLdb:"
import MySQLdb
miConexion = MySQLdb.connect( host='localhost', user= 'root', passwd='', db='pitbull_gym' )
cur = miConexion.cursor()
cur.execute( "SELECT tipo_documento, id_cliente FROM clientes" )
for tipo_documento, id_cliente in cur.fetchall() :
    print tipo_documento, id_cliente
miConexion.close()