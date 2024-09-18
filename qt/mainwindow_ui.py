# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QProgressBar, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QToolButton, QVBoxLayout, QWidget)
import resources_rc

class Ui_Nugget(object):
    def setupUi(self, Nugget):
        if not Nugget.objectName():
            Nugget.setObjectName(u"Nugget")
        Nugget.resize(1000, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Nugget.sizePolicy().hasHeightForWidth())
        Nugget.setSizePolicy(sizePolicy)
        Nugget.setMinimumSize(QSize(1000, 600))
        Nugget.setMaximumSize(QSize(1000, 600))
        Nugget.setWindowOpacity(1.000000000000000)
        Nugget.setStyleSheet(u"QWidget {\n"
"    color: #FFFFFF;\n"
"    background-color: transparent;\n"
"	spacing: 0px;\n"
"}\n"
"\n"
"QWidget:focus {\n"
"    outline: none;\n"
"}\n"
"\n"
"QWidget [cls=central] {\n"
"    background-color: #1e1e1e;\n"
"	border-radius: 0px;\n"
"	border: 1px solid #4B4B4B;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QToolButton {\n"
"    background-color: #3b3b3b;\n"
"    border: none;\n"
"    color: #e8e8e8;\n"
"    font-size: 14px;\n"
"	min-height: 35px;\n"
"	icon-size: 16px;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QToolButton[cls=sidebarBtn] {\n"
"    background-color: transparent;\n"
"	icon-size: 24px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #535353;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"    background-color: #2860ca;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QCheckBox {\n"
"	spacing: 8px;\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"QRadioButton {\n"
"	spacing: 8px;\n"
"	font-size: 14px;\n"
"}\n"
""
                        "\n"
"QLineEdit {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	color: #FFFFFF;\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background: transparent;\n"
"    width: 8px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    background: transparent;\n"
"    height: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    background: #3b3b3b;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:pressed {\n"
"    background: #535353;\n"
"}\n"
"\n"
"QScrollBar::add-line,\n"
"QScrollBar::sub-line {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page,\n"
"QScrollBar::sub-page {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    background-color: #3b3b3b;\n"
"    height: 4px;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: #535353;\n"
"    width: 8px;\n"
"    margin: -8px 0;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: #3b82f7;\n"
"}\n"
"\n"
"QSl"
                        "ider::tick:horizontal {\n"
"    background-color: #535353;\n"
"    width: 1px;\n"
"}\n"
"")
        self.centralwidget = QWidget(Nugget)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setContextMenuPolicy(Qt.NoContextMenu)
        self.centralwidget.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.verticalLayout_11 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.deviceBar = QWidget(self.centralwidget)
        self.deviceBar.setObjectName(u"deviceBar")
        self.horizontalLayout_4 = QHBoxLayout(self.deviceBar)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_2 = QWidget(self.deviceBar)
        self.horizontalWidget_2.setObjectName(u"horizontalWidget_2")
        self.horizontalWidget_2.setMinimumSize(QSize(300, 0))
        self.horizontalLayout_19 = QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_19.setSpacing(1)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_3 = QWidget(self.horizontalWidget_2)
        self.horizontalWidget_3.setObjectName(u"horizontalWidget_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.horizontalWidget_3.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_3.setSizePolicy(sizePolicy1)
        self.horizontalLayout_15 = QHBoxLayout(self.horizontalWidget_3)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.toolButton_6 = QToolButton(self.horizontalWidget_3)
        self.toolButton_6.setObjectName(u"toolButton_6")
        self.toolButton_6.setEnabled(False)
        self.toolButton_6.setStyleSheet(u"QToolButton {\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/phone.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_6.setIcon(icon)

        self.horizontalLayout_15.addWidget(self.toolButton_6)

        self.devicePicker = QComboBox(self.horizontalWidget_3)
        self.devicePicker.setObjectName(u"devicePicker")
        self.devicePicker.setStyleSheet(u"#devicePicker {\n"
"	background-color: #3b3b3b;\n"
"    border: none;\n"
"    color: #e8e8e8;\n"
"    font-size: 14px;\n"
"    min-height: 38px;\n"
"	min-width: 35px;\n"
"	padding-left: 8px;\n"
"}\n"
"\n"
"#devicePicker::drop-down {\n"
"    image: url(:/icon/caret-down-fill.svg);\n"
"	icon-size: 16px;\n"
"    subcontrol-position: right center;\n"
"	margin-right: 8px;\n"
"}\n"
"\n"
"#devicePicker QAbstractItemView {\n"
"	background-color: #3b3b3b;\n"
"    outline: none;\n"
"	margin-top: 1px;\n"
"}\n"
"\n"
"#devicePicker QAbstractItemView::item {\n"
"	background-color: #3b3b3b;\n"
"	color: #e8e8e8;\n"
"	min-height: 38px;\n"
"    padding-left: 8px;\n"
"}\n"
"\n"
"#devicePicker QAbstractItemView::item:hover {\n"
"    background-color: #535353;\n"
"    color: #ffffff;\n"
"}")
        self.devicePicker.setDuplicatesEnabled(True)

        self.horizontalLayout_15.addWidget(self.devicePicker)


        self.horizontalLayout_19.addWidget(self.horizontalWidget_3)

        self.refreshBtn = QToolButton(self.horizontalWidget_2)
        self.refreshBtn.setObjectName(u"refreshBtn")
        self.refreshBtn.setStyleSheet(u"QToolButton {\n"
"	border-radius: 0px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/arrow-clockwise.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshBtn.setIcon(icon1)
        self.refreshBtn.setCheckable(False)
        self.refreshBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.horizontalLayout_19.addWidget(self.refreshBtn)


        self.horizontalLayout_4.addWidget(self.horizontalWidget_2)

        self.titleBar = QToolButton(self.deviceBar)
        self.titleBar.setObjectName(u"titleBar")
        self.titleBar.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleBar.sizePolicy().hasHeightForWidth())
        self.titleBar.setSizePolicy(sizePolicy2)
        self.titleBar.setStyleSheet(u"QToolButton {\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.titleBar)


        self.verticalLayout_11.addWidget(self.deviceBar)

        self.body = QWidget(self.centralwidget)
        self.body.setObjectName(u"body")
        self.body.setMinimumSize(QSize(0, 20))
        self.horizontalLayout_18 = QHBoxLayout(self.body)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.sidebar = QWidget(self.body)
        self.sidebar.setObjectName(u"sidebar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.sidebar.sizePolicy().hasHeightForWidth())
        self.sidebar.setSizePolicy(sizePolicy3)
        self.sidebar.setMinimumSize(QSize(300, 0))
        self.sidebar.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.sidebar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 9, 9, 0)
        self.homePageBtn = QToolButton(self.sidebar)
        self.homePageBtn.setObjectName(u"homePageBtn")
        sizePolicy2.setHeightForWidth(self.homePageBtn.sizePolicy().hasHeightForWidth())
        self.homePageBtn.setSizePolicy(sizePolicy2)
        icon2 = QIcon()
        icon2.addFile(u":/icon/house.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homePageBtn.setIcon(icon2)
        self.homePageBtn.setCheckable(True)
        self.homePageBtn.setChecked(True)
        self.homePageBtn.setAutoExclusive(True)
        self.homePageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.homePageBtn)

        self.explorePageBtn = QToolButton(self.sidebar)
        self.explorePageBtn.setObjectName(u"explorePageBtn")
        self.explorePageBtn.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.explorePageBtn.sizePolicy().hasHeightForWidth())
        self.explorePageBtn.setSizePolicy(sizePolicy2)
        icon3 = QIcon()
        icon3.addFile(u":/icon/compass.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.explorePageBtn.setIcon(icon3)
        self.explorePageBtn.setCheckable(True)
        self.explorePageBtn.setAutoExclusive(True)
        self.explorePageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.explorePageBtn)

        self.locSimPageBtn = QToolButton(self.sidebar)
        self.locSimPageBtn.setObjectName(u"locSimPageBtn")
        sizePolicy2.setHeightForWidth(self.locSimPageBtn.sizePolicy().hasHeightForWidth())
        self.locSimPageBtn.setSizePolicy(sizePolicy2)
        icon4 = QIcon()
        icon4.addFile(u":/icon/geo-alt.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.locSimPageBtn.setIcon(icon4)
        self.locSimPageBtn.setCheckable(True)
        self.locSimPageBtn.setAutoExclusive(True)
        self.locSimPageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.locSimPageBtn)

        self.sidebarDiv1 = QFrame(self.sidebar)
        self.sidebarDiv1.setObjectName(u"sidebarDiv1")
        self.sidebarDiv1.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.sidebarDiv1.setFrameShadow(QFrame.Plain)
        self.sidebarDiv1.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.sidebarDiv1)

        self.customOperationsPageBtn = QToolButton(self.sidebar)
        self.customOperationsPageBtn.setObjectName(u"customOperationsPageBtn")
        sizePolicy2.setHeightForWidth(self.customOperationsPageBtn.sizePolicy().hasHeightForWidth())
        self.customOperationsPageBtn.setSizePolicy(sizePolicy2)
        icon5 = QIcon()
        icon5.addFile(u":/icon/pencil.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.customOperationsPageBtn.setIcon(icon5)
        self.customOperationsPageBtn.setCheckable(True)
        self.customOperationsPageBtn.setAutoExclusive(True)
        self.customOperationsPageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.customOperationsPageBtn)

        self.gestaltPageBtn = QToolButton(self.sidebar)
        self.gestaltPageBtn.setObjectName(u"gestaltPageBtn")
        sizePolicy2.setHeightForWidth(self.gestaltPageBtn.sizePolicy().hasHeightForWidth())
        self.gestaltPageBtn.setSizePolicy(sizePolicy2)
        icon6 = QIcon()
        icon6.addFile(u":/icon/iphone-island.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.gestaltPageBtn.setIcon(icon6)
        self.gestaltPageBtn.setIconSize(QSize(24, 28))
        self.gestaltPageBtn.setCheckable(True)
        self.gestaltPageBtn.setAutoExclusive(True)
        self.gestaltPageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.gestaltPageBtn.setArrowType(Qt.NoArrow)

        self.verticalLayout.addWidget(self.gestaltPageBtn)

        self.featureFlagsPageBtn = QToolButton(self.sidebar)
        self.featureFlagsPageBtn.setObjectName(u"featureFlagsPageBtn")
        sizePolicy2.setHeightForWidth(self.featureFlagsPageBtn.sizePolicy().hasHeightForWidth())
        self.featureFlagsPageBtn.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setFamilies([u".AppleSystemUIFont"])
        self.featureFlagsPageBtn.setFont(font)
        icon7 = QIcon()
        icon7.addFile(u":/icon/flag.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.featureFlagsPageBtn.setIcon(icon7)
        self.featureFlagsPageBtn.setCheckable(True)
        self.featureFlagsPageBtn.setAutoExclusive(True)
        self.featureFlagsPageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.featureFlagsPageBtn)

        self.euEnablerPageBtn = QToolButton(self.sidebar)
        self.euEnablerPageBtn.setObjectName(u"euEnablerPageBtn")
        sizePolicy2.setHeightForWidth(self.euEnablerPageBtn.sizePolicy().hasHeightForWidth())
        self.euEnablerPageBtn.setSizePolicy(sizePolicy2)
        self.euEnablerPageBtn.setIcon(icon4)
        self.euEnablerPageBtn.setCheckable(True)
        self.euEnablerPageBtn.setAutoExclusive(True)
        self.euEnablerPageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.euEnablerPageBtn)

        self.internalOptionsPageBtn = QToolButton(self.sidebar)
        self.internalOptionsPageBtn.setObjectName(u"internalOptionsPageBtn")
        sizePolicy2.setHeightForWidth(self.internalOptionsPageBtn.sizePolicy().hasHeightForWidth())
        self.internalOptionsPageBtn.setSizePolicy(sizePolicy2)
        icon8 = QIcon()
        icon8.addFile(u":/icon/hdd.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.internalOptionsPageBtn.setIcon(icon8)
        self.internalOptionsPageBtn.setCheckable(True)
        self.internalOptionsPageBtn.setAutoExclusive(True)
        self.internalOptionsPageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.internalOptionsPageBtn)

        self.sidebarDiv2 = QFrame(self.sidebar)
        self.sidebarDiv2.setObjectName(u"sidebarDiv2")
        self.sidebarDiv2.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.sidebarDiv2.setFrameShadow(QFrame.Plain)
        self.sidebarDiv2.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.sidebarDiv2)

        self.applyPageBtn = QToolButton(self.sidebar)
        self.applyPageBtn.setObjectName(u"applyPageBtn")
        sizePolicy2.setHeightForWidth(self.applyPageBtn.sizePolicy().hasHeightForWidth())
        self.applyPageBtn.setSizePolicy(sizePolicy2)
        icon9 = QIcon()
        icon9.addFile(u":/icon/check-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.applyPageBtn.setIcon(icon9)
        self.applyPageBtn.setCheckable(True)
        self.applyPageBtn.setAutoExclusive(True)
        self.applyPageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.applyPageBtn)

        self.settingsPageBtn = QToolButton(self.sidebar)
        self.settingsPageBtn.setObjectName(u"settingsPageBtn")
        sizePolicy2.setHeightForWidth(self.settingsPageBtn.sizePolicy().hasHeightForWidth())
        self.settingsPageBtn.setSizePolicy(sizePolicy2)
        icon10 = QIcon()
        icon10.addFile(u":/icon/gear.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsPageBtn.setIcon(icon10)
        self.settingsPageBtn.setCheckable(True)
        self.settingsPageBtn.setAutoExclusive(True)
        self.settingsPageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.settingsPageBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_18.addWidget(self.sidebar)

        self.main = QWidget(self.body)
        self.main.setObjectName(u"main")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy4)
        self._3 = QVBoxLayout(self.main)
        self._3.setSpacing(0)
        self._3.setObjectName(u"_3")
        self._3.setContentsMargins(9, 0, 0, 0)
        self.pages = QStackedWidget(self.main)
        self.pages.setObjectName(u"pages")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.verticalLayout_2 = QVBoxLayout(self.homePage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget = QWidget(self.homePage)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 9, 0, 9)
        self.toolButton_9 = QToolButton(self.horizontalWidget)
        self.toolButton_9.setObjectName(u"toolButton_9")
        self.toolButton_9.setEnabled(False)
        self.toolButton_9.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_9.setIcon(icon)

        self.horizontalLayout.addWidget(self.toolButton_9)

        self.verticalWidget = QWidget(self.horizontalWidget)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalLayout_3 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.phoneNameLbl = QLabel(self.verticalWidget)
        self.phoneNameLbl.setObjectName(u"phoneNameLbl")
        font1 = QFont()
        font1.setBold(False)
        self.phoneNameLbl.setFont(font1)

        self.verticalLayout_3.addWidget(self.phoneNameLbl)

        self.phoneVersionLbl = QLabel(self.verticalWidget)
        self.phoneVersionLbl.setObjectName(u"phoneVersionLbl")
        self.phoneVersionLbl.setCursor(QCursor(Qt.PointingHandCursor))
        self.phoneVersionLbl.setTextFormat(Qt.RichText)
        self.phoneVersionLbl.setOpenExternalLinks(False)

        self.verticalLayout_3.addWidget(self.phoneVersionLbl)


        self.horizontalLayout.addWidget(self.verticalWidget)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addWidget(self.horizontalWidget)

        self.line_4 = QFrame(self.homePage)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setFrameShape(QFrame.HLine)

        self.verticalLayout_2.addWidget(self.line_4)

        self.horizontalWidget1 = QWidget(self.homePage)
        self.horizontalWidget1.setObjectName(u"horizontalWidget1")
        self.horizontalLayout_27 = QHBoxLayout(self.horizontalWidget1)
        self.horizontalLayout_27.setSpacing(50)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_2)

        self.bigNuggetBtn = QToolButton(self.horizontalWidget1)
        self.bigNuggetBtn.setObjectName(u"bigNuggetBtn")
        self.bigNuggetBtn.setStyleSheet(u"QToolButton {\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/credits/big_nugget.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bigNuggetBtn.setIcon(icon11)
        self.bigNuggetBtn.setIconSize(QSize(150, 200))

        self.horizontalLayout_27.addWidget(self.bigNuggetBtn)

        self.verticalWidget1 = QWidget(self.horizontalWidget1)
        self.verticalWidget1.setObjectName(u"verticalWidget1")
        self.verticalLayout_26 = QVBoxLayout(self.verticalWidget1)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_11)

        self.label_2 = QLabel(self.verticalWidget1)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"QLabel {\n"
"	font-size: 35px;\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_2)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_12)

        self.discordBtn = QToolButton(self.verticalWidget1)
        self.discordBtn.setObjectName(u"discordBtn")
        icon12 = QIcon()
        icon12.addFile(u":/icon/discord.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.discordBtn.setIcon(icon12)
        self.discordBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_26.addWidget(self.discordBtn)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_4)


        self.horizontalLayout_27.addWidget(self.verticalWidget1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_12)


        self.verticalLayout_2.addWidget(self.horizontalWidget1)

        self.verticalWidget_2 = QWidget(self.homePage)
        self.verticalWidget_2.setObjectName(u"verticalWidget_2")
        self.verticalLayout_25 = QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_25.setSpacing(15)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 30, 0, 30)
        self.horizontalWidget2 = QWidget(self.verticalWidget_2)
        self.horizontalWidget2.setObjectName(u"horizontalWidget2")
        self.horizontalWidget2.setEnabled(True)
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalWidget2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.leminBtn = QToolButton(self.horizontalWidget2)
        self.leminBtn.setObjectName(u"leminBtn")
        self.leminBtn.setEnabled(True)
        self.leminBtn.setMinimumSize(QSize(150, 35))
        self.leminBtn.setStyleSheet(u"QToolButton {\n"
"	background: none;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/credits/LeminLimez.png", QSize(), QIcon.Normal, QIcon.Off)
        self.leminBtn.setIcon(icon13)
        self.leminBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_6.addWidget(self.leminBtn)

        self.leminTwitterBtn = QToolButton(self.horizontalWidget2)
        self.leminTwitterBtn.setObjectName(u"leminTwitterBtn")
        self.leminTwitterBtn.setStyleSheet(u"QToolButton {\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	background: none;\n"
"	border: 1px solid #3b3b3b;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #535353;\n"
"    color: #FFFFFF;\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/icon/twitter.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.leminTwitterBtn.setIcon(icon14)

        self.horizontalLayout_6.addWidget(self.leminTwitterBtn)

        self.leminKoFiBtn = QToolButton(self.horizontalWidget2)
        self.leminKoFiBtn.setObjectName(u"leminKoFiBtn")
        self.leminKoFiBtn.setStyleSheet(u"QToolButton {\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"	background: none;\n"
"	border: 1px solid #3b3b3b;\n"
"	border-left: none;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #535353;\n"
"    color: #FFFFFF;\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/icon/currency-dollar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.leminKoFiBtn.setIcon(icon15)

        self.horizontalLayout_6.addWidget(self.leminKoFiBtn)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.toolButton_14 = QToolButton(self.horizontalWidget2)
        self.toolButton_14.setObjectName(u"toolButton_14")
        self.toolButton_14.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.toolButton_14.sizePolicy().hasHeightForWidth())
        self.toolButton_14.setSizePolicy(sizePolicy2)
        self.toolButton_14.setStyleSheet(u"QToolButton {\n"
"	background: none;\n"
"}")

        self.horizontalLayout_6.addWidget(self.toolButton_14)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)


        self.verticalLayout_25.addWidget(self.horizontalWidget2)

        self.verticalSpacer_16 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_25.addItem(self.verticalSpacer_16)

        self.horizontalWidget_21 = QWidget(self.verticalWidget_2)
        self.horizontalWidget_21.setObjectName(u"horizontalWidget_21")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget_21)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.helpFromBtn = QToolButton(self.horizontalWidget_21)
        self.helpFromBtn.setObjectName(u"helpFromBtn")
        self.helpFromBtn.setEnabled(True)
        self.helpFromBtn.setMinimumSize(QSize(150, 35))
        self.helpFromBtn.setStyleSheet(u"QToolButton {\n"
"	background: none;\n"
"}")
        self.helpFromBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_2.addWidget(self.helpFromBtn)

        self.jjtechBtn = QToolButton(self.horizontalWidget_21)
        self.jjtechBtn.setObjectName(u"jjtechBtn")
        sizePolicy2.setHeightForWidth(self.jjtechBtn.sizePolicy().hasHeightForWidth())
        self.jjtechBtn.setSizePolicy(sizePolicy2)
        self.jjtechBtn.setMinimumSize(QSize(0, 37))
        self.jjtechBtn.setStyleSheet(u"QToolButton {\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	background: none;\n"
"	border: 1px solid #3b3b3b;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #535353;\n"
"    color: #FFFFFF;\n"
"}")

        self.horizontalLayout_2.addWidget(self.jjtechBtn)

        self.disfordottieBtn = QToolButton(self.horizontalWidget_21)
        self.disfordottieBtn.setObjectName(u"disfordottieBtn")
        sizePolicy2.setHeightForWidth(self.disfordottieBtn.sizePolicy().hasHeightForWidth())
        self.disfordottieBtn.setSizePolicy(sizePolicy2)
        self.disfordottieBtn.setMinimumSize(QSize(0, 37))
        self.disfordottieBtn.setStyleSheet(u"QToolButton {\n"
"	border-radius: 0px;\n"
"	background: none;\n"
"	border: 1px solid #3b3b3b;\n"
"	border-left: none;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #535353;\n"
"    color: #FFFFFF;\n"
"}")

        self.horizontalLayout_2.addWidget(self.disfordottieBtn)

        self.lrdsnowBtn = QToolButton(self.horizontalWidget_21)
        self.lrdsnowBtn.setObjectName(u"lrdsnowBtn")
        sizePolicy2.setHeightForWidth(self.lrdsnowBtn.sizePolicy().hasHeightForWidth())
        self.lrdsnowBtn.setSizePolicy(sizePolicy2)
        self.lrdsnowBtn.setMinimumSize(QSize(0, 37))
        self.lrdsnowBtn.setStyleSheet(u"QToolButton {\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"	background: none;\n"
"	border: 1px solid #3b3b3b;\n"
"	border-left: none;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #535353;\n"
"    color: #FFFFFF;\n"
"}")

        self.horizontalLayout_2.addWidget(self.lrdsnowBtn)


        self.verticalLayout_25.addWidget(self.horizontalWidget_21)

        self.horizontalWidget3 = QWidget(self.verticalWidget_2)
        self.horizontalWidget3.setObjectName(u"horizontalWidget3")
        self.horizontalLayout_24 = QHBoxLayout(self.horizontalWidget3)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.toolButton_15 = QToolButton(self.horizontalWidget3)
        self.toolButton_15.setObjectName(u"toolButton_15")
        self.toolButton_15.setEnabled(False)
        self.toolButton_15.setMinimumSize(QSize(150, 35))
        self.toolButton_15.setStyleSheet(u"QToolButton {\n"
"	background: none;\n"
"}")

        self.horizontalLayout_24.addWidget(self.toolButton_15)

        self.libiBtn = QToolButton(self.horizontalWidget3)
        self.libiBtn.setObjectName(u"libiBtn")
        sizePolicy2.setHeightForWidth(self.libiBtn.sizePolicy().hasHeightForWidth())
        self.libiBtn.setSizePolicy(sizePolicy2)
        self.libiBtn.setStyleSheet(u"QToolButton {\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	background: none;\n"
"	border: 1px solid #3b3b3b;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #535353;\n"
"    color: #FFFFFF;\n"
"}")

        self.horizontalLayout_24.addWidget(self.libiBtn)

        self.qtBtn = QToolButton(self.horizontalWidget3)
        self.qtBtn.setObjectName(u"qtBtn")
        sizePolicy2.setHeightForWidth(self.qtBtn.sizePolicy().hasHeightForWidth())
        self.qtBtn.setSizePolicy(sizePolicy2)
        self.qtBtn.setStyleSheet(u"QToolButton {\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"	background: none;\n"
"	border: 1px solid #3b3b3b;\n"
"	border-left: none;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #535353;\n"
"    color: #FFFFFF;\n"
"}")

        self.horizontalLayout_24.addWidget(self.qtBtn)


        self.verticalLayout_25.addWidget(self.horizontalWidget3)


        self.verticalLayout_2.addWidget(self.verticalWidget_2)

        self.label = QLabel(self.homePage)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.pages.addWidget(self.homePage)
        self.explorePage = QWidget()
        self.explorePage.setObjectName(u"explorePage")
        self.verticalLayout_31 = QVBoxLayout(self.explorePage)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.explorePageHeader = QWidget(self.explorePage)
        self.explorePageHeader.setObjectName(u"explorePageHeader")
        self.horizontalLayout_31 = QHBoxLayout(self.explorePageHeader)
        self.horizontalLayout_31.setSpacing(10)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, -1, 0, -1)
        self.toolButton_16 = QToolButton(self.explorePageHeader)
        self.toolButton_16.setObjectName(u"toolButton_16")
        self.toolButton_16.setEnabled(False)
        self.toolButton_16.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_16.setIcon(icon3)

        self.horizontalLayout_31.addWidget(self.toolButton_16)

        self.verticalWidget_9 = QWidget(self.explorePageHeader)
        self.verticalWidget_9.setObjectName(u"verticalWidget_9")
        self.verticalLayout_30 = QVBoxLayout(self.verticalWidget_9)
        self.verticalLayout_30.setSpacing(6)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.exploreLbl = QLabel(self.verticalWidget_9)
        self.exploreLbl.setObjectName(u"exploreLbl")
        self.exploreLbl.setFont(font1)

        self.verticalLayout_30.addWidget(self.exploreLbl)

        self.exploreSubLbl = QLabel(self.verticalWidget_9)
        self.exploreSubLbl.setObjectName(u"exploreSubLbl")

        self.verticalLayout_30.addWidget(self.exploreSubLbl)


        self.horizontalLayout_31.addWidget(self.verticalWidget_9)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_13)


        self.verticalLayout_31.addWidget(self.explorePageHeader)

        self.line_3 = QFrame(self.explorePage)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setFrameShape(QFrame.HLine)

        self.verticalLayout_31.addWidget(self.line_3)

        self.exploreThemesCnt = QWidget(self.explorePage)
        self.exploreThemesCnt.setObjectName(u"exploreThemesCnt")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.exploreThemesCnt.sizePolicy().hasHeightForWidth())
        self.exploreThemesCnt.setSizePolicy(sizePolicy5)

        self.verticalLayout_31.addWidget(self.exploreThemesCnt)

        self.pages.addWidget(self.explorePage)
        self.locSimPage = QWidget()
        self.locSimPage.setObjectName(u"locSimPage")
        self.verticalLayout_28 = QVBoxLayout(self.locSimPage)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.locSimPageHeader = QWidget(self.locSimPage)
        self.locSimPageHeader.setObjectName(u"locSimPageHeader")
        self.horizontalLayout_28 = QHBoxLayout(self.locSimPageHeader)
        self.horizontalLayout_28.setSpacing(10)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, -1, 0, -1)
        self.toolButton_13 = QToolButton(self.locSimPageHeader)
        self.toolButton_13.setObjectName(u"toolButton_13")
        self.toolButton_13.setEnabled(False)
        self.toolButton_13.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_13.setIcon(icon4)

        self.horizontalLayout_28.addWidget(self.toolButton_13)

        self.verticalWidget_8 = QWidget(self.locSimPageHeader)
        self.verticalWidget_8.setObjectName(u"verticalWidget_8")
        self.verticalLayout_27 = QVBoxLayout(self.verticalWidget_8)
        self.verticalLayout_27.setSpacing(6)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.statusBarLbl_2 = QLabel(self.verticalWidget_8)
        self.statusBarLbl_2.setObjectName(u"statusBarLbl_2")
        self.statusBarLbl_2.setFont(font1)

        self.verticalLayout_27.addWidget(self.statusBarLbl_2)

        self.label_4 = QLabel(self.verticalWidget_8)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_27.addWidget(self.label_4)


        self.horizontalLayout_28.addWidget(self.verticalWidget_8)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_11)

        self.loadLocSimBtn = QToolButton(self.locSimPageHeader)
        self.loadLocSimBtn.setObjectName(u"loadLocSimBtn")

        self.horizontalLayout_28.addWidget(self.loadLocSimBtn)


        self.verticalLayout_28.addWidget(self.locSimPageHeader)

        self.line_2 = QFrame(self.locSimPage)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setFrameShape(QFrame.HLine)

        self.verticalLayout_28.addWidget(self.line_2)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer_14)

        self.locSimCnt = QWidget(self.locSimPage)
        self.locSimCnt.setObjectName(u"locSimCnt")
        self.locSimPageContent = QVBoxLayout(self.locSimCnt)
        self.locSimPageContent.setObjectName(u"locSimPageContent")
        self.locSimPageContent.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget2 = QWidget(self.locSimCnt)
        self.verticalWidget2.setObjectName(u"verticalWidget2")
        self.verticalLayout_29 = QVBoxLayout(self.verticalWidget2)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.verticalWidget2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_7)

        self.latitudeTxt = QLineEdit(self.verticalWidget2)
        self.latitudeTxt.setObjectName(u"latitudeTxt")
        self.latitudeTxt.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.latitudeTxt)

        self.label_11 = QLabel(self.verticalWidget2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_11)

        self.longitudeTxt = QLineEdit(self.verticalWidget2)
        self.longitudeTxt.setObjectName(u"longitudeTxt")
        self.longitudeTxt.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.longitudeTxt)

        self.horizontalWidget4 = QWidget(self.verticalWidget2)
        self.horizontalWidget4.setObjectName(u"horizontalWidget4")
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalWidget4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.setLocationBtn = QToolButton(self.horizontalWidget4)
        self.setLocationBtn.setObjectName(u"setLocationBtn")

        self.horizontalLayout_3.addWidget(self.setLocationBtn)


        self.verticalLayout_29.addWidget(self.horizontalWidget4)

        self.horizontalWidget_22 = QWidget(self.verticalWidget2)
        self.horizontalWidget_22.setObjectName(u"horizontalWidget_22")
        self.horizontalLayout_29 = QHBoxLayout(self.horizontalWidget_22)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.resetLocationBtn = QToolButton(self.horizontalWidget_22)
        self.resetLocationBtn.setObjectName(u"resetLocationBtn")

        self.horizontalLayout_29.addWidget(self.resetLocationBtn)


        self.verticalLayout_29.addWidget(self.horizontalWidget_22)


        self.locSimPageContent.addWidget(self.verticalWidget2)


        self.verticalLayout_28.addWidget(self.locSimCnt)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer_13)

        self.pages.addWidget(self.locSimPage)
        self.themingPage = QWidget()
        self.themingPage.setObjectName(u"themingPage")
        self.verticalLayout_23 = QVBoxLayout(self.themingPage)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_8 = QWidget(self.themingPage)
        self.horizontalWidget_8.setObjectName(u"horizontalWidget_8")
        self.horizontalLayout_23 = QHBoxLayout(self.horizontalWidget_8)
        self.horizontalLayout_23.setSpacing(10)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 9, 0, 9)
        self.themesBtn = QToolButton(self.horizontalWidget_8)
        self.themesBtn.setObjectName(u"themesBtn")
        self.themesBtn.setEnabled(True)
        self.themesBtn.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.themesBtn.setIcon(icon6)
        self.themesBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_23.addWidget(self.themesBtn)

        self.verticalWidget_7 = QWidget(self.horizontalWidget_8)
        self.verticalWidget_7.setObjectName(u"verticalWidget_7")
        self.verticalLayout_21 = QVBoxLayout(self.verticalWidget_7)
        self.verticalLayout_21.setSpacing(6)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.themesLbl = QLabel(self.verticalWidget_7)
        self.themesLbl.setObjectName(u"themesLbl")
        self.themesLbl.setFont(font1)

        self.verticalLayout_21.addWidget(self.themesLbl)


        self.horizontalLayout_23.addWidget(self.verticalWidget_7)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_10)

        self.horizontalWidget5 = QWidget(self.horizontalWidget_8)
        self.horizontalWidget5.setObjectName(u"horizontalWidget5")
        self.horizontalLayout_26 = QHBoxLayout(self.horizontalWidget5)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.importThemeBtn = QToolButton(self.horizontalWidget5)
        self.importThemeBtn.setObjectName(u"importThemeBtn")
        self.importThemeBtn.setEnabled(False)
        self.importThemeBtn.setStyleSheet(u"QToolButton {\n"
"	background: none;\n"
"}")

        self.horizontalLayout_26.addWidget(self.importThemeBtn)

        self.importThemeFolderBtn = QToolButton(self.horizontalWidget5)
        self.importThemeFolderBtn.setObjectName(u"importThemeFolderBtn")
        icon16 = QIcon()
        icon16.addFile(u":/icon/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.importThemeFolderBtn.setIcon(icon16)

        self.horizontalLayout_26.addWidget(self.importThemeFolderBtn)

        self.importThemeZipBtn = QToolButton(self.horizontalWidget5)
        self.importThemeZipBtn.setObjectName(u"importThemeZipBtn")
        icon17 = QIcon()
        icon17.addFile(u":/icon/file-earmark-zip.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.importThemeZipBtn.setIcon(icon17)

        self.horizontalLayout_26.addWidget(self.importThemeZipBtn)


        self.horizontalLayout_23.addWidget(self.horizontalWidget5)


        self.verticalLayout_23.addWidget(self.horizontalWidget_8)

        self.line_15 = QFrame(self.themingPage)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_15.setFrameShadow(QFrame.Plain)
        self.line_15.setFrameShape(QFrame.HLine)

        self.verticalLayout_23.addWidget(self.line_15)

        self.themesPageContent = QWidget(self.themingPage)
        self.themesPageContent.setObjectName(u"themesPageContent")
        self.themesPageContent.setEnabled(False)
        self.verticalLayout_22 = QVBoxLayout(self.themesPageContent)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.themesCnt = QWidget(self.themesPageContent)
        self.themesCnt.setObjectName(u"themesCnt")

        self.verticalLayout_22.addWidget(self.themesCnt)

        self.line = QFrame(self.themesPageContent)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout_22.addWidget(self.line)

        self.label_3 = QLabel(self.themesPageContent)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_22.addWidget(self.label_3)

        self.iconsCnt = QWidget(self.themesPageContent)
        self.iconsCnt.setObjectName(u"iconsCnt")

        self.verticalLayout_22.addWidget(self.iconsCnt)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_9)

        self.horizontalWidget6 = QWidget(self.themesPageContent)
        self.horizontalWidget6.setObjectName(u"horizontalWidget6")
        self.horizontalLayout_16 = QHBoxLayout(self.horizontalWidget6)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.hideNamesBtn = QToolButton(self.horizontalWidget6)
        self.hideNamesBtn.setObjectName(u"hideNamesBtn")
        sizePolicy2.setHeightForWidth(self.hideNamesBtn.sizePolicy().hasHeightForWidth())
        self.hideNamesBtn.setSizePolicy(sizePolicy2)

        self.horizontalLayout_16.addWidget(self.hideNamesBtn)

        self.borderAllBtn = QToolButton(self.horizontalWidget6)
        self.borderAllBtn.setObjectName(u"borderAllBtn")
        sizePolicy2.setHeightForWidth(self.borderAllBtn.sizePolicy().hasHeightForWidth())
        self.borderAllBtn.setSizePolicy(sizePolicy2)

        self.horizontalLayout_16.addWidget(self.borderAllBtn)

        self.addAllBtn = QToolButton(self.horizontalWidget6)
        self.addAllBtn.setObjectName(u"addAllBtn")
        sizePolicy2.setHeightForWidth(self.addAllBtn.sizePolicy().hasHeightForWidth())
        self.addAllBtn.setSizePolicy(sizePolicy2)

        self.horizontalLayout_16.addWidget(self.addAllBtn)


        self.verticalLayout_22.addWidget(self.horizontalWidget6)


        self.verticalLayout_23.addWidget(self.themesPageContent)

        self.pages.addWidget(self.themingPage)
        self.gestaltPage = QWidget()
        self.gestaltPage.setObjectName(u"gestaltPage")
        self.verticalLayout_4 = QVBoxLayout(self.gestaltPage)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.statusBarPageHeader = QWidget(self.gestaltPage)
        self.statusBarPageHeader.setObjectName(u"statusBarPageHeader")
        self.horizontalLayout_5 = QHBoxLayout(self.statusBarPageHeader)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.toolButton_8 = QToolButton(self.statusBarPageHeader)
        self.toolButton_8.setObjectName(u"toolButton_8")
        self.toolButton_8.setEnabled(False)
        self.toolButton_8.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_8.setIcon(icon6)
        self.toolButton_8.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.toolButton_8)

        self.verticalWidget_21 = QWidget(self.statusBarPageHeader)
        self.verticalWidget_21.setObjectName(u"verticalWidget_21")
        self.verticalLayout_5 = QVBoxLayout(self.verticalWidget_21)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.statusBarLbl = QLabel(self.verticalWidget_21)
        self.statusBarLbl.setObjectName(u"statusBarLbl")
        self.statusBarLbl.setFont(font1)

        self.verticalLayout_5.addWidget(self.statusBarLbl)

        self.verticalSpacer_8 = QSpacerItem(20, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_8)


        self.horizontalLayout_5.addWidget(self.verticalWidget_21)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addWidget(self.statusBarPageHeader)

        self.line_8 = QFrame(self.gestaltPage)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_8.setFrameShadow(QFrame.Plain)
        self.line_8.setFrameShape(QFrame.HLine)

        self.verticalLayout_4.addWidget(self.line_8)

        self.scrollArea = QScrollArea(self.gestaltPage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 650, 1200))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(650, 1200))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(650, 1200))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gestaltPageContent = QWidget(self.scrollAreaWidgetContents)
        self.gestaltPageContent.setObjectName(u"gestaltPageContent")
        self.gestaltPageContent.setEnabled(False)
        self.verticalLayout_8 = QVBoxLayout(self.gestaltPageContent)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.gestaltPageContent)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_8.addWidget(self.label_9)

        self.dynamicIslandDrp = QComboBox(self.gestaltPageContent)
        self.dynamicIslandDrp.addItem("")
        self.dynamicIslandDrp.addItem("")
        self.dynamicIslandDrp.addItem("")
        self.dynamicIslandDrp.addItem("")
        self.dynamicIslandDrp.addItem("")
        self.dynamicIslandDrp.addItem("")
        self.dynamicIslandDrp.addItem("")
        self.dynamicIslandDrp.setObjectName(u"dynamicIslandDrp")
        self.dynamicIslandDrp.setMinimumSize(QSize(0, 0))
        self.dynamicIslandDrp.setMaximumSize(QSize(325, 16777215))
        self.dynamicIslandDrp.setStyleSheet(u"QComboBox {\n"
"	background-color: #3b3b3b;\n"
"    border: none;\n"
"    color: #e8e8e8;\n"
"    font-size: 14px;\n"
"	padding-left: 8px;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    image: url(:/icon/caret-down-fill.svg);\n"
"	icon-size: 16px;\n"
"    subcontrol-position: right center;\n"
"	margin-right: 8px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	background-color: #3b3b3b;\n"
"    outline: none;\n"
"	margin-top: 1px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"	background-color: #3b3b3b;\n"
"	color: #e8e8e8;\n"
"    padding-left: 8px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #535353;\n"
"    color: #ffffff;\n"
"}")
        self.dynamicIslandDrp.setMaxVisibleItems(15)

        self.verticalLayout_8.addWidget(self.dynamicIslandDrp)

        self.modelNameChk = QCheckBox(self.gestaltPageContent)
        self.modelNameChk.setObjectName(u"modelNameChk")

        self.verticalLayout_8.addWidget(self.modelNameChk)

        self.modelNameTxt = QLineEdit(self.gestaltPageContent)
        self.modelNameTxt.setObjectName(u"modelNameTxt")

        self.verticalLayout_8.addWidget(self.modelNameTxt)

        self.bootChimeChk = QCheckBox(self.gestaltPageContent)
        self.bootChimeChk.setObjectName(u"bootChimeChk")

        self.verticalLayout_8.addWidget(self.bootChimeChk)

        self.chargeLimitChk = QCheckBox(self.gestaltPageContent)
        self.chargeLimitChk.setObjectName(u"chargeLimitChk")

        self.verticalLayout_8.addWidget(self.chargeLimitChk)

        self.tapToWakeChk = QCheckBox(self.gestaltPageContent)
        self.tapToWakeChk.setObjectName(u"tapToWakeChk")

        self.verticalLayout_8.addWidget(self.tapToWakeChk)

        self.iphone16SettingsChk = QCheckBox(self.gestaltPageContent)
        self.iphone16SettingsChk.setObjectName(u"iphone16SettingsChk")

        self.verticalLayout_8.addWidget(self.iphone16SettingsChk)

        self.parallaxChk = QCheckBox(self.gestaltPageContent)
        self.parallaxChk.setObjectName(u"parallaxChk")

        self.verticalLayout_8.addWidget(self.parallaxChk)

        self.horizontalWidget7 = QWidget(self.gestaltPageContent)
        self.horizontalWidget7.setObjectName(u"horizontalWidget7")
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalWidget7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_8.addWidget(self.horizontalWidget7)

        self.line_7 = QFrame(self.gestaltPageContent)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_7.setFrameShadow(QFrame.Plain)
        self.line_7.setFrameShape(QFrame.HLine)

        self.verticalLayout_8.addWidget(self.line_7)

        self.stageManagerChk = QCheckBox(self.gestaltPageContent)
        self.stageManagerChk.setObjectName(u"stageManagerChk")

        self.verticalLayout_8.addWidget(self.stageManagerChk)

        self.ipadAppsChk = QCheckBox(self.gestaltPageContent)
        self.ipadAppsChk.setObjectName(u"ipadAppsChk")

        self.verticalLayout_8.addWidget(self.ipadAppsChk)

        self.shutterChk = QCheckBox(self.gestaltPageContent)
        self.shutterChk.setObjectName(u"shutterChk")

        self.verticalLayout_8.addWidget(self.shutterChk)

        self.pencilChk = QCheckBox(self.gestaltPageContent)
        self.pencilChk.setObjectName(u"pencilChk")

        self.verticalLayout_8.addWidget(self.pencilChk)

        self.actionButtonChk = QCheckBox(self.gestaltPageContent)
        self.actionButtonChk.setObjectName(u"actionButtonChk")

        self.verticalLayout_8.addWidget(self.actionButtonChk)

        self.line_9 = QFrame(self.gestaltPageContent)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_9.setFrameShadow(QFrame.Plain)
        self.line_9.setFrameShape(QFrame.HLine)

        self.verticalLayout_8.addWidget(self.line_9)

        self.internalInstallChk = QCheckBox(self.gestaltPageContent)
        self.internalInstallChk.setObjectName(u"internalInstallChk")

        self.verticalLayout_8.addWidget(self.internalInstallChk)

        self.internalStorageChk = QCheckBox(self.gestaltPageContent)
        self.internalStorageChk.setObjectName(u"internalStorageChk")

        self.verticalLayout_8.addWidget(self.internalStorageChk)

        self.line_10 = QFrame(self.gestaltPageContent)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_10.setFrameShadow(QFrame.Plain)
        self.line_10.setFrameShape(QFrame.HLine)

        self.verticalLayout_8.addWidget(self.line_10)

        self.collisionSOSChk = QCheckBox(self.gestaltPageContent)
        self.collisionSOSChk.setObjectName(u"collisionSOSChk")

        self.verticalLayout_8.addWidget(self.collisionSOSChk)

        self.sleepApneaChk = QCheckBox(self.gestaltPageContent)
        self.sleepApneaChk.setObjectName(u"sleepApneaChk")

        self.verticalLayout_8.addWidget(self.sleepApneaChk)

        self.aodChk = QCheckBox(self.gestaltPageContent)
        self.aodChk.setObjectName(u"aodChk")

        self.verticalLayout_8.addWidget(self.aodChk)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)


        self.verticalLayout_9.addWidget(self.gestaltPageContent)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)

        self.pages.addWidget(self.gestaltPage)
        self.customOperationsPage = QWidget()
        self.customOperationsPage.setObjectName(u"customOperationsPage")
        self.verticalLayout_20 = QVBoxLayout(self.customOperationsPage)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_7 = QWidget(self.customOperationsPage)
        self.horizontalWidget_7.setObjectName(u"horizontalWidget_7")
        self.horizontalLayout_22 = QHBoxLayout(self.horizontalWidget_7)
        self.horizontalLayout_22.setSpacing(10)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 9, 0, 9)
        self.toolButton_12 = QToolButton(self.horizontalWidget_7)
        self.toolButton_12.setObjectName(u"toolButton_12")
        self.toolButton_12.setEnabled(False)
        self.toolButton_12.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_12.setIcon(icon5)
        self.toolButton_12.setIconSize(QSize(25, 25))

        self.horizontalLayout_22.addWidget(self.toolButton_12)

        self.verticalWidget_6 = QWidget(self.horizontalWidget_7)
        self.verticalWidget_6.setObjectName(u"verticalWidget_6")
        self.verticalLayout_18 = QVBoxLayout(self.verticalWidget_6)
        self.verticalLayout_18.setSpacing(6)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.customOperationsLbl = QLabel(self.verticalWidget_6)
        self.customOperationsLbl.setObjectName(u"customOperationsLbl")
        self.customOperationsLbl.setFont(font1)

        self.verticalLayout_18.addWidget(self.customOperationsLbl)

        self.label_14 = QLabel(self.verticalWidget_6)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_18.addWidget(self.label_14)


        self.horizontalLayout_22.addWidget(self.verticalWidget_6)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_9)


        self.verticalLayout_20.addWidget(self.horizontalWidget_7)

        self.line_14 = QFrame(self.customOperationsPage)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_14.setFrameShadow(QFrame.Plain)
        self.line_14.setFrameShape(QFrame.HLine)

        self.verticalLayout_20.addWidget(self.line_14)

        self.customOperationsPageContent = QWidget(self.customOperationsPage)
        self.customOperationsPageContent.setObjectName(u"customOperationsPageContent")
        self.customOperationsPageContent.setEnabled(True)
        self.verticalLayout_19 = QVBoxLayout(self.customOperationsPageContent)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.customOpsTopBtns = QHBoxLayout()
#ifndef Q_OS_MAC
        self.customOpsTopBtns.setSpacing(-1)
#endif
        self.customOpsTopBtns.setObjectName(u"customOpsTopBtns")
        self.customOpsTopBtns.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.customOpsTopBtns.addItem(self.horizontalSpacer_17)

        self.importOperationBtn = QToolButton(self.customOperationsPageContent)
        self.importOperationBtn.setObjectName(u"importOperationBtn")
        self.importOperationBtn.setEnabled(True)
        icon18 = QIcon()
        icon18.addFile(u":/icon/import.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.importOperationBtn.setIcon(icon18)
        self.importOperationBtn.setIconSize(QSize(20, 20))
        self.importOperationBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.customOpsTopBtns.addWidget(self.importOperationBtn, 0, Qt.AlignLeft)

        self.newOperationBtn = QToolButton(self.customOperationsPageContent)
        self.newOperationBtn.setObjectName(u"newOperationBtn")
        self.newOperationBtn.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.newOperationBtn.sizePolicy().hasHeightForWidth())
        self.newOperationBtn.setSizePolicy(sizePolicy2)
        self.newOperationBtn.setMinimumSize(QSize(0, 35))
        icon19 = QIcon()
        icon19.addFile(u":/icon/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.newOperationBtn.setIcon(icon19)
        self.newOperationBtn.setIconSize(QSize(16, 16))
        self.newOperationBtn.setCheckable(False)
        self.newOperationBtn.setAutoExclusive(True)
        self.newOperationBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.customOpsTopBtns.addWidget(self.newOperationBtn, 0, Qt.AlignLeft)


        self.verticalLayout_19.addLayout(self.customOpsTopBtns)

        self.operationsCnt = QWidget(self.customOperationsPageContent)
        self.operationsCnt.setObjectName(u"operationsCnt")
        self.operationsCnt.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.operationsCnt.sizePolicy().hasHeightForWidth())
        self.operationsCnt.setSizePolicy(sizePolicy5)

        self.verticalLayout_19.addWidget(self.operationsCnt)


        self.verticalLayout_20.addWidget(self.customOperationsPageContent)

        self.pages.addWidget(self.customOperationsPage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.verticalLayout_10 = QVBoxLayout(self.settingsPage)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_4 = QWidget(self.settingsPage)
        self.horizontalWidget_4.setObjectName(u"horizontalWidget_4")
        self.horizontalLayout_13 = QHBoxLayout(self.horizontalWidget_4)
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 9, 0, 9)
        self.toolButton_7 = QToolButton(self.horizontalWidget_4)
        self.toolButton_7.setObjectName(u"toolButton_7")
        self.toolButton_7.setEnabled(False)
        self.toolButton_7.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_7.setIcon(icon10)

        self.horizontalLayout_13.addWidget(self.toolButton_7)

        self.verticalWidget_3 = QWidget(self.horizontalWidget_4)
        self.verticalWidget_3.setObjectName(u"verticalWidget_3")
        self.verticalLayout_7 = QVBoxLayout(self.verticalWidget_3)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.springboardOptionsLbl = QLabel(self.verticalWidget_3)
        self.springboardOptionsLbl.setObjectName(u"springboardOptionsLbl")
        self.springboardOptionsLbl.setFont(font1)

        self.verticalLayout_7.addWidget(self.springboardOptionsLbl)

        self.verticalSpacer_17 = QSpacerItem(20, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_17)


        self.horizontalLayout_13.addWidget(self.verticalWidget_3)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_6)


        self.verticalLayout_10.addWidget(self.horizontalWidget_4)

        self.line_11 = QFrame(self.settingsPage)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_11.setFrameShadow(QFrame.Plain)
        self.line_11.setFrameShape(QFrame.HLine)

        self.verticalLayout_10.addWidget(self.line_11)

        self.settingsPageContent = QWidget(self.settingsPage)
        self.settingsPageContent.setObjectName(u"settingsPageContent")
        self.settingsPageContent.setEnabled(True)
        self.settingsPageContent.setMaximumSize(QSize(650, 16777215))
        self._2 = QVBoxLayout(self.settingsPageContent)
        self._2.setObjectName(u"_2")
        self._2.setContentsMargins(0, 0, 0, 0)
        self.allowWifiApplyingChk = QCheckBox(self.settingsPageContent)
        self.allowWifiApplyingChk.setObjectName(u"allowWifiApplyingChk")
        self.allowWifiApplyingChk.setChecked(True)

        self._2.addWidget(self.allowWifiApplyingChk)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self._2.addItem(self.verticalSpacer_5)


        self.verticalLayout_10.addWidget(self.settingsPageContent)

        self.pages.addWidget(self.settingsPage)
        self.featureFlagsPage = QWidget()
        self.featureFlagsPage.setObjectName(u"featureFlagsPage")
        self.verticalLayout_14 = QVBoxLayout(self.featureFlagsPage)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_5 = QWidget(self.featureFlagsPage)
        self.horizontalWidget_5.setObjectName(u"horizontalWidget_5")
        self.horizontalLayout_20 = QHBoxLayout(self.horizontalWidget_5)
        self.horizontalLayout_20.setSpacing(10)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 9, 0, 9)
        self.toolButton_10 = QToolButton(self.horizontalWidget_5)
        self.toolButton_10.setObjectName(u"toolButton_10")
        self.toolButton_10.setEnabled(False)
        self.toolButton_10.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_10.setIcon(icon7)

        self.horizontalLayout_20.addWidget(self.toolButton_10)

        self.verticalWidget_4 = QWidget(self.horizontalWidget_5)
        self.verticalWidget_4.setObjectName(u"verticalWidget_4")
        self.verticalLayout_12 = QVBoxLayout(self.verticalWidget_4)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.internalOptionsLbl = QLabel(self.verticalWidget_4)
        self.internalOptionsLbl.setObjectName(u"internalOptionsLbl")
        self.internalOptionsLbl.setFont(font1)

        self.verticalLayout_12.addWidget(self.internalOptionsLbl)

        self.verticalSpacer_15 = QSpacerItem(20, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_12.addItem(self.verticalSpacer_15)


        self.horizontalLayout_20.addWidget(self.verticalWidget_4)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_7)


        self.verticalLayout_14.addWidget(self.horizontalWidget_5)

        self.line_12 = QFrame(self.featureFlagsPage)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_12.setFrameShadow(QFrame.Plain)
        self.line_12.setFrameShape(QFrame.HLine)

        self.verticalLayout_14.addWidget(self.line_12)

        self.featureFlagsPageContent = QWidget(self.featureFlagsPage)
        self.featureFlagsPageContent.setObjectName(u"featureFlagsPageContent")
        self.featureFlagsPageContent.setEnabled(True)
        self.verticalLayout_13 = QVBoxLayout(self.featureFlagsPageContent)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.clockAnimChk = QCheckBox(self.featureFlagsPageContent)
        self.clockAnimChk.setObjectName(u"clockAnimChk")

        self.verticalLayout_13.addWidget(self.clockAnimChk)

        self.lockscreenChk = QCheckBox(self.featureFlagsPageContent)
        self.lockscreenChk.setObjectName(u"lockscreenChk")

        self.verticalLayout_13.addWidget(self.lockscreenChk)

        self.div = QFrame(self.featureFlagsPageContent)
        self.div.setObjectName(u"div")
        self.div.setEnabled(False)
        self.div.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.div.setFrameShadow(QFrame.Plain)
        self.div.setFrameShape(QFrame.HLine)

        self.verticalLayout_13.addWidget(self.div)

        self.photosChk = QCheckBox(self.featureFlagsPageContent)
        self.photosChk.setObjectName(u"photosChk")

        self.verticalLayout_13.addWidget(self.photosChk)

        self.aiChk = QCheckBox(self.featureFlagsPageContent)
        self.aiChk.setObjectName(u"aiChk")

        self.verticalLayout_13.addWidget(self.aiChk)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_6)


        self.verticalLayout_14.addWidget(self.featureFlagsPageContent)

        self.pages.addWidget(self.featureFlagsPage)
        self.euEnablerPage = QWidget()
        self.euEnablerPage.setObjectName(u"euEnablerPage")
        self.verticalLayout_17 = QVBoxLayout(self.euEnablerPage)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_6 = QWidget(self.euEnablerPage)
        self.horizontalWidget_6.setObjectName(u"horizontalWidget_6")
        self.horizontalLayout_21 = QHBoxLayout(self.horizontalWidget_6)
        self.horizontalLayout_21.setSpacing(10)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 9, 0, 9)
        self.toolButton_11 = QToolButton(self.horizontalWidget_6)
        self.toolButton_11.setObjectName(u"toolButton_11")
        self.toolButton_11.setEnabled(False)
        self.toolButton_11.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_11.setIcon(icon4)

        self.horizontalLayout_21.addWidget(self.toolButton_11)

        self.verticalWidget_5 = QWidget(self.horizontalWidget_6)
        self.verticalWidget_5.setObjectName(u"verticalWidget_5")
        self.verticalLayout_15 = QVBoxLayout(self.verticalWidget_5)
        self.verticalLayout_15.setSpacing(6)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.setupOptionsLbl = QLabel(self.verticalWidget_5)
        self.setupOptionsLbl.setObjectName(u"setupOptionsLbl")
        self.setupOptionsLbl.setFont(font1)

        self.verticalLayout_15.addWidget(self.setupOptionsLbl)

        self.euEnablerEnabledChk = QCheckBox(self.verticalWidget_5)
        self.euEnablerEnabledChk.setObjectName(u"euEnablerEnabledChk")

        self.verticalLayout_15.addWidget(self.euEnablerEnabledChk)


        self.horizontalLayout_21.addWidget(self.verticalWidget_5)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_8)


        self.verticalLayout_17.addWidget(self.horizontalWidget_6)

        self.line_13 = QFrame(self.euEnablerPage)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_13.setFrameShadow(QFrame.Plain)
        self.line_13.setFrameShape(QFrame.HLine)

        self.verticalLayout_17.addWidget(self.line_13)

        self.euEnablerPageContent = QWidget(self.euEnablerPage)
        self.euEnablerPageContent.setObjectName(u"euEnablerPageContent")
        self.euEnablerPageContent.setEnabled(False)
        self.verticalLayout_16 = QVBoxLayout(self.euEnablerPageContent)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.euEnablerPageContent)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_16.addWidget(self.label_5)

        self.methodChoiceDrp = QComboBox(self.euEnablerPageContent)
        self.methodChoiceDrp.addItem("")
        self.methodChoiceDrp.addItem("")
        self.methodChoiceDrp.setObjectName(u"methodChoiceDrp")
        self.methodChoiceDrp.setMaximumSize(QSize(150, 16777215))
        self.methodChoiceDrp.setStyleSheet(u"QComboBox {\n"
"	background-color: #3b3b3b;\n"
"    border: none;\n"
"    color: #e8e8e8;\n"
"    font-size: 14px;\n"
"	padding-left: 8px;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    image: url(:/icon/caret-down-fill.svg);\n"
"	icon-size: 16px;\n"
"    subcontrol-position: right center;\n"
"	margin-right: 8px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	background-color: #3b3b3b;\n"
"    outline: none;\n"
"	margin-top: 1px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"	background-color: #3b3b3b;\n"
"	color: #e8e8e8;\n"
"    padding-left: 8px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #535353;\n"
"    color: #ffffff;\n"
"}")

        self.verticalLayout_16.addWidget(self.methodChoiceDrp)

        self.label_6 = QLabel(self.euEnablerPageContent)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_16.addWidget(self.label_6)

        self.regionCodeTxt = QLineEdit(self.euEnablerPageContent)
        self.regionCodeTxt.setObjectName(u"regionCodeTxt")

        self.verticalLayout_16.addWidget(self.regionCodeTxt)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_7)


        self.verticalLayout_17.addWidget(self.euEnablerPageContent)

        self.pages.addWidget(self.euEnablerPage)
        self.applyPage = QWidget()
        self.applyPage.setObjectName(u"applyPage")
        self.verticalLayout_6 = QVBoxLayout(self.applyPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget3 = QWidget(self.applyPage)
        self.verticalWidget3.setObjectName(u"verticalWidget3")
        self.verticalLayout_24 = QVBoxLayout(self.verticalWidget3)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.locSimPageHeader_2 = QWidget(self.verticalWidget3)
        self.locSimPageHeader_2.setObjectName(u"locSimPageHeader_2")
        self.horizontalLayout_33 = QHBoxLayout(self.locSimPageHeader_2)
        self.horizontalLayout_33.setSpacing(10)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, -1, 0, -1)
        self.toolButton_18 = QToolButton(self.locSimPageHeader_2)
        self.toolButton_18.setObjectName(u"toolButton_18")
        self.toolButton_18.setEnabled(False)
        self.toolButton_18.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_18.setIcon(icon9)

        self.horizontalLayout_33.addWidget(self.toolButton_18)

        self.verticalWidget_11 = QWidget(self.locSimPageHeader_2)
        self.verticalWidget_11.setObjectName(u"verticalWidget_11")
        self.verticalLayout_33 = QVBoxLayout(self.verticalWidget_11)
        self.verticalLayout_33.setSpacing(6)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.statusBarLbl_5 = QLabel(self.verticalWidget_11)
        self.statusBarLbl_5.setObjectName(u"statusBarLbl_5")
        self.statusBarLbl_5.setFont(font1)

        self.verticalLayout_33.addWidget(self.statusBarLbl_5)

        self.label_16 = QLabel(self.verticalWidget_11)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_33.addWidget(self.label_16)


        self.horizontalLayout_33.addWidget(self.verticalWidget_11)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_15)


        self.verticalLayout_24.addWidget(self.locSimPageHeader_2)

        self.line_5 = QFrame(self.verticalWidget3)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_5.setFrameShadow(QFrame.Plain)
        self.line_5.setFrameShape(QFrame.HLine)

        self.verticalLayout_24.addWidget(self.line_5)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_10)

        self.modifiedTweaksLbl = QLabel(self.verticalWidget3)
        self.modifiedTweaksLbl.setObjectName(u"modifiedTweaksLbl")
        self.modifiedTweaksLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.modifiedTweaksLbl)

        self.gestaltLocationLbl = QLabel(self.verticalWidget3)
        self.gestaltLocationLbl.setObjectName(u"gestaltLocationLbl")
        self.gestaltLocationLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.gestaltLocationLbl)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 10, -1, 0)
        self.chooseGestaltBtn = QToolButton(self.verticalWidget3)
        self.chooseGestaltBtn.setObjectName(u"chooseGestaltBtn")
        self.chooseGestaltBtn.setIcon(icon16)
        self.chooseGestaltBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_7.addWidget(self.chooseGestaltBtn)


        self.verticalLayout_24.addLayout(self.horizontalLayout_7)

        self.horizontalWidget8 = QWidget(self.verticalWidget3)
        self.horizontalWidget8.setObjectName(u"horizontalWidget8")
        self.horizontalLayout_17 = QHBoxLayout(self.horizontalWidget8)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.applyTweaksBtn = QToolButton(self.horizontalWidget8)
        self.applyTweaksBtn.setObjectName(u"applyTweaksBtn")
        self.applyTweaksBtn.setIcon(icon9)
        self.applyTweaksBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_17.addWidget(self.applyTweaksBtn)


        self.verticalLayout_24.addWidget(self.horizontalWidget8)

        self.statusLbl = QLabel(self.verticalWidget3)
        self.statusLbl.setObjectName(u"statusLbl")
        self.statusLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.statusLbl)

        self.restoreProgressBar = QProgressBar(self.verticalWidget3)
        self.restoreProgressBar.setObjectName(u"restoreProgressBar")
        sizePolicy.setHeightForWidth(self.restoreProgressBar.sizePolicy().hasHeightForWidth())
        self.restoreProgressBar.setSizePolicy(sizePolicy)
        self.restoreProgressBar.setMinimumSize(QSize(150, 0))
        self.restoreProgressBar.setValue(0)
        self.restoreProgressBar.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.restoreProgressBar, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_2)

        self.horizontalWidget9 = QWidget(self.verticalWidget3)
        self.horizontalWidget9.setObjectName(u"horizontalWidget9")
        self.horizontalLayout_25 = QHBoxLayout(self.horizontalWidget9)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_14)

        self.removeTweaksBtn = QToolButton(self.horizontalWidget9)
        self.removeTweaksBtn.setObjectName(u"removeTweaksBtn")

        self.horizontalLayout_25.addWidget(self.removeTweaksBtn)

        self.resetGestaltBtn = QToolButton(self.horizontalWidget9)
        self.resetGestaltBtn.setObjectName(u"resetGestaltBtn")

        self.horizontalLayout_25.addWidget(self.resetGestaltBtn)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_16)


        self.verticalLayout_24.addWidget(self.horizontalWidget9)


        self.verticalLayout_6.addWidget(self.verticalWidget3)

        self.pages.addWidget(self.applyPage)

        self._3.addWidget(self.pages)


        self.horizontalLayout_18.addWidget(self.main)


        self.verticalLayout_11.addWidget(self.body)

        Nugget.setCentralWidget(self.centralwidget)

        self.retranslateUi(Nugget)

        self.devicePicker.setCurrentIndex(-1)
        self.pages.setCurrentIndex(0)
        self.dynamicIslandDrp.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Nugget)
    # setupUi

    def retranslateUi(self, Nugget):
        Nugget.setWindowTitle(QCoreApplication.translate("Nugget", u"Nugget", None))
        self.centralwidget.setProperty("cls", QCoreApplication.translate("Nugget", u"central", None))
        self.devicePicker.setPlaceholderText(QCoreApplication.translate("Nugget", u"None", None))
        self.refreshBtn.setProperty("cls", QCoreApplication.translate("Nugget", u"btn", None))
        self.titleBar.setText(QCoreApplication.translate("Nugget", u"Nugget", None))
        self.homePageBtn.setText(QCoreApplication.translate("Nugget", u"    Home", None))
        self.homePageBtn.setProperty("cls", QCoreApplication.translate("Nugget", u"sidebarBtn", None))
        self.explorePageBtn.setText(QCoreApplication.translate("Nugget", u"    Explore", None))
        self.explorePageBtn.setProperty("cls", QCoreApplication.translate("Nugget", u"sidebarBtn", None))
        self.locSimPageBtn.setText(QCoreApplication.translate("Nugget", u"    Location Simulation", None))
        self.locSimPageBtn.setProperty("cls", QCoreApplication.translate("Nugget", u"sidebarBtn", None))
        self.customOperationsPageBtn.setText(QCoreApplication.translate("Nugget", u"    Custom Operations", None))
        self.customOperationsPageBtn.setProperty("cls", QCoreApplication.translate("Nugget", u"sidebarBtn", None))
        self.gestaltPageBtn.setText(QCoreApplication.translate("Nugget", u"     Mobile Gestalt", None))
        self.gestaltPageBtn.setProperty("cls", QCoreApplication.translate("Nugget", u"sidebarBtn", None))
        self.featureFlagsPageBtn.setText(QCoreApplication.translate("Nugget", u"    Feature Flags", None))
        self.featureFlagsPageBtn.setProperty("cls", QCoreApplication.translate("Nugget", u"sidebarBtn", None))
        self.euEnablerPageBtn.setText(QCoreApplication.translate("Nugget", u"    EU Enabler", None))
        self.euEnablerPageBtn.setProperty("cls", QCoreApplication.translate("Nugget", u"sidebarBtn", None))
        self.internalOptionsPageBtn.setText(QCoreApplication.translate("Nugget", u"    Internal Options", None))
        self.internalOptionsPageBtn.setProperty("cls", QCoreApplication.translate("Nugget", u"sidebarBtn", None))
        self.applyPageBtn.setText(QCoreApplication.translate("Nugget", u"    Apply", None))
        self.applyPageBtn.setProperty("cls", QCoreApplication.translate("Nugget", u"sidebarBtn", None))
        self.settingsPageBtn.setText(QCoreApplication.translate("Nugget", u"    Settings", None))
        self.settingsPageBtn.setProperty("cls", QCoreApplication.translate("Nugget", u"sidebarBtn", None))
        self.phoneNameLbl.setText(QCoreApplication.translate("Nugget", u"Phone", None))
        self.phoneVersionLbl.setText(QCoreApplication.translate("Nugget", u"<a style=\"text-decoration:none; color: white\" href=\"#\">Version</a>", None))
        self.bigNuggetBtn.setText(QCoreApplication.translate("Nugget", u"...", None))
        self.label_2.setText(QCoreApplication.translate("Nugget", u"Nugget", None))
        self.discordBtn.setText(QCoreApplication.translate("Nugget", u"  Join the Discord", None))
        self.leminBtn.setText(QCoreApplication.translate("Nugget", u"  LeminLimez", None))
        self.leminTwitterBtn.setText(QCoreApplication.translate("Nugget", u"...", None))
        self.leminKoFiBtn.setText(QCoreApplication.translate("Nugget", u"...", None))
        self.toolButton_14.setText(QCoreApplication.translate("Nugget", u"Main Developer", None))
        self.helpFromBtn.setText(QCoreApplication.translate("Nugget", u"With Help From", None))
        self.jjtechBtn.setText(QCoreApplication.translate("Nugget", u"JJTech\n"
"Sparserestore", None))
        self.disfordottieBtn.setText(QCoreApplication.translate("Nugget", u"disfordottie\n"
"Clock Anim, Photos UI", None))
        self.lrdsnowBtn.setText(QCoreApplication.translate("Nugget", u"lrdsnow\n"
"EU Enabler", None))
        self.toolButton_15.setText(QCoreApplication.translate("Nugget", u"Additional Thanks", None))
        self.libiBtn.setText(QCoreApplication.translate("Nugget", u"pymobiledevice3", None))
        self.qtBtn.setText(QCoreApplication.translate("Nugget", u"Qt Creator", None))
        self.label.setText(QCoreApplication.translate("Nugget", u"Nugget GUI - Version 2.2", None))
        self.exploreLbl.setText(QCoreApplication.translate("Nugget", u"Explore", None))
        self.exploreSubLbl.setText("")
        self.statusBarLbl_2.setText(QCoreApplication.translate("Nugget", u"Location Simulation", None))
        self.label_4.setText("")
        self.loadLocSimBtn.setText(QCoreApplication.translate("Nugget", u"Start Location Simulation", None))
        self.label_7.setText(QCoreApplication.translate("Nugget", u"Latitude", None))
        self.latitudeTxt.setPlaceholderText(QCoreApplication.translate("Nugget", u"XXX.XXXXX", None))
        self.label_11.setText(QCoreApplication.translate("Nugget", u"Longitude", None))
        self.longitudeTxt.setPlaceholderText(QCoreApplication.translate("Nugget", u"XXX.XXXXX", None))
        self.setLocationBtn.setText(QCoreApplication.translate("Nugget", u"Set Location", None))
        self.resetLocationBtn.setText(QCoreApplication.translate("Nugget", u"Reset Location", None))
        self.themesLbl.setText(QCoreApplication.translate("Nugget", u"Mobile Gestalt Modifications", None))
        self.importThemeBtn.setText(QCoreApplication.translate("Nugget", u"Import Theme:", None))
        self.importThemeFolderBtn.setText(QCoreApplication.translate("Nugget", u"...", None))
        self.importThemeZipBtn.setText(QCoreApplication.translate("Nugget", u"...", None))
        self.label_3.setText(QCoreApplication.translate("Nugget", u"Customize Individual Apps", None))
        self.hideNamesBtn.setText(QCoreApplication.translate("Nugget", u"Hide/Show All App Names", None))
        self.borderAllBtn.setText(QCoreApplication.translate("Nugget", u"Toggle All \"Border\"", None))
        self.addAllBtn.setText(QCoreApplication.translate("Nugget", u"Toggle All \"Add to Device\"", None))
        self.statusBarLbl.setText(QCoreApplication.translate("Nugget", u"Mobile Gestalt", None))
        self.label_9.setText(QCoreApplication.translate("Nugget", u"Device Subtype Preset", None))
        self.dynamicIslandDrp.setItemText(0, QCoreApplication.translate("Nugget", u"None", None))
        self.dynamicIslandDrp.setItemText(1, QCoreApplication.translate("Nugget", u"2436 (iPhone X Gestures for SE phones)", None))
        self.dynamicIslandDrp.setItemText(2, QCoreApplication.translate("Nugget", u"2556 (iPhone 14 Pro Dynamic Island)", None))
        self.dynamicIslandDrp.setItemText(3, QCoreApplication.translate("Nugget", u"2796 (iPhone 14 Pro Max Dynamic Island)", None))
        self.dynamicIslandDrp.setItemText(4, QCoreApplication.translate("Nugget", u"2976 (iPhone 15 Pro Max Dynamic Island)", None))
        self.dynamicIslandDrp.setItemText(5, QCoreApplication.translate("Nugget", u"2622 (iPhone 16 Pro Dynamic Island)", None))
        self.dynamicIslandDrp.setItemText(6, QCoreApplication.translate("Nugget", u"2868 (iPhone 16 Pro Max Dynamic Island)", None))

        self.dynamicIslandDrp.setCurrentText(QCoreApplication.translate("Nugget", u"None", None))
        self.modelNameChk.setText(QCoreApplication.translate("Nugget", u"Change Device Model Name", None))
        self.modelNameTxt.setPlaceholderText(QCoreApplication.translate("Nugget", u"Model Name", None))
        self.bootChimeChk.setText(QCoreApplication.translate("Nugget", u"Enable Boot Chime", None))
        self.chargeLimitChk.setText(QCoreApplication.translate("Nugget", u"Enable Charge Limit", None))
        self.tapToWakeChk.setText(QCoreApplication.translate("Nugget", u"Enable Tap to Wake (for iPhone SEs)", None))
        self.iphone16SettingsChk.setText(QCoreApplication.translate("Nugget", u"Enable iPhone 16 Settings", None))
        self.parallaxChk.setText(QCoreApplication.translate("Nugget", u"Disable Wallpaper Parallax", None))
        self.stageManagerChk.setText(QCoreApplication.translate("Nugget", u"Enable Stage Manager Supported (WARNING: risky on some devices, mainly phones)", None))
        self.ipadAppsChk.setText(QCoreApplication.translate("Nugget", u"Allow iPad Apps on iPhone", None))
        self.shutterChk.setText(QCoreApplication.translate("Nugget", u"Disable Region Restrictions (ie. Shutter Sound)", None))
        self.pencilChk.setText(QCoreApplication.translate("Nugget", u"Enable Apple Pencil Settings Tab", None))
        self.actionButtonChk.setText(QCoreApplication.translate("Nugget", u"Enable Action Button Settings Tab", None))
        self.internalInstallChk.setText(QCoreApplication.translate("Nugget", u"Set as Apple Internal Install (ie Metal HUD in any app)", None))
        self.internalStorageChk.setText(QCoreApplication.translate("Nugget", u"Enable Internal Storage (WARNING: risky for some devices, mainly iPads)", None))
        self.collisionSOSChk.setText(QCoreApplication.translate("Nugget", u"Enable Collision SOS", None))
        self.sleepApneaChk.setText(QCoreApplication.translate("Nugget", u"Enable Sleep Apnea (real) [for Apple Watches]", None))
        self.aodChk.setText(QCoreApplication.translate("Nugget", u"Enable Always On Display", None))
        self.customOperationsLbl.setText(QCoreApplication.translate("Nugget", u"Custom Operations", None))
        self.label_14.setText("")
        self.importOperationBtn.setText(QCoreApplication.translate("Nugget", u"  Import .cowperation", None))
        self.newOperationBtn.setText(QCoreApplication.translate("Nugget", u"  New Operation", None))
        self.springboardOptionsLbl.setText(QCoreApplication.translate("Nugget", u"Nugget Settings", None))
        self.allowWifiApplyingChk.setText(QCoreApplication.translate("Nugget", u"Allow Applying Over WiFi", None))
        self.internalOptionsLbl.setText(QCoreApplication.translate("Nugget", u"Feature Flags", None))
        self.clockAnimChk.setText(QCoreApplication.translate("Nugget", u"Enable Lockscreen Clock Animation", None))
        self.lockscreenChk.setText(QCoreApplication.translate("Nugget", u"Enable Duplicate Lockscreen Button and Lockscreen Quickswitch", None))
        self.photosChk.setText(QCoreApplication.translate("Nugget", u"Enable Old Photo UI", None))
        self.aiChk.setText(QCoreApplication.translate("Nugget", u"Enable Apple Intelligence", None))
        self.setupOptionsLbl.setText(QCoreApplication.translate("Nugget", u"EU Enabler", None))
        self.euEnablerEnabledChk.setText(QCoreApplication.translate("Nugget", u"Enabled", None))
        self.label_5.setText(QCoreApplication.translate("Nugget", u"Method Type", None))
        self.methodChoiceDrp.setItemText(0, QCoreApplication.translate("Nugget", u"Method 1", None))
        self.methodChoiceDrp.setItemText(1, QCoreApplication.translate("Nugget", u"Method 2", None))

        self.label_6.setText(QCoreApplication.translate("Nugget", u"Region Code (Should be 2 letters)", None))
        self.regionCodeTxt.setPlaceholderText(QCoreApplication.translate("Nugget", u"Region Code (Default: US)", None))
        self.statusBarLbl_5.setText(QCoreApplication.translate("Nugget", u"Apply", None))
        self.label_16.setText("")
        self.modifiedTweaksLbl.setText(QCoreApplication.translate("Nugget", u"Current gestalt file location:", None))
        self.gestaltLocationLbl.setText(QCoreApplication.translate("Nugget", u"None", None))
        self.chooseGestaltBtn.setText(QCoreApplication.translate("Nugget", u"  Choose Gestalt File", None))
        self.applyTweaksBtn.setText(QCoreApplication.translate("Nugget", u"  Apply Changes", None))
        self.statusLbl.setText(QCoreApplication.translate("Nugget", u"Ready!", None))
        self.removeTweaksBtn.setText(QCoreApplication.translate("Nugget", u"Remove All Tweaks", None))
        self.resetGestaltBtn.setText(QCoreApplication.translate("Nugget", u"Reset Mobile Gestalt", None))
    # retranslateUi

