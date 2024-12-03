from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QLineEdit
from solutionType import checkSolutionType
from CheloskyDecomposition import is_symmetric
import numpy as np


class Ui_Dialog(object):
  
    def setupUi(self, Dialog, parent):
        self.parent = parent
        Dialog.setObjectName("Dialog")
        Dialog.resize(651, 514)
        Dialog.setStyleSheet("background-color:#2e2e2d;")

        self.mainLayout = QtWidgets.QHBoxLayout(Dialog)


        self.leftLayout = QtWidgets.QVBoxLayout()
        
        self.sig_f = 0 
        self.have_sig = False 
        self.topLabel = QtWidgets.QLabel(Dialog)
        self.topLabel.setObjectName("topLabel")
        self.topLabel.setText("")
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.topLabel.setFont(font)
        self.topLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.topLabel.setStyleSheet("color: white;")

     
        self.leftLayout.addWidget(self.topLabel)

        self.temp = QtWidgets.QLabel(Dialog)
        self.temp.setText("kero")
        self.temp.setVisible(False)
        self.leftLayout.addWidget(self.temp)



        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        # Contents inside the scroll area
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        # Add scroll area to the left layout
        self.leftLayout.addWidget(self.scrollArea)

        # Solve button
        self.solve_button = QtWidgets.QPushButton(Dialog)
        self.solve_button.setObjectName("solveButton")
        self.solve_button.setText("Solve")
        font.setPointSize(15)
        self.solve_button.setFont(font)
        self.solve_button.clicked.connect(self.solve)
        self.solve_button.setStyleSheet("color: #03fc39;""background:black")
        self.leftLayout.addWidget(self.solve_button)

        # method button to show/hide the sidebar
        self.chooseMethod_button = QtWidgets.QPushButton(Dialog)
        self.chooseMethod_button.setObjectName("methodButton")
        self.chooseMethod_button.setText("Choose Solving Method")
        font.setPointSize(15)
        self.chooseMethod_button.setFont(font)
        self.chooseMethod_button.setStyleSheet("color: #f803fc;""background:black")
        self.chooseMethod_button.clicked.connect(self.toggle_sidebar)
        self.leftLayout.addWidget(self.chooseMethod_button)


 
        self.clear_button = QtWidgets.QPushButton(Dialog)
        self.clear_button.setObjectName("clearbutton")
        self.clear_button.setText("Clear")
        font.setPointSize(15)
        self.clear_button.setFont(font)
        self.clear_button.clicked.connect(self.clear)
        self.clear_button.setStyleSheet("color:yellow;""background:black")
        self.leftLayout.addWidget(self.clear_button)

        # Back button
        self.backButton = QtWidgets.QPushButton(Dialog)
        self.backButton.setObjectName("backButton")
        self.backButton.setText("Back")
        shortcut = QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key.Key_Escape), Dialog)
        shortcut.activated.connect(self.backButton.click)
        font.setPointSize(15)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet("color: red;""background:black")
        self.backButton.clicked.connect(self.go_back)
        self.leftLayout.addWidget(self.backButton)

        # Add the left layout to the main layout
        self.mainLayout.addLayout(self.leftLayout)

        # Right sidebar (initially hidden)
        self.sidebar = QtWidgets.QWidget(Dialog)
        self.sidebar.setObjectName("sidebar")
        self.sidebar.setFixedWidth(300)  
        self.sidebar.setStyleSheet("background-color: #4B2D52;")
        
        # Sidebar layout
        sidebar_layout = QtWidgets.QVBoxLayout(self.sidebar)

        # Title label for the sidebar
        title_label = QtWidgets.QLabel("Choose Method", self.sidebar)
        title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        title_label.setFont(font)
        sidebar_layout.addWidget(title_label)




        self.choosed = QtWidgets.QLabel("", self.sidebar)
        self.choosed.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.choosed.setFont(font)
        sidebar_layout.addWidget(self.choosed)

        # List of methods with their associated widgets
        methods = [
            "Gauss Elimination",
            "Gauss-Jordan",
            "LU Decomposition",
            "Gauss-Seidel",
            "Jacobi"
        ]

        # Add buttons for each method
        self.method_buttons = {}
        for method in methods:
            button = QtWidgets.QPushButton(method, self.sidebar)
            button.setStyleSheet("background-color:#424242;")
            font = QtGui.QFont()
            font.setPointSize(15)
            button.setFont(font)
            button.clicked.connect(lambda checked, method=method: self.show_method_options(method))  
            sidebar_layout.addWidget(button)
            self.method_buttons[method] = button

        # LU Decomposition label
        self.lu_label = QtWidgets.QLabel("LU Method", self.sidebar)
        self.lu_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.lu_label.setFont(font)
        self.lu_label.setVisible(False)  # Initially hidden
        sidebar_layout.addWidget(self.lu_label)

        self.lu_choosed = QtWidgets.QLabel("Doolittle Form", self.sidebar)
        self.lu_choosed.setStyleSheet("color:#03fc39;")
        self.lu_choosed.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lu_choosed.setVisible(False) 
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.lu_choosed.setFont(font)
        sidebar_layout.addWidget(self.lu_choosed)

        # LU Decomposition drop-down for the L & U format
        self.lu_combobox = QtWidgets.QComboBox(self.sidebar)
        self.lu_combobox.addItems(["Doolittle Form", "Crout Form", "Cholesky Form"])
        self.lu_combobox.setVisible(False)
        self.lu_combobox.setStyleSheet("""
            QComboBox {
                background-color: black;  
                color: white; 
                font-size: 16px; 
                border: 2px solid #444444;  
                border-radius: 5px; 
                padding: 5px;
            }
            QComboBox::drop-down {
                background-color: #2e2e2d;  
                color: white; 
                font-size: 14px; 
            }
            QComboBox QAbstractItemView {
                background-color: #4B2D52;  
                color: white; 
                font-size: 14px;  
            }
        """)

        sidebar_layout.addWidget(self.lu_combobox)
        self.lu_combobox.currentIndexChanged.connect(self.on_combobox_changed)

        self.mainLayout.addWidget(self.sidebar)
        self.sidebar.setVisible(False)  # Initially hidden

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def sig_fig(value,self):
        if(value=='none'):
            self.have_sig = False 
        else:
            self.sig_f = value    
    def isValid(self):
        for row in range(self.gridLayout.rowCount()):
            for col in range(self.gridLayout.columnCount()):
               item = self.gridLayout.itemAtPosition(row, col)
               if item is not None:  
                   widget = item.widget()
                   if isinstance(widget, QLineEdit): 
                      if(not self.is_number(widget.text())):
                          return True
        return False       
    def is_number(self ,string):
     try:
        float(string)  
        return True
     except ValueError:
        return False
    def clear (self):
        for row in range(self.gridLayout.rowCount()):
            for col in range(self.gridLayout.columnCount()):
               item = self.gridLayout.itemAtPosition(row, col)
               if item is not None:  # Check if there's an item at this position
                 widget = item.widget()
                 if isinstance(widget, QLineEdit):  # Check if the widget is a QLineEdit
                    widget.clear()  
           
    def on_combobox_changed(self):
        # Get the selected text from the combo box
        self.lu_choosed.setText(self.lu_combobox.currentText())      
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dynamic Grid Layout"))
    
    def updateGrid(self, num_rows):
        
        self.topLabel.setText("Number Of Equations is = "+str(num_rows))
        self.temp.setText(str(num_rows))
        while self.gridLayout.count():
            item = self.gridLayout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        # Calculate number of columns
        num_columns = num_rows + 1

        # Populate the grid layout with QLineEdit widgets
        for row in range(num_rows):
            for col in range(num_columns):
                line_edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
                line_edit.setObjectName(f"lineEdit_{row}_{col}")
                line_edit.setStyleSheet("background-color:black;""font-size:16px;""color: white;""font-weight: bold;")
                line_edit.setPlaceholderText(f"A{row},{col}")
                if(col==num_columns-1):
                    line_edit.setStyleSheet("background-color:black; font-size:16px; color:white; font-weight:bold; margin-left:40px;")
                    line_edit.setPlaceholderText(f"B{row}")
                line_edit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.gridLayout.addWidget(line_edit, row, col)
                

    def go_back(self):
        self.parent.go_to_second_page()

    def toggle_sidebar(self):
        """Toggle the visibility of the sidebar when the Solve button is clicked."""
        current_visibility = self.sidebar.isVisible()
        self.sidebar.setVisible(not current_visibility)
        if self.sidebar.isVisible():
            self.chooseMethod_button.setText("Return to Equations")
        else:
            self.chooseMethod_button.setText("Choose your Solving Method")
    def save_the_matrix(self):
     matrix = []  # To store the matrix excluding the last column
     last_column = []  # To store the last column values
     for row in range(int(self.temp.text())):
         rows = []  # To store the current row excluding the last column

         for col in range(int(self.temp.text())+1):
             item = self.gridLayout.itemAtPosition(row, col)
             if item is not None:
                 widget = item.widget()
                 if isinstance(widget, QLineEdit):  # Check if it's a QLineEdit widget
                     text = widget.text().strip()  # Get and clean the text
                     if self.is_number(text):  # Validate if the input is a number
                         value = float(text)
                         if col < int(self.temp.text()):
                             rows.append(value)  # Add to rows excluding the last column
                         elif col == int(self.temp.text()):
                             last_column.append(value)  # Add to the last column array
 
         matrix.append(rows)  # Add the row (without last column) to matrix
 
     return matrix, last_column


    def solve (self):
       
        if(self.choosed.text()=="" or self.isValid()):
             QtWidgets.QMessageBox.warning(None, "Invalid Input", "Please try again.")
            
        else:
            matrix,last_cloumn = self.save_the_matrix()
            typeofsol = checkSolutionType(matrix,last_cloumn)
            if(typeofsol =="No solution"):
                QtWidgets.QMessageBox.warning(None, "Invalid Input", "No solution")
                return
            if(typeofsol =="Infinite solutions"):
                QtWidgets.QMessageBox.warning(None, "Invalid Input", "Infinite solutions")
                return
            method = self.choosed.text()
            num_rows =  self.temp.text()
            if(method=="Gauss-Seidel" or method=="Jacobi"):
                self.parent.go_to_fourth_page(value=int(num_rows),A=matrix,B=last_cloumn,method=method)
            else:
             method_continue = ""
             if(method=="LU Decomposition"):
                  method_continue = self.lu_choosed.text()
                  method=method+method_continue 
             if (((not np.all(np.linalg.eigvals(matrix) > 0)) or (not is_symmetric(matrix)))and (method=="LU DecompositionCholesky Form") ):
                   QtWidgets.QMessageBox.warning(None, "Invalid Input", "not postive definite or no symmetric")
                   return  
             self.parent.go_to_fifth_page(method=method,A=matrix,B=last_cloumn,)    



    def show_method_options(self, method):
        """Show additional options based on the selected method."""
        self.lu_combobox.setVisible(False)
        self.lu_label.setVisible(False)  # Hide the LU Method label
        self.choosed.setText(method)
        self.choosed.setStyleSheet("color:#03fc39;")
        self.lu_choosed.setVisible(False) 
        if method == "LU Decomposition":
            self.lu_combobox.setVisible(True)
            self.lu_choosed.setVisible(True) 
            self.lu_label.setVisible(True)  # Show the LU Method label

        
