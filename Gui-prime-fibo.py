'''
GUI to find the prime numbers and fibonacci series
'''

import sys
from PyQt5 import QtCore, QtGui,QtWidgets


class myApp(object):
    
  
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(599, 506)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("myIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.horizontalLayout.addWidget(self.label_1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.SubmitButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.SubmitButton.setFont(font)
        self.SubmitButton.setObjectName("SubmitButton")
        self.horizontalLayout.addWidget(self.SubmitButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout_3.addWidget(self.textEdit_2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 599, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def fibonacci(self,n):                        #To find the fibonacci series n-no. of terms
       
        last=0
        before_last=0
        number=1
        for i in range(1,n+1):
            if i == 1:
                
                self.textEdit.setText(str(1))
                
            else:
                before_last = last
                last = number
                number = last + before_last
                self.textEdit.append(str(number))
                
            
    def prime(self,n):                          #To find prime numbers from 1 to n
        
        if n==2:
            self.textEdit_2.setText(str(2))
        else:
            for i in range(2,n+1):
                flag=1
                for j in range(2,int(i/2)+1):
                    if i%j == 0:
                        flag=0
                        break
                if flag==1:
                    self.textEdit_2.append(str(i))


    def onclick(self):
        n = int(self.lineEdit.text())             #Reading input from a lineEdit and converting to int
        self.textEdit.setReadOnly(True)           #Using textedits as displays
        self.textEdit_2.setReadOnly(True)
        self.fibonacci(n)
        self.prime(n)
        

   
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Prime No\'s and Fibonacci Series GUI"))
        self.label_1.setText(_translate("MainWindow", "Enter a number"))
        self.SubmitButton.setText(_translate("MainWindow", "Submit"))
        self.label_2.setText(_translate("MainWindow", "Fibonacci series"))
        self.label_3.setText(_translate("MainWindow", "Prime numbers"))
        self.SubmitButton.clicked.connect(self.onclick)       #Proving action when clicked



if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()                      #Creating an object called MainWindow
    ui = myApp()                                              
    ui.setupUi(MainWindow)                     
    MainWindow.show()
    sys.exit(app.exec_())
