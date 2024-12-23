import sys
from PyQt6 import QtCore, QtGui, QtWidgets
import numpy as np
import matplotlib.pyplot as plt

class PlotDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Plot Function")
        
        # Layout for the dialog
        self.layout = QtWidgets.QVBoxLayout(self)

        # Input for x_min and x_max
        self.x_min_label = QtWidgets.QLabel("Enter x_min:")
        self.x_min_input = QtWidgets.QLineEdit(self)
        self.layout.addWidget(self.x_min_label)
        self.layout.addWidget(self.x_min_input)

        self.x_max_label = QtWidgets.QLabel("Enter x_max:")
        self.x_max_input = QtWidgets.QLineEdit(self)
        self.layout.addWidget(self.x_max_label)
        self.layout.addWidget(self.x_max_input)

        # Input for number of points
        self.points_label = QtWidgets.QLabel("Enter number of points:")
        self.points_input = QtWidgets.QLineEdit(self)
        self.layout.addWidget(self.points_label)
        self.layout.addWidget(self.points_input)

        # Input for the function
        self.function_label = QtWidgets.QLabel("Enter the function (e.g., x**2):")
        self.function_input = QtWidgets.QLineEdit(self)
        self.layout.addWidget(self.function_label)
        self.layout.addWidget(self.function_input)

        # Submit button
        self.submit_button = QtWidgets.QPushButton("Plot", self)
        self.submit_button.clicked.connect(self.plot_function)
        self.layout.addWidget(self.submit_button)

    def plot_function(self):
        try:
            x_min = float(self.x_min_input.text())
            x_max = float(self.x_max_input.text())
            num_points = int(self.points_input.text())
            func_str = self.function_input.text()

            x = np.linspace(x_min, x_max, num_points)

            # Evaluate the function using lambda
            func = eval(f"lambda x: {func_str}")
            y = func(x)

            # Plot the function
            plt.plot(x, y)
            plt.xlabel("x")
            plt.ylabel("y")
            plt.title(f"Plot of y = {func_str}")
            plt.grid(True)
            plt.show()

            # Close the dialog
            self.accept()
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Invalid Input", f"Error: {str(e)}")

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QVBoxLayout(self)

        # Plot button
        self.plot_button = QtWidgets.QPushButton("Plot Function", self)
        self.plot_button.clicked.connect(self.open_plot_dialog)
        self.layout.addWidget(self.plot_button)

    def open_plot_dialog(self):
        # Open the plot dialog
        dialog = PlotDialog(self)
        dialog.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
