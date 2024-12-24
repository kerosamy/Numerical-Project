from PyQt6.QtWidgets import QDialog, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6 import QtGui

class StepWindow(QDialog):
    def __init__(self, steps):
        super().__init__()
        self.setWindowTitle('Steps Window')
        self.setGeometry(100, 100, 600, 400)

        self.setStyleSheet("background-color: black; color: white;")

        layout = QVBoxLayout()

        if steps:
            columns = list(steps[0].keys()) 
        else:
            columns = []
       
        self.table = QTableWidget(len(steps), len(columns))

        self.table.setStyleSheet("""
            QTableWidget {
                background-color: #333333;
                border: 1px solid #444444;
            }
            QTableWidget::item {
                background-color: #333333;
                color: white;
            }
            QHeaderView::section {
                background-color: #444444;
                color: white;
                padding: 5px;
                border: 1px solid #555555;
            }
        """)

        self.table.setHorizontalHeaderLabels(columns)

        for row, step in enumerate(steps):
            for col, column in enumerate(columns):
                self.set_table_item(row, col, step.get(column, None))

        layout.addWidget(self.table)
        self.setLayout(layout)

    def set_table_item(self, row, col, value):
        if value is None or value == 'N/A':
            self.table.setItem(row, col, QTableWidgetItem(''))  
        else:
            item = QTableWidgetItem(str(value))
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter) 
            self.table.setItem(row, col, item)

