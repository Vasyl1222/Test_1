from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QPushButton,QLabel, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QLineEdit
from instr import*

class TestWin(QWidget):
    def __init__(self):
       QWidget.__init__(self)
       self.set_appear()
       self.initUi()
       self.connects()
      

    def set_appear(self):
      self.setWindowTitle(title_text)
      self.resize(win_x,win_y)
      self.move(win_x,win_y)
    
    def initUi(self):
        self.btn_text = QPushButton (txt_sendresults, self)
        self.btn_test1 = QPushButton (txt_starttest1, self)
        self.btn_test2 = QPushButton(txt_starttest2, self)
        self.btn_tests = QPushButton(txt_starttest3, self)

        self.text_name = QLabel (txt_name)
        self.text_age = QLabel(txt_age)
        self.text_testl1= QLabel(txt_test1)
        self.text_test2 = QLabel (txt_test2)
        self.text_tests = QLabel(txt_test3)
        self.text_timer = QLabel (txt_timer)
      
        self.line_name = QLineEdit (txt_hintname)
        self.line_age = QLineEdit(txt_hintage)
        self.line_testi = QLineEdit(txt_hinttest1)
        self.line_test = QLineEdit(txt_hinttest2)
        self.line_test3 = QLineEdit(txt_hinttest3)

        self.text_timer=QLabel(txt_timer)
        self.text_name=QLabel(txt_name)

        self.h_line=QHBoxLayout()
        self.r_line=QVBoxLayout()
        self.l_line=QHBoxLayout()

        self.r_line.addWidget(self.text_timer, alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.text_name, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.line_name, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.text_age, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.line_age, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.txt_test1, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test1, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.line_test1, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.text_test2, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test2, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.text_test3, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test3, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.line_test2, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.line_test3, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn_next, alignment=Qt.AlignCenter)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    
    def connects(self):
        pass