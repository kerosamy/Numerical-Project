import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt

class Ui_ansg(object):
    def setupUi(self, Dialog, parent=None):
        self.parent = parent
        Dialog.setObjectName("Dialog")
        Dialog.resize(651, 514)
        Dialog.setStyleSheet("background-color:#2e2e2d;")

        self.mainLayout = QtWidgets.QHBoxLayout(Dialog)

        self.leftLayout = QtWidgets.QVBoxLayout()
        
        self.sizeMatrix = 0 
        self.sig_f = 0 
        self.topLabel = QtWidgets.QLabel(Dialog)
        self.topLabel.setObjectName("topLabel")
        self.topLabel.setText("")
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.topLabel.setFont(font)
        self.topLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.topLabel.setStyleSheet("color: white;")
        self.leftLayout.addWidget(self.topLabel)

        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        # Using QVBoxLayout to arrange the widgets vertically (in a column)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.leftLayout.addWidget(self.scrollArea)

        self.backButton = QtWidgets.QPushButton(Dialog)
        self.backButton.setObjectName("backButton")
        self.backButton.setText("Back")
        shortcut = QtGui.QShortcut(QtGui.QKeySequence(Qt.Key.Key_Escape), Dialog)
        shortcut.activated.connect(self.backButton.click)
        font.setPointSize(15)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet("color: red;""background:black")
        self.backButton.clicked.connect(self.go_back)
        self.leftLayout.addWidget(self.backButton)


        self.calcAgain = QtWidgets.QPushButton(Dialog)
        self.calcAgain.setObjectName("new system")
        self.calcAgain.setText("new system")
        font.setPointSize(15)
        self.calcAgain.setFont(font)
        self.calcAgain.setStyleSheet("color: red;""background:black")
        self.calcAgain.clicked.connect(self.go_lobby)
        self.leftLayout.addWidget(self.calcAgain)


        self.mainLayout.addLayout(self.leftLayout)
    def go_lobby(self):
        self.parent.go_to_second_page()
    def go_back(self):
        self.parent.go_to_third_page(self.sizeMatrix,self.sig_f)
    def updateGrid_ans(self, num_rows,ans,time,sig):
        self.sizeMatrix=num_rows
        self.sig_f=sig
        self.topLabel.setText(f"TIME taken = {time:.15f}")
        while self.verticalLayout.count():
            item = self.verticalLayout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        # Now populate the layout with widgets arranged vertically (one widget per row)
        for row in range(num_rows):
            label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            label.setObjectName(f"lineEdit_{row}")
            label.setStyleSheet("background-color:black;""font-size:30px;""color: white;""font-weight: bold;")
            label.setText(f"x{row} = {ans[row]}")
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.verticalLayout.addWidget(label)  # Add to the vertical layout

def main():
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_ansg()
    ui.setupUi(Dialog)

    # Example of updating the grid with 5 rows (1 column)
    ui.updateGrid_ans(20)

    Dialog.setWindowTitle("Matrix Input")
    Dialog.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
