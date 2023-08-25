from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QPushButton,QLabel, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QLineEdit
from instr import*
from second_win import*

class MainWin(QWidget):
    def set_appear(self):
      self.setWindowTitle(title_text)
      self.resize(win_x,win_y)
      self.move(win_x,win_y)
    
    def initUi(self):
      self.hello_txt=QLabel(txt_hello)
      self.btn_next=QPushButton(txt_next)
      self.instructions=QLabel(txt_instructions)
      self.layout=QVBoxLayout()

      self.hello_txt.addWidget(self.layout)
      self.btn_next.addWidget(self.layout)
      self.instructions.addWidget(self.layout)
    
    def connects(self):
      self.btn_next.clicked.connect(self.next_click)
    
    def next_click(self):
       self.hide()
       self.tw=TestWin()

app=QApplication([])
mw=MainWin()
app.exec_()