# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_format.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1357, 920)
        MainWindow.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.cot_lista = QtWidgets.QListWidget(self.centralwidget)
        self.cot_lista.setObjectName("cot_lista")

        self.verticalLayout_2.addWidget(self.cot_lista)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_cot = QtWidgets.QPushButton(self.centralwidget)
        self.button_cot.setStyleSheet("")
        self.button_cot.setObjectName("button_cot")
        self.verticalLayout.addWidget(self.button_cot)
        self.button_tend_servicios = QtWidgets.QPushButton(self.centralwidget)
        self.button_tend_servicios.setObjectName("button_tend_servicios")
        self.verticalLayout.addWidget(self.button_tend_servicios)
        self.button_past_service = QtWidgets.QPushButton(self.centralwidget)
        self.button_past_service.setObjectName("button_past_service")
        self.verticalLayout.addWidget(self.button_past_service)
        self.eliminar = QtWidgets.QPushButton(self.centralwidget)
        self.eliminar.setObjectName("eliminar")
        self.verticalLayout.addWidget(self.eliminar)
        self.button_mens_consume = QtWidgets.QPushButton(self.centralwidget)
        self.button_mens_consume.setObjectName("button_mens_consume")
        self.verticalLayout.addWidget(self.button_mens_consume)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1357, 26))
        self.menubar.setObjectName("menubar")
        self.menuconfiguracion = QtWidgets.QMenu(self.menubar)
        self.menuconfiguracion.setObjectName("menuconfiguracion")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionimpresora = QtWidgets.QAction(MainWindow)
        self.actionimpresora.setObjectName("actionimpresora")
        self.actionmaterial = QtWidgets.QAction(MainWindow)
        self.actionmaterial.setObjectName("actionmaterial")
        self.actionGeneral = QtWidgets.QAction(MainWindow)
        self.actionGeneral.setObjectName("actionGeneral")
        self.actionmaterial_2 = QtWidgets.QAction(MainWindow)
        self.actionmaterial_2.setObjectName("actionmaterial_2")
        self.menuconfiguracion.addSeparator()
        self.menuconfiguracion.addAction(self.actionimpresora)
        self.menuconfiguracion.addAction(self.actionGeneral)
        self.menuconfiguracion.addAction(self.actionmaterial_2)
        self.menubar.addAction(self.menuconfiguracion.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Cotizaciones"))
        __sortingEnabled = self.cot_lista.isSortingEnabled()
        self.cot_lista.setSortingEnabled(False)

        self.cot_lista.setSortingEnabled(__sortingEnabled)
        self.button_cot.setText(_translate("MainWindow", "Cotizar"))
        self.button_tend_servicios.setText(_translate("MainWindow", "Analisis de tendencia en los servicios"))
        self.button_past_service.setText(_translate("MainWindow", "abrir cotizacion"))
        self.eliminar.setText(_translate("MainWindow", "Eliminar cotizacion"))
        self.button_mens_consume.setText(_translate("MainWindow", "Análisis mensual de consumo"))
        self.menuconfiguracion.setTitle(_translate("MainWindow", "configuracion"))
        self.actionimpresora.setText(_translate("MainWindow", "Impresora"))
        self.actionmaterial.setText(_translate("MainWindow", "Materiales"))
        self.actionGeneral.setText(_translate("MainWindow", "General"))
        self.actionmaterial_2.setText(_translate("MainWindow", "material"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
