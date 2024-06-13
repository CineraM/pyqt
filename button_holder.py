from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class ButtonHolder(QMainWindow): # inherit from QMainWindow
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window title!")
        button = QPushButton("button text")

        self.setCentralWidget(button)