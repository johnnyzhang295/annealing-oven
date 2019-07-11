from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import numpy as np

class Material(QWidget):
	def __init__(self):
		super().__init__()

		self.m_box = QComboBox()
		self.m_box.addItem("polycarbonate")
		self.m_box.addItem("polysulfone")
		self.m_box.setFixedWidth(200)

		self.m_label = QLabel("Material: ")


class Thickness(QWidget):
	def __init__(self):
		super().__init__()
		self.t_box = QLineEdit("0")
		self.t_box.setValidator(QDoubleValidator())
		self.t_box.setFixedWidth(50)

		self.t_label = QLabel("Thickness (mm): ")


class Start(QWidget):
	def __init__(self):
		super().__init__()
		self.start_button = QPushButton("Start")
		self.start_button.setFixedWidth(100)
		self.start_button.setStyleSheet("""
			QPushButton{
				background-color: 
			}
			QPushButton:pressed{
				background-color: #3cbaa2
			}
			""")

	def saveInput(self, material, thickness):

		m_value = material.currentText()
		t_value = thickness.text()
		user_input = np.array([m_value, t_value])

		np.savetxt('gui_output.txt', user_input, fmt='%s', newline=" ")
		self.start_button.setEnabled(False)
		
	
if __name__ == '__main__':

	app = QApplication([])
	app.setStyle('Windows')

	window = QWidget()
	layout = QGridLayout()

	m = Material()
	t = Thickness()

	s = Start()

	layout.addWidget(m.m_label,1,1)
	layout.addWidget(t.t_label,2,1)
	layout.addWidget(m.m_box,1,2)
	layout.addWidget(t.t_box,2,2)
	layout.addWidget(s.start_button,3,1)
	layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)

	s.start_button.clicked.connect(lambda:Start.saveInput(s, m.m_box, t.t_box))


	window.setLayout(layout)
	window.setGeometry(500,500,700,500)
	window.show()



	app.exec_()

