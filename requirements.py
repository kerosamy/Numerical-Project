from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_jacobi(object):
    def setupUi(self, Dialog, parent):
        self.parent = parent
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet("background-color:#2e2e2d;")
        
        # Main layout
        self.main_layout = QtWidgets.QVBoxLayout(Dialog)
  
        # Title section
        self.label = QtWidgets.QLabel("Initial Guess", parent=Dialog)
        self.label.setStyleSheet("color:white;font-size: 30px;font-weight: bold;")  # Green color
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.label)

        # Scroll Area for inputs
        self.scrollArea = QtWidgets.QScrollArea(parent=Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scroll_layout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.main_layout.addWidget(self.scrollArea)

        # Stopping condition label
        self.label_2 = QtWidgets.QLabel("Stopping Condition", parent=Dialog)
        self.label_2.setStyleSheet("color:white;font-size: 30px;font-weight: bold;")  # Pink color
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.label_2)

        # Buttons and corresponding line edits
        self.button_layout = QtWidgets.QVBoxLayout()
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.pushButton = QtWidgets.QPushButton("Absolute Relative Error", parent=Dialog)
        self.pushButton.setStyleSheet("background-color: black; color:#f803fc;")  # Green button
        self.pushButton.setFixedHeight(50)  # Set equal height
        self.pushButton.setFont(font)
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_4.setVisible(False)
        font1 = QtGui.QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("margin: 20px;""background:black")
        self.lineEdit_4.setPlaceholderText(f"Enter Absolute Relative Error")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_4.setObjectName("input_significant")
        self.button_layout.addWidget(self.pushButton)
        self.button_layout.addWidget(self.lineEdit_4)

        self.pushButton_2 = QtWidgets.QPushButton("Number of Iterations", parent=Dialog)
        self.pushButton_2.setStyleSheet("background-color: black; color:#05ddf5 ; ")  # Pink button
        self.pushButton_2.setFixedHeight(50)  # Set equal height
        self.pushButton_2.setFont(font)
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_5.setVisible(False)
        font1 = QtGui.QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("margin: 20px;""background:black")
        self.lineEdit_5.setPlaceholderText(f"Enter Number of Iterations")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_5.setObjectName("input_significant")
        self.button_layout.addWidget(self.pushButton_2)
        self.button_layout.addWidget(self.lineEdit_5)

        self.main_layout.addLayout(self.button_layout)

        # Add a Submit button
        self.submit_button = QtWidgets.QPushButton("Submit", parent=Dialog)
        self.submit_button.setFixedHeight(50)  # Set equal height
        self.submit_button.setStyleSheet("background-color: black; color:  #03fc39;")  # Orange Submit button
        self.submit_button.setFont(font)
        self.submit_button.clicked.connect(self.submit)
        self.main_layout.addWidget(self.submit_button)

        # Add a Back button below Submit
        self.back_button = QtWidgets.QPushButton("Back", parent=Dialog)
        self.back_button.setFixedHeight(50)  # Set equal height
        self.back_button.setStyleSheet("background-color: black; color: red;")  # Red Back button
        self.back_button.clicked.connect(self.go_back)
        self.back_button.setFont(font)
        self.main_layout.addWidget(self.back_button)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Connect buttons to their respective handlers
        self.pushButton.clicked.connect(self.show_absolute_relative_error)
        self.pushButton_2.clicked.connect(self.show_number_of_iterations)
        self.back_button.clicked.connect(self.go_back)
    def collect(self) : 
     values = [] 
     error_found = False 
     for index, line_edit in enumerate(self.text_boxes):
         try:
             value = float(line_edit.text())  
             values.append(value) 
         except ValueError:
             error_found = True  
             QtWidgets.QMessageBox.warning(None, "Input Error", f"Invalid input in X{index}. Please enter a numeric value.")
             break 
    
     if not error_found:
         return values   

    def is_number(self ,string):
     try:
        float(string)  
        return True
     except ValueError:
        return False
    def submit (self):
        values = self.collect()
        it = self.lineEdit_5.text()
        error = self.lineEdit_4.text()
        if(not(self.is_number(it) or self.is_number(error))):
            QtWidgets.QMessageBox.warning(None, "Input Error", f"please select the stoping condition ")
            return
        self.parent.go_to_fifth_page_from_fourth(values,it,error)

    def create(self, value):
      
        while self.scroll_layout.count():
            item = self.scroll_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        self.text_boxes = []  # Store the text boxes for later access
        for i in range(value):
            line_edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
            line_edit.setObjectName(f"lineEdit_{i}_{0}")
            line_edit.setStyleSheet("background-color:black;""font-size:16px;""color: white;""font-weight: bold;")
            line_edit.setPlaceholderText(f"X{i}")
            line_edit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.scroll_layout.addWidget(line_edit)
            self.text_boxes.append(line_edit)
        box_height = self.text_boxes[0].sizeHint().height() if self.text_boxes else 30
        self.scrollArea.setFixedHeight(box_height + 40)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

    def show_absolute_relative_error(self):
        """Toggle the visibility of the input for Absolute Relative Error."""
        self.lineEdit_5.clear()
        self.lineEdit_4.setVisible(True)
        self.lineEdit_5.setVisible(False)

    def show_number_of_iterations(self):
        """Toggle the visibility of the input for Number of Iterations."""
        self.lineEdit_4.clear()
        self.lineEdit_5.setVisible(True)
        self.lineEdit_4.setVisible(False)

    def go_back(self):
        self.parent.go_to_third_page_without_value()
