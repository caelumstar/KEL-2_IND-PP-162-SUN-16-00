from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from intsr import *
from final_win import *

class TestWin (QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setapper()
        self.show()

    def initUI(self):
        self.btn_next = QPushButton( txt_sendresult, self)
        self.btn_next.cliked.connect(self.next_click)
        layout = QVBoxLayout()
        layout.addWidget(self.btn_next, aligment = Qt.AlignCenter)
        
    def next_click(self):
        self.hide()


        ###part 1

    from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from intsr import *
from final_win import *

class TestWin (QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setapper()
        self.show()

    def next_click(self):
        self.hide()
        self.fw = FinalWin()
    def connect(self):
        self.btn_next.clicked.connect(self.next_click)
    def set_apper(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.btn_next = QPushButton(txt_sendresults, self)
        self.btn_test1 = QPushButton(txt_starttest1, self)
        self.btn_test2 = QPushButton(txt_starttest2, self)
        self.btn_test3 = QPushButton(txt_starttest3, self)
        self.text_name = QLabel(txt_name)
        self.text_age = QLabel(txt_age)
        self.text_test1 = QLabel(txt_test1)
        self.text_test2 = QLabel(txt_test2)
        self.text_test3 = QLabel(txt_test3)
        self.text_timer = QLabel(txt_timer)
        self.line_name = QLineEdit(txt_hintname)
        self.line_age = QLineEdit(txt_hintage)
        self.line_test1 = QLineEdit(txt_hinttest1)
        self.line_test2 = QLineEdit(txt_hinttest2)
        self.line_test3 = QLineEdit(txt_hinttest3)
        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.h_line = QHBoxLayout()
        self.fw = finalwin()
    def set_apper(self):
        self.setWindowTitle(txt_title)
        self.resize (win_width, win_height)
        self.move(win_x, win_y)
