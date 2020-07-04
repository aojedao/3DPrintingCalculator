from matplotlib import pyplot
from list_arrays import *
class Graficas:

    def graficoconsumo(self,data):

        dta=data
        datos = ('Filamento','Electricidad','Depreciacion de la impresora','Preparacion','Post-procesing','Consumibles')


        slices = (dta[1], dta[2], dta[3], dta[4],
                  dta[5], dta[0])


        colores = ('red','blue','green','pink','yellow','orange')

        pyplot.pie(slices, colors=colores, autopct="%1.1f%%")
        pyplot.axis("equal")
        pyplot.title("costo de frabricación")
        pyplot.legend(labels=datos)
        pyplot.show()


    def grafico2(self,dias):
        titulo = ['Material consumido ','Energia consumida','Tiempo de uso de Impresora','tiempo de proceso consumido']
        cantidad_anexos = len(titulo)
        datos = []
        slices = []
        colores = ('red','blue','green','pink','yellow','orange')
        for i in range(1,cantidad_anexos+1):
            ax = pyplot.subplot(2,2,i)

            for a in dias.lista:
                print(a[0].day())
                dato_uni = str(a[0].day())+"/"+str(a[0].month())+"/"+str(a[0].year())
                datos.append(dato_uni)
                slices_uni = a[i]
                slices.append(slices_uni)


            datos.sort()
            ax.plot(datos,slices, color = colores[i])
            ax.set_title(str(titulo[i-1]))
            ax.set_xlabel("dias")
            ax.set_ylabel("consumo")
            datos = []
            slices = []

        pyplot.show()
