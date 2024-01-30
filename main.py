import sys
from PySide2 import QtWidgets

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QWidget()

window.resize(500, 500)
window.setWindowTitle('First GUI app')

window.show()

sys.exit(app.exec_())