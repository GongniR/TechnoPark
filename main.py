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

        # Путь к изображению
        self.image_path = ''

        # Минимальные значения для слайдеров
        self.min_B = self.Min_B_horizontalSlider.value()
        self.min_G = self.Min_G_horizontalSlider.value()
        self.min_R = self.Min_R_horizontalSlider.value()

#         Кнопки
        self.OpenFile_pushButton.clicked.connect(self.push_btn)
        # Действие при изменении слайдера
        self.Min_B_horizontalSlider.valueChanged.connect(self.change_sl)
        self.Min_G_horizontalSlider.valueChanged.connect(self.change_sl)
        self.Min_R_horizontalSlider.valueChanged.connect(self.change_sl)

    # Действие при нажатие на слайдер
    def change_sl(self):
        # Изменение минимальных параметров
        self.min_B = self.Min_B_horizontalSlider.value()
        self.min_G = self.Min_G_horizontalSlider.value()
        self.min_R = self.Min_R_horizontalSlider.value()
        # Загрузка картинки
        self.view_image(self.image_path[0])
    #
    # Действие при нажатие кнопоку
    def push_btn(self):
        # Создание класса для диалога
        ofd = QFileDialog()
        # Путь для изображения
        self.image_path = ofd.getOpenFileName(ofd)
        # Добавление пути в лейбл
        self.PathFile_lineEdit.setText(self.image_path[0])
        # Показ картики
        self.view_image(self.image_path[0])

    # Получение изображения
    def view_image(self, image_path):
        # Считываю изображение по пути
        image = cv2.imread(image_path)
        # Изменение цветового пространства
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Изменение размера изображения
        size = self.Image_label.size()
        h, w = size.height(), size.width()
        image = cv2.resize(image,(w,h),cv2.INTER_CUBIC)

        # Обнуление не подходящих пикселей
        new = cv2.inRange(image, (self.min_B, self.min_G, self.min_R), (255,255,255))

        # Перевод изображения в Qpixmap
        image2pixmap = QPixmap.fromImage(qimage2ndarray.array2qimage(new))

        # Отображение
        self.Image_label.setPixmap(image2pixmap)

app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.show()
app.exec_()