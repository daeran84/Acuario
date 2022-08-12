from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from datetime import date

#text = '9:35 AM'

#text = (int(text.split(' ')[0].split(":")[0]), int(text.split(' ')[0].split(":")[1]))
#text = text[0].split(':')
#print(text)

l = ['sdf', 'asdfawef']

#def to_string(a):
#    li = ''
#    for i in (a):
#       li += f' {i},'
#    return li.strip().strip(',')

#print(to_string(l))

#a = 'Camilo Rioseco'

#b = a.replace(' ', '').isalpha()
#print(b)

def calculate_age(born):
    today = date.today()
    try:
        birthday = born.replace(year=today.year)
    except ValueError: # raised when birth date is February 29 and the current year is not a leap year
        birthday = born.replace(year=today.year, month=born.month+1, day=1)
    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year

print(calculate_age(date(int(1977), int(1), int(1))))