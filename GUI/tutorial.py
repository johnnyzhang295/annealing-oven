from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

app = QApplication([])
app.setStyle('Windows')

window = QWidget()

layout = QGridLayout()
m_label = QLabel("Material: ")
t_label = QLabel("Thickness (mm): ")

materials = QComboBox()
materials.addItem("polycarbonate")
materials.addItem("polysulfone")
materials.setFixedWidth(200)

thickness = QLineEdit("0")
thickness.setValidator(QDoubleValidator())
thickness.setFixedWidth(50)

start_button = QPushButton("Start")
start_button.setFixedWidth(100)

layout.addWidget(m_label,1,1)
layout.addWidget(t_label,2,1)
layout.addWidget(materials,1,2)
layout.addWidget(thickness,2,2)
layout.addWidget(start_button,3,1)
layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)

window.setLayout(layout)
window.setGeometry(500,500,700,500)
window.show()

app.exec_()