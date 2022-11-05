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

        # Максимальное значение для слайдеров
        self.max_B = self.Max_B_horizontalSlider.value()
        self.max_G = self.Max_G_horizontalSlider.value()
        self.max_R = self.Max_R_horizontalSlider.value()


#         Кнопки
        self.OpenFile_pushButton.clicked.connect(self.push_btn)
        # Действие при изменении слайдера
        # MIN
        self.Min_B_horizontalSlider.valueChanged.connect(self.change_sl)
        self.Min_G_horizontalSlider.valueChanged.connect(self.change_sl)
        self.Min_R_horizontalSlider.valueChanged.connect(self.change_sl)
        #MAX
        self.Max_B_horizontalSlider.valueChanged.connect(self.change_sl)
        self.Max_G_horizontalSlider.valueChanged.connect(self.change_sl)
        self.Max_R_horizontalSlider.valueChanged.connect(self.change_sl)

        # RadioButton
        self.Range_radioButton.clicked.connect(lambda: self.view_image(self.image_path[0]))
        self.Original_radioButton.clicked.connect(lambda: self.view_image(self.image_path[0]))
        self.BRG_radioButton.clicked.connect(lambda: self.view_image(self.image_path[0]))
        self.HSV_radioButton.clicked.connect(lambda: self.view_image(self.image_path[0]))
        self.GRAY_radioButton.clicked.connect(lambda: self.view_image(self.image_path[0]))


    def change_sl(self):
        # Изменение минимальных параметров
        self.min_B = self.Min_B_horizontalSlider.value()
        self.min_G = self.Min_G_horizontalSlider.value()
        self.min_R = self.Min_R_horizontalSlider.value()

        self.max_B = self.Max_B_horizontalSlider.value()
        self.max_G = self.Max_G_horizontalSlider.value()
        self.max_R = self.Max_R_horizontalSlider.value()
        # Загрузка картинки
        self.view_image(self.image_path[0])
    #
    # Действие при нажатие кнопку
    def push_btn(self):
        # Создание класса для диалога
        ofd = QFileDialog()
        # Путь для изображения
        self.image_path = ofd.getOpenFileName(ofd)
        # Добавление пути в лейбл
        self.PathFile_lineEdit.setText(self.image_path[0])
        # Показ картики
        self.view_image(self.image_path[0])

    def slider_enable(self, bool):
        self.Min_B_horizontalSlider.setEnabled(bool)
        self.Min_R_horizontalSlider.setEnabled(bool)
        self.Max_B_horizontalSlider.setEnabled(bool)
        self.Max_R_horizontalSlider.setEnabled(bool)
    # Получение изображения
    def view_image(self, image_path):
        # Считываю изображение по пути
        image = cv2.imread(image_path)

        # Изменение цветового пространства
        if self.BRG_radioButton.isChecked():
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if self.HSV_radioButton.isChecked():
            image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
        if self.GRAY_radioButton.isChecked():
            image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        # Изменение размера изображения
        size = self.Image_label.size()
        h, w = size.height(), size.width()
        image = cv2.resize(image,(w,h),cv2.INTER_CUBIC)

        if self.Range_radioButton.isChecked():
            # Обнуление не подходящих пикселей
            if self.GRAY_radioButton.isChecked():
                self.slider_enable(False)
                image = cv2.inRange(image, self.min_G, self.max_G)
            else:
                self.slider_enable(True)
                image = cv2.inRange(image, (self.min_B, self.min_G, self.min_R), (self.max_B, self.max_G, self.max_R))

        # Перевод изображения в Qpixmap
        image2pixmap = QPixmap.fromImage(qimage2ndarray.array2qimage(image))

        # Отображение
        self.Image_label.setPixmap(image2pixmap)

app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.show()
app.exec_()