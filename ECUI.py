from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from SequenceMonitor import SequenceMonitor

class ECUI(QWidget):

	def __init__(self, parent=None):
		super(ECUI, self).__init__(parent)

		#sequence Monitor
		seqMonitor = SequenceMonitor()

		vLayout = QVBoxLayout()
		vLayout.addWidget(seqMonitor)

		self.setLayout(vLayout)


if __name__ == '__main__':

	import sys

	app = QApplication(sys.argv)

	mainWindow = ECUI()

	mainWindow.show()

	sys.exit(app.exec_())