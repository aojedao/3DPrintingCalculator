from PyQt5 import uic
from main_format import *
from format_cotiz import *
from general_format import *
from material_format import *
from format_printer import *
from clases import*



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.button_cot.clicked.connect(self.window_cot)
        self.actionGeneral.triggered.connect(self.window_generales)
        self.actionimpresora.triggered.connect(self.window_printer)
        self.actionmaterial.triggered.connect(self.window_material)
        self.flag=False
        self.flag2=False
        self.flag3=False
        self.data_cotizacion=None
        self.data_impresora=None
        self.data_material=None
        self.data_general=None

    def window_cot(self):
        if self.flag and self.flag2 and self.flag3:
            self.ventana = QtWidgets.QDialog()
            self.ui = Ui_Dialog()
            self.ui.setupUi(self.ventana)
            self.ventana.exec_()
            self.data_cotizacion=self.ui.dates_printer

            self.union(self.data_cotizacion,self.data_impresora,self.data_general,self.data_material)


    def window_printer(self):

        self.ventana = QtWidgets.QDialog()
        self.ui = Ui_Dialog2()
        self.ui.setupUi(self.ventana)
        self.ventana.exec_()
        self.flag=True
        self.data_impresora=self.ui.data


    def window_generales(self):

        self.ventana = QtWidgets.QDialog()
        self.ui = Ui_Dialog3()
        self.ui.setupUi(self.ventana)
        self.ventana.exec_()
        self.flag2=True
        self.data_general=self.ui.data

    def window_material(self):

        self.ventana = QtWidgets.QDialog()
        self.ui = Ui_Dialog4()
        self.ui.setupUi(self.ventana)
        self.ventana.exec_()
        self.data_material=self.ui.data
        self.flag3=True

    def union(self,cot,printer,general,material):

        self.cotizacion=cotizar(cot,printer,general,material)
        #llamar funciones



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


