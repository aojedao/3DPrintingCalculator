import math
import pickle
from time import time
from linked_list import*
from list_arrays import*
import numpy as np
from os import path
from hash_table import *
from arboles_avl import *
from calendario_clase import *
class opciones:

    def createFiles(self):

        pickle_t = open("cotizacioness", 'wb')
        pickle.dump([], pickle_t)  # Se crea el pickle
        pickle_t.close()


    def savecotizacion(self,data):

        with open("cotizacioness", 'rb') as pickle_file:
            cotizacion = pickle.load(pickle_file)  # Abre el pickle en lectura binaria para extraer la lista guardada
            pickle_file.close()

        with open("cotizacioness", 'wb') as pickle_file:

            pickle.dump(data, pickle_file)
            pickle_file.close()


    def cargar_cotizacion(self):
        with open("cotizacioness", 'rb') as pickle_file:
            cotizaciones = pickle.load(pickle_file)  # Lee el archivo pickle
            pickle_file.close()

        return cotizaciones

    def verificar_dia(self,dia):
        c=self.cargar_cotizacion()

        if len(c)>0:
            for i in range(len(c)):
                if c[i][0].year() == dia.year() and c[i][0].month() == dia.month() and c[i][0].day() == dia.day() :
                    return i
        return -1




class cotizar(opciones):
    def __init__(self,data,impresora,general,material,data_hash,avl):

        self.subtota_l = 0
        self.resultado=0
        self.lists=[]
        self.hash_t=data_hash
        self.avll=avl
        #datos cotizacion

        self.cli_nombre=data[0]

        self.cli_fecha=calendarioo(data[1])

        self.cli_descripcion=data[2]
        self.imp_impresora=data[3]
        self.imp_filamento=data[4]
        self.imp_peso=data[5]
        self.imp_timeImpresion=data[6]
        self.pre_slicing=data[7]
        self.pre_cambioMaterial=data[8]
        self.pre_tranandArr=data[9]
        self.post_remPieza=data[10]
        self.post_remSoportes=data[11]
        self.post_tradicional=data[12]
        self.mis_consumibles=data[13]
        self.cob_ganancia=data[14]
        self.tiempo_post=data[15]
        self.tiempo_pre=data[16]

        #datos impresora
        self.opcion_imp_diametro=impresora[0]
        self.opcion_imp_costo=impresora[1]
        self.opcion_imp_timeDepre=impresora[2]
        self.opcion_imp_costServicio = impresora[3]
        self.opcion_imp_consumo = impresora[4]

        #datos general
        self.opcion_gen_costEner=general[0]
        self.opcion_gen_costMano = general[1]
        self.opcion_gen_frecuencia = general[2]
        self.opcion_gen_unidad = general[3]

        #datos material
        self.opcion_mat_fabricante=material[0]
        self.opcion_mat_diametro=material[1]
        self.opcion_mat_costo = material[2]
        self.opcion_mat_tamano = material[3]
        self.opcion_mat_densidad = material[4]
        self.opcion_mat_tempEx = material[5]
        self.opcion_mat_tempCam = material[6]

        #costos
        self.cant_material=self.material_consumido()
        self.filamento_total=self.cost_filamento()
        self.electricidad_total=self.cost_electricidad()
        self.depre_total=self.depreciacion_impresora()
        self.pre_total=self.preparacion()
        self.pro_total=self.post_proces()
        self.sub_total=self.subtotal(self.lists)
        self.fail_total=self.incluye_fallos()
        self.precio_total=self.precio_sug()
        self.ti_pre=self.tiempo_preparacion()
        self.ti_pro=self.tiempo_post_procesing()
        self.savess()

    #guardar cotizacion

    def savess(self):

        dta=self.cargar_cotizacion()

        ver=self.verificar_dia(self.cli_fecha)

        if ver>-1 :

            data_d=list_array(43)
            data_d.insertar(self.cli_nombre)
            data_d.insertar(self.cli_descripcion)
            data_d.insertar(self.imp_impresora)
            data_d.insertar(self.imp_filamento)
            data_d.insertar(self.imp_peso)
            data_d.insertar(self.imp_timeImpresion)
            data_d.insertar(self.pre_slicing)
            data_d.insertar(self.pre_cambioMaterial)
            data_d.insertar(self.pre_tranandArr)
            data_d.insertar(self.post_remPieza)
            data_d.insertar(self.post_remSoportes)
            data_d.insertar(self.post_tradicional)
            data_d.insertar(self.mis_consumibles)
            data_d.insertar(self.cob_ganancia)
            data_d.insertar(self.tiempo_post)
            data_d.insertar(self.tiempo_pre)
            data_d.insertar(self.opcion_imp_diametro)
            data_d.insertar(self.opcion_imp_costo)
            data_d.insertar(self.opcion_imp_timeDepre)
            data_d.insertar(self.opcion_imp_costServicio)
            data_d.insertar(self.opcion_imp_consumo)
            data_d.insertar(self.opcion_gen_costEner)
            data_d.insertar(self.opcion_gen_costMano)
            data_d.insertar(self.opcion_gen_frecuencia)
            data_d.insertar(self.opcion_gen_unidad)
            data_d.insertar(self.opcion_mat_fabricante)
            data_d.insertar(self.opcion_mat_diametro)
            data_d.insertar(self.opcion_mat_costo)
            data_d.insertar(self.opcion_mat_tamano)
            data_d.insertar(self.opcion_mat_densidad)
            data_d.insertar(self.opcion_mat_tempEx)
            data_d.insertar(self.opcion_mat_tempCam)
            data_d.insertar(self.cant_material)
            data_d.insertar(self.filamento_total)
            data_d.insertar(self.electricidad_total)
            data_d.insertar(self.depre_total)
            data_d.insertar(self.pre_total)
            data_d.insertar(self.pre_total)
            data_d.insertar(self.sub_total)
            data_d.insertar(self.fail_total)
            data_d.insertar(self.precio_total)
            data_d.insertar(self.ti_pre)
            data_d.insertar(self.ti_pro)

            dta[ver][1].append(data_d)




        else:
            x=10

            new=[]
            data_d=list_array(43)
            data_d.insertar(self.cli_nombre)
            data_d.insertar(self.cli_descripcion)
            data_d.insertar(self.imp_impresora)
            data_d.insertar(self.imp_filamento)
            data_d.insertar(self.imp_peso)
            data_d.insertar(self.imp_timeImpresion)
            data_d.insertar(self.pre_slicing)
            data_d.insertar(self.pre_cambioMaterial)
            data_d.insertar(self.pre_tranandArr)
            data_d.insertar(self.post_remPieza)
            data_d.insertar(self.post_remSoportes)
            data_d.insertar(self.post_tradicional)
            data_d.insertar(self.mis_consumibles)
            data_d.insertar(self.cob_ganancia)
            data_d.insertar(self.tiempo_post)
            data_d.insertar(self.tiempo_pre)
            data_d.insertar(self.opcion_imp_diametro)
            data_d.insertar(self.opcion_imp_costo)
            data_d.insertar(self.opcion_imp_timeDepre)
            data_d.insertar(self.opcion_imp_costServicio)
            data_d.insertar(self.opcion_imp_consumo)
            data_d.insertar(self.opcion_gen_costEner)
            data_d.insertar(self.opcion_gen_costMano)
            data_d.insertar(self.opcion_gen_frecuencia)
            data_d.insertar(self.opcion_gen_unidad)
            data_d.insertar(self.opcion_mat_fabricante)
            data_d.insertar(self.opcion_mat_diametro)
            data_d.insertar(self.opcion_mat_costo)
            data_d.insertar(self.opcion_mat_tamano)
            data_d.insertar(self.opcion_mat_densidad)
            data_d.insertar(self.opcion_mat_tempEx)
            data_d.insertar(self.opcion_mat_tempCam)
            data_d.insertar(self.cant_material)
            data_d.insertar(self.filamento_total)
            data_d.insertar(self.electricidad_total)
            data_d.insertar(self.depre_total)
            data_d.insertar(self.pre_total)
            data_d.insertar(self.pre_total)
            data_d.insertar(self.sub_total)
            data_d.insertar(self.fail_total)
            data_d.insertar(self.precio_total)
            data_d.insertar(self.ti_pre)
            data_d.insertar(self.ti_pro)
            new.append(data_d)
            ver=len(dta)
            dta.append([self.cli_fecha,new])


        self.savecotizacion(dta)

        z=nodd(data_d.lista,ver)

        self.hash_t.Polihash(z.valuee,z)

        self.avll.avl_insert(self.cli_fecha,self.cli_nombre)








    #calculo materiales -------------------------
    def longitud(self):
        long=(self.opcion_mat_tamano*4000)/(math.pi*self.opcion_mat_densidad*math.pow(2,self.opcion_mat_diametro))
        return long
    def costo_porkg(self):
        cost=self.opcion_mat_costo/self.opcion_mat_tamano
        return cost

    #calculo impresora ------------------------
    def depreciacion(self):
        depre=(self.opcion_imp_costo+self.opcion_imp_costServicio)/self.opcion_imp_timeDepre
        return depre
    #calculo general ------------------------------------

    def material_consumido(self):
        material_consumido=((self.imp_peso/self.opcion_mat_densidad)*4)/((math.pow(2,self.opcion_mat_diametro))*math.pi)
        self.lists.append(material_consumido)
        return material_consumido

    def tiempo_preparacion(self):

        suma=self.pre_slicing+self.pre_cambioMaterial+self.pre_tranandArr+self.tiempo_pre


        return suma/60

    def tiempo_post_procesing(self):
        suma=self.post_remPieza+self.post_remSoportes+self.post_tradicional+self.tiempo_post
        return suma/60
    #calcular costos -------------------------------------

    def cost_filamento(self):
        costo_filamento=(self.imp_peso/1000)*self.costo_porkg()
        self.lists.append(costo_filamento)
        return costo_filamento

    def cost_electricidad(self):
        costo_electricidad=self.imp_timeImpresion*self.opcion_imp_consumo*self.opcion_gen_costEner
        self.lists.append(costo_electricidad)
        return costo_electricidad
    def depreciacion_impresora(self):
        depreciacion=self.imp_timeImpresion*self.depreciacion()
        self.lists.append(depreciacion)
        return depreciacion

    def preparacion(self):

        preparar=self.tiempo_preparacion()*self.opcion_gen_costMano
        self.lists.append(preparar)
        return preparar
    def post_proces(self):
        preparar=self.tiempo_post_procesing()*self.opcion_gen_costMano
        self.lists.append(preparar)
        return preparar


    def subtotal(self,lista_anteriores):

        for i in lista_anteriores:
            self.subtota_l+=i
        return self.subtota_l
    def incluye_fallos(self):
        self.resultado=(self.subtota_l*(self.opcion_gen_frecuencia/(100+1)))+self.subtota_l

        return self.resultado

    # cobro

    def precio_sug(self):
        total=(self.cob_ganancia/100)*self.resultado
        return total

    def export(self):

        grafica=list_array(10)
        grafica.insertar(self.cant_material)
        grafica.insertar(self.filamento_total)
        grafica.insertar(self.electricidad_total)
        grafica.insertar(self.depre_total)
        grafica.insertar(self.pre_total)
        grafica.insertar(self.pro_total)
        grafica.insertar(self.sub_total)
        grafica.insertar(self.fail_total)
        grafica.insertar(self.precio_total)
        grafica.insertar(self.mis_consumibles)

        return grafica.lista

    def resumen_data(self):

        grafica = list_array(14)
        grafica.insertar(self.filamento_total)
        grafica.insertar(self.electricidad_total)
        grafica.insertar(self.depre_total)
        grafica.insertar(self.pre_total)
        grafica.insertar(self.pro_total)

        grafica.insertar(self.mis_consumibles)
        grafica.insertar(self.sub_total)
        grafica.insertar(self.fail_total)
        grafica.insertar(self.ti_pre)
        grafica.insertar(self.ti_pro)
        grafica.insertar((self.imp_filamento))
        grafica.insertar(self.cant_material)
        grafica.insertar(self.imp_timeImpresion)
        grafica.insertar(self.precio_total)

        return grafica.lista

class solicitud(opciones):
    def __init__(self):
        self.verify_exist()

    def verify_exist(self):

        if not path.exists("cotizacioness"):  # comprueba que los pickles existan de no ser asi son creados
            self.createFiles()

    def load_data(self,data):
        if len(data)>0 :

            restar=list_array(3)
            data_d=Hash_table()
            names=list_array(100)
            avl=AVL_tree()
            for i in data:
                for j in i[1]:

                    names.insertar(j.lista[0])
                    avl.avl_insert(i[0],j.lista[0])
                    nod=nodd(j.lista,i[0])
                    data_d.Polihash(nod.valuee,nod)
            restar.insertar(data[0][1][0].lista[16:21])
            restar.insertar(data[0][1][0].lista[21:25])
            restar.insertar(data[0][1][0].lista[25:32])

            return restar,names,data_d,avl

        return False,False,False,False
    def searching2(self,name,data):

        a=data.search_hash(name)

        if a:

            data_resumen=list_array(15)
            data_resumen.insertar(a.otherr[33])
            data_resumen.insertar(a.otherr[34])
            data_resumen.insertar(a.otherr[35])
            data_resumen.insertar(a.otherr[36])
            data_resumen.insertar(a.otherr[37])
            data_resumen.insertar(a.otherr[12])
            data_resumen.insertar(a.otherr[38])
            data_resumen.insertar(a.otherr[39])
            data_resumen.insertar(a.otherr[41])
            data_resumen.insertar(a.otherr[42])
            data_resumen.insertar(a.otherr[3])
            data_resumen.insertar(a.otherr[32])
            data_resumen.insertar(a.otherr[5])
            data_resumen.insertar(a.otherr[40])

            return a.otherr[32:41],data_resumen
        return False,False

    def delete_cotiz(self,name,data,ha,avl):
        daat = data
        ha.delete(name)

        for i in daat:
            for j in i[1]:

                if j.lista[0]==name:
                    avl.delete_value(i[0],name)
                    i[1].remove(j)
                    if len(i[1])<1:
                        daat.remove(i)
                    break

        self.savecotizacion(daat)




    def analisis_tend(self,data):

        final=list_array(len(data))
        #1 mat
        #2 energia = []
        # 3tiempous = []
        #4 tiempopro = []

        for i in data:
            s1=0
            s2=0
            s3=0
            s4=0

            for j in i[1]:
                s1+=j.lista[32]
                s2+=j.lista[20]
                s3+=j.lista[5]
                s4+=j.lista[5]+j.lista[14]+j.lista[15]

            final.insertar([i[0],s1,s2,s3,s4])


        return final
