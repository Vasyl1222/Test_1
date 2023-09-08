from PyQt5.QtCore import Qt, QTimer,QTime
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication,QPushButton,QLabel, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QLineEdit
from instr import*
from final_win import*

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

        self.txt_timer=QLabel(txt_name)
        self.txt_name=QLabel(txt_hintname)
        self.line_name=QLineEdit(txt_age)
        self.text_age=QLabel(txt_hinttest1)
        self.line_age=QLineEdit(txt_test3)
        self.txt_test1=QLabel(txt_starttest1)
        self.btn_test1=QLabel(txt_hinttest2)
        self.txt_test2=QLabel(txt_test2)
        self.line_test1=QLineEdit(txt_starttest2)
        self.btn_test2=QLabel(txt_test3)
        self.txt_test3=QLabel(txt_starttest3)
        self.btn_test3=QLabel(txt_hinttest3)
        self.line_test2=QLineEdit(txt_hinttest3)
        self.line_test3=QLineEdit(txt_sendresults)
        self.btn_next=QLabel()



        self.h_line=QHBoxLayout()
        self.r_line=QVBoxLayout()
        self.l_line=QHBoxLayout()

        self.r_line.addWidget(self.txt_timer, alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.txt_name, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.line_name, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.text_age, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.line_age, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.txt_test1, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test1, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.line_test1, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.txt_test2, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test2, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.txt_test3, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test3, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.line_test2, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.line_test3, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn_next, alignment=Qt.AlignCenter)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def timer_test(self):
      global time
      time=QTime(0,0,15)
      self.timer=QTimer()
      self.timer.timeout.connect(self.timer1Event)
      self.timer.start(1000)

    def timer_final(self):
      global time
      time=QTime(0,1,1)
      self.timer=QTimer()
      self.timer.timeout.connect(self.timerEvent)
      self.timer.start(1000)

    def timer1Event(self):
      global time 
      time=time.addSecs(-1)
      self.text_timer.setText(time.toString("hh:mm:ss"))
      self.text_timer.setFont(QFont("Times",36,QFont.Bold))
      self.text_timer.setStyleSheet("color:rgb(0,0,0)")  
      if time.toString(("hh:mm:ss"))=="00:00:00":     
         self.timer.stop()   
    
    def timer2Event(self):
      global time 
      time=time.addSecs(-1)
      self.text_timer.setText(time.toString("hh:mm:ss"))
      self.text_timer.setFont(QFont("Times",36,QFont.Bold))
      self.text_timer.setStyleSheet("color:rgb(0,0,0)")  
      if time.toString(("hh:mm:ss"))=="00:00:00":     
         self.timer.stop() 

    def timer3Event (self):
      global time
      time = time.addSecs (-1)
      self.text_timer.setText(time.tostring("рh:mь:ss"))
      self.text_timer.setfont(QFont ("Times", 36, QFont .Bold)) 

      if int(time.toString("hh:mm:ss")[6:8])>=45:
        self.text_timer. setStyleSheet("color:rgb(0,255,0)")
      if int(time.toString("hh:mm:ss")[6:8])<45:
        self.text_timer.setStyleSheet("color:rgb(0,0,0)")
      if int(time.toString("hh:mm:ss")[6:8])<15:
        self.text_timer. setStyleSheet ("color:rgb(0,255,0)")
      
      if time. tostring("hh:mm: ss")=='00:00:00' :
        self.timer .stop()

    def connects(self):
      self.btn_next.clicked.connect(self.next_click)
      self.btn_test1.clicked.connect(self.timer_test)
      self.btn_test1.clicked.connect(self.timer_sits)
      self.btn_test1.clicked.connect(self.timer_final)
    
    def next_click(self):
      self.tw=TestWin()
      self.hide()
