from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


#text = '9:35 AM'

#text = (int(text.split(' ')[0].split(":")[0]), int(text.split(' ')[0].split(":")[1]))
#text = text[0].split(':')
#print(text)

l = ['sdf', 'asdfawef']

def to_string(a):
    li = ''
    for i in (a):
        li += f' {i},'
    return li.strip().strip(',')

print(to_string(l))