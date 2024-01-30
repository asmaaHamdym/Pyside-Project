import sys

from PySide2.QtWidgets import *
from PySide2.QtCore import *

app = QApplication(sys.argv)
window = QWidget()



l1 = QLabel(window)
l1.setText("Welcome Asma")
l1.autoFillBackground()
l1.setGeometry(QRect(20,20,200,20))

window.setWindowTitle("Label Example")
window.resize(500, 500)
window.show()


sys.exit(app.exec_())