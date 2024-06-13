from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


############### global scale
# app = QApplication(sys.argv)

# window = QMainWindow()
# window.setWindowTitle("Window title!")

# button = QPushButton()
# button.setText("button text")

# window.setCentralWidget(button)

# window.show()
# app.exec()

## clas approach


# class ButtonHolder(QMainWindow): # inherit from QMainWindow
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Window title!")
#         button = QPushButton("button text")

#         self.setCentralWidget(button)

from button_holder import ButtonHolder

app = QApplication(sys.argv)

window = ButtonHolder()
window.show()
app.exec()

