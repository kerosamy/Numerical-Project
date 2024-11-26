

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget

class Ui_Size(object):
    def setupUi(self, Size,parent):
        self.parent = parent 
        Size.setObjectName("Size")
        Size.resize(465, 365)
        Size.setStyleSheet("background-color:#2e2e2d;")
        self.verticalLayout = QtWidgets.QVBoxLayout(Size)
        self.verticalLayout.setObjectName("verticalLayout")
        self.enter_quote = QtWidgets.QLabel(parent=Size)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.enter_quote.setFont(font)
        self.enter_quote.setStyleSheet("color:white")
        self.enter_quote.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.enter_quote.setObjectName("enter_quote")
        self.verticalLayout.addWidget(self.enter_quote)
        self.label = QtWidgets.QLabel(parent=Size)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.input_size = QtWidgets.QLineEdit(parent=Size)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.input_size.setFont(font)
        self.input_size.setStyleSheet("margin: 20px;""background:black")
        self.input_size.setPlaceholderText(f"Number of Equations")
        self.input_size.setText("")
        self.input_size.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.input_size.setObjectName("input_size")
        self.verticalLayout.addWidget(self.input_size)



        self.enter_quote_signigicant = QtWidgets.QLabel(parent=Size)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.enter_quote_signigicant.setFont(font)
        self.enter_quote_signigicant.setStyleSheet("color:white")
        self.enter_quote_signigicant.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.enter_quote_signigicant.setObjectName("enter_quote_signigicant")
        self.verticalLayout.addWidget(self.enter_quote_signigicant)

        self.label2 = QtWidgets.QLabel(parent=Size)
        self.label2.setText("")
        self.label2.setObjectName("label2")
        self.verticalLayout.addWidget(self.label2)

        self.input_significant = QtWidgets.QLineEdit(parent=Size)
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


        self.label_3 = QtWidgets.QLabel(parent=Size)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.size_button = QtWidgets.QPushButton(parent=Size)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(15)
        self.size_button.setFont(font)
        self.size_button.setStyleSheet("color:#03fc39;""background:black")
        self.size_button.setObjectName("size_button")
        shortcut = QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key.Key_Return), Size)
        shortcut.activated.connect(self.size_button.click) 
        self.size_button.clicked.connect(self.submit_value)
        self.verticalLayout.addWidget(self.size_button)
        self.Back_size_button = QtWidgets.QPushButton(parent=Size)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(15)
        self.Back_size_button.setFont(font)
        self.Back_size_button.setStyleSheet("color:red;""background:black;")
        self.Back_size_button.setObjectName("Back_size_button")
        shortcut = QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key.Key_Escape), Size)
        shortcut.activated.connect(self.Back_size_button.click)
        self.Back_size_button.clicked.connect(self.go_to_first_page)
        self.verticalLayout.addWidget(self.Back_size_button)

        self.retranslateUi(Size)
        QtCore.QMetaObject.connectSlotsByName(Size)

    def go_to_first_page(self):
        self.parent.go_to_first_page()
    def submit_value (self):
        value = self.input_size.text()
        if value.isdigit() and int(value) > 0:  # Validate the input
          self.parent.go_to_third_page(value)
        else:
          QtWidgets.QMessageBox.warning(None, "Invalid Input", "Please enter a positive integer.")



    def retranslateUi(self, Size):
        _translate = QtCore.QCoreApplication.translate
        Size.setWindowTitle(_translate("Size", "Form"))
        self.enter_quote.setText(_translate("Size", "Please enter the number of Equations"))
        self.enter_quote_signigicant.setText(_translate("Size", "Please enter the number signigicant"))
        self.size_button.setText(_translate("Size", "Submit"))
        self.Back_size_button.setText(_translate("Size", "Back"))
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Size = QtWidgets.QWidget()
    ui = Ui_Size()
    ui.setupUi(Size)
    Size.show()
    sys.exit(app.exec())
