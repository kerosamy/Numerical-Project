from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QDialog
import numpy as np
import matplotlib.pyplot as plt

class PlotDialog(QDialog):
    def __init__(self, st, parent=None, draw_line=False):
        super().__init__(parent)
        self.setWindowTitle("Plot Function")
        self.equation = st
        self.x_line = draw_line
        self.layout = QtWidgets.QVBoxLayout(self)
        self.x_min_label = QtWidgets.QLabel("Enter x_min:")
        self.x_min_input = QtWidgets.QLineEdit(self)
        self.x_min_input.setText("-10")
        self.layout.addWidget(self.x_min_label)
        self.layout.addWidget(self.x_min_input)
        self.x_max_label = QtWidgets.QLabel("Enter x_max:")
        self.x_max_input = QtWidgets.QLineEdit(self)
        self.x_max_input.setText("10")
        self.layout.addWidget(self.x_max_label)
        self.layout.addWidget(self.x_max_input)
        self.points_label = QtWidgets.QLabel("Enter number of points:")
        self.points_input = QtWidgets.QLineEdit(self)
        self.points_input.setText("500")
        self.layout.addWidget(self.points_label)
        self.layout.addWidget(self.points_input)
        self.submit_button = QtWidgets.QPushButton("Plot", self)
        self.submit_button.clicked.connect(self.plot_function)
        self.layout.addWidget(self.submit_button)

    def plot_function(self,draw_line=True):
     try:
         if(self.x_min_input.text()==""):
             x_min = float(-10)
         else:
             x_min = float(self.x_min_input.text())
        
         if(self.x_max_input.text()==""):
             x_max = float(10)
         else:
             x_max = float(self.x_max_input.text())
        
         if(self.points_input.text()==""):
             num_points = int(500)
         else:
             num_points = int(self.points_input.text())

         func_str = self.equation

         x = np.linspace(x_min, x_max, num_points)

         func = eval(f"lambda x: {func_str}")
         y = func(x)
 
         plt.style.use('dark_background')  

         plt.plot(x, y, color='cyan', linewidth=2) 
         if(self.x_line):
           plt.plot(x, x, color='magenta', linewidth=2, label='y = x')
         plt.scatter(0, 0, color='red', zorder=5, label='Origin (x=0, y=0)', s=100, edgecolor='black')  
         plt.axhline(0, color='white', linewidth=2, linestyle='--', label='y=0') 
         plt.axvline(0, color='white', linewidth=2, linestyle='--', label='x=0')  
         plt.xlabel("x", color='white', fontsize=14, fontweight='bold') 
         plt.ylabel("y", color='white', fontsize=14, fontweight='bold')  
         
         plt.title(f"Plot of y = {func_str}", color='white', fontsize=16, fontweight='bold') 

         plt.grid(True, color='gray', linestyle='--', linewidth=0.5) 
         ax = plt.gca()
         ax.spines['left'].set_linewidth(2)  
         ax.spines['bottom'].set_linewidth(2) 
         ax.spines['right'].set_visible(False) 
         ax.spines['top'].set_visible(False)  
         ax.xaxis.set_ticks_position('bottom')  
         ax.yaxis.set_ticks_position('left')  # Show ticks only on the left


         ax.tick_params(axis='x', colors='white', labelsize=12) 
         ax.tick_params(axis='y', colors='white', labelsize=12) 
         if draw_line:
             plt.plot(x, x, color='magenta', linestyle='--', linewidth=2, label='y = x')
          
         plt.show()

         self.accept()

     except Exception as e:
         QtWidgets.QMessageBox.warning(self, "Invalid Input", f"Error: {str(e)}")


class Ui_Choose_Method(QDialog):
    def setupUi(self, Choose_Method,parent):
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

        self.Plot_button= QtWidgets.QPushButton(parent=Choose_Method)
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
    def open_plot_dialog(self,x_line):
        st = self.equation
        dialog = PlotDialog(st=st, parent=self, draw_line=x_line)
        dialog.exec()
    def SendEquation(self,value):
        self.equation =value
    def go_to_forth_page(self,method):
        self.parent._phase_2_go_to_fourth_page(method)
    def retranslateUi(self):
        self.Choose_quote.setText( "Please Choose The Method")
        self.brackting.setText("Brackting Methods:")
        self.Bisecting.setText("Bisecting")
        self.Regula_Falsi.setText("Regula Falsi")
        self.Fixed_Point.setText("Fixed Point")
        self.Newton_Raphson.setText("Newton Raphson")
        self.Newton_Raphson_Modified.setText("Newton Raphson Modified")
        self.open_Iterative.setText( "Open Iterative Methods:")
        self.Modified_Secant.setText( "Modified Secant")
        self.Secant.setText("Secant")
        self.Plot_button.setText("Plot")
        self.Back_button.setText("Back")
