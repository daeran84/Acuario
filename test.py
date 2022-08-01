from PyQt5.QtCore import QDate
from PyQt5 import QtCore
from datetime import date


nac = QDate(2015, 4, 2)
nac_string = nac.toString(QtCore.Qt.ISODate)

print(nac_string)