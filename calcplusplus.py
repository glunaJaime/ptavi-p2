#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija
import csv

fichero = sys.argv[1]
with open('fichero.csv', 'r') as fich:
    fichero = csv.reader(fich)
    calcplus = calcoohija.CalculadoraHija()

    for line in fichero:
        operations = line[0]
        datos = line[1:]
        result = int(datos[0])

        if operations == "multiplica":
            print("resultado multiplicación = ")
            for n in range(1, len(datos)):
                resultado = calcplus.multiply(result, int(datos[n]))

        elif operations == "divide":
            print("resultado división = ")
            for n in range(1, len(datos)):
                if datos == "0":
                    resultado = ("Error: no se puede dividir por 0")
                else:
                    resultado = calcplus.divide(result, int(datos[n]))
        elif operations == "suma":
            print("resultado suma = ")
            for n in range(1, len(datos)):
                resultado = calcplus.plus(result, int(datos[n]))

        elif operations == "resta":
            print("resultado resta = ")
            for n in range(1, len(datos)):
                resultado = calcplus.min(result, int(datos[n]))
        else:
            sys.exit("sólo puede ser multiplicación, división, suma o resta")

        print(result)
