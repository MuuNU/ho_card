# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RCWCRHEy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(680, 460)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(680, 460))
        MainWindow.setMaximumSize(QSize(680, 460))
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(50)
        sizePolicy1.setVerticalStretch(50)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setBaseSize(QSize(0, 0))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 382, 401))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_7.setFont(font1)
        self.label_7.setAcceptDrops(False)
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.UN_Name_Line = QLineEdit(self.layoutWidget)
        self.UN_Name_Line.setObjectName(u"UN_Name_Line")

        self.horizontalLayout.addWidget(self.UN_Name_Line)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.RC_Login_Line = QLineEdit(self.layoutWidget)
        self.RC_Login_Line.setObjectName(u"RC_Login_Line")

        self.horizontalLayout_2.addWidget(self.RC_Login_Line)

        self.RC_Login_CheckBox = QCheckBox(self.layoutWidget)
        self.RC_Login_CheckBox.setObjectName(u"RC_Login_CheckBox")

        self.horizontalLayout_2.addWidget(self.RC_Login_CheckBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.RC_Pass_Line = QLineEdit(self.layoutWidget)
        self.RC_Pass_Line.setObjectName(u"RC_Pass_Line")

        self.horizontalLayout_3.addWidget(self.RC_Pass_Line)

        self.RC_Password_checkBox = QCheckBox(self.layoutWidget)
        self.RC_Password_checkBox.setObjectName(u"RC_Password_checkBox")

        self.horizontalLayout_3.addWidget(self.RC_Password_checkBox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.RC_Group_comboBox = QComboBox(self.layoutWidget)
        self.RC_Group_comboBox.setObjectName(u"RC_Group_comboBox")
        self.RC_Group_comboBox.setEnabled(True)

        self.horizontalLayout_7.addWidget(self.RC_Group_comboBox)

        self.RC_Add_Button = QPushButton(self.layoutWidget)
        self.RC_Add_Button.setObjectName(u"RC_Add_Button")

        self.horizontalLayout_7.addWidget(self.RC_Add_Button)

        self.RC_Delete_Button = QPushButton(self.layoutWidget)
        self.RC_Delete_Button.setObjectName(u"RC_Delete_Button")

        self.horizontalLayout_7.addWidget(self.RC_Delete_Button)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.RC_Groups_List = QListWidget(self.layoutWidget)
        self.RC_Groups_List.setObjectName(u"RC_Groups_List")

        self.verticalLayout.addWidget(self.RC_Groups_List)

        self.RC_Create_Button = QPushButton(self.layoutWidget)
        self.RC_Create_Button.setObjectName(u"RC_Create_Button")

        self.verticalLayout.addWidget(self.RC_Create_Button)

        self.RC_Status_Label = QLabel(self.layoutWidget)
        self.RC_Status_Label.setObjectName(u"RC_Status_Label")

        self.verticalLayout.addWidget(self.RC_Status_Label)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(400, 10, 21, 401))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.Overall_Status = QLabel(self.centralwidget)
        self.Overall_Status.setObjectName(u"Overall_Status")
        self.Overall_Status.setGeometry(QRect(10, 430, 651, 16))
        self.Overall_Status.setFont(font1)
        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(10, 410, 651, 16))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(431, 12, 231, 401))
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setAcceptDrops(False)
        self.label_9.setScaledContents(False)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_9)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_9.addWidget(self.label_13)

        self.RD_Domain_ComboBox = QComboBox(self.widget)
        self.RD_Domain_ComboBox.setObjectName(u"RD_Domain_ComboBox")

        self.horizontalLayout_9.addWidget(self.RD_Domain_ComboBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.RD_Login_Line = QLineEdit(self.widget)
        self.RD_Login_Line.setObjectName(u"RD_Login_Line")

        self.horizontalLayout_4.addWidget(self.RD_Login_Line)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.RD_Password_Line = QLineEdit(self.widget)
        self.RD_Password_Line.setObjectName(u"RD_Password_Line")

        self.horizontalLayout_5.addWidget(self.RD_Password_Line)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setAcceptDrops(False)
        self.label_12.setScaledContents(False)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_12)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_6.addWidget(self.label_10)

        self.EM_Line = QLineEdit(self.widget)
        self.EM_Line.setObjectName(u"EM_Line")

        self.horizontalLayout_6.addWidget(self.EM_Line)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_8.addWidget(self.label_11)

        self.EM_Pass_Line = QLineEdit(self.widget)
        self.EM_Pass_Line.setObjectName(u"EM_Pass_Line")

        self.horizontalLayout_8.addWidget(self.EM_Pass_Line)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.EM_Create_Button = QPushButton(self.widget)
        self.EM_Create_Button.setObjectName(u"EM_Create_Button")

        self.verticalLayout_3.addWidget(self.EM_Create_Button)

        self.Email_Status = QLabel(self.widget)
        self.Email_Status.setObjectName(u"Email_Status")

        self.verticalLayout_3.addWidget(self.Email_Status)

        self.line_3 = QFrame(self.widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_3)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)
        self.label_15.setAcceptDrops(False)
        self.label_15.setScaledContents(False)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_15)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_17 = QLabel(self.widget)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_11.addWidget(self.label_17)

        self.SIP_Line = QLineEdit(self.widget)
        self.SIP_Line.setObjectName(u"SIP_Line")

        self.horizontalLayout_11.addWidget(self.SIP_Line)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_18 = QLabel(self.widget)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_12.addWidget(self.label_18)

        self.SIP_Pass_Line = QLineEdit(self.widget)
        self.SIP_Pass_Line.setObjectName(u"SIP_Pass_Line")

        self.horizontalLayout_12.addWidget(self.SIP_Pass_Line)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.Create_Excel_File = QPushButton(self.widget)
        self.Create_Excel_File.setObjectName(u"Create_Excel_File")

        self.verticalLayout_5.addWidget(self.Create_Excel_File)

        self.Excel_Status = QLabel(self.widget)
        self.Excel_Status.setObjectName(u"Excel_Status")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Excel_Status.sizePolicy().hasHeightForWidth())
        self.Excel_Status.setSizePolicy(sizePolicy2)
        self.Excel_Status.setMaximumSize(QSize(16777215, 13))

        self.verticalLayout_5.addWidget(self.Excel_Status)

        MainWindow.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.UN_Name_Line)
        self.label_2.setBuddy(self.RC_Login_Line)
        self.label_3.setBuddy(self.RC_Pass_Line)
        self.label_8.setBuddy(self.RC_Group_comboBox)
        self.label_13.setBuddy(self.RC_Login_Line)
        self.label_5.setBuddy(self.RC_Login_Line)
        self.label_6.setBuddy(self.RC_Login_Line)
        self.label_10.setBuddy(self.RC_Login_Line)
        self.label_11.setBuddy(self.RC_Login_Line)
        self.label_17.setBuddy(self.RC_Login_Line)
        self.label_18.setBuddy(self.RC_Login_Line)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.RC_Login_Line, self.RC_Pass_Line)
        QWidget.setTabOrder(self.RC_Pass_Line, self.RC_Password_checkBox)
        QWidget.setTabOrder(self.RC_Password_checkBox, self.RC_Login_CheckBox)
        QWidget.setTabOrder(self.RC_Login_CheckBox, self.UN_Name_Line)
        QWidget.setTabOrder(self.UN_Name_Line, self.RC_Create_Button)
        QWidget.setTabOrder(self.RC_Create_Button, self.RC_Group_comboBox)
        QWidget.setTabOrder(self.RC_Group_comboBox, self.RC_Delete_Button)
        QWidget.setTabOrder(self.RC_Delete_Button, self.RC_Groups_List)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Rocket Chat", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.UN_Name_Line.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.RC_Login_CheckBox.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.RC_Password_checkBox.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Select group", None))
        self.RC_Add_Button.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.RC_Delete_Button.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.RC_Create_Button.setText(QCoreApplication.translate("MainWindow", u"Create Rocket-Chat account", None))
        self.RC_Status_Label.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.Overall_Status.setText(QCoreApplication.translate("MainWindow", u"Overall status", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Remote Desktop", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Domain:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Login:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"E-Mail", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.EM_Create_Button.setText(QCoreApplication.translate("MainWindow", u"Create E-Mail", None))
        self.Email_Status.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Line 24", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Sip extension", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.Create_Excel_File.setText(QCoreApplication.translate("MainWindow", u"Create Excel Card", None))
        self.Excel_Status.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
    # retranslateUi

