#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

if(sys.argv[1] == 'fichero'):
    fichero = open('fichero.csv', 'r')
    fichero = fichero.readlines()
else:
    sys.exit("file not found")

if __name__ == "__main__":

    calcplus = calcoohija.CalculadoraHija()

    for line in fichero:
        operations = line.split(',')[0]
        datos = line.split(',')[1:]
        resultado = int(datos[0])

        if operations == "multiplica":
            print("resultado multiplicacion = ")
            for n in range(1, len(datos)):
                resultado = calcplus.multiply(resultado, int(datos[n]))

        elif operations == "divide":
            print("resultado division = ")
            for n in range(1, len(datos)):
                if datos == "0":
                    resultado = ("Error: no se puede dividir por 0")
                else:
                    resultado = calcplus.divide(resultado, int(datos[n]))
        elif operations == "suma":
            print("resultado suma = ")
            for n in range(1, len(datos)):
                resultado = calcplus.plus(resultado, int(datos[n]))

        elif operations == "resta":
            print("resultado resta = ")
            for n in range(1, len(datos)):
                resultado = calcplus.min(resultado, int(datos[n]))
        else:
            sys.exit("sólo puede ser multiplicación, división, suma o resta")

        print(resultado)
