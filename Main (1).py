from PyQt6 import QtCore, QtGui, QtWidgets
from menu import Ui_Form
from size_input import Ui_Size 
from Matrix import Ui_Dialog
from requirements import Ui_jacobi
import pygame

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        try:
            pygame.mixer.init()
        except pygame.error as e:
            print(f"Error initializing pygame mixer: {e}")

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

        self.stackedWidget.addWidget(self.first_page)
        self.stackedWidget.addWidget(self.second_page)
        self.stackedWidget.addWidget(self.third_page)
        self.stackedWidget.addWidget(self.fourth_page)
        
        self.stackedWidget.setCurrentWidget(self.first_page)

        # Start playing the music
        self.play_music()

    def play_music(self):
        try:   
            pygame.mixer.music.load("mu.mp3") 
            pygame.mixer.music.play(-1, 0.0)    
        except pygame.error as e:
            print(f"Error playing music: {e}")

    def closeEvent(self, event):
        if pygame.mixer.get_init():  
            pygame.mixer.music.stop()
        event.accept()

    def go_to_first_page(self):
        self.stackedWidget.setCurrentWidget(self.first_page)

    def go_to_second_page(self):
        self.stackedWidget.setCurrentWidget(self.second_page)

    def go_to_third_page(self, value):
        self.third_ui.updateGrid(int(value))
        self.stackedWidget.setCurrentWidget(self.third_page)
        
    def go_to_third_page_without_value(self):
        self.stackedWidget.setCurrentWidget(self.third_page)

    def go_to_fourth_page(self, value):
        self.fourth_ui.create(int(value))
        self.stackedWidget.setCurrentWidget(self.fourth_page)    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())
