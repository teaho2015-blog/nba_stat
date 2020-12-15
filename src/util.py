import math
from decimal import Decimal


def takeWin(elem):
    return elem['win']

def takeGDP(elem):
    gdp_str = str(elem['gdp'])
    num = Decimal(gdp_str[0:gdp_str.index('E')]) * Decimal(math.pow(10, int(gdp_str[gdp_str.index('E')+1:len(gdp_str)])))
    return num