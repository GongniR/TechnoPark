from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog
import sys
import cv2
import qimage2ndarray

# Класс для формочки
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main_form.ui',self)

#         Кнопки
        self.OpenFile_pushButton.clicked.connect(self.push_btn)

    #  Действие для кнопок
    def push_btn(self):
        ofd = QFileDialog()
        path = ofd.getOpenFileName(ofd, filter= " FILTERS (*.png, *jpg, *.jpeg)")
        self.PathFile_lineEdit.setText(path[0])

app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.show()
app.exec_()