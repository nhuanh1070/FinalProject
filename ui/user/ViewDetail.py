# Form implementation generated from reading ui file 'D:\FinalProject\FinalProject\ui\user\ViewDetail.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(984, 667)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(984, 667))
        Dialog.setMaximumSize(QtCore.QSize(984, 667))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Logo/images/Logo/Movie_logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color:  rgb(83, 9, 11);")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_2 = QtWidgets.QWidget(parent=self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(316, 0))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setContentsMargins(9, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(parent=self.widget_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_poster = QtWidgets.QLabel(parent=self.frame_4)
        self.label_poster.setMinimumSize(QtCore.QSize(287, 400))
        self.label_poster.setMaximumSize(QtCore.QSize(287, 400))
        self.label_poster.setText("")
        self.label_poster.setPixmap(QtGui.QPixmap(":/Poster/images/Poster/Avatar.jpg"))
        self.label_poster.setScaledContents(True)
        self.label_poster.setObjectName("label_poster")
        self.verticalLayout_3.addWidget(self.label_poster)
        self.verticalLayout.addWidget(self.frame_4, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.frame = QtWidgets.QFrame(parent=self.widget_2)
        self.frame.setStyleSheet("border: none\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pushButtonBuyTickets = QtWidgets.QPushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonBuyTickets.sizePolicy().hasHeightForWidth())
        self.pushButtonBuyTickets.setSizePolicy(sizePolicy)
        self.pushButtonBuyTickets.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButtonBuyTickets.setStyleSheet("font: 87 16pt \"Segoe UI Black\";\n"
"color: rgb(254, 254, 255);\n"
"background-color: rgb(251, 190, 20);\n"
"border-radius: 10px;")
        self.pushButtonBuyTickets.setObjectName("pushButtonBuyTickets")
        self.verticalLayout_8.addWidget(self.pushButtonBuyTickets)
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setMinimumSize(QtCore.QSize(271, 151))
        self.label.setMaximumSize(QtCore.QSize(271, 151))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/slogan/images/Welcome/slogan.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout_8.addWidget(self.label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout.addWidget(self.widget_2)
        self.widget_4 = QtWidgets.QWidget(parent=self.widget)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_6 = QtWidgets.QWidget(parent=self.widget_4)
        self.widget_6.setStyleSheet("border: none")
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_5 = QtWidgets.QFrame(parent=self.widget_6)
        self.frame_5.setStyleSheet("font: 87 30pt \"Segoe UI Black\";\n"
"color: rgb(254, 254, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_title = QtWidgets.QLabel(parent=self.frame_5)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_7.addWidget(self.label_title)
        self.verticalLayout_6.addWidget(self.frame_5)
        self.frame_7 = QtWidgets.QFrame(parent=self.widget_6)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(parent=self.frame_7)
        self.label_8.setMaximumSize(QtCore.QSize(24, 24))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/WhiteIcons/images/icons/WhiteIcons/tag_ic.svg"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.label_genre = QtWidgets.QLabel(parent=self.frame_7)
        self.label_genre.setStyleSheet("font: 75  12pt \"Segoe UI Variable Display\";\n"
"color: rgb(254, 254, 255);")
        self.label_genre.setObjectName("label_genre")
        self.horizontalLayout_5.addWidget(self.label_genre)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout_6.addWidget(self.frame_7)
        self.frame_15 = QtWidgets.QFrame(parent=self.widget_6)
        self.frame_15.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_24 = QtWidgets.QLabel(parent=self.frame_15)
        self.label_24.setMaximumSize(QtCore.QSize(24, 24))
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap(":/WhiteIcons/images/icons/WhiteIcons/clock_ic.svg"))
        self.label_24.setScaledContents(True)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_13.addWidget(self.label_24)
        self.label_duration = QtWidgets.QLabel(parent=self.frame_15)
        self.label_duration.setStyleSheet("font: 75  12pt \"Segoe UI Variable Display\";\n"
"color: rgb(254, 254, 255);")
        self.label_duration.setObjectName("label_duration")
        self.horizontalLayout_13.addWidget(self.label_duration)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem1)
        self.verticalLayout_6.addWidget(self.frame_15)
        self.frame_14 = QtWidgets.QFrame(parent=self.widget_6)
        self.frame_14.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_22 = QtWidgets.QLabel(parent=self.frame_14)
        self.label_22.setMaximumSize(QtCore.QSize(24, 24))
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap(":/WhiteIcons/images/icons/WhiteIcons/globe_ic.svg"))
        self.label_22.setScaledContents(True)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_12.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(parent=self.frame_14)
        self.label_23.setStyleSheet("font: 75  12pt \"Segoe UI Variable Display\";\n"
"color: rgb(254, 254, 255);")
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_12.addWidget(self.label_23)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem2)
        self.verticalLayout_6.addWidget(self.frame_14)
        self.frame_13 = QtWidgets.QFrame(parent=self.widget_6)
        self.frame_13.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_20 = QtWidgets.QLabel(parent=self.frame_13)
        self.label_20.setMaximumSize(QtCore.QSize(24, 24))
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap(":/WhiteIcons/images/icons/WhiteIcons/message_ic.svg"))
        self.label_20.setScaledContents(True)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_11.addWidget(self.label_20)
        self.label_language = QtWidgets.QLabel(parent=self.frame_13)
        self.label_language.setStyleSheet("font: 75  12pt \"Segoe UI Variable Display\";\n"
"color: rgb(254, 254, 255);")
        self.label_language.setObjectName("label_language")
        self.horizontalLayout_11.addWidget(self.label_language)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem3)
        self.verticalLayout_6.addWidget(self.frame_13)
        self.frame_8 = QtWidgets.QFrame(parent=self.widget_6)
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_10 = QtWidgets.QLabel(parent=self.frame_8)
        self.label_10.setMaximumSize(QtCore.QSize(24, 24))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/WhiteIcons/images/icons/WhiteIcons/user_check_ic.svg"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.label_rating = QtWidgets.QLabel(parent=self.frame_8)
        self.label_rating.setStyleSheet("font: 75  12pt \"Segoe UI Variable Display\";\n"
"color: rgb(254, 254, 255);\n"
"")
        self.label_rating.setWordWrap(False)
        self.label_rating.setObjectName("label_rating")
        self.horizontalLayout_6.addWidget(self.label_rating)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout_6.addWidget(self.frame_8)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.widget_3 = QtWidgets.QWidget(parent=self.widget_4)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_2 = QtWidgets.QFrame(parent=self.widget_3)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_4.setStyleSheet("font: 87 16pt \"Segoe UI Black\";\n"
"color: rgb(254, 254, 255);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.textEditMovieContent = QtWidgets.QTextEdit(parent=self.frame_2)
        self.textEditMovieContent.setStyleSheet("background-color: rgb(250, 243, 224);\n"
"color: rgb(92, 64, 51);\n"
"font: 75  14pt \"Segoe UI Variable Display\";")
        self.textEditMovieContent.setObjectName("textEditMovieContent")
        self.verticalLayout_5.addWidget(self.textEditMovieContent)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.horizontalLayout.addWidget(self.widget_4)
        self.horizontalLayout_2.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Movie Details"))
        self.pushButtonBuyTickets.setText(_translate("Dialog", "BUY TICKETS"))
        self.label_title.setText(_translate("Dialog", "AVATAR: THE WAY OF WATER"))
        self.label_genre.setText(_translate("Dialog", "Comedy"))
        self.label_duration.setText(_translate("Dialog", "137\'"))
        self.label_23.setText(_translate("Dialog", "Other"))
        self.label_language.setText(_translate("Dialog", "VN"))
        self.label_rating.setText(_translate("Dialog", "T18: Movies are allowed to be disseminated to viewers aged 18 years and over (18+)"))
        self.label_4.setText(_translate("Dialog", "MOVIE CONTENT"))
        self.textEditMovieContent.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI Variable Display\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Set in 2154, </span><span style=\" font-size:12pt; font-style:italic;\">Avatar</span><span style=\" font-size:12pt;\"> follows </span><span style=\" font-size:12pt; font-weight:600;\">Jake Sully</span><span style=\" font-size:12pt;\">, a paralyzed ex-Marine, who joins the </span><span style=\" font-size:12pt; font-weight:600;\">Avatar Program</span><span style=\" font-size:12pt;\"> on the alien planet </span><span style=\" font-size:12pt; font-weight:600;\">Pandora</span><span style=\" font-size:12pt;\">. Humans are exploiting the planet’s resources, but the native </span><span style=\" font-size:12pt; font-weight:600;\">Na\'vi</span><span style=\" font-size:12pt;\"> fiercely protect their land. Through his </span><span style=\" font-size:12pt; font-weight:600;\">Avatar</span><span style=\" font-size:12pt;\">, Jake integrates into Na\'vi society and falls in love with </span><span style=\" font-size:12pt; font-weight:600;\">Neytiri</span><span style=\" font-size:12pt;\">.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">As tensions rise, humans, led by </span><span style=\" font-size:12pt; font-weight:600;\">Colonel Quaritch</span><span style=\" font-size:12pt;\">, launch an attack to seize Pandora’s resources. Jake switches sides, fights for the Na\'vi, and ultimately leaves his human body to live permanently as a Na\'vi. The film is known for its stunning visuals and strong environmental message.</span></p></body></html>"))
