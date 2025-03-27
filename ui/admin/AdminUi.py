# Form implementation generated from reading ui file 'D:\FinalProject\FinalProject\ui\admin\AdminUi.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 650)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 650))
        MainWindow.setMaximumSize(QtCore.QSize(1149, 773))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Logo/images/Logo/group_lg.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1000, 650))
        self.centralwidget.setMaximumSize(QtCore.QSize(1000, 650))
        self.centralwidget.setStyleSheet("* {\n"
"    color: #000;\n"
"}\n"
"#frame_8{\n"
"    background-color:#fbbe14;\n"
"}\n"
"#centralwidget, #tab_MovieManagement{\n"
"    background-color: #fdfdfa;\n"
"}\n"
"QLineEdit {\n"
"    background: transparent;\n"
"    color: #7c000b;\n"
"}\n"
"#searchMoiveName {\n"
"    border-radius: 3px;\n"
"    border: 2px solid #7c000b;\n"
"}\n"
"#appHeader {\n"
"    color: #7c000b;\n"
"}\n"
"\n"
"#pushButton, #pushButton_2 {\n"
"    background-color: #7c000b;\n"
"    color: #fff;\n"
"    border-radius: 10px;\n"
"}\n"
"#widget_4, #widget_5, #frame_12, #widget_6 {\n"
"    background-color: #fefeff;\n"
"    border-radius: 20px;\n"
"}\n"
"#headerFrame {\n"
"    background-color: #fefeff;\n"
"}\n"
"\n"
"QPushButton {\n"
"    padding: 10px 5px;\n"
"    text-align: left;\n"
"}\n"
"#pushButtonDelete, #pushButtonEdit, #pushButtonCreate, #pushButtonDetails {\n"
"    background-color: #7c000b;\n"
"    color: #fff;\n"
"    border-radius: 10px;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(1000, 650))
        self.tabWidget.setMaximumSize(QtCore.QSize(1000, 650))
        self.tabWidget.setBaseSize(QtCore.QSize(1148, 773))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.West)
        self.tabWidget.setIconSize(QtCore.QSize(35, 35))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_MovieManagement = QtWidgets.QWidget()
        self.tab_MovieManagement.setMinimumSize(QtCore.QSize(1000, 650))
        self.tab_MovieManagement.setMaximumSize(QtCore.QSize(1000, 650))
        self.tab_MovieManagement.setStyleSheet("")
        self.tab_MovieManagement.setObjectName("tab_MovieManagement")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_MovieManagement)
        self.gridLayout.setContentsMargins(0, 0, 24, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.mainBody = QtWidgets.QWidget(parent=self.tab_MovieManagement)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy)
        self.mainBody.setMinimumSize(QtCore.QSize(1000, 650))
        self.mainBody.setMaximumSize(QtCore.QSize(1000, 650))
        self.mainBody.setStyleSheet("")
        self.mainBody.setObjectName("mainBody")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainBody)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerFrame = QtWidgets.QWidget(parent=self.mainBody)
        self.headerFrame.setMinimumSize(QtCore.QSize(1000, 64))
        self.headerFrame.setMaximumSize(QtCore.QSize(1000, 64))
        self.headerFrame.setObjectName("headerFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.headerFrame)
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 10)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_2 = QtWidgets.QWidget(parent=self.headerFrame)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.appHeader = QtWidgets.QLabel(parent=self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.appHeader.setFont(font)
        self.appHeader.setStyleSheet("font: 87 16pt \"Segoe UI Black\";")
        self.appHeader.setObjectName("appHeader")
        self.horizontalLayout_3.addWidget(self.appHeader)
        self.horizontalLayout_2.addWidget(self.widget_2, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.widget_4 = QtWidgets.QWidget(parent=self.headerFrame)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Account_btn = QtWidgets.QPushButton(parent=self.widget_4)
        self.Account_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/Nhu Anh/.designer/images/icons/RedIcons/user_ic.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Account_btn.setIcon(icon1)
        self.Account_btn.setIconSize(QtCore.QSize(32, 32))
        self.Account_btn.setObjectName("Account_btn")
        self.horizontalLayout_6.addWidget(self.Account_btn)
        self.horizontalLayout_2.addWidget(self.widget_4, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout.addWidget(self.headerFrame)
        self.mainFrame = QtWidgets.QWidget(parent=self.mainBody)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy)
        self.mainFrame.setMinimumSize(QtCore.QSize(1000, 580))
        self.mainFrame.setMaximumSize(QtCore.QSize(1000, 580))
        self.mainFrame.setObjectName("mainFrame")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.mainFrame)
        self.horizontalLayout_12.setContentsMargins(0, 0, 9, 0)
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.widget_5 = QtWidgets.QWidget(parent=self.mainFrame)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_5.setMaximumSize(QtCore.QSize(800, 550))
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_5 = QtWidgets.QFrame(parent=self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.frame_5.setFont(font)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_14 = QtWidgets.QLabel(parent=self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("font: 87 16pt \"Segoe UI Black\";")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_13.addWidget(self.label_14, 0, QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.verticalLayout_6.addWidget(self.frame_5)
        self.searchMoiveName = QtWidgets.QFrame(parent=self.widget_5)
        self.searchMoiveName.setMinimumSize(QtCore.QSize(190, 0))
        self.searchMoiveName.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.searchMoiveName.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.searchMoiveName.setObjectName("searchMoiveName")
        self.horizontalLayout_54 = QtWidgets.QHBoxLayout(self.searchMoiveName)
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName("horizontalLayout_54")
        self.label_54 = QtWidgets.QLabel(parent=self.searchMoiveName)
        self.label_54.setMinimumSize(QtCore.QSize(32, 32))
        self.label_54.setMaximumSize(QtCore.QSize(32, 32))
        self.label_54.setText("")
        self.label_54.setPixmap(QtGui.QPixmap(":/RedIcons/images/icons/RedIcons/search_ic.svg"))
        self.label_54.setScaledContents(True)
        self.label_54.setObjectName("label_54")
        self.horizontalLayout_54.addWidget(self.label_54)
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=self.searchMoiveName)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(0, 15))
        self.lineEdit_6.setMaximumSize(QtCore.QSize(16777215, 32))
        self.lineEdit_6.setStyleSheet("background-color: rgb(254, 254, 255);\n"
"font: 12pt \"Sans Serif Collection\";")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_54.addWidget(self.lineEdit_6)
        self.verticalLayout_6.addWidget(self.searchMoiveName)
        self.tableWidget = QtWidgets.QTableWidget(parent=self.widget_5)
        self.tableWidget.setMinimumSize(QtCore.QSize(600, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget.setStyleSheet("background-color: rgb(254, 254, 255);\n"
"font: 75 bold 10pt \"MS Shell Dlg 2\";")
        self.tableWidget.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhUppercaseOnly)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(97)
        self.verticalLayout_6.addWidget(self.tableWidget)
        self.horizontalLayout_12.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(parent=self.mainFrame)
        self.widget_6.setMinimumSize(QtCore.QSize(0, 500))
        self.widget_6.setMaximumSize(QtCore.QSize(16777215, 550))
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_7.setContentsMargins(-1, -1, 15, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_14 = QtWidgets.QFrame(parent=self.widget_6)
        self.frame_14.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.frame_6 = QtWidgets.QFrame(parent=self.frame_14)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_15 = QtWidgets.QLabel(parent=self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("font: 87 14pt \"Segoe UI Black\";")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_14.addWidget(self.label_15)
        self.horizontalLayout_18.addWidget(self.frame_6)
        self.verticalLayout_7.addWidget(self.frame_14)
        self.frame_13 = QtWidgets.QFrame(parent=self.widget_6)
        self.frame_13.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.frame_7 = QtWidgets.QFrame(parent=self.frame_13)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pushButtonDetails = QtWidgets.QPushButton(parent=self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonDetails.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/WhiteIcons/images/icons/WhiteIcons/details_ic.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonDetails.setIcon(icon2)
        self.pushButtonDetails.setIconSize(QtCore.QSize(32, 32))
        self.pushButtonDetails.setObjectName("pushButtonDetails")
        self.verticalLayout_8.addWidget(self.pushButtonDetails)
        self.pushButtonDelete = QtWidgets.QPushButton(parent=self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonDelete.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/WhiteIcons/images/icons/WhiteIcons/delete_ic.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonDelete.setIcon(icon3)
        self.pushButtonDelete.setIconSize(QtCore.QSize(32, 32))
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.verticalLayout_8.addWidget(self.pushButtonDelete)
        self.pushButtonEdit = QtWidgets.QPushButton(parent=self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonEdit.setFont(font)
        self.pushButtonEdit.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/WhiteIcons/images/icons/WhiteIcons/edit_ic.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonEdit.setIcon(icon4)
        self.pushButtonEdit.setIconSize(QtCore.QSize(32, 32))
        self.pushButtonEdit.setCheckable(False)
        self.pushButtonEdit.setObjectName("pushButtonEdit")
        self.verticalLayout_8.addWidget(self.pushButtonEdit)
        self.pushButtonCreate = QtWidgets.QPushButton(parent=self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonCreate.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/WhiteIcons/images/icons/WhiteIcons/create_ic.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonCreate.setIcon(icon5)
        self.pushButtonCreate.setIconSize(QtCore.QSize(32, 32))
        self.pushButtonCreate.setObjectName("pushButtonCreate")
        self.verticalLayout_8.addWidget(self.pushButtonCreate)
        self.horizontalLayout_17.addWidget(self.frame_7)
        self.verticalLayout_7.addWidget(self.frame_13, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.frame_15 = QtWidgets.QFrame(parent=self.widget_6)
        self.frame_15.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_16 = QtWidgets.QLabel(parent=self.frame_15)
        self.label_16.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("C:/Users/Nhu Anh/.designer/images/Admin/UEL_Logo.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_19.addWidget(self.label_16)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.horizontalLayout_19.addItem(spacerItem)
        self.label_22 = QtWidgets.QLabel(parent=self.frame_15)
        self.label_22.setMaximumSize(QtCore.QSize(50, 50))
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap("C:/Users/Nhu Anh/.designer/images/Admin/FIS_Logo.png"))
        self.label_22.setScaledContents(True)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_19.addWidget(self.label_22)
        self.verticalLayout_7.addWidget(self.frame_15)
        self.horizontalLayout_12.addWidget(self.widget_6, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.verticalLayout.addWidget(self.mainFrame)
        self.gridLayout.addWidget(self.mainBody, 0, 0, 1, 1)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Menu/images/icons_menu/cinema_ic.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tabWidget.addTab(self.tab_MovieManagement, icon6, "")
        self.tab_Revenue = QtWidgets.QWidget()
        self.tab_Revenue.setStyleSheet("    background-color: #fdfdfa;")
        self.tab_Revenue.setObjectName("tab_Revenue")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_Revenue)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(parent=self.tab_Revenue)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_9 = QtWidgets.QWidget(parent=self.widget)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.widget_8 = QtWidgets.QWidget(parent=self.widget_9)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(12)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.comboMonthYear = QtWidgets.QComboBox(parent=self.widget_8)
        self.comboMonthYear.setMinimumSize(QtCore.QSize(0, 32))
        self.comboMonthYear.setMaximumSize(QtCore.QSize(16777215, 32))
        self.comboMonthYear.setStyleSheet("background-color: rgb(254, 254, 255);\n"
"font: 75 bold 11pt \"MS Shell Dlg 2\";")
        self.comboMonthYear.setObjectName("comboMonthYear")
        self.horizontalLayout_5.addWidget(self.comboMonthYear)
        self.btnFilter = QtWidgets.QPushButton(parent=self.widget_8)
        self.btnFilter.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.btnFilter.setStyleSheet("border-radius: 12px;\n"
"font: 87 10pt \"Segoe UI Black\";\n"
"background-color: rgb(255, 235, 192);\n"
"color: rgb(0, 0, 0);")
        self.btnFilter.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/RedIcons/images/icons/RedIcons/filter_ic.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnFilter.setIcon(icon7)
        self.btnFilter.setIconSize(QtCore.QSize(32, 32))
        self.btnFilter.setObjectName("btnFilter")
        self.horizontalLayout_5.addWidget(self.btnFilter, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout_7.addWidget(self.widget_8, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.widget_7 = QtWidgets.QWidget(parent=self.widget_9)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblMovieRevenue = QtWidgets.QLabel(parent=self.widget_7)
        self.lblMovieRevenue.setMinimumSize(QtCore.QSize(0, 32))
        self.lblMovieRevenue.setStyleSheet("background-color: rgb(254, 254, 255);\n"
"font: 75 bold 11pt \"MS Shell Dlg 2\";\n"
"border-radius: 8px;")
        self.lblMovieRevenue.setObjectName("lblMovieRevenue")
        self.verticalLayout_2.addWidget(self.lblMovieRevenue)
        self.lblFoodRevenue = QtWidgets.QLabel(parent=self.widget_7)
        self.lblFoodRevenue.setMinimumSize(QtCore.QSize(0, 32))
        self.lblFoodRevenue.setStyleSheet("background-color: rgb(254, 254, 255);\n"
"font: 75 bold 11pt \"MS Shell Dlg 2\";\n"
"border-radius: 8px;")
        self.lblFoodRevenue.setObjectName("lblFoodRevenue")
        self.verticalLayout_2.addWidget(self.lblFoodRevenue)
        self.lblTotalRevenue = QtWidgets.QLabel(parent=self.widget_7)
        self.lblTotalRevenue.setMinimumSize(QtCore.QSize(0, 32))
        self.lblTotalRevenue.setStyleSheet("background-color: rgb(254, 254, 255);\n"
"font: 75 bold 11pt \"MS Shell Dlg 2\";\n"
"border-radius: 8px;")
        self.lblTotalRevenue.setObjectName("lblTotalRevenue")
        self.verticalLayout_2.addWidget(self.lblTotalRevenue)
        self.horizontalLayout_7.addWidget(self.widget_7)
        self.verticalLayout_3.addWidget(self.widget_9)
        self.widget_3 = QtWidgets.QWidget(parent=self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tableMovies = QtWidgets.QTableWidget(parent=self.widget_3)
        self.tableMovies.setStyleSheet("background-color: rgb(254, 254, 255);\n"
"font: 75 bold 10pt \"MS Shell Dlg 2\";")
        self.tableMovies.setObjectName("tableMovies")
        self.tableMovies.setColumnCount(0)
        self.tableMovies.setRowCount(0)
        self.horizontalLayout_4.addWidget(self.tableMovies)
        self.tableFoods = QtWidgets.QTableWidget(parent=self.widget_3)
        self.tableFoods.setStyleSheet("background-color: rgb(254, 254, 255);\n"
"font: 75 bold 10pt \"MS Shell Dlg 2\";")
        self.tableFoods.setObjectName("tableFoods")
        self.tableFoods.setColumnCount(0)
        self.tableFoods.setRowCount(0)
        self.horizontalLayout_4.addWidget(self.tableFoods)
        self.verticalLayout_3.addWidget(self.widget_3)
        self.gridLayout_2.addWidget(self.widget, 1, 0, 1, 1)
        self.widget_10 = QtWidgets.QWidget(parent=self.tab_Revenue)
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_10)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.headerFrame_2 = QtWidgets.QWidget(parent=self.widget_10)
        self.headerFrame_2.setMinimumSize(QtCore.QSize(1000, 64))
        self.headerFrame_2.setMaximumSize(QtCore.QSize(1000, 64))
        self.headerFrame_2.setObjectName("headerFrame_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.headerFrame_2)
        self.horizontalLayout_8.setContentsMargins(9, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.widget_11 = QtWidgets.QWidget(parent=self.headerFrame_2)
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.appHeader_2 = QtWidgets.QLabel(parent=self.widget_11)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.appHeader_2.setFont(font)
        self.appHeader_2.setStyleSheet("font: 87 16pt \"Segoe UI Black\";")
        self.appHeader_2.setObjectName("appHeader_2")
        self.horizontalLayout_9.addWidget(self.appHeader_2)
        self.horizontalLayout_8.addWidget(self.widget_11, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.widget_12 = QtWidgets.QWidget(parent=self.headerFrame_2)
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_12)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.Account_btn_2 = QtWidgets.QPushButton(parent=self.widget_12)
        self.Account_btn_2.setText("")
        self.Account_btn_2.setIcon(icon1)
        self.Account_btn_2.setIconSize(QtCore.QSize(32, 32))
        self.Account_btn_2.setObjectName("Account_btn_2")
        self.horizontalLayout_10.addWidget(self.Account_btn_2)
        self.horizontalLayout_8.addWidget(self.widget_12, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_4.addWidget(self.headerFrame_2)
        self.gridLayout_2.addWidget(self.widget_10, 0, 0, 1, 1)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/Menu/images/icons_menu/revenue_ic.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tabWidget.addTab(self.tab_Revenue, icon8, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Movie Magagement"))
        self.appHeader.setText(_translate("MainWindow", "MOVIE MANAGEMENT"))
        self.label_14.setText(_translate("MainWindow", "List of movies"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "Search movie name"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Genre"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Country"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Year"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Duration"))
        self.label_15.setText(_translate("MainWindow", "Functions"))
        self.pushButtonDetails.setText(_translate("MainWindow", "Details"))
        self.pushButtonDelete.setText(_translate("MainWindow", "Delete"))
        self.pushButtonEdit.setText(_translate("MainWindow", "Edit"))
        self.pushButtonCreate.setText(_translate("MainWindow", "Create"))
        self.lblMovieRevenue.setText(_translate("MainWindow", "TextLabel"))
        self.lblFoodRevenue.setText(_translate("MainWindow", "TextLabel"))
        self.lblTotalRevenue.setText(_translate("MainWindow", "TextLabel"))
        self.appHeader_2.setText(_translate("MainWindow", "CINEX CINEMA REVENUE"))
