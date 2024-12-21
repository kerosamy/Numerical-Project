from PyQt6 import QtCore, QtGui, QtWidgets
from GUI_phase_1.menu import Ui_Form
from GUI_phase_1.size_input import Ui_Size 
from GUI_phase_1.Matrix import Ui_Dialog
from GUI_phase_1.requirements import Ui_jacobi
from GUI_phase_1.final_ans import Ui_ansg
from control import choose_the_method


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
       
        self.sizeMatrix =  0
        self.stackedWidget = QtWidgets.QStackedWidget(self)
        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().addWidget(self.stackedWidget)

        self.first_page = QtWidgets.QWidget()
        self.first_ui = Ui_Form()
        self.first_ui.setupUi(self.first_page, self)
        
        self.second_page = QtWidgets.QWidget()
        self.second_ui = Ui_Size()
        self.second_ui.setupUi(self.second_page, self)

        self.third_page = QtWidgets.QWidget()
        self.third_ui = Ui_Dialog()
        self.third_ui.setupUi(self.third_page, self)

        self.fourth_page = QtWidgets.QWidget()
        self.fourth_ui = Ui_jacobi()
        self.fourth_ui.setupUi(self.fourth_page, self)

        self.fifth_page = QtWidgets.QWidget()
        self.fifth_ui = Ui_ansg()
        self.fifth_ui.setupUi(self.fifth_page,self)
        

        self.stackedWidget.addWidget(self.first_page)
        self.stackedWidget.addWidget(self.second_page)
        self.stackedWidget.addWidget(self.third_page)
        self.stackedWidget.addWidget(self.fourth_page)
        self.stackedWidget.addWidget(self.fifth_page)
        
        self.stackedWidget.setCurrentWidget(self.first_page)

        
       

  
   

    def go_to_first_page(self):
        self.stackedWidget.setCurrentWidget(self.first_page)

    def go_to_second_page(self):
        self.stackedWidget.setCurrentWidget(self.second_page)

    def go_to_third_page(self, value,value_sig):
        self.sizeMatrix = value
        self.third_ui.updateGrid(int(value))
        self.sig = value_sig   
        self.stackedWidget.setCurrentWidget(self.third_page)

        
    def go_to_third_page_without_value(self):
        self.stackedWidget.setCurrentWidget(self.third_page)

    def go_to_fourth_page(self, value,method,A,B):
        self.method = method
        self.matrix = A 
        self.last_col = B 
        self.fourth_ui.create(int(value))
        self.stackedWidget.setCurrentWidget(self.fourth_page)    
    def go_to_fifth_page_from_fourth(self,intial_guess,it=None,r_error=None): 
            ans , time,max_it,check = choose_the_method(size=int(self.sizeMatrix),A=self.matrix,B=self.last_col,method=self.method,sig=self.sig,intial_guess=intial_guess,it=it,r_error=r_error)  
            self.fifth_ui.updateGrid_ans(num_rows=int(self.sizeMatrix),ans=ans,time=time,sig =self.sig,it=max_it,check=check)
            self.stackedWidget.setCurrentWidget(self.fifth_page)
    def go_to_fifth_page(self,method,A,B):
            ans , time = choose_the_method(size=int(self.sizeMatrix),A=A,B=B,method=method,sig=self.sig)  
            self.fifth_ui.updateGrid_ans(num_rows=int(self.sizeMatrix),ans=ans,time=time,sig =self.sig)
            self.stackedWidget.setCurrentWidget(self.fifth_page)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())
