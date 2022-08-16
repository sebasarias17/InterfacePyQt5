from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog,QApplication,QFileDialog
from PyQt5.QtGui import QPixmap
import sys

#Iniciamos la app
app = QtWidgets.QApplication([])

#Cargamos archivos .ui
feed = uic.loadUi("Ventana1.ui")
SeleccionarFoto = uic.loadUi("Ventana2.ui")
BuscarImagen= uic.loadUi("Ventana3.ui")

def gui_seleccionar():
    feed.hide()
    SeleccionarFoto.show()

def gui_archivo():
    fname = QFileDialog.getOpenFileName(caption="Open File",directory="",filter="All Files(*);;CSV Files(*.CSV);;PDF Files(*.pdf)")
    SeleccionarFoto.lineEdit.setText(fname[0])

def gui_foto():
    feed.hide()
    BuscarImagen.show()

def gui_selectfoto():
    fname = QFileDialog.getOpenFileName(caption="Open File",directory="",filter="All Files(*);;JPG Files(*.jpg);;JPEG Files(*.jpeg);;PNG Files(*.png)")
    BuscarImagen.pixmap = QPixmap(fname[0])
    BuscarImagen.label_2.setPixmap(BuscarImagen.pixmap)

def gui_volverArchivo():
    SeleccionarFoto.hide()
    feed.show()

def gui_volverImagenes():
    BuscarImagen.hide()
    feed.show()



#Botones

# Botones Feed:
feed.Archivo.clicked.connect(gui_seleccionar)
feed.SelextImagen.clicked.connect(gui_foto)

#Botones Seleccionar Archivo
SeleccionarFoto.pushButton_3.clicked.connect(gui_volverArchivo)
SeleccionarFoto.SearchButton.clicked.connect(gui_archivo)

#Botones Seleccionar Imagen
BuscarImagen.SelectButtom.clicked.connect(gui_selectfoto)
BuscarImagen.back_2.clicked.connect(gui_volverImagenes)


#Ejecutable
feed.show()
app.exec_()