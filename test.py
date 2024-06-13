from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Window title!")

button = QPushButton()
button.setText("button text")

window.setCentralWidget(button)

window.show()
app.exec()