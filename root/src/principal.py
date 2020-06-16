
from graficos2 import *
from updates import *
from format_cotiz import *
from general_format import *
from material_format import *
from format_printer import *
from clases_cotizacion import*
from resumen import *



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.grafica=Graficas()
        self.button_past_service.clicked.connect(self.abrir_cotiz)
        self.button_tend_servicios.clicked.connect(self.analisis)
        self.eliminar.clicked.connect(self.delete)
        self.button_cot.clicked.connect(self.window_cot)
        self.button_search.clicked.connect(self.new_search)
        self.actionGeneral.triggered.connect(self.window_generales)
        self.actionimpresora.triggered.connect(self.window_printer)
        self.actionmaterial_2.triggered.connect(self.window_material)
        self.button_date_search.clicked.connect(self.search_filter)
        self.load=solicitud()

        self.data_totalcotizaciones=self.load.cargar_cotizacion()

        self.verificar,self.names_cotiza,self.data_hash,self.avl=self.load.load_data(self.data_totalcotizaciones)

        self.flag = False
        self.flag2 = False
        self.flag3 = False
        self.data_cotizacion = None
        self.data_impresora = None
        self.data_material = None
        self.data_general = None
        if not self.data_hash:
            self.data_hash=Hash_table()
            self.avl=AVL_tree()
        if self.names_cotiza:
            for i in self.names_cotiza.lista:
                if i==0:
                    break
                self.cot_lista.addItem(i)
                self.cot_lista.setStatusTip(i)

            self.data_impresora=self.verificar.lista[0]
            self.data_general = self.verificar.lista[1]
            self.data_material = self.verificar.lista[2]
            self.flag = True
            self.flag2 = True
            self.flag3 = True



    def new_search(self):
        a=self.line_search.text()
        c,b=self.load.searching2(a,self.data_hash)
        if b:
            self.grafica.graficoconsumo(c)
            self.resumen(b.lista)
        else:
            print("no ")

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

    def resumen(self,data):

        self.ventana = QtWidgets.QDialog()
        self.ui = Ui_resumen()
        self.ui.setupUi(self.ventana,data)
        self.ventana.exec_()

    def union(self,cot,printer,general,material):

        self.cotizacion=cotizar(cot,printer,general,material,self.data_hash,self.avl)

        self.cot_lista.addItem(cot[0])

        self.cot_lista.item(self.cot_lista.count()-1).setStatusTip(cot[0])

        self.data_totalcotizaciones=self.load.cargar_cotizacion()

        self.grafica.graficoconsumo(self.cotizacion.export())

        self.resumen(self.cotizacion.resumen_data())
        #llamar funciones

    def abrir_cotiz(self):
        p=self.cot_lista.currentRow()
        print(p,"werr")
        if p>=0:
            name=self.cot_lista.item(p).text()
            dta2,res=self.load.searching2(name,self.data_hash)
            self.grafica.graficoconsumo(dta2)
            self.resumen(res.lista)

    def delete(self):
        p = self.cot_lista.currentRow()
        if p >= 0:
            name = self.cot_lista.item(p).text()
            self.cot_lista.takeItem(p)
            self.load.delete_cotiz(name,self.data_totalcotizaciones,self.data_hash,self.avl)
            self.data_totalcotizaciones=self.load.cargar_cotizacion()
    def filter_data(self,data):
        for i in data:
            self.cot_lista.addItem(i)
            self.cot_lista.setStatusTip(i)
    def search_filter(self):
        a=int(self.start.text())
        b=int(self.end.text())

        c=self.avl.search_range(a,b)
        self.cot_lista.clear()
        if c:
            self.filter_data(c)


    def analisis(self):
        self.grafica.grafico2(self.load.analisis_tend(self.data_totalcotizaciones))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
