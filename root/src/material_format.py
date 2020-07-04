# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'material_format.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog4(object):
    def setupUi(self, Dialog):
        self.list_filament={"Esun PLA":	[1.75,99000,1,1,24,200,70],"4DLabs":[1.75,75000,1,1.05,200,60
        ],"BIMEK":[1.75,75000,1,1.03,190,80],"3D Innovation":[1.75,91630,1,1.24,205,65],
        "Moviltronics":[1.75,80000,1,1.24,205,60],"Printart3D":[1.75,82900,1,1.24,205,65],
        "Drop Materializa":[1.75,175100,1,1.24,205,65]}
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        Dialog.setStyleSheet("background-color: rgb(39, 39, 39);\n"
"color: rgb(255, 255, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(31)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
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
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.maker = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        self.maker.setFont(font)
        self.maker.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.maker.setObjectName("maker")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.maker)
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.diameter_material = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        self.diameter_material.setFont(font)
        self.diameter_material.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.diameter_material.setObjectName("diameter_material")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.diameter_material)
        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.reel_cost = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        self.reel_cost.setFont(font)
        self.reel_cost.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.reel_cost.setObjectName("reel_cost")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.reel_cost)
        self.label_5 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.size_reel = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        self.size_reel.setFont(font)
        self.size_reel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.size_reel.setObjectName("size_reel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.size_reel)
        self.label_6 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.density = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        self.density.setFont(font)
        self.density.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.density.setObjectName("density")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.density)
        self.label_7 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.extruder_temperature = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        self.extruder_temperature.setFont(font)
        self.extruder_temperature.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.extruder_temperature.setObjectName("extruder_temperature")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.extruder_temperature)
        self.label_8 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.bed_temperature = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        self.bed_temperature.setFont(font)
        self.bed_temperature.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.bed_temperature.setObjectName("bed_temperature")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.bed_temperature)
        self.verticalLayout.addLayout(self.formLayout)
        self.button_save_material = QtWidgets.QDialogButtonBox(Dialog)
        self.button_save_material.setStyleSheet("background-color: rgb(220, 185, 88);\n"
"color: rgb(0, 0, 0);")
        self.button_save_material.setOrientation(QtCore.Qt.Horizontal)
        self.button_save_material.setStandardButtons(QtWidgets.QDialogButtonBox.Save)
        self.button_save_material.setObjectName("button_save_material")
        self.verticalLayout.addWidget(self.button_save_material)
        self.data=None
        self.retranslateUi(Dialog)
        self.button_save_material.clicked.connect(self.save_material)
        self.button_save_material.accepted.connect(Dialog.accept)
        self.button_save_material.rejected.connect(Dialog.reject)
        self.pushButton.clicked.connect(self.updatess)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def updatess(self):

        data=self.list_filament[self.comboBox.currentText()]
        self.maker.setText(self.comboBox.currentText())
        self.diameter_material.setText(str(data[0]))
        self.reel_cost.setText(str(data[1]))
        self.size_reel.setText(str(data[2]))
        self.density.setText(str(data[3]))
        self.extruder_temperature.setText(str(data[4]))
        self.bed_temperature.setText(str(data[5]))

    def save_material(self):
        self.data=[self.maker.text(),float(self.diameter_material.text()),float(self.reel_cost.text())
                   ,float(self.size_reel.text()),float(self.density.text()),float(self.extruder_temperature.text())
                   ,float(self.bed_temperature.text())]



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Material"))
        self.label_2.setText(_translate("Dialog", "Material"))
        self.label.setText(_translate("Dialog", "Fabricante:"))
        self.label_3.setText(_translate("Dialog", "Diametro:"))
        self.diameter_material.setPlaceholderText(_translate("Dialog", "mm"))
        self.label_4.setText(_translate("Dialog", "Costo de carrete :"))
        self.reel_cost.setPlaceholderText(_translate("Dialog", "pesos"))
        self.label_5.setText(_translate("Dialog", "Tamaño de carrete:"))
        self.size_reel.setPlaceholderText(_translate("Dialog", "kg"))
        self.label_6.setText(_translate("Dialog", "Densidad:"))
        self.density.setPlaceholderText(_translate("Dialog", "g/cm^3"))
        self.label_7.setText(_translate("Dialog", "Temperatura de extrusor:"))
        self.extruder_temperature.setPlaceholderText(_translate("Dialog", "°C"))
        self.label_8.setText(_translate("Dialog", "temperatura de cama:"))
        self.bed_temperature.setPlaceholderText(_translate("Dialog", "°C"))
        self.comboBox.setItemText(0, _translate("Dialog", "Esun PLA"))
        self.comboBox.setItemText(1, _translate("Dialog", "4DLabs"))
        self.comboBox.setItemText(2, _translate("Dialog", "BIMEK"))
        self.comboBox.setItemText(3, _translate("Dialog", "3D Innovation"))
        self.comboBox.setItemText(4, _translate("Dialog", "Moviltronics"))
        self.comboBox.setItemText(5, _translate("Dialog", "Printart3D"))
        self.comboBox.setItemText(6, _translate("Dialog", "Drop Materializa"))
        self.pushButton.setText(_translate("Dialog", "actualizar"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog4()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
