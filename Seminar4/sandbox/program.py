#!/usr/bin/env python3

"""
Popis programu:
Opakuje nekolikrat to co mu zadate.
"""

def opakuj():
    promenna = input("Zadej co mam zopakovat: ")
    pocet = int(input("Zadej kolikrat to mam zopakovat: "))
    print((promenna + '\n') * pocet)


if __name__ == '__main__':
    opakuj()