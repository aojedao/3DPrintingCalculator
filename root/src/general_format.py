# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'format_general.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog3(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(716, 562)
        Dialog.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(255, 255, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(30)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Futura Bk BT")
        font.setPointSize(12)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.name_general = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        self.name_general.setFont(font)
        self.name_general.setStyleSheet("color: rgb(39, 39, 39);\n"
"background-color: rgb(255, 255, 255);")
        self.name_general.setObjectName("name_general")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_general)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Futura Bk BT")
        font.setPointSize(12)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.energy_cost = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        self.energy_cost.setFont(font)
        self.energy_cost.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(39, 39, 39);")
        self.energy_cost.setObjectName("energy_cost")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.energy_cost)
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Futura Bk BT")
        font.setPointSize(12)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.workforce_cost = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        self.workforce_cost.setFont(font)
        self.workforce_cost.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(39, 39, 39);")
        self.workforce_cost.setObjectName("workforce_cost")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.workforce_cost)
        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Futura Bk BT")
        font.setPointSize(12)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.frecuency_fail_printer = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        self.frecuency_fail_printer.setFont(font)
        self.frecuency_fail_printer.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(39, 39, 39);")
        self.frecuency_fail_printer.setObjectName("frecuency_fail_printer")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.frecuency_fail_printer)
        self.monetary_unity = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        self.monetary_unity.setFont(font)
        self.monetary_unity.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(39, 39, 39);")
        self.monetary_unity.setObjectName("monetary_unity")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.monetary_unity)
        self.label_5 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Futura Bk BT")
        font.setPointSize(12)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.verticalLayout.addLayout(self.formLayout)
        self.button_save_general = QtWidgets.QDialogButtonBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        self.button_save_general.setFont(font)
        self.button_save_general.setStyleSheet("background-color: rgb(220, 185, 88);\n"
"color: rgb(39, 39, 39);")
        self.button_save_general.setOrientation(QtCore.Qt.Horizontal)
        self.button_save_general.setStandardButtons(QtWidgets.QDialogButtonBox.Save)
        self.button_save_general.setObjectName("button_save_general")
        self.verticalLayout.addWidget(self.button_save_general)
        self.data=None
        self.retranslateUi(Dialog)
        self.button_save_general.clicked.connect(self.save_general)
        self.button_save_general.accepted.connect(Dialog.accept)
        self.button_save_general.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def save_general(self):
        try:
            self.data=[float(self.energy_cost.text()),float(self.workforce_cost.text()),float(self.frecuency_fail_printer.text()),
                       self.monetary_unity.text()]

        except ValueError:
            print("se presento un error al convertir en format general")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Generales"))
        self.label_6.setText(_translate("Dialog", "General"))
        self.label.setText(_translate("Dialog", "Nombre:"))
        self.label_2.setText(_translate("Dialog", "Costo de la energía:"))
        self.energy_cost.setPlaceholderText(_translate("Dialog", "pesos/kWh"))
        self.label_3.setText(_translate("Dialog", "Costo de la mano de obra:"))
        self.workforce_cost.setPlaceholderText(_translate("Dialog", "pesos/hora"))
        self.label_4.setText(_translate("Dialog", "Frecuencia de fallos en la impresión:"))
        self.frecuency_fail_printer.setPlaceholderText(_translate("Dialog", "%"))
        self.label_5.setText(_translate("Dialog", "Unidad Monetaria:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
