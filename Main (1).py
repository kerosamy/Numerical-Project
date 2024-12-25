from PyQt6 import QtCore, QtGui, QtWidgets
from menu import Ui_Form
from GUI_phase_1.size_input import Ui_Size 
from GUI_phase_1.Matrix import Ui_Dialog
from GUI_phase_1.requirements import Ui_jacobi
from GUI_phase_1.final_ans import Ui_ansg
from GUI_phase_2.inputEquation import Ui_InputEq
from GUI_phase_2.chooseMethode import Ui_Choose_Method
from GUI_phase_2.Points import Ui_Points
from GUI_phase_2.final_ans import Ui_FinalAns
from control import choose_the_method
from control import choose_the_method_phase_2


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
       
        self._phase_1_sizeMatrix =  0
        self.stackedWidget = QtWidgets.QStackedWidget(self)
        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().addWidget(self.stackedWidget)

        self.Menu_page = QtWidgets.QWidget()
        self.Menu_ui = Ui_Form()
        self.Menu_ui.setupUi(self.Menu_page, self)


        
        self._phase_1_second_page = QtWidgets.QWidget()
        self._phase_1_second_ui = Ui_Size()
        self._phase_1_second_ui.setupUi(self._phase_1_second_page, self)

        self._phase_2_second_page = QtWidgets.QWidget()
        self._phase_2_second_ui = Ui_InputEq()
        self._phase_2_second_ui.setupUi(self._phase_2_second_page, self)




        self._phase_1_third_page = QtWidgets.QWidget()
        self._phase_1_third_ui = Ui_Dialog()
        self._phase_1_third_ui.setupUi(self._phase_1_third_page, self)

        self._phase_2_third_page = QtWidgets.QWidget()
        self._phase_2_third_ui = Ui_Choose_Method()
        self._phase_2_third_ui.setupUi(self._phase_2_third_page, self)




        self._phase_1_fourth_page = QtWidgets.QWidget()
        self._phase_1_fourth_ui = Ui_jacobi()
        self._phase_1_fourth_ui.setupUi(self._phase_1_fourth_page, self)

        self._phase_2_fourth_page = QtWidgets.QWidget()
        self._phase_2_fourth_ui = Ui_Points()
        self._phase_2_fourth_ui.setupUi(self._phase_2_fourth_page, self)





        self._phase_1_fifth_page = QtWidgets.QWidget()
        self._phase_1_fifth_ui = Ui_ansg()
        self._phase_1_fifth_ui.setupUi(self._phase_1_fifth_page,self)

        self._phase_2_fifth_page = QtWidgets.QWidget()
        self._phase_2_fifth_ui = Ui_FinalAns()
        self._phase_2_fifth_ui.setupUi(self._phase_2_fifth_page,self)
        

        self.stackedWidget.addWidget(self.Menu_page)
        
        #second page 
        self.stackedWidget.addWidget(self._phase_1_second_page)
        self.stackedWidget.addWidget(self._phase_2_second_page)

        #third page
        self.stackedWidget.addWidget(self._phase_1_third_page)
        self.stackedWidget.addWidget(self._phase_2_third_page)


        #forth page
        self.stackedWidget.addWidget(self._phase_1_fourth_page)
        self.stackedWidget.addWidget(self._phase_2_fourth_page)


        self.stackedWidget.addWidget(self._phase_1_fifth_page)
        self.stackedWidget.addWidget(self._phase_2_fifth_page)
        

        self.stackedWidget.setCurrentWidget(self.Menu_page)

    def go_to_Menu(self):
        self.stackedWidget.setCurrentWidget(self.Menu_page)

    def ploting(self,x_line):
        self._phase_2_third_ui.open_plot_dialog(x_line=x_line)



    def _phase_1_go_to_second_page(self):
        self.stackedWidget.setCurrentWidget(self._phase_1_second_page)
    def _phase_2_go_to_second_page(self):
        self.stackedWidget.setCurrentWidget(self._phase_2_second_page)



    def _phase_1_go_to_third_page(self, value, value_sig):
        self._phase_1_sizeMatrix = value
        self._phase_1_third_ui.updateGrid(int(value))
        self._phase_1_sig = value_sig   
        self.stackedWidget.setCurrentWidget(self._phase_1_third_page)
    def _phase_1_go_to_third_page_without_value(self):
        self.stackedWidget.setCurrentWidget(self._phase_1_third_page)      

    def _phase_2_go_to_third_page(self, value, value_sig):
        self._phase_2_equation = value
        self._phase_2_sig = value_sig  
        self._phase_2_third_ui.SendEquation(value) 
        self.stackedWidget.setCurrentWidget(self._phase_2_third_page)

    def _phase_2_go_to_third_page_without_value(self):
        self.stackedWidget.setCurrentWidget(self._phase_2_third_page)     
    

    def _phase_1_go_to_fourth_page(self, value, method, A, B):
        self._phase_1_method = method
        self._phase_1_matrix = A 
        self._phase_1_last_col = B 
        self._phase_1_fourth_ui.create(int(value))
        self.stackedWidget.setCurrentWidget(self._phase_1_fourth_page)   

    def _phase_2_go_to_fourth_page(self, method):
        self._phase_2_method = method
        self._phase_2_fourth_ui.Method_type(method,self._phase_2_equation)
        self.stackedWidget.setCurrentWidget(self._phase_2_fourth_page)   
    


    def _phase_1_go_to_fifth_page_from_fourth(self, initial_guess, it=None, r_error=None): 
        ans, time, max_it, check = choose_the_method(size=int(self._phase_1_sizeMatrix), A=self._phase_1_matrix, B=self._phase_1_last_col, method=self._phase_1_method, sig=self._phase_1_sig, initial_guess=initial_guess, it=it, r_error=r_error)  
        self._phase_1_fifth_ui.updateGrid_ans(num_rows=int(self._phase_1_sizeMatrix), ans=ans, time=time, sig=self._phase_1_sig, it=max_it, check=check)
        self.stackedWidget.setCurrentWidget(self._phase_1_fifth_page)
    
    def _phase_1_go_to_fifth_page(self, method, A, B):
        ans, time = choose_the_method(size=int(self._phase_1_sizeMatrix), A=A, B=B, method=method, sig=self._phase_1_sig)  
        self._phase_1_fifth_ui.updateGrid_ans(num_rows=int(self._phase_1_sizeMatrix), ans=ans, time=time, sig=self._phase_1_sig)
        self.stackedWidget.setCurrentWidget(self._phase_1_fifth_page)

    def _phase_2_go_to_fifth_page(self, method, x0, x1, it , r_error):
        ans,itr,error,fig,time,string,steps = choose_the_method_phase_2(equation=self._phase_2_equation,method=method,X0=x0,X1=x1,sig=self._phase_2_sig,it=it,r_error=r_error)
        self._phase_2_fifth_ui.set_final_ans(method=method,root=ans,it=itr,error=error,sig=fig,time=time,string=string,steps=steps)
        self.stackedWidget.setCurrentWidget(self._phase_2_fifth_page)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())
