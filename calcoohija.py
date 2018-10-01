#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo


class CalculadoraHija(calcoo.calculadora):

    def multiply(self, op1, op2):
        return op1 * op2

    def divide(self, op1, op2):
        return op1 / op2

if __name__ == "__main__":

    try:
        calculadorahija = CalculadoraHija()

        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "multiplicacion":
        result = calculadorahija.multiply(operando1, operando2)
    elif sys.argv[2] == "division":
            if operando2 == 0:
                result = "Error: Division by 0 is not allowed"
            else:
                result = calculadorahija.divide(operando1, operando2)
    elif sys.argv[2] == "suma":
        result = calculadorahija.plus(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = calculadorahija.min(operando1, operando2)
    else:
        sys.exit('solo se puede suma, resta, multiplicacion o division')
    print(result)
