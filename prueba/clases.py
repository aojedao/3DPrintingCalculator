import math

def __createPickles(self,cotizacion_name):
    pickle_t = open(cotizacion_name, 'wb')
    pickle.dump([], pickle_t)  # Se crea el pickle guardando una lista vacia
    pickle_t.close()


def saveTags(self,cotizacion_name):

    with open(pickle_name, 'rb') as pickle_file:
        all_tags = pickle.load(pickle_file)  # Abre el pickle en lectura binaria para extraer la lista guardada
        pickle_file.close()

    with open(pickle_name, 'wb') as pickle_file:
        all_tags.append(tags)  # Añade el nuevo tag a la lista
        pickle.dump(all_tags, pickle_file)  # Abre el pickle en escritura binaria para volver a guardar
        pickle_file.close()


def readTags(self, isAlbum=False):
    """Recibe el tipo de archivo y devuelve los datos guardados en el pickle"""

    pickle_name = self.album_pickle if isAlbum else self.pickle

    with open(pickle_name, 'rb') as pickle_file:
        all_tags = pickle.load(pickle_file)  # Lee el archivo pickle
        pickle_file.close()

    return all_tags


def __saveAllTags(self, all_tags_list, isAlbum=False):
    """Guarda el objeto recibido como primer argumento en el pickle de su tipo"""

    pickle_name = self.album_pickle if isAlbum else self.pickle

    with open(pickle_name, 'wb') as pickle_file:
        pickle.dump(all_tags_list, pickle_file)  # Escribe en el pickle el primer argumento
        pickle_file.close()


def deleteTags(self, file_path, isAlbum=False):
    """Borra los datos de un archivo desde su ruta guardada, pide el tipo de archivo(music, video, photo) """

    all_tags = self.readTags(isAlbum)

    for dicc in all_tags:
        if dicc["file_name"] == file_path:  # Busca el archivo por su ruta
            all_tags.remove(dicc)

    self.__saveAllTags(all_tags, isAlbum)

class cotizar:
    def __init__(self,data,impresora,general,material):

        self.subtota_l = 0
        self.resultado=0

        #datos cotizacion

        self.cli_nombre=data["nombre"]
        self.cli_fecha=data["fecha"]
        self.cli_descripcion=data["descripcion"]
        self.imp_impresora=data["impresora"]
        self.imp_filamento=data["filamento"]
        self.imp_peso=data["peso"]
        self.imp_timeImpresion=data["tiempo_impresion"]
        self.pre_slicing=data["slicing"]
        self.pre_cambioMaterial=data["cambio_material"]
        self.pre_tranandArr=data["transferencia_arranque"]
        self.post_remPieza=data["remocion_pieza"]
        self.post_remSoportes=data["remocion_soporte"]
        self.post_tradicional=data["trabajo_adicional"]
        self.mis_consumibles=data["consumible"]
        self.cob_ganancia=data["ganancia"]
        self.tiempo_post=data["tiempo_post"]
        self.tiempo_pre=data["tiempo_preparacion"]

        #datos impresora
        self.opcion_imp_diametro=impresora["diametro"]
        self.opcion_imp_costo=impresora["costo"]
        self.opcion_imp_timeDepre=impresora["tiempo_depreciacion"]
        self.opcion_imp_costServicio = impresora["costo_servicio"]
        self.opcion_imp_consumo = impresora["consumo_energetico"]

        #datos general
        self.opcion_gen_costEner=general["costo_energia"]
        self.opcion_gen_costMano = general["costo_obra"]
        self.opcion_gen_frecuencia = general["frecuencia_fallos"]
        self.opcion_gen_unidad = general["unidad_monetaria"]

        #datos material
        self.opcion_mat_fabricante=material["fabricante"]
        self.opcion_mat_diametro=material["diametro"]
        self.opcion_mat_costo = material["costo_carrete"]
        self.opcion_mat_tamano = material["tamano_carrete"]
        self.opcion_mat_densidad = material["densidad"]
        self.opcion_mat_tempEx = material["temperatura_extrusor"]
        self.opcion_mat_tempCam = material["temperatura_cama"]

        self.lista=[]
        self.lista.append(self.material_consumido())
        self.lista.append(self.cost_filamento())
        self.lista.append(self.cost_electricidad())
        self.lista.append(self.depreciacion_impresora())
        self.lista.append(self.preparacion())
        self.lista.append(self.post_proces())
        self.lista.append(self.subtotal(self.lista))
        self.lista.append(self.incluye_fallos())
        self.lista.append(self.precio_sug())
        print(self.lista)

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
        return material_consumido

    #calcular costos -------------------------------------

    def cost_filamento(self):
        costo_filamento=(self.imp_peso/1000)*self.costo_porkg()
        return costo_filamento

    def cost_electricidad(self):
        costo_electricidad=self.imp_timeImpresion*self.opcion_imp_consumo*self.opcion_gen_costEner
        return costo_electricidad
    def depreciacion_impresora(self):
        depreciacion=self.imp_timeImpresion*self.depreciacion()
        return depreciacion
    def preparacion(self):
        preparar=self.tiempo_pre*self.opcion_gen_costMano
        return preparar
    def post_proces(self):
        preparar=self.tiempo_post*self.opcion_gen_costMano
        return preparar

    def subtotal(self,lista_anteriores):

        for i in lista_anteriores:
            self.subtota_l+=i
        return self.subtota_l
    def incluye_fallos(self):
        self.resultado=self.subtota_l/(100+1)
        return self.resultado

    # cobro

    def precio_sug(self):
        total=self.cob_ganancia*self.resultado
        return total