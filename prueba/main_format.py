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
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(800, 390, 251, 191))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_cot = QtWidgets.QPushButton(self.widget)
        self.button_cot.setStyleSheet("")
        self.button_cot.setObjectName("button_cot")
        self.verticalLayout.addWidget(self.button_cot)
        self.button_tend_servicios = QtWidgets.QPushButton(self.widget)
        self.button_tend_servicios.setObjectName("button_tend_servicios")
        self.verticalLayout.addWidget(self.button_tend_servicios)
        self.button_past_service = QtWidgets.QPushButton(self.widget)
        self.button_past_service.setObjectName("button_past_service")
        self.verticalLayout.addWidget(self.button_past_service)
        self.button_mens_consume = QtWidgets.QPushButton(self.widget)
        self.button_mens_consume.setObjectName("button_mens_consume")
        self.verticalLayout.addWidget(self.button_mens_consume)
        self.button_cot.raise_()
        self.button_tend_servicios.raise_()
        self.button_past_service.raise_()
        self.button_mens_consume.raise_()
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
        self.menuconfiguracion.addSeparator()
        self.menuconfiguracion.addAction(self.actionimpresora)
        self.menuconfiguracion.addAction(self.actionmaterial)
        self.menuconfiguracion.addAction(self.actionGeneral)
        self.menubar.addAction(self.menuconfiguracion.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_cot.setText(_translate("MainWindow", "Cotizar"))
        self.button_tend_servicios.setText(_translate("MainWindow", "Analisis de tendencia en los servicios"))
        self.button_past_service.setText(_translate("MainWindow", "Servicios pasados"))
        self.button_mens_consume.setText(_translate("MainWindow", "Análisis mensual de consumo"))
        self.menuconfiguracion.setTitle(_translate("MainWindow", "configuracion"))
        self.actionimpresora.setText(_translate("MainWindow", "Impresora"))
        self.actionmaterial.setText(_translate("MainWindow", "Materiales"))
        self.actionGeneral.setText(_translate("MainWindow", "General"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
