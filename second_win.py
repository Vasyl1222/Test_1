from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QPushButton,QLabel, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QLineEdit
from instr import*

class TestWin(QWidget):
    def set_appear(self):
      self.setWindowTitle(title_text)
      self.resize(win_x,win_y)
      self.move(win_x,win_y)
    
    def initUi(self):
        pass
    
    def connects(self):
        pass