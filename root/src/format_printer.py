# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'printer_format.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        self.list_filament={"Ender CR-10":	[1.75,2014005,3000,402801,0.15],"Sidewinder X1":[1.75,1695792,2500,339158.4,0.16]
        ,"Ender 3":[1.75,862270,3000,172454,0.12],"Prusa i3":[1.75,2808001,5000,561600.2,0.12]}
        Dialog.setObjectName("Dialog")
        Dialog.resize(691, 568)
        Dialog.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(255, 255, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label_6 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Futura Bk BT")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.horizontalLayout_2.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setEnabled(True)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("unnamed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(-1, -1, -1, 0)
        self.formLayout.setHorizontalSpacing(5)
        self.formLayout.setVerticalSpacing(24)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Futura Bk BT")
        font.setPointSize(17)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.diameter_printer = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        self.diameter_printer.setFont(font)
        self.diameter_printer.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.diameter_printer.setObjectName("diameter_printer")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.diameter_printer)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Futura Bk BT")
        font.setPointSize(17)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.cost_printer = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        self.cost_printer.setFont(font)
        self.cost_printer.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.cost_printer.setObjectName("cost_printer")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cost_printer)
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Futura Bk BT")
        font.setPointSize(17)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Futura Bk BT")
        font.setPointSize(17)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.service_cost = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        self.service_cost.setFont(font)
        self.service_cost.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.service_cost.setObjectName("service_cost")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.service_cost)
        self.label_5 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Futura Bk BT")
        font.setPointSize(17)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.energy_consumption = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        self.energy_consumption.setFont(font)
        self.energy_consumption.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.energy_consumption.setObjectName("energy_consumption")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.energy_consumption)
        self.depreciation_time = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        self.depreciation_time.setFont(font)
        self.depreciation_time.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.depreciation_time.setObjectName("depreciation_time")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.depreciation_time)
        self.verticalLayout.addLayout(self.formLayout)
        self.button_save_printer = QtWidgets.QDialogButtonBox(Dialog)
        self.button_save_printer.setStyleSheet("background-color: rgb(220, 185, 88);\n"
"color: rgb(39, 39, 39);")
        self.button_save_printer.setOrientation(QtCore.Qt.Horizontal)
        self.button_save_printer.setStandardButtons(QtWidgets.QDialogButtonBox.Save)
        self.button_save_printer.setObjectName("button_save_printer")
        self.verticalLayout.addWidget(self.button_save_printer)
        self.data=None
        self.retranslateUi(Dialog)
        self.button_save_printer.clicked.connect(self.save_dates)
        self.button_save_printer.accepted.connect(Dialog.accept)
        self.button_save_printer.rejected.connect(Dialog.reject)
        self.pushButton.clicked.connect(self.updatess)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def updatess(self):

        data=self.list_filament[self.comboBox.currentText()]
        self.diameter_printer.setText(str(data[0]))
        self.cost_printer.setText(str(data[1]))
        self.depreciation_time.setText(str(data[2]))
        self.service_cost.setText(str(data[3]))
        self.energy_consumption.setText(str(data[4]))

    def save_dates(self):
        try:
            self.data=[float(self.diameter_printer.text()),float(self.cost_printer.text()),float(self.depreciation_time.text()),
                       float(self.service_cost.text()),float(self.energy_consumption.text())]
        except ValueError:
            print("se presento un error al convertir en format printer")



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Configuración impresora"))
        self.label_6.setText(_translate("Dialog", "Impresora"))
        self.label.setText(_translate("Dialog", "Diametro:"))
        self.diameter_printer.setPlaceholderText(_translate("Dialog", "mm"))
        self.label_2.setText(_translate("Dialog", "Costo:"))
        self.cost_printer.setPlaceholderText(_translate("Dialog", "pesos"))
        self.label_3.setText(_translate("Dialog", "Tiempo de depreciación:"))
        self.label_4.setText(_translate("Dialog", "Costo de servicio:"))
        self.service_cost.setPlaceholderText(_translate("Dialog", "Pesos"))
        self.label_5.setText(_translate("Dialog", "Consumo energético:"))
        self.energy_consumption.setPlaceholderText(_translate("Dialog", "KWh/h"))
        self.depreciation_time.setPlaceholderText(_translate("Dialog", "Horas"))
        self.comboBox.setItemText(0, _translate("Dialog", "Ender CR-10"))
        self.comboBox.setItemText(1, _translate("Dialog", "Sidewinder X1"))
        self.comboBox.setItemText(2, _translate("Dialog", "Ender 3"))
        self.comboBox.setItemText(3, _translate("Dialog", "Prusa i3"))
        self.pushButton.setText(_translate("Dialog", "actualizar"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
