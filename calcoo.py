#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class calculadora():
    """ Creo la clase calculadora """


    def plus(self, op1, op2):
        return op1 + op2


    def min(self, op1, op2):
        return op1 - op2

if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numercial paramter")

    calculadora = calculadora()

    if sys.argv[2] == "suma":
        result = calculadora.plus(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = calculadora.min(operando1, operando2)
    else:
        sys.exit('operacion solo puede ser suma o resta')
    print(result)
