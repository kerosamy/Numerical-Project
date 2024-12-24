from PyQt6.QtWidgets import QDialog, QMessageBox, QVBoxLayout, QLabel, QLineEdit, QPushButton
import numpy as np
import matplotlib.pyplot as plt


class PlotDialog(QDialog):
    def __init__(self, st, parent=None, draw_line=False):
        super().__init__(parent)
        self.setWindowTitle("Plot Function")
        self.equation = st
        self.x_line = draw_line
        self.layout = QVBoxLayout(self)
        self.x_min_label = QLabel("Enter x_min:")
        self.x_min_input = QLineEdit(self)
        self.x_min_input.setText("-10")
        self.layout.addWidget(self.x_min_label)
        self.layout.addWidget(self.x_min_input)
        self.x_max_label = QLabel("Enter x_max:")
        self.x_max_input = QLineEdit(self)
        self.x_max_input.setText("10")
        self.layout.addWidget(self.x_max_label)
        self.layout.addWidget(self.x_max_input)
        self.points_label = QLabel("Enter number of points:")
        self.points_input = QLineEdit(self)
        self.points_input.setText("500")
        self.layout.addWidget(self.points_label)
        self.layout.addWidget(self.points_input)
        self.submit_button = QPushButton("Plot", self)
        self.submit_button.clicked.connect(self.plot_function)
        self.layout.addWidget(self.submit_button)

    def plot_function(self, draw_line=True):
        try:
            x_min = float(self.x_min_input.text()) if self.x_min_input.text() else -10
            x_max = float(self.x_max_input.text()) if self.x_max_input.text() else 10
            num_points = int(self.points_input.text()) if self.points_input.text() else 500

            func_str = self.equation
            x = np.linspace(x_min, x_max, num_points)

            func = eval(f"lambda x: {func_str}")
            y = func(x)

            plt.style.use('dark_background')
            plt.plot(x, y, color='cyan', linewidth=2)
            if self.x_line:
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
            ax.yaxis.set_ticks_position('left')
            ax.tick_params(axis='x', colors='white', labelsize=12)
            ax.tick_params(axis='y', colors='white', labelsize=12)

            if draw_line:
                plt.plot(x, x, color='magenta', linestyle='--', linewidth=2, label='y = x')

            plt.show()
            self.accept()

        except Exception as e:
            QMessageBox.warning(self, "Invalid Input", f"Error: {str(e)}")
