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

	def saveInput(self, material, thickness):
		m_value = material.currentText()
		t_value = thickness.text()
		user_input = np.array([m_value, t_value])

		np.savetxt('gui_output.txt', user_input, fmt='%s', newline=" ")
		self.start_button.setEnabled(False)

class Temperature(QWidget):
	def __init__(self):
		super().__init__()
		self.t_box = QLineEdit("0")
		self.t_box.setValidator(QDoubleValidator())
		self.t_box.setFixedWidth(50)

		self.t_label = QLabel("Desired Temperature (C): ")

	
if __name__ == '__main__':

	app = QApplication([])
	app.setStyle('Windows')

	tab_window = QTabWidget()
	window = QWidget()
	mode_2 = QWidget()
	tab_window.addTab(window, "Mode 1")
	tab_window.addTab(mode_2, "Mode 2")
	layout = QGridLayout()
	mode2_layout = QGridLayout()

	m = Material()
	t = Thickness()
	s = Start()
	temp = Temperature()
	mode2_layout.addWidget(temp.t_label, 2,1)
	mode2_layout.addWidget(temp.t_box,2,2)
	mode2_layout.setAlignment(Qt.AlignLeft)

	layout.addWidget(m.m_label,1,1)
	layout.addWidget(t.t_label,2,1)
	layout.addWidget(m.m_box,1,2)
	layout.addWidget(t.t_box,2,2)
	layout.addWidget(s.start_button,3,1)
	layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)

	s.start_button.clicked.connect(lambda:Start.saveInput(s, m.m_box, t.t_box))

	window.setLayout(layout)
	mode_2.setLayout(mode2_layout)
	tab_window.setGeometry(500,500,700,500)
	tab_window.show()

	app.exec_()

