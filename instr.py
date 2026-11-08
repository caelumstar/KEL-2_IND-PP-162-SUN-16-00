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

# Day 3 "Marsnandra"
time = Qtime (0,0,15)
tx_timer = time.toString("hh:mm:ss")
txt_res1 = 'low. See yoour doctor right away!'
txt_res2 = 'satisfactory. See your doctor!'
txt_res3 = 'average. It may be worth seeing your doctor to get checked out.' 
txt_res4 = 'above average'
txt_res5 = 'high'
