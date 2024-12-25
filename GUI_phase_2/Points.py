from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Points(object):
    def setupUi(self, Dialog ,parent):
        self.parent = parent
        Dialog.resize(600, 250)
        Dialog.setStyleSheet("background-color:#2e2e2d;")

        # Main vertical layout
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)

        # Label and input for X0
        self.enter_quote_x0 = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.enter_quote_x0.setFont(font)
        self.enter_quote_x0.setStyleSheet("color:white")
        self.enter_quote_x0.setText("Enter X0:")
        self.verticalLayout.addWidget(self.enter_quote_x0)

        self.input_X0 = QtWidgets.QLineEdit(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.input_X0.setFont(font)
        self.input_X0.setStyleSheet("background:black; color:white;")
        self.input_X0.setPlaceholderText("X0")
        self.input_X0.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.input_X0)

        # Label and input for X1
        self.enter_quote_X1 = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.enter_quote_X1.setFont(font)
        self.enter_quote_X1.setStyleSheet("color:white")
        self.enter_quote_X1.setText("Enter X1:")
        self.verticalLayout.addWidget(self.enter_quote_X1)

        self.input_X1 = QtWidgets.QLineEdit(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.input_X1.setFont(font)
        self.input_X1.setStyleSheet("background:black; color:white;")
        self.input_X1.setPlaceholderText("X1")
        self.input_X1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.input_X1)

        # Label and input for Absolute Relative Error
        self.enter_quote_error = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.enter_quote_error.setFont(font)
        self.enter_quote_error.setStyleSheet("color:white")
        self.enter_quote_error.setText("Enter Absolute Relative Error:")
        self.verticalLayout.addWidget(self.enter_quote_error)

        self.input_error = QtWidgets.QLineEdit(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.input_error.setFont(font)
        self.input_error.setStyleSheet("background:black; color:white;")
        self.input_error.setPlaceholderText("Absolute Relative Error = 1e-6 default")
        self.input_error.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.input_error)

        self.enter_quote_iteration = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.enter_quote_iteration.setFont(font)
        self.enter_quote_iteration.setStyleSheet("color:white")
        self.enter_quote_iteration.setText("Enter Number of Iterations:")
        self.verticalLayout.addWidget(self.enter_quote_iteration)

        self.input_Iteration = QtWidgets.QLineEdit(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)   
        font.setBold(True)
        self.input_Iteration.setFont(font)
        self.input_Iteration.setStyleSheet("background:black; color:white;")
        self.input_Iteration.setPlaceholderText("Number of Iterations = 100 default") 
        self.input_Iteration.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.input_Iteration)


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

       
        self.submit = QtWidgets.QPushButton(parent=Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(15)
        self.submit.setFont(font)
        self.submit.setStyleSheet("color:#03fc39; background:black;")
        self.submit.setText("Submit")
        self.submit.clicked.connect(self.submit_value)
        self.verticalLayout.addWidget(self.submit)


        self.Back_size_button = QtWidgets.QPushButton(parent=Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(15)
        self.Back_size_button.setFont(font)
        self.Back_size_button.setStyleSheet("color:red; background:black;")
        self.Back_size_button.setText("Back")
        self.Back_size_button.clicked.connect(self.go_to_third_page)
        self.verticalLayout.addWidget(self.Back_size_button)



    def submit_value(self):

     if(self.method=="Secant" or self.method=="Bisecting" or self.method=="Regula_Falsi"):
      try:
         x0 = float(self.input_X0.text())
         x1 = float(self.input_X1.text())
         if(self.input_error.text()==""):
            error=0.0005
         else:
            error = float(self.input_error.text())
         if(self.input_Iteration.text()==""):
            it = 100
         else:
            it = int(self.input_Iteration.text())
      except ValueError as e:
          QtWidgets.QMessageBox.warning(None, "Invalid Input", "Please ensure:\n- x0 ,x1 (float)")
          return
     else:
        try:
         x0 = float(self.input_X0.text())
         x1 = 0 
         if(self.input_error.text()==""):
            error=1e-6
         else:
            error = float(self.input_error.text())
         if(self.input_Iteration.text()==""):
            it = 100
         else:
            it = int(self.input_Iteration.text())
        except ValueError as e:
          QtWidgets.QMessageBox.warning(None, "Invalid Input", "Please ensure:\n- x0 (float)")
          return
     if(self.method=="Regula_Falsi" or self.method=="Bisecting"):
        result1 = eval(self.equation, {"x": x0, "__builtins__": None})
        result2 = eval(self.equation, {"x": x1, "__builtins__": None})
        if(result2*result1>0):
            QtWidgets.QMessageBox.warning(None, "Invalid Input", "No roots or even number of roots")
            return
        elif(result1>0):
           temp = x1 
           x1 = x0 
           x0 = temp
     self.parent._phase_2_go_to_fifth_page(method=self.method, x0=x0, x1=x1, it=it , r_error=error)

     self.parent
    def Method_type(self,method,equation):
        self.equation = equation
        self.method = method
        self.input_X1.setVisible(False)
        self.enter_quote_X1.setVisible(False)
        if(method=="Secant" or method=="Bisecting" or method=="Regula_Falsi"):
             self.input_X1.setVisible(True)
             self.enter_quote_X1.setVisible(True)
           
    def go_to_third_page(self):
        self.parent._phase_2_go_to_third_page_without_value()

    def ploting(self):
        if(self.method=="Fixed_Point"):
           self.parent.ploting(True)
        else:
           self.parent.ploting(False)

