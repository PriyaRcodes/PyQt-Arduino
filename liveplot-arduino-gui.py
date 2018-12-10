'''
To plot real time data from arduino using matplotlib and open it on the click of a button inPyQt5
'''

import matplotlib.pyplot as plt
import serial
from drawnow import *
import numpy
import PyQt5
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


serialData = serial.Serial('COM3',9600)
set1=[]
set2=[]
count=0
plt.ion()                                  #setting interactive mode on

def makeFig():
    plt.subplot(2,1,1)                     #subplot no.1
    plt.plot(set1,'ro-',label = 'SET1')
    plt.legend(loc = 'upper left')
    plt.title('PLOT 1')

    plt.subplot(2,1,2)                     #subplot no.2
    plt.plot(set2,'bo-',label = 'SET2')
    plt.legend(loc = 'upper left')
    plt.title('PLOT 2')
    
               
class myApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setAutoFillBackground(True)
        
        self.setWindowTitle('Plotting two sets of Real Time Data')
        self.setGeometry(400,250,600,400)
        self.setWindowIcon(QIcon('myIcon.png'))
        p = self.palette()
        p.setColor(self.backgroundRole(),Qt.yellow)   #setting background color to yellow
        self.setPalette(p)
               
        button = QPushButton('Show Graphs',self)
        button.clicked.connect(self.buttonPressed)

        grid = QGridLayout()
        grid.addWidget(button,1,0)

        self.setLayout(grid)
        
    def buttonPressed(self):
           
        while True:
           while(serialData.inWaiting()):
           
                data = serialData.readline()         #reading from the serial monitor
                val1,val2 = data.split( )            #storing in two separate variables
                set1.append(float(val1))             
                set2.append(float(val2))
                drawnow(makeFig)                     #using drawnow
                plt.pause(0.0001)
                count = count + 1
                if(count>25):                        #after 30 values old data will be start to get deleted 
                    set1.pop(0)                      #deleting oldest data
                    set2.pop(0)            
       
           
       
         
if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = myApp()
    window.show()    
    sys.exit(app.exec_())

