#day3 Erailyn

# File second_win.py (PART 1)
from PyQt5.QtCore import Qt, QTimer, QTime, QLocale # tambahkan
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # checking the types of input values
from PyQt5.QtWidgets import *
from instr import *
from final_win import *

class Experiment(): # tambahkan pembuatan kelas utama
    def __init__(self, age, test1, test2, test3):
        self.age = age
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)

    # tambahkan p1
    def timer_test(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)

    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    # #part2
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    # #part2
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()


# write a code for saving text instructions for the app
#window preparation

from PyQt5 import Qtime 

win_x, win_y = 100, 100 
win_width, win_height = 1000, 600

txt_hello = '--Welcome to The Health Status Detection Program!--'
txt_next = 'Start'
text_instruction = ('This application allows you to use Rufie tezt to make an initial diagnosis of your health.\n'
                    'The Rufier test is a set of physical exercises designed to assess your cardiac performance during physical exertion. \n'
                    'The subject lies in the supine position for 5 minutes and has their pulse rate measured for 15 seconds;\n'
                    'then, within 45 seconds, the subject performs 30 squats.\n'
                    'When the exercise ends, the subject lies down their and their pulse rate is measured again for the first 15 seconds;\n'
                    'and then for the last 15 seconds of the first minute of the recovery period.\n'
                    'Important! If you feel unwell during the test (dizziness,\n'
                    'tinnitus, shortness of breath, etc.), stop the test and consult a physician.')
txt_title = 'Health'
txt_name = 'Enter your full name: '
txt_hintname = 'Full name:'
txt_sendresults = 'Send the results'
txt_finalwin = 'Results'

#day 3 part 2 "Erailyn"
txt_hintage = '0'
txt_test1 = 'Lie on your back and take your pulse for 15 seconds. Click the "Start first test" button to start the timer.\n'\
'Write down the result in the appropriate field.'
txt_test2 = 'Perform 30 squats in 45 seconds. To do this, click the "Start doing squats" button\nto start the squat counter.'
txt_test3 = 'Lie on your back and take your pulse for the first 15 seconds of the minute, then for the last 15 seconds of the '\
'minute. \nPress the "Start final test" button to start the timer.\nThe seconds that should be measured are indicated in green '\
'and the minutes that should not be measured are indicated in black. Write down the results in the appropriate fields.'
txt_hinttest1 = '0'
txt_hinttest2 = '0'
txt_hinttest3 = '0'
txt_starttest1 = 'Start the first test'
txt_starttest2 = 'Start doing squats'
txt_starttest3 = 'Start the final test'
txt_timer = ''
txt_age = 'Full years:'
txt_finalwin = 'Results'
txt_index = 'Roufier Index:'
txt_workheart = Cardiac performance:'

# Day 3 "Marsnandra"
time = Qtime (0,0,15)
tx_timer = time.toString("hh:mm:ss")
txt_res1 = 'low. See yoour doctor right away!'
txt_res2 = 'satisfactory. See your doctor!'
txt_res3 = 'average. It may be worth seeing your doctor to get checked out.' 
txt_res4 = 'above average'
txt_res5 = 'high'



#final_win
from PyQt5.QtCore import Qt,QTimer,QTime,QLocale
from PyQt5.QtGui import QDoubleValidator,QIntValidator,QFont
from PyQt5.QtWidgets import *
from instr import *

class FinalWin(QWidget):
    def __init__(self, exp=None):
        super().__init__()
        self.exp = exp
        self.initUI()
        self.set_appear()
        self.show()

    def initUI(self):
        pass

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    

     #DAY 3
    def results(self):
        if self.exp.age<7: 
            self.index=0
            return "there is no data for this age"
        self.index=(4*(int(self.exp.t1)+int(self.exp.t2)+int (self.exp.t3))-200)/10
        if self.exp.age==7 or self.exp.age==8:
            if self.index>=21:
                return txt_res1
            elif self.index<21 and self.index›=17:
                return txt_res2
            elif self.index<17 and self.index›=12:
                return txt_res3
            elif self.index<12 and self. iddex>=6.5:
                return txt_res4
            else:
                return txt_res5 
        if self.exp.age==g or self.exp.age==10:
            if self.index›=19.5:
                 return txt_res1
            elif self. index<19.5 and self. index›=15.5:
                return txt_res2
            elif self. index<15.5 and self. index›=10.5:
                return txt_res3 
            elif self.index<10.5 and self.index›=5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age == 11 or self.exp.age == 12:
            if self.index >= 18:
                return txt_res1
            elif self.index < 18 and self.index >= 14:
                return txt_res2
            elif self.index < 14 and self.index >= 9:
                return txt_res3
            elif self.index < 9 and self.index >= 3.5:
                return txt_res4
            else:
                return txt_res5

        if self.exp.age == 13 or self.exp.age == 14:
            if self.index >= 16.5:
                return txt_res1
            elif self.index < 16.5 and self.index >= 12.5:
                return txt_res2
            elif self.index < 12.5 and self.index >= 7.5:
                return txt_res3
            elif self.index < 7.5 and self.index >= 2:
                return txt_res4
            else:
                return txt_res5

        if self.exp.age >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index < 15 and self.index >= 11:
                return txt_res2
            elif self.index < 11 and self.index >= 6:
                return txt_res3
            elif self.index < 6 and self.index >= 0.5:
                return txt_res4
            else:
                return txt_res5

