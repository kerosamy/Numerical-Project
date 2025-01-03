
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget

class Ui_Form(object):
    def setupUi(self, Form,parent):
        self.parent = parent 
        
        Form.setObjectName("Numerical")
        Form.resize(626, 393)
        
        Form.setStyleSheet("background-color:#2e2e2d;")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Welcome = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        self.Welcome.setFont(font)
        self.Welcome.setStyleSheet("color:white;")
        
        self.Welcome.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Welcome.setObjectName("Welcome")
        self.verticalLayout.addWidget(self.Welcome)
        self.label_2 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-image: url('assets/images.png');""background-position: center;""background-repeat: no-repeat;""margin-bottom:40px;")
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.Start_Phase1 = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Start_Phase1.sizePolicy().hasHeightForWidth())
        self.Start_Phase1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.Start_Phase1.setFont(font)
        self.Start_Phase1.setStyleSheet("color:#03fc39;""background-color:black;")
        self.Start_Phase1.setObjectName("Start Phase 1")
        self.Start_Phase1.clicked.connect(self.go_to_second_page_phase_1)
        self.verticalLayout.addWidget(self.Start_Phase1)


        self.Start_Phase2 = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Start_Phase2.sizePolicy().hasHeightForWidth())
        self.Start_Phase2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.Start_Phase2.setFont(font)
        self.Start_Phase2.setStyleSheet("color:#5ae0da;""background-color:black;")
        self.Start_Phase2.setObjectName("Start Phase 2")
        self.verticalLayout.addWidget(self.Start_Phase2)
        self.Start_Phase2.clicked.connect(self.go_to_second_page_phase_2)
        shortcut = QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key.Key_Return), Form)
        shortcut.activated.connect(self.Start_Phase2.click)



        self.Exit = QtWidgets.QPushButton(parent=Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(15)
        self.Exit.setFont(font)
        self.Exit.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.Exit.setStyleSheet("color:red;""background-color:black;")
        self.Exit.setObjectName("Exit")
        shortcut = QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key.Key_Escape), Form)
        shortcut.activated.connect(self.Exit.click)
        self.Exit.clicked.connect( self.parent.close)
        self.verticalLayout.addWidget(self.Exit)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def go_to_second_page_phase_1(self):
       self.parent._phase_1_go_to_second_page()
    def go_to_second_page_phase_2(self):
       self.parent._phase_2_go_to_second_page()   
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Welcome.setText(_translate("Form", "Welcome To Numerical Project"))
        self.Start_Phase1.setText(_translate("Form", "Start Phase 1"))
        self.Start_Phase2.setText(_translate("Form", "Start Phase 2"))
        self.Exit.setText(_translate("Form", "Exit"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
