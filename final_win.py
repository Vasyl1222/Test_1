from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QPushButton,QLabel, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QLineEdit
from instr import*
from second_win import*

class MainWin(QWidget):
    def __init__(self):
       QWidget.__init__(self)
       self.set_appear()
       self.initUi()
       self.connects()
       self.show()

    def set_appear(self):
      self.setWindowTitle(title_text)
      self.resize(win_x,win_y)
      self.move(win_x,win_y)
    
    def initUi(self):
      self.workh_test=QLabel(txt_workheart)
      self.index_test=QLabel(txt_index)

      self.line_layout=QVBoxLayout()

      self.line_layout.addWidget(self.index_test,alignment=Qt.AlignCenter)
      self.line_layout.addWidget(self.workh_test,alignment= Qt.AlignCenter)

      self.setLayout(self.line_layout)

    def connects(self):
        pass