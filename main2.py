#створи тут фоторедактор Easy Editor!
from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageFilter, ImageEnhance  
from ui import Ui_MainWindow
import os

class ImageEditor(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.original = None
        self.workdir = ""
        self.ui.btn_folder.clicked.connect(self.show_files)
        self.ui.list_files.itemClicked.connect(self.clicks)
        self.ui.btn_B_W.clicked.connect(self.bw_filter)
        self.ui.btn_doleft.clicked.connect(self.left_filter)
        self.ui.btn_doright.clicked.connect(self.right_filter)
        self.ui.btn_mirror.clicked.connect(self.mirror_filter)
        self.ui.btn_sharp.clicked.connect(self.sharpen_filter)
        self.ui.btn_blur.clicked.connect(self.blur_filter)
        self.ui.btn_contrast.clicked.connect(self.contrast_filter)
        self.ui.btn_smooth.clicked.connect(self.smooth_filter)
        self.ui.btn_sigma.clicked.connect(self.outline)
        self.ui.btn_green.clicked.connect(self.green)
        self.ui.btn_save.clicked.connect(self.to_save)

        

    def sort_files(self, files):
        exentions = [".jpg", ".png", ".bmp", ".jpeg"]
        result = []
        for file in files:
            for ex in exentions:
                if file.endswith(ex):
                    result.append(file)
            return result
    def open(self):
        self.workdir = QtWidgets.QFileDialog.getExistingDirectory()

    def show_files(self):
        self.open()
        filename = os.listdir(self.workdir)
        filename = self.sort_files(filename)
        self.ui.list_files.clear()
        for filee in filename:
            self.ui.list_files.addItem(filee)

    def load_image(self, file_name):
        self.path = os.path.join(self.workdir,file_name)
        self.original = Image.open(self.path)

    def show_image(self):
        photo = QtGui.QPixmap(self.path)
        w, h = self.ui.image.width(), self.ui.image.height()
        photo = photo.scaled(w, h, QtCore.Qt.KeepAspectRatio)
        self.ui.image.setPixmap(photo)

    def clicks(self):
        if self.ui.list_files.currentRow() >= 0:
            file = self.ui.list_files.currentItem().text()
            self.load_image(file)
            self.show_image()

    def save_image(self):
        self.path = os.path.join(self.workdir, "new_image.jpg")
        self.original.save(self.path)

    def to_save(self):
        path = QtWidgets.QFileDialog.getExistingDirectory()
        name,ok = QtWidgets.QInputDialog.getText(self.ui, "Збереження", "Назвіть свій файл")
        if ok == True and name != '': 
            name = name+".png"
            new_path = os.path.join(path, name)
            self.original.save(new_path)
            print(new_path)
        


    def bw_filter(self):
        if self.original:
            self.original = self.original.convert("L")
            self.save_image()
            self.show_image()
    def left_filter(self):
        if self.original:
            self.original = self.original.rotate(90)
            self.original = self.original.convert('RGB')
            self.save_image()
            self.show_image()
    def right_filter(self):
        if self.original:
            self.original = self.original.rotate(-90)
            self.original = self.original.convert('RGB')
            self.save_image()
            self.show_image()
    def mirror_filter(self):
        if self.original:
            self.original = self.original.transpose(Image.FLIP_LEFT_RIGHT)
            self.save_image()
            self.show_image()
    def sharpen_filter(self):
        if self.original:
            self.original = self.original.filter(ImageFilter.SHARPEN)
            self.save_image()
            self.show_image()
    def blur_filter(self):
        if self.original:
            self.original = self.original.filter(ImageFilter.BLUR)
            self.save_image()
            self.show_image()
    def contrast_filter(self):
        if self.original:
            self.original = ImageEnhance.Contrast(self.original)
            self.original = self.original.enhance(1.5)
            self.original = self.original.convert('RGB')
            self.save_image()
            self.show_image()
    def smooth_filter(self):
        if self.original:
            self.original = self.original.filter(ImageFilter.SMOOTH)
            self.original = self.original.convert('RGB')
            self.save_image()
            self.show_image()
    def green(self):
        if self.original:
            green = self.original.split()
            zeroed_band = green[1].point(lambda _: 0)
            self.original = Image.merge("RGB", (zeroed_band, green[1], zeroed_band))
            self.save_image()
            self.show_image()
    def outline(self):
        if self.original:
            self.original = self.original.filter(ImageFilter.CONTOUR)
            self.original = self.original.convert('RGB')
            self.save_image()
            self.show_image()

    



    

 




#print("Без імнені .jpg".endswith(".jpg"))
            
app = QtWidgets.QApplication([])
win = ImageEditor()
win.show()
app.exec()
