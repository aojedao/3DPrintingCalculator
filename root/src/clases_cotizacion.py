import math
import pickle
from time import time
from linked_list import*
from list_arrays import*
import numpy as np
from os import path
class opciones:

    def createFiles(self):

        pickle_t = open("cotizaciones", 'wb')
        pickle.dump([], pickle_t)  # Se crea el pickle
        pickle_t.close()


    def savecotizacion(self,data):

        with open("cotizaciones", 'rb') as pickle_file:
            cotizacion = pickle.load(pickle_file)  # Abre el pickle en lectura binaria para extraer la lista guardada
            pickle_file.close()

        with open("cotizaciones", 'wb') as pickle_file:

            pickle.dump(data, pickle_file)
            pickle_file.close()


    def cargar_cotizacion(self):
        with open("cotizaciones", 'rb') as pickle_file:
            cotizaciones = pickle.load(pickle_file)  # Lee el archivo pickle
            pickle_file.close()

        return cotizaciones




    def deleteTags(self, name_cotizacion):
        """
            cotizaciones = self.cargar_cotizacion()

            for cotizacion in cotizaciones:
                if dicc["file_name"] == file_path:  # Busca el archivo por su ruta
                    all_tags.remove(dicc)

            self.__saveAllTags(all_tags, isAlbum) Borra los datos de un archivo desde su ruta guardada, pide el tipo de archivo(music, video, photo) """
        pass

    def verificar_dia(self,dia):
        c=self.cargar_cotizacion()

        if len(c)>=0:
            for i in range(len(c)):
                if c[i][0] == dia:
                    return i
        return -1




class cotizar(opciones):
    def __init__(self,data,impresora,general,material):

        self.subtota_l = 0
        self.resultado=0
        self.lists=[]

        #datos cotizacion

        self.cli_nombre=data[0]
        self.cli_fecha=data[1]
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
        print(ver)
        if ver>=0 :


            dta[ver][1][0].insertar(self.cli_nombre)
            dta[ver][1][1].insertar(self.cli_descripcion)
            dta[ver][1][2].insertar(self.imp_impresora)
            dta[ver][1][3].insertar(self.imp_filamento)
            dta[ver][1][4].insertar(self.imp_peso)
            dta[ver][1][5].insertar(self.imp_timeImpresion)
            dta[ver][1][6].insertar(self.pre_slicing)
            dta[ver][1][7].insertar(self.pre_cambioMaterial)
            dta[ver][1][8].insertar(self.pre_tranandArr)
            dta[ver][1][9].insertar(self.post_remPieza)
            dta[ver][1][10].insertar(self.post_remSoportes)

            dta[ver][1][11].insertar(self.post_tradicional)

            dta[ver][1][12].insertar(self.mis_consumibles)

            dta[ver][1][13].insertar(self.cob_ganancia)

            dta[ver][1][14].insertar(self.tiempo_post)

            dta[ver][1][15].insertar(self.tiempo_pre)

            dta[ver][1][16].insertar(self.opcion_imp_diametro)
            dta[ver][1][17].insertar(self.opcion_imp_costo)
            dta[ver][1][18].insertar(self.opcion_imp_timeDepre)
            dta[ver][1][19].insertar(self.opcion_imp_costServicio)
            dta[ver][1][20].insertar(self.opcion_imp_consumo)

            dta[ver][1][21].insertar(self.opcion_gen_costEner)
            dta[ver][1][22].insertar(self.opcion_gen_costMano)
            dta[ver][1][23].insertar(self.opcion_gen_frecuencia)
            dta[ver][1][24].insertar(self.opcion_gen_unidad)

            dta[ver][1][25].insertar(self.opcion_mat_fabricante)
            dta[ver][1][26].insertar(self.opcion_mat_diametro)
            dta[ver][1][27].insertar(self.opcion_mat_costo)
            dta[ver][1][28].insertar(self.opcion_mat_tamano)
            dta[ver][1][29].insertar(self.opcion_mat_densidad)
            dta[ver][1][30].insertar(self.opcion_mat_tempEx)
            dta[ver][1][31].insertar(self.opcion_mat_tempCam)

            dta[ver][1][32].insertar(self.cant_material)
            dta[ver][1][33].insertar(self.filamento_total)
            dta[ver][1][34].insertar(self.electricidad_total)
            dta[ver][1][35].insertar(self.depre_total)
            dta[ver][1][36].insertar(self.pre_total)
            dta[ver][1][37].insertar(self.pro_total)
            dta[ver][1][38].insertar(self.sub_total)
            dta[ver][1][39].insertar(self.fail_total)
            dta[ver][1][40].insertar(self.precio_total)
            dta[ver][1][41].insertar(self.ti_pre)
            dta[ver][1][42].insertar(self.ti_pro)






        else:
            x=10
            new=[]
            nombres=list_array(x)
            nombres.insertar(self.cli_nombre)
            new.append(nombres)
            descripcion = list_array(x)
            descripcion.insertar(self.cli_descripcion)
            new.append(descripcion)
            impresora = list_array(x)
            impresora.insertar(self.imp_impresora)
            new.append(impresora)
            filamento = list_array(x)
            filamento.insertar(self.imp_filamento)
            new.append(filamento)
            peso = list_array(x)
            peso.insertar(self.imp_peso)
            new.append(peso)
            tiempo_impresion = list_array(x )
            tiempo_impresion.insertar(self.imp_timeImpresion)
            new.append(tiempo_impresion)
            slicing = list_array(x )
            slicing.insertar(self.pre_slicing)
            new.append(slicing)
            cambio_material = list_array(x)
            cambio_material.insertar(self.pre_cambioMaterial)
            new.append(cambio_material)
            pre_trand = list_array(x)
            pre_trand.insertar(self.pre_tranandArr)
            new.append(pre_trand)
            post_rem = list_array(x)
            post_rem.insertar(self.post_remPieza)
            new.append(post_rem)
            post_rems = list_array(x)
            post_rems.insertar(self.post_remSoportes)
            new.append(post_rems)
            trad = list_array(x)
            trad.insertar(self.post_tradicional)
            new.append(trad)
            consum = list_array(x)
            consum.insertar(self.mis_consumibles)
            new.append(consum)
            ganan = list_array(x)
            ganan.insertar(self.cob_ganancia)
            new.append(ganan)
            post_t = list_array(x)
            post_t.insertar(self.tiempo_post)
            new.append(post_t)
            tiempo_p = list_array(x)
            tiempo_p.insertar(self.tiempo_pre)
            new.append(tiempo_p)
            dia = list_array(x)
            dia.insertar(self.opcion_imp_diametro)
            new.append(dia)
            cost_a = list_array(x)
            cost_a.insertar(self.opcion_imp_costo)
            new.append(cost_a)
            cost_t = list_array(x)
            cost_t.insertar(self.opcion_imp_timeDepre)
            new.append(cost_t)
            serv = list_array(x)
            serv.insertar(self.opcion_imp_costServicio)
            new.append(serv)
            con = list_array(x)
            con.insertar(self.opcion_imp_consumo)
            new.append(con)
            ener = list_array(x)
            ener.insertar(self.opcion_gen_costEner)
            new.append(ener)
            mano = list_array(x)
            mano.insertar(self.opcion_gen_costMano)
            new.append(mano)
            fail = list_array(x)
            fail.insertar(self.opcion_gen_frecuencia)
            new.append(fail)
            uni = list_array(x)
            uni.insertar(self.opcion_gen_unidad)
            new.append(uni)
            fabri = list_array(x)
            fabri.insertar(self.opcion_mat_fabricante)
            new.append(fabri)
            matdi = list_array(x)
            matdi.insertar(self.opcion_mat_diametro)
            new.append(matdi)
            matcosto = list_array(x)
            matcosto.insertar(self.opcion_mat_costo)
            new.append(matcosto)
            tam = list_array(x)
            tam.insertar(self.opcion_mat_tamano)
            new.append(tam)
            matden = list_array(x)
            matden.insertar(self.opcion_mat_densidad)
            new.append(matden)
            tempex = list_array(x)
            tempex.insertar(self.opcion_mat_tempEx)
            new.append(tempex)
            temca = list_array(x)
            temca.insertar(self.opcion_mat_tempCam)
            new.append(temca)
            matecon = list_array(x)
            matecon.insertar(self.cant_material)
            new.append(matecon)
            filacos = list_array(x)
            filacos.insertar(self.filamento_total)
            new.append(filacos)
            elecos = list_array(x)
            elecos.insertar(self.electricidad_total)
            new.append(elecos)
            depres = list_array(x)
            depres.insertar(self.depre_total)
            new.append(depres)
            prepa = list_array(x)
            prepa.insertar(self.pre_total)
            new.append(prepa)
            postpro = list_array(x)
            postpro.insertar(self.pre_total)
            new.append(postpro)
            sub = list_array(x)
            sub.insertar(self.sub_total)
            new.append(sub)
            infail = list_array(x)
            infail.insertar(self.fail_total)
            new.append(infail)
            sug = list_array(x)
            sug.insertar(self.precio_total)
            new.append(sug)
            qw = list_array(x)
            qw.insertar(self.ti_pre)
            new.append(sug)
            we = list_array(x)
            we.insertar(self.ti_pro)
            new.append(sug)



            dta.append([self.cli_fecha,new])
        self.savecotizacion(dta)






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
        return grafica

    def resumen_data(self):
        grafica = []
        grafica.append(self.filamento_total)
        grafica.append(self.electricidad_total)
        grafica.append(self.depre_total)
        grafica.append(self.pre_total)
        grafica.append(self.pro_total)

        grafica.append(self.mis_consumibles)
        grafica.append(self.sub_total)
        grafica.append(self.fail_total)
        grafica.append(self.ti_pre)
        grafica.append(self.ti_pro)
        grafica.append((self.imp_filamento))
        grafica.append(self.cant_material)
        grafica.append(self.imp_timeImpresion)
        grafica.append(self.precio_total)
        return grafica

class solicitud(opciones):
    def __init__(self):
        self.verify_exist()

    def verify_exist(self):
        if not path.exists("cotizaciones"):  # comprueba que los pickles existan de no ser asi son creados
            self.createFiles()
    def load_data(self,data,flag=False):

        if len(data)>0 :
            if not flag:

                printer=[]
                for i in data[0][1][16:21]:

                    printer.append(i.search_pos(0))
                general = []
                for i in data[0][1][21:25]:
                    general.append(i.search_pos(0))
                material=[]
                for i in data[0][1][25:32]:
                    material.append(i.search_pos(0))

                restar=[printer,general,material]

                return restar

        return False

    def load_names(self,data):

        if len(data)>0:
            names=np.array([],"object")

            for i in data:
                names=np.hstack((names,i[1][0].consulta()))

            return names
        return []
    def return_data(self,name,data,flag=False):

        daat=data

        place=0
        pos=0

        for i in range(len(daat)):

            pos =daat[i][1][0].search(name)
            if pos>=0:
                place=i
                break

        dat=list_array(43)
        count=0

        for i in daat[place][1]:

            dat.insertar(i.search_pos(pos))
            count+=1
        if flag:
            print(dat.lista)
            data_resumen=[]

            data_resumen.append(dat.lista[33])

            data_resumen.append(dat.lista[34])
            data_resumen.append(dat.lista[35])
            data_resumen.append(dat.lista[36])
            data_resumen.append(dat.lista[37])
            data_resumen.append(dat.lista[12])
            data_resumen.append(dat.lista[38])
            data_resumen.append(dat.lista[39])
            data_resumen.append(dat.lista[41])
            data_resumen.append(dat.lista[42])
            data_resumen.append(dat.lista[3])
            data_resumen.append(dat.lista[32])
            data_resumen.append(dat.lista[5])
            data_resumen.append(dat.lista[40])

            return data_resumen




        return dat.lista[32:41]

    def delete_cotiz(self,name,data):
        daat = data
        place = 0



        for i in range(len(daat)):
            pos = daat[i][1][0].search(name)
            if pos >= 0:
                place = i
                break
        for i in daat[place][1]:
            i.delete_pos(pos)
            if i.count==0:
                daat.pop(place)
                break

        self.savecotizacion(daat)




    def analisis_tend(self,data):

        final=list_array(len(data))
        #1 mat
        #2 energia = []
        # 3tiempous = []
        #4 tiempopro = []

        for i in data:
            final.insertar([i[0],i[1][32].sumatoria(),i[1][20].sumatoria(),i[1][5].sumatoria(),i[1][14].sumatoria() + i[1][15].sumatoria() + i[1][5].sumatoria()])


        return final










