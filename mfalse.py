# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'false.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import random


class Ui_Form_False(object):
    def setupUi(self, Form):
        picture_list = ["fota.png", "vader.jpg", "minecraft_bad.png", "mario_sad.jpg"]
        pic = random.choice(list(picture_list))

        Form.setObjectName("Form")
        Form.resize(640, 640)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 0, 840, 640))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(pic))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "To błąd !"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
