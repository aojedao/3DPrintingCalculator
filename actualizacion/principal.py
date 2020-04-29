from PyQt5 import uic
from graficos import *
from formats import *
from format_cotiz import *
from general_format import *
from material_format import *
from format_printer import *
from clases_cotizacion import*



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.grafica=Graficas()
        self.button_past_service.clicked.connect(self.abrir_cotiz)
        self.button_tend_servicios.clicked.connect(self.analisis)
        self.eliminar.clicked.connect(self.delete)
        self.button_cot.clicked.connect(self.window_cot)
        self.actionGeneral.triggered.connect(self.window_generales)
        self.actionimpresora.triggered.connect(self.window_printer)
        self.actionmaterial_2.triggered.connect(self.window_material)
        self.load=solicitud()
        self.data_totalcotizaciones=self.load.cargar_cotizacion()
        self.verificar=self.load.load_data(self.data_totalcotizaciones)
        self.flag = False
        self.flag2 = False
        self.flag3 = False
        self.data_cotizacion = None
        self.data_impresora = None
        self.data_material = None
        self.data_general = None
        self.names_cotiza=self.load.load_names(self.data_totalcotizaciones)
        if len(self.names_cotiza)>0:
            for i in self.names_cotiza:
                self.cot_lista.addItem(i)
                self.cot_lista.setStatusTip(i)

            if self.verificar:
                self.data_impresora=self.verificar[0]
                self.data_general = self.verificar[1]
                self.data_material = self.verificar[2]
                self.flag = True
                self.flag2 = True
                self.flag3 = True


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
        self.cot_lista.addItem(cot[0])
        self.cot_lista.item(self.cot_lista.count()-1).setStatusTip(cot[0])
        self.data_totalcotizaciones=self.load.cargar_cotizacion()
        self.grafica.graficoconsumo(self.cotizacion.export())
        #llamar funciones

    def abrir_cotiz(self):
        p=self.cot_lista.currentRow()
        if p>=0:
            name=self.cot_lista.item(p).text()
            print("pasa")
            dta=self.load.return_data(name,self.data_totalcotizaciones)
            print("pasa")
            self.grafica.graficoconsumo(dta,True)
    def delete(self):
        p = self.cot_lista.currentRow()
        if p >= 0:
            name = self.cot_lista.item(p).text()
            self.cot_lista.takeItem(p)
            self.load.delete_cotiz(name,self.data_totalcotizaciones)
            self.data_totalcotizaciones=self.load.cargar_cotizacion()
    def analisis(self):
        self.load.analisis_tend(self.data_totalcotizaciones)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


