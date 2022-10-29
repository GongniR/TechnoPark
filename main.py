from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
import sys
import cv2
import qimage2ndarray

# Класс для формочки
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main_form.ui',self)
        self.image_path = ''
#         Кнопки
        self.OpenFile_pushButton.clicked.connect(self.push_btn)

    #  Действие для кнопок
    def push_btn(self):
        ofd = QFileDialog()
        self.image_path = ofd.getOpenFileName(ofd)
        self.PathFile_lineEdit.setText(self.image_path[0])
        self.view_image(self.image_path[0])

    def view_image(self, image_path):
        image = cv2.imread(image_path)
        pixmap = QPixmap(image_path)
        self.Image_label.setPixmap(pixmap)
app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.show()
app.exec_()