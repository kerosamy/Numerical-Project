from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from GUI_phase_2.steps import StepWindow 

class Ui_FinalAns(object):
    def setupUi(self, Dialog ,parant):
        self.parent =parant
        Dialog.resize(600, 250)
        Dialog.setStyleSheet("background-color:#2e2e2d;")

        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)

 
        self.SelectedMethod = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.SelectedMethod.setFont(font)
        self.SelectedMethod.setStyleSheet("color:white")
        self.SelectedMethod.setText("Choosed Method")
        self.SelectedMethod.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.SelectedMethod)

        self.Method = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.Method.setFont(font)
        self.Method.setStyleSheet("color:#03fc39")
        self.Method.setText("")
        self.Method.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.Method)


        self.RootEqual = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.RootEqual.setFont(font)
        self.RootEqual.setStyleSheet("color:white")
        self.RootEqual.setText("Final Answer")
        self.RootEqual.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.RootEqual)


        self.Root = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.Root.setFont(font)
        self.Root.setStyleSheet("color:white")
        self.Root.setText("")
        self.Root.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.Root)

        self.NumberOfIteration = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.NumberOfIteration.setFont(font)
        self.NumberOfIteration.setStyleSheet("color:white")
        self.NumberOfIteration.setText("Number of Iterations : ")
        self.NumberOfIteration.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.NumberOfIteration)

        self.RError = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.RError.setFont(font)
        self.RError.setStyleSheet("color:white")
        self.RError.setText("R_Error :")
        self.RError.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.RError)


        self.sig_f = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.sig_f.setFont(font)
        self.sig_f.setStyleSheet("color:white")
        self.sig_f.setText("Number of correct significant figures : ")
        self.sig_f.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.sig_f)


        self.time = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.time.setFont(font)
        self.time.setStyleSheet("color:white")
        self.time.setText("Time taken : ")
        self.time.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.time)


        self.statuse = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.statuse.setFont(font)
        self.statuse.setStyleSheet("color:white")
        self.statuse.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.statuse)


        self.space = QtWidgets.QLabel(parent=Dialog)
        self.verticalLayout.addWidget(self.space)

        self.plot = QtWidgets.QPushButton(parent=Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(15)
        self.plot.setFont(font)
        self.plot.setStyleSheet("color:yellow; background:black;")
        self.plot.setText("Plot")
        self.plot.clicked.connect(self.ploting)
        self.verticalLayout.addWidget(self.plot)
        

        self.show_steps_button = QtWidgets.QPushButton(parent=Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(15)
        self.show_steps_button.setFont(font)
        self.show_steps_button.setStyleSheet("color:blue; background:black;")
        self.show_steps_button.setText("Steps")
        self.show_steps_button.clicked.connect(self.show_steps)
        self.verticalLayout.addWidget(self.show_steps_button)


   

        
        self.Back = QtWidgets.QPushButton(parent=Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(15)
        self.Back.setFont(font)
        self.Back.setStyleSheet("color:red; background:black;")
        self.Back.setText("Back")
        self.Back.clicked.connect(self.go_to_back)
        self.verticalLayout.addWidget(self.Back)


        self.Back_to_menu = QtWidgets.QPushButton(parent=Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(15)
        self.Back_to_menu.setFont(font)
        self.Back_to_menu.setStyleSheet("color:red; background:black;")
        self.Back_to_menu.setText("Back to menu")
        self.Back_to_menu.clicked.connect(self.go_to_menu)
        self.verticalLayout.addWidget(self.Back_to_menu)

    def set_final_ans(self,method,root,it,error,sig,time,string,steps):
        self.steps = steps
        self.method=method
        self.Method.setText(method)
        self.Root.setText(str(root))
        self.NumberOfIteration.setText(self.NumberOfIteration.text()+ str(it))
        self.RError.setText(self.RError.text()+str(error))
        self.sig_f.setText(self.sig_f.text()+str(sig))
        self.time.setText(self.time.text()+ str(time))
        self.statuse.setText(string)



    def show_steps(self):
        self.step_window = StepWindow(self.steps)
        self.step_window.exec()
 


        

    def go_to_menu(self):
        self.parent.go_to_Menu()
    def go_to_back(self):
        self.parent._phase_2_go_to_fourth_page(self.method)    

    def ploting(self):
        if(self.method=="Fixed_Point"):
           self.parent.ploting(True)
        else:
           self.parent.ploting(False)

