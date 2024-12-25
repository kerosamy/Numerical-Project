from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog
from GUI_phase_2.ploting import PlotDialog


class Ui_Choose_Method(QDialog):
    def setupUi(self, Choose_Method, parent):
        self.parent = parent
        Choose_Method.setObjectName("Size")
        Choose_Method.resize(465, 365)
        Choose_Method.setStyleSheet("background-color:#2e2e2d;")

        self.buttonContainer = QtWidgets.QWidget(parent=Choose_Method)
        self.buttonContainerLayout = QtWidgets.QVBoxLayout(self.buttonContainer)
        self.buttonContainerLayout.setContentsMargins(20, 20, 20, 20)
        self.buttonContainer2 = QtWidgets.QWidget(parent=Choose_Method)
        self.buttonContainerLayout2 = QtWidgets.QVBoxLayout(self.buttonContainer2)
        self.buttonContainerLayout2.setContentsMargins(20, 20, 20, 20)

        self.verticalLayout = QtWidgets.QVBoxLayout(Choose_Method)
        self.Choose_quote = QtWidgets.QLabel(parent=Choose_Method)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.Choose_quote.setFont(font)
        self.Choose_quote.setStyleSheet("color:white")
        self.Choose_quote.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.Choose_quote)

        self.brackting = QtWidgets.QLabel(parent=Choose_Method)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.brackting.setFont(font)
        self.brackting.setStyleSheet("color:white")
        self.verticalLayout.addWidget(self.brackting)

        self.Bisecting = QtWidgets.QPushButton(parent=Choose_Method)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(15)
        self.Bisecting.setFont(font)
        self.Bisecting.setStyleSheet("color:#03fc39;""background:black")
        self.Bisecting.clicked.connect(lambda: self.go_to_forth_page("Bisecting"))
        self.buttonContainerLayout2.addWidget(self.Bisecting)

        self.Regula_Falsi = QtWidgets.QPushButton(parent=Choose_Method)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(15)
        self.Regula_Falsi.setFont(font)
        self.Regula_Falsi.setStyleSheet("color:#03fc39;""background:black")
        self.buttonContainerLayout2.addWidget(self.Regula_Falsi)
        self.Regula_Falsi.clicked.connect(lambda: self.go_to_forth_page("Regula_Falsi"))
        self.verticalLayout.addWidget(self.buttonContainer2)

        self.open_Iterative = QtWidgets.QLabel(parent=Choose_Method)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.open_Iterative.setFont(font)
        self.open_Iterative.setStyleSheet("color:white")
        self.verticalLayout.addWidget(self.open_Iterative)

        self.Fixed_Point = QtWidgets.QPushButton(parent=Choose_Method)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(15)
        self.Fixed_Point.setFont(font)
        self.Fixed_Point.setStyleSheet("color:#03fc39;""background:black")
        self.Fixed_Point.clicked.connect(lambda: self.go_to_forth_page("Fixed_Point"))
        self.buttonContainerLayout.addWidget(self.Fixed_Point)

        self.Newton_Raphson = QtWidgets.QPushButton(parent=Choose_Method)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(15)
        self.Newton_Raphson.setFont(font)
        self.Newton_Raphson.setStyleSheet("color:#03fc39;""background:black")
        self.Newton_Raphson.clicked.connect(lambda: self.go_to_forth_page("Newton_Raphson"))
        self.buttonContainerLayout.addWidget(self.Newton_Raphson)

        self.Newton_Raphson_Modified = QtWidgets.QPushButton(parent=Choose_Method)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(15)
        self.Newton_Raphson_Modified.setFont(font)
        self.Newton_Raphson_Modified.setStyleSheet("color:#03fc39;""background:black")
        self.Newton_Raphson_Modified.clicked.connect(lambda: self.go_to_forth_page("Newton_Raphson_Modified"))
        self.buttonContainerLayout.addWidget(self.Newton_Raphson_Modified)

        self.Secant = QtWidgets.QPushButton(parent=Choose_Method)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(15)
        self.Secant.setFont(font)
        self.Secant.setStyleSheet("color:#03fc39;""background:black")
        self.Secant.clicked.connect(lambda: self.go_to_forth_page("Secant"))
        self.buttonContainerLayout.addWidget(self.Secant)

        self.Modified_Secant = QtWidgets.QPushButton(parent=Choose_Method)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(15)
        self.Modified_Secant.setFont(font)
        self.Modified_Secant.setStyleSheet("color:#03fc39;""background:black")
        self.Modified_Secant.clicked.connect(lambda: self.go_to_forth_page("Modified_Secant"))
        self.buttonContainerLayout.addWidget(self.Modified_Secant)
        self.verticalLayout.addWidget(self.buttonContainer)

        self.Plot_button = QtWidgets.QPushButton(parent=Choose_Method)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(15)
        self.Plot_button.setFont(font)
        self.Plot_button.setStyleSheet("color:yellow;""background:black;")
        self.Plot_button.clicked.connect(self.open_plot_dialog)
        self.verticalLayout.addWidget(self.Plot_button)

        self.Back_button = QtWidgets.QPushButton(parent=Choose_Method)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(15)
        self.Back_button.setFont(font)
        self.Back_button.setStyleSheet("color:red;""background:black;")
        shortcut = QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key.Key_Escape), Choose_Method)
        shortcut.activated.connect(self.Back_button.click)
        self.Back_button.clicked.connect(self.go_to_second_page)
        self.verticalLayout.addWidget(self.Back_button)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(Choose_Method)

    def go_to_second_page(self):
        self.parent._phase_2_go_to_second_page()

    def open_plot_dialog(self, x_line):
        st = self.equation
        dialog = PlotDialog(st=st, parent=self, draw_line=x_line)
        dialog.exec()

    def SendEquation(self, value):
        self.equation = value

    def go_to_forth_page(self, method):
        self.parent._phase_2_go_to_fourth_page(method)

    def retranslateUi(self):
        self.Choose_quote.setText("Please Choose The Method")
        self.brackting.setText("Brackting Methods:")
        self.Bisecting.setText("Bisecting")
        self.Regula_Falsi.setText("Regula Falsi")
        self.Fixed_Point.setText("Fixed Point")
        self.Newton_Raphson.setText("Newton Raphson")
        self.Newton_Raphson_Modified.setText("Newton Raphson Modified")
        self.open_Iterative.setText("Open Iterative Methods:")
        self.Modified_Secant.setText("Modified Secant")
        self.Secant.setText("Secant")
        self.Plot_button.setText("Plot")
        self.Back_button.setText("Back")
