# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'printer_format.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(691, 568)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.diameter_printer = QtWidgets.QLineEdit(Dialog)
        self.diameter_printer.setObjectName("diameter_printer")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.diameter_printer)
        self.cost_printer = QtWidgets.QLineEdit(Dialog)
        self.cost_printer.setObjectName("cost_printer")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cost_printer)
        self.depreciation_time = QtWidgets.QLineEdit(Dialog)
        self.depreciation_time.setObjectName("depreciation_time")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.depreciation_time)
        self.service_cost = QtWidgets.QLineEdit(Dialog)
        self.service_cost.setObjectName("service_cost")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.service_cost)
        self.energy_consumption = QtWidgets.QLineEdit(Dialog)
        self.energy_consumption.setObjectName("energy_consumption")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.energy_consumption)
        self.verticalLayout.addLayout(self.formLayout)
        self.button_save_printer = QtWidgets.QDialogButtonBox(Dialog)
        self.button_save_printer.setOrientation(QtCore.Qt.Horizontal)
        self.button_save_printer.setStandardButtons(QtWidgets.QDialogButtonBox.Save)
        self.button_save_printer.setObjectName("button_save_printer")
        self.verticalLayout.addWidget(self.button_save_printer)
        self.data=None
        self.retranslateUi(Dialog)
        self.button_save_printer.clicked.connect(self.save_dates)
        self.button_save_printer.accepted.connect(Dialog.accept)
        self.button_save_printer.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def save_dates(self):
        try:
            self.data=[float(self.diameter_printer.text()),float(self.cost_printer.text()),float(self.depreciation_time.text()),
                       float(self.service_cost.text()),float(self.energy_consumption.text())]
        except ValueError:
            print("se presento un error al convertir en format printer")
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_6.setText(_translate("Dialog", "Impresora"))
        self.label.setText(_translate("Dialog", "Diametro:"))
        self.label_2.setText(_translate("Dialog", "Costo:"))
        self.label_3.setText(_translate("Dialog", "Tiempo de depreciación:"))
        self.label_4.setText(_translate("Dialog", "Costo de servicio:"))
        self.label_5.setText(_translate("Dialog", "Consumo energético:"))
        self.diameter_printer.setPlaceholderText(_translate("Dialog", "mm"))
        self.cost_printer.setPlaceholderText(_translate("Dialog", "pesos"))
        self.depreciation_time.setPlaceholderText(_translate("Dialog", "Horas"))
        self.service_cost.setPlaceholderText(_translate("Dialog", "Pesos"))
        self.energy_consumption.setPlaceholderText(_translate("Dialog", "KWh/h"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
