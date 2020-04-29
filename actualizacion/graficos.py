from matplotlib import pyplot
from list_arrays import *
class Graficas:

    def graficoconsumo(self,data,flag=False):
        print("llega")
        dta=data
        datos = ('Filamento','Electricidad','Depreciacion de la impresora','Preparacion','Post-procesing','Consumibles')

        if not flag:
            slices = (dta.search_pos(1), dta.search_pos(2), dta.search_pos(3), dta.search_pos(4),
                      dta.search_pos(5), dta.search_pos(0))
        else:

            slices = (dta[1], dta[2], dta[3], dta[4],
                      dta[5], dta[0])


        colores = ('red','blue','green','pink','yellow','orange')

        pyplot.pie(slices, colors=colores, autopct="%1.1f%%")
        pyplot.axis("equal")
        pyplot.title("costo de frabricación")
        pyplot.legend(labels=datos)
        pyplot.show()

    def graficotendensia__(self):

        datos = ('Tiempo de uso de Impresora','Energia consumida','tiempo de proceso consumido')
        slices = (self.imp_timeImpresion,self.opcion_imp_consumo,self.opcion_imp_timeDepre)

        pyplot.plot(datos,slices)
        pyplot.title("Analisis de tendencias en los servicios")
        pyplot.legend(labels=datos)
        pyplot.show()

    def grafico__(self):
        datos = ('Tiempo de uso de Impresora','Energia consumida','tiempo de proceso consumido')
        slices = (120,20,50,140)

        pyplot.plot(datos,slices)
        pyplot.title("Analisis de tendencias en los servicios")
        pyplot.legend(labels=datos)
        pyplot.show()

