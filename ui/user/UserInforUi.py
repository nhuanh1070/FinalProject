# Form implementation generated from reading ui file 'D:\FinalProject\FinalProject\ui\user\UserInforUi.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(486, 635)
        Dialog.setStyleSheet("background-color: rgb(124, 0, 11);")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setStyleSheet("background-color: rgb(124, 0, 11);\n"
"border: None")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=self.widget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setMinimumSize(QtCore.QSize(60, 60))
        self.label.setMaximumSize(QtCore.QSize(60, 60))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/WhiteIcons/images/icons/WhiteIcons/user_ic.svg"))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.widget_10 = QtWidgets.QWidget(parent=self.frame)
        self.widget_10.setStyleSheet("border: None")
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_10)
        self.verticalLayout_9.setContentsMargins(12, -1, 12, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_9 = QtWidgets.QFrame(parent=self.widget_10)
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_9)
        self.label_4.setMaximumSize(QtCore.QSize(32, 32))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/WhiteIcons/images/icons/WhiteIcons/alert_circle_ic.svg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.label_9 = QtWidgets.QLabel(parent=self.frame_9)
        self.label_9.setStyleSheet("color: rgb(254, 254, 255);\n"
"font: 63 12pt \"Segoe UI Semibold\";")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_9.addWidget(self.frame_9)
        self.gridLayout_2.addWidget(self.widget_10, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.widget_4 = QtWidgets.QWidget(parent=self.widget)
        self.widget_4.setStyleSheet("border: None")
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.widget_2 = QtWidgets.QWidget(parent=self.widget_4)
        self.widget_2.setStyleSheet("border: None")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(12, -1, 12, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(parent=self.widget_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_2.setStyleSheet("color: rgb(254, 254, 255);\n"
"font: 63 12pt \"Segoe UI Semibold\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.lineEditUserName = QtWidgets.QLineEdit(parent=self.frame_3)
        self.lineEditUserName.setMinimumSize(QtCore.QSize(320, 36))
        self.lineEditUserName.setMaximumSize(QtCore.QSize(320, 16777215))
        self.lineEditUserName.setStyleSheet("    border-radius: 10px;\n"
"    border: 2px solid #D2B48C;\n"
"background-color: rgb(253, 253, 250);\n"
"font: 63 12pt \"Segoe UI Semibold\";\n"
"color: rgb(0, 0, 0);")
        self.lineEditUserName.setObjectName("lineEditUserName")
        self.horizontalLayout.addWidget(self.lineEditUserName, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.verticalLayout_8.addWidget(self.widget_2)
        self.widget_5 = QtWidgets.QWidget(parent=self.widget_4)
        self.widget_5.setStyleSheet("border: None")
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setContentsMargins(12, -1, 12, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_4 = QtWidgets.QFrame(parent=self.widget_5)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_3.setStyleSheet("color: rgb(254, 254, 255);\n"
"font: 63 12pt \"Segoe UI Semibold\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.lineEditFullName = QtWidgets.QLineEdit(parent=self.frame_4)
        self.lineEditFullName.setMinimumSize(QtCore.QSize(320, 36))
        self.lineEditFullName.setMaximumSize(QtCore.QSize(320, 16777215))
        self.lineEditFullName.setStyleSheet("color: rgb(0, 0, 0);    border-radius: 10px;\n"
"    border: 2px solid #D2B48C;\n"
"background-color: rgb(253, 253, 250);\n"
"font: 63 12pt \"Segoe UI Semibold\";")
        self.lineEditFullName.setObjectName("lineEditFullName")
        self.horizontalLayout_2.addWidget(self.lineEditFullName, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.verticalLayout_8.addWidget(self.widget_5)
        self.widget_9 = QtWidgets.QWidget(parent=self.widget_4)
        self.widget_9.setStyleSheet("border: None")
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_9)
        self.verticalLayout_7.setContentsMargins(12, -1, 12, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_8 = QtWidgets.QFrame(parent=self.widget_9)
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(parent=self.frame_8)
        self.label_7.setStyleSheet("color: rgb(254, 254, 255);\n"
"font: 63 12pt \"Segoe UI Semibold\";")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.lineEditBirthDay = QtWidgets.QLineEdit(parent=self.frame_8)
        self.lineEditBirthDay.setMinimumSize(QtCore.QSize(320, 36))
        self.lineEditBirthDay.setMaximumSize(QtCore.QSize(320, 16777215))
        self.lineEditBirthDay.setStyleSheet("color: rgb(0, 0, 0);    border-radius: 10px;\n"
"    border: 2px solid #D2B48C;\n"
"background-color: rgb(253, 253, 250);\n"
"font: 63 12pt \"Segoe UI Semibold\";")
        self.lineEditBirthDay.setObjectName("lineEditBirthDay")
        self.horizontalLayout_6.addWidget(self.lineEditBirthDay, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_7.addWidget(self.frame_8)
        self.verticalLayout_8.addWidget(self.widget_9)
        self.widget_8 = QtWidgets.QWidget(parent=self.widget_4)
        self.widget_8.setStyleSheet("border: None")
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_6.setContentsMargins(12, -1, 12, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_7 = QtWidgets.QFrame(parent=self.widget_8)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(parent=self.frame_7)
        self.label_6.setStyleSheet("color: rgb(254, 254, 255);\n"
"font: 63 12pt \"Segoe UI Semibold\";")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.lineEditPhoneNumber = QtWidgets.QLineEdit(parent=self.frame_7)
        self.lineEditPhoneNumber.setMinimumSize(QtCore.QSize(320, 36))
        self.lineEditPhoneNumber.setMaximumSize(QtCore.QSize(320, 16777215))
        self.lineEditPhoneNumber.setStyleSheet("color: rgb(0, 0, 0);    border-radius: 10px;\n"
"    border: 2px solid #D2B48C;\n"
"background-color: rgb(253, 253, 250);\n"
"font: 63 12pt \"Segoe UI Semibold\";")
        self.lineEditPhoneNumber.setPlaceholderText("Your Phone Numer")
        self.lineEditPhoneNumber.setObjectName("lineEditPhoneNumber")
        self.horizontalLayout_5.addWidget(self.lineEditPhoneNumber, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_6.addWidget(self.frame_7)
        self.verticalLayout_8.addWidget(self.widget_8)
        self.widget_7 = QtWidgets.QWidget(parent=self.widget_4)
        self.widget_7.setStyleSheet("border: None")
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_5.setContentsMargins(12, -1, 12, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_6 = QtWidgets.QFrame(parent=self.widget_7)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_5.setStyleSheet("color: rgb(254, 254, 255);\n"
"font: 63 12pt \"Segoe UI Semibold\";")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.lineEditEmail = QtWidgets.QLineEdit(parent=self.frame_6)
        self.lineEditEmail.setMinimumSize(QtCore.QSize(320, 36))
        self.lineEditEmail.setMaximumSize(QtCore.QSize(320, 16777215))
        self.lineEditEmail.setStyleSheet("color: rgb(0, 0, 0);    border-radius: 10px;\n"
"    border: 2px solid #D2B48C;\n"
"background-color: rgb(253, 253, 250);\n"
"font: 63 12pt \"Segoe UI Semibold\";")
        self.lineEditEmail.setPlaceholderText("Fill in email")
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.horizontalLayout_4.addWidget(self.lineEditEmail, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_5.addWidget(self.frame_6)
        self.verticalLayout_8.addWidget(self.widget_7)
        self.widget_6 = QtWidgets.QWidget(parent=self.widget_4)
        self.widget_6.setStyleSheet("border: None")
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_4.setContentsMargins(12, -1, 12, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_5 = QtWidgets.QFrame(parent=self.widget_6)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox = QtWidgets.QCheckBox(parent=self.frame_5)
        self.checkBox.setMinimumSize(QtCore.QSize(30, 30))
        self.checkBox.setStyleSheet("")
        self.checkBox.setText("")
        self.checkBox.setIconSize(QtCore.QSize(32, 32))
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_3.addWidget(self.checkBox, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label_8 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_8.setStyleSheet("color: rgb(254, 254, 255);\n"
"font: 63 12pt \"Segoe UI Semibold\";")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.verticalLayout_4.addWidget(self.frame_5)
        self.verticalLayout_8.addWidget(self.widget_6)
        self.verticalLayout.addWidget(self.widget_4, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.widget_3 = QtWidgets.QWidget(parent=self.widget)
        self.widget_3.setStyleSheet("border: None")
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_2 = QtWidgets.QFrame(parent=self.widget_3)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_9.setContentsMargins(30, 0, 30, 0)
        self.horizontalLayout_9.setSpacing(40)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButtonConfirm = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButtonConfirm.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButtonConfirm.setStyleSheet("border-radius: 8px;\n"
"font: 87 10pt \"Segoe UI Black\";\n"
"background-color: rgb(255, 235, 192);\n"
"color: rgb(0, 0, 0);")
        self.pushButtonConfirm.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonConfirm.setObjectName("pushButtonConfirm")
        self.horizontalLayout_9.addWidget(self.pushButtonConfirm)
        self.pushButtonLogOut = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButtonLogOut.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButtonLogOut.setStyleSheet("border-radius: 8px;\n"
"font: 87 10pt \"Segoe UI Black\";\n"
"background-color: rgb(255, 235, 192);\n"
"color: rgb(0, 0, 0);")
        self.pushButtonLogOut.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonLogOut.setObjectName("pushButtonLogOut")
        self.horizontalLayout_9.addWidget(self.pushButtonLogOut)
        self.horizontalLayout_8.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.widget_3)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_9.setText(_translate("Dialog", "  Please check and fill in your information to receive <br> incentives from Cinex."))
        self.label_2.setText(_translate("Dialog", "User Name:"))
        self.lineEditUserName.setPlaceholderText(_translate("Dialog", "Your User Name"))
        self.label_3.setText(_translate("Dialog", "Full Name:"))
        self.lineEditFullName.setPlaceholderText(_translate("Dialog", "Your Full Name"))
        self.label_7.setText(_translate("Dialog", "Birthday:"))
        self.lineEditBirthDay.setPlaceholderText(_translate("Dialog", "dd/mm/yyyy"))
        self.label_6.setText(_translate("Dialog", "Phone:"))
        self.label_5.setText(_translate("Dialog", "Email:"))
        self.label_8.setText(_translate("Dialog", "\n"
"Customers have agreed to the terms and conditions <br> of Cinex membership"))
        self.pushButtonConfirm.setText(_translate("Dialog", "Confirm"))
        self.pushButtonLogOut.setText(_translate("Dialog", "Log Out"))
