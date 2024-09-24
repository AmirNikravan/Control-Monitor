import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QCheckBox, QPushButton, QDateEdit, QLabel
from PySide6.QtCore import QDate
import numpy as np
import matplotlib.pyplot as plt

class GraphPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Graph Page")
        self.layout = QVBoxLayout()

        # Checkboxes for data selection
        self.checkbox1 = QCheckBox("Data Series 1")
        self.checkbox2 = QCheckBox("Data Series 2")
        self.checkbox3 = QCheckBox("Data Series 3")

        self.layout.addWidget(self.checkbox1)
        self.layout.addWidget(self.checkbox2)
        self.layout.addWidget(self.checkbox3)

        # Date selection
        self.start_date = QDateEdit()
        self.start_date.setDate(QDate.currentDate().addMonths(-1))
        self.start_date.setCalendarPopup(True)
        self.layout.addWidget(QLabel("Start Date:"))
        self.layout.addWidget(self.start_date)

        self.end_date = QDateEdit()
        self.end_date.setDate(QDate.currentDate())
        self.end_date.setCalendarPopup(True)
        self.layout.addWidget(QLabel("End Date:"))
        self.layout.addWidget(self.end_date)

        # Button to update graph
        self.update_button = QPushButton("Update Graph")
        self.update_button.clicked.connect(self.update_graph)
        self.layout.addWidget(self.update_button)

        self.setLayout(self.layout)

    def update_graph(self):
        # Gather selected data
        data_series = []
        if self.checkbox1.isChecked():
            data_series.append(self.generate_data(1))
        if self.checkbox2.isChecked():
            data_series.append(self.generate_data(2))
        if self.checkbox3.isChecked():
            data_series.append(self.generate_data(3))

        # Filter by date range (mock implementation)
        start = self.start_date.date().toPyDate()
        end = self.end_date.date().toPyDate()
        
        # Create the graph
        self.plot_graph(data_series, start, end)

    def generate_data(self, series_number):
        x = np.arange(0, 100)
        y = np.random.rand(100) * series_number * 10
        return x, y

    def plot_graph(self, data_series, start, end):
        plt.clf()  # Clear previous plot
        for series in data_series:
            x, y = series
            plt.plot(x, y, label=f"Series {len(data_series)}")

        plt.xlim(0, 100)
        plt.ylim(0, 30)
        plt.title(f"Graph from {start} to {end}")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.legend()
        plt.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GraphPage()
    window.show()
    sys.exit(app.exec())
