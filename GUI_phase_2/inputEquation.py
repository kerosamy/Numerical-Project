from PyQt6 import QtCore, QtGui, QtWidgets
import re
import numpy as np

class Ui_InputEq(object):
    def setupUi(self, Dialog,parent):
        self.parent = parent 
        Dialog.setObjectName("Size")
        Dialog.resize(465, 365)
        Dialog.setStyleSheet("background-color:#2e2e2d;")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.enter_quote = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.enter_quote.setFont(font)
        self.enter_quote.setStyleSheet("color:white")
        self.enter_quote.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.enter_quote.setObjectName("enter_quote")
        self.verticalLayout.addWidget(self.enter_quote)
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.input_size = QtWidgets.QLineEdit(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.input_size.setFont(font)
        self.input_size.setStyleSheet("margin: 20px;""background:black")
        self.input_size.setPlaceholderText(f"Valid Equation")
        self.input_size.setText("")
        self.input_size.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.input_size.setObjectName("input_size")
        self.verticalLayout.addWidget(self.input_size)



        self.enter_quote_signigicant = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.enter_quote_signigicant.setFont(font)
        self.enter_quote_signigicant.setStyleSheet("color:white")
        self.enter_quote_signigicant.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.enter_quote_signigicant.setObjectName("enter_quote_signigicant")
        self.verticalLayout.addWidget(self.enter_quote_signigicant)

        self.label2 = QtWidgets.QLabel(parent=Dialog)
        self.label2.setText("")
        self.label2.setObjectName("label2")
        self.verticalLayout.addWidget(self.label2)

        self.input_significant = QtWidgets.QLineEdit(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.input_significant.setFont(font)
        self.input_significant.setStyleSheet("margin: 20px;""background:black")
        self.input_significant.setPlaceholderText(f"Number of significant")
        self.input_significant.setText("")
        self.input_significant.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.input_significant.setObjectName("input_significant")
        self.verticalLayout.addWidget(self.input_significant)


        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.size_button = QtWidgets.QPushButton(parent=Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(15)
        self.size_button.setFont(font)
        self.size_button.setStyleSheet("color:#03fc39;""background:black")
        self.size_button.setObjectName("size_button")
        shortcut = QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key.Key_Return), Dialog)
        shortcut.activated.connect(self.size_button.click) 
        self.size_button.clicked.connect(self.submit_value)
        self.verticalLayout.addWidget(self.size_button)
        self.Back_size_button = QtWidgets.QPushButton(parent=Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(15)
        self.Back_size_button.setFont(font)
        self.Back_size_button.setStyleSheet("color:red;""background:black;")
        self.Back_size_button.setObjectName("Back_size_button")
        shortcut = QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key.Key_Escape), Dialog)
        shortcut.activated.connect(self.Back_size_button.click)
        self.Back_size_button.clicked.connect(self.go_to_first_page)
        self.verticalLayout.addWidget(self.Back_size_button)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def go_to_first_page(self):
        self.parent.go_to_Menu()

 

    def retranslateUi(self):
        self.enter_quote.setText("Please enter a Valid Equation")
        self.enter_quote_signigicant.setText( "Please enter the number signigicant")
        self.size_button.setText( "Submit")
        self.Back_size_button.setText("Back")

    def is_valid_x_equation(self, equation: str) -> bool:
        equation = equation.replace(" ", "")  
        equation = equation.replace('e', str(np.e))
        equation = equation.replace('^', "**")
        pattern = r"^[0-9\.\+\-\*/\(\)x]*" \
          r"((e\^|e\*\*)[x0-9\.\+\-\*/\(\)]+|" \
          r"exp\([^\)]*\)|" \
          r"(sin|cos|tan|ln|log)\([^\)]*\)[\+\-\*/0-9x]*|" \
          r"[0-9\.\+\-\*/\(\)x]+)$"
    
        try:
         return bool(re.match(pattern, equation))
        except re.error as e:
          print(f"Regex error: {e}")
          return False
    def d():
        print("x**5 - 11*x**4 + 46*x**3 - 90*x**2 + 81*x-27")
    def submit_value (self):
        value = self.input_size.text()
        value_sig = self.input_significant.text()
        if(value_sig==""):
            value_sig="none"
           
        if(self.is_valid_x_equation(value)):
           value = value.replace('e',str(np.e))
           value = value.replace(" ","")
           value = value.replace('^', "**")
           self.parent._phase_2_go_to_third_page(value,value_sig)
        else:
          QtWidgets.QMessageBox.warning(None, "Invalid Input", "Please enter a Valid equation.")


