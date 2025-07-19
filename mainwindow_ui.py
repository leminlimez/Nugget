# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QProgressBar, QRadioButton,
    QScrollArea, QSizePolicy, QSlider, QSpacerItem,
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
        Nugget.setWindowTitle(u"Nugget")
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
        self.centralwidget.setProperty(u"cls", u"central")
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
        self.phoneIconBtn = QToolButton(self.horizontalWidget_3)
        self.phoneIconBtn.setObjectName(u"phoneIconBtn")
        self.phoneIconBtn.setEnabled(False)
        self.phoneIconBtn.setStyleSheet(u"QToolButton {\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/phone.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.phoneIconBtn.setIcon(icon)

        self.horizontalLayout_15.addWidget(self.phoneIconBtn)

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
        self.devicePicker.setProperty(u"placeholderText", u"None")

        self.horizontalLayout_15.addWidget(self.devicePicker)


        self.horizontalLayout_19.addWidget(self.horizontalWidget_3)

        self.refreshBtn = QToolButton(self.horizontalWidget_2)
        self.refreshBtn.setObjectName(u"refreshBtn")
        self.refreshBtn.setStyleSheet(u"QToolButton {\n"
"	border-radius: 0px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/arrow-clockwise.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.refreshBtn.setIcon(icon1)
        self.refreshBtn.setCheckable(False)
        self.refreshBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.refreshBtn.setProperty(u"cls", u"btn")

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
        self.titleBar.setText(u"Nugget")

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
        icon2.addFile(u":/icon/house.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.homePageBtn.setIcon(icon2)
        self.homePageBtn.setCheckable(True)
        self.homePageBtn.setChecked(True)
        self.homePageBtn.setAutoExclusive(True)
        self.homePageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.homePageBtn.setProperty(u"cls", u"sidebarBtn")

        self.verticalLayout.addWidget(self.homePageBtn)

        self.sidebarDiv1 = QFrame(self.sidebar)
        self.sidebarDiv1.setObjectName(u"sidebarDiv1")
        self.sidebarDiv1.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.sidebarDiv1.setFrameShadow(QFrame.Plain)
        self.sidebarDiv1.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout.addWidget(self.sidebarDiv1)

        self.posterboardPageBtn = QToolButton(self.sidebar)
        self.posterboardPageBtn.setObjectName(u"posterboardPageBtn")
        self.posterboardPageBtn.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.posterboardPageBtn.sizePolicy().hasHeightForWidth())
        self.posterboardPageBtn.setSizePolicy(sizePolicy2)
        icon3 = QIcon()
        icon3.addFile(u":/icon/wallpaper.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.posterboardPageBtn.setIcon(icon3)
        self.posterboardPageBtn.setCheckable(True)
        self.posterboardPageBtn.setAutoExclusive(True)
        self.posterboardPageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.posterboardPageBtn.setProperty(u"cls", u"sidebarBtn")

        self.verticalLayout.addWidget(self.posterboardPageBtn)

        self.gestaltPageBtn = QToolButton(self.sidebar)
        self.gestaltPageBtn.setObjectName(u"gestaltPageBtn")
        sizePolicy2.setHeightForWidth(self.gestaltPageBtn.sizePolicy().hasHeightForWidth())
        self.gestaltPageBtn.setSizePolicy(sizePolicy2)
        icon4 = QIcon()
        icon4.addFile(u":/icon/iphone-island.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.gestaltPageBtn.setIcon(icon4)
        self.gestaltPageBtn.setIconSize(QSize(24, 28))
        self.gestaltPageBtn.setCheckable(True)
        self.gestaltPageBtn.setAutoExclusive(True)
        self.gestaltPageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.gestaltPageBtn.setArrowType(Qt.NoArrow)
        self.gestaltPageBtn.setProperty(u"cls", u"sidebarBtn")

        self.verticalLayout.addWidget(self.gestaltPageBtn)

        self.featureFlagsPageBtn = QToolButton(self.sidebar)
        self.featureFlagsPageBtn.setObjectName(u"featureFlagsPageBtn")
        sizePolicy2.setHeightForWidth(self.featureFlagsPageBtn.sizePolicy().hasHeightForWidth())
        self.featureFlagsPageBtn.setSizePolicy(sizePolicy2)
        font = QFont()
        self.featureFlagsPageBtn.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u":/icon/flag.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.featureFlagsPageBtn.setIcon(icon5)
        self.featureFlagsPageBtn.setCheckable(True)
        self.featureFlagsPageBtn.setAutoExclusive(True)
        self.featureFlagsPageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.featureFlagsPageBtn.setProperty(u"cls", u"sidebarBtn")

        self.verticalLayout.addWidget(self.featureFlagsPageBtn)

        self.euEnablerPageBtn = QToolButton(self.sidebar)
        self.euEnablerPageBtn.setObjectName(u"euEnablerPageBtn")
        sizePolicy2.setHeightForWidth(self.euEnablerPageBtn.sizePolicy().hasHeightForWidth())
        self.euEnablerPageBtn.setSizePolicy(sizePolicy2)
        icon6 = QIcon()
        icon6.addFile(u":/icon/geo-alt.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.euEnablerPageBtn.setIcon(icon6)
        self.euEnablerPageBtn.setCheckable(True)
        self.euEnablerPageBtn.setAutoExclusive(True)
        self.euEnablerPageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.euEnablerPageBtn.setProperty(u"cls", u"sidebarBtn")

        self.verticalLayout.addWidget(self.euEnablerPageBtn)

        self.statusBarPageBtn = QToolButton(self.sidebar)
        self.statusBarPageBtn.setObjectName(u"statusBarPageBtn")
        sizePolicy2.setHeightForWidth(self.statusBarPageBtn.sizePolicy().hasHeightForWidth())
        self.statusBarPageBtn.setSizePolicy(sizePolicy2)
        icon7 = QIcon()
        icon7.addFile(u":/icon/wifi.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.statusBarPageBtn.setIcon(icon7)
        self.statusBarPageBtn.setCheckable(True)
        self.statusBarPageBtn.setAutoExclusive(True)
        self.statusBarPageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.statusBarPageBtn.setProperty(u"cls", u"sidebarBtn")

        self.verticalLayout.addWidget(self.statusBarPageBtn)

        self.templatesPageBtn = QToolButton(self.sidebar)
        self.templatesPageBtn.setObjectName(u"templatesPageBtn")
        self.templatesPageBtn.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.templatesPageBtn.sizePolicy().hasHeightForWidth())
        self.templatesPageBtn.setSizePolicy(sizePolicy2)
        icon8 = QIcon()
        icon8.addFile(u":/icon/pencil.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.templatesPageBtn.setIcon(icon8)
        self.templatesPageBtn.setCheckable(True)
        self.templatesPageBtn.setAutoExclusive(True)
        self.templatesPageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.templatesPageBtn.setProperty(u"cls", u"sidebarBtn")

        self.verticalLayout.addWidget(self.templatesPageBtn)

        self.miscOptionsBtn = QToolButton(self.sidebar)
        self.miscOptionsBtn.setObjectName(u"miscOptionsBtn")
        sizePolicy2.setHeightForWidth(self.miscOptionsBtn.sizePolicy().hasHeightForWidth())
        self.miscOptionsBtn.setSizePolicy(sizePolicy2)
        icon9 = QIcon()
        icon9.addFile(u":/icon/ellipsis.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.miscOptionsBtn.setIcon(icon9)
        self.miscOptionsBtn.setCheckable(True)
        self.miscOptionsBtn.setAutoExclusive(True)
        self.miscOptionsBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.miscOptionsBtn.setProperty(u"cls", u"sidebarBtn")

        self.verticalLayout.addWidget(self.miscOptionsBtn)

        self.sidebarDiv2 = QFrame(self.sidebar)
        self.sidebarDiv2.setObjectName(u"sidebarDiv2")
        self.sidebarDiv2.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.sidebarDiv2.setFrameShadow(QFrame.Plain)
        self.sidebarDiv2.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout.addWidget(self.sidebarDiv2)

        self.applyPageBtn = QToolButton(self.sidebar)
        self.applyPageBtn.setObjectName(u"applyPageBtn")
        sizePolicy2.setHeightForWidth(self.applyPageBtn.sizePolicy().hasHeightForWidth())
        self.applyPageBtn.setSizePolicy(sizePolicy2)
        icon10 = QIcon()
        icon10.addFile(u":/icon/check-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.applyPageBtn.setIcon(icon10)
        self.applyPageBtn.setCheckable(True)
        self.applyPageBtn.setAutoExclusive(True)
        self.applyPageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.applyPageBtn.setProperty(u"cls", u"sidebarBtn")

        self.verticalLayout.addWidget(self.applyPageBtn)

        self.settingsPageBtn = QToolButton(self.sidebar)
        self.settingsPageBtn.setObjectName(u"settingsPageBtn")
        sizePolicy2.setHeightForWidth(self.settingsPageBtn.sizePolicy().hasHeightForWidth())
        self.settingsPageBtn.setSizePolicy(sizePolicy2)
        icon11 = QIcon()
        icon11.addFile(u":/icon/gear.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsPageBtn.setIcon(icon11)
        self.settingsPageBtn.setCheckable(True)
        self.settingsPageBtn.setAutoExclusive(True)
        self.settingsPageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.settingsPageBtn.setProperty(u"cls", u"sidebarBtn")

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
        font1 = QFont()
        font1.setFamilies([u".AppleSystemUIFont"])
        self.homePage.setFont(font1)
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
        self.phoneNameLbl.setFont(font)
        self.phoneNameLbl.setText(u"Phone")

        self.verticalLayout_3.addWidget(self.phoneNameLbl)

        self.phoneVersionLbl = QLabel(self.verticalWidget)
        self.phoneVersionLbl.setObjectName(u"phoneVersionLbl")
        self.phoneVersionLbl.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.phoneVersionLbl.setText(u"<a style=\"text-decoration:none; color: white\" href=\"#\">Version</a>")
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
        self.line_4.setFrameShape(QFrame.Shape.HLine)

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
        icon12 = QIcon()
        icon12.addFile(u":/credits/big_nugget.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bigNuggetBtn.setIcon(icon12)
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
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"QLabel {\n"
"	font-size: 35px;\n"
"}")
        self.label_2.setText(u"Nugget")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_2)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_12)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, -1, 0, 0)
        self.discordBtn = QToolButton(self.verticalWidget1)
        self.discordBtn.setObjectName(u"discordBtn")
        icon13 = QIcon()
        icon13.addFile(u":/icon/discord.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.discordBtn.setIcon(icon13)
        self.discordBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_8.addWidget(self.discordBtn)

        self.starOnGithubBtn = QToolButton(self.verticalWidget1)
        self.starOnGithubBtn.setObjectName(u"starOnGithubBtn")
        icon14 = QIcon()
        icon14.addFile(u":/icon/star.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.starOnGithubBtn.setIcon(icon14)
        self.starOnGithubBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_8.addWidget(self.starOnGithubBtn)


        self.verticalLayout_26.addLayout(self.horizontalLayout_8)

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
        icon15 = QIcon()
        icon15.addFile(u":/credits/LeminLimez.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.leminBtn.setIcon(icon15)
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
        icon16 = QIcon()
        icon16.addFile(u":/icon/twitter.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.leminTwitterBtn.setIcon(icon16)

        self.horizontalLayout_6.addWidget(self.leminTwitterBtn)

        self.leminGithubBtn = QToolButton(self.horizontalWidget2)
        self.leminGithubBtn.setObjectName(u"leminGithubBtn")
        self.leminGithubBtn.setStyleSheet(u"QToolButton {\n"
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
        icon17 = QIcon()
        icon17.addFile(u":/icon/github.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.leminGithubBtn.setIcon(icon17)

        self.horizontalLayout_6.addWidget(self.leminGithubBtn)

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
        icon18 = QIcon()
        icon18.addFile(u":/icon/currency-dollar.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.leminKoFiBtn.setIcon(icon18)

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
        self.helpFromBtn.setMinimumSize(QSize(140, 35))
        self.helpFromBtn.setStyleSheet(u"QToolButton {\n"
"	background: none;\n"
"}")
        self.helpFromBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_2.addWidget(self.helpFromBtn)

        self.posterRestoreBtn = QToolButton(self.horizontalWidget_21)
        self.posterRestoreBtn.setObjectName(u"posterRestoreBtn")
        sizePolicy2.setHeightForWidth(self.posterRestoreBtn.sizePolicy().hasHeightForWidth())
        self.posterRestoreBtn.setSizePolicy(sizePolicy2)
        self.posterRestoreBtn.setMinimumSize(QSize(0, 37))
        self.posterRestoreBtn.setStyleSheet(u"QToolButton {\n"
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

        self.horizontalLayout_2.addWidget(self.posterRestoreBtn)

        self.snoolieBtn = QToolButton(self.horizontalWidget_21)
        self.snoolieBtn.setObjectName(u"snoolieBtn")
        self.snoolieBtn.setStyleSheet(u"QToolButton {\n"
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

        self.horizontalLayout_2.addWidget(self.snoolieBtn)

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

        self.mikasaBtn = QToolButton(self.horizontalWidget_21)
        self.mikasaBtn.setObjectName(u"mikasaBtn")
        sizePolicy2.setHeightForWidth(self.mikasaBtn.sizePolicy().hasHeightForWidth())
        self.mikasaBtn.setSizePolicy(sizePolicy2)
        self.mikasaBtn.setMinimumSize(QSize(0, 37))
        self.mikasaBtn.setStyleSheet(u"QToolButton {\n"
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

        self.horizontalLayout_2.addWidget(self.mikasaBtn)


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
        self.toolButton_15.setMinimumSize(QSize(145, 35))
        self.toolButton_15.setStyleSheet(u"QToolButton {\n"
"	background: none;\n"
"}")

        self.horizontalLayout_24.addWidget(self.toolButton_15)

        self.translatorsBtn = QToolButton(self.horizontalWidget3)
        self.translatorsBtn.setObjectName(u"translatorsBtn")
        self.translatorsBtn.setStyleSheet(u"QToolButton {\n"
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

        self.horizontalLayout_24.addWidget(self.translatorsBtn)

        self.libiBtn = QToolButton(self.horizontalWidget3)
        self.libiBtn.setObjectName(u"libiBtn")
        sizePolicy2.setHeightForWidth(self.libiBtn.sizePolicy().hasHeightForWidth())
        self.libiBtn.setSizePolicy(sizePolicy2)
        self.libiBtn.setStyleSheet(u"QToolButton {\n"
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

        self.horizontalLayout_24.addWidget(self.libiBtn)

        self.jjtechBtn = QToolButton(self.horizontalWidget3)
        self.jjtechBtn.setObjectName(u"jjtechBtn")
        sizePolicy2.setHeightForWidth(self.jjtechBtn.sizePolicy().hasHeightForWidth())
        self.jjtechBtn.setSizePolicy(sizePolicy2)
        self.jjtechBtn.setStyleSheet(u"QToolButton {\n"
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

        self.horizontalLayout_24.addWidget(self.jjtechBtn)

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

        self.appVersionLbl = QLabel(self.homePage)
        self.appVersionLbl.setObjectName(u"appVersionLbl")
        self.appVersionLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.appVersionLbl)

        self.pages.addWidget(self.homePage)
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
        self.toolButton_8.setIcon(icon4)
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
        self.statusBarLbl.setFont(font)

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
        self.line_8.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_4.addWidget(self.line_8)

        self.mgaWarningLbl = QLabel(self.gestaltPage)
        self.mgaWarningLbl.setObjectName(u"mgaWarningLbl")
        self.mgaWarningLbl.setFont(font)

        self.verticalLayout_4.addWidget(self.mgaWarningLbl)

        self.mgaScrollArea = QScrollArea(self.gestaltPage)
        self.mgaScrollArea.setObjectName(u"mgaScrollArea")
        self.mgaScrollArea.setFrameShape(QFrame.NoFrame)
        self.mgaScrollArea.setFrameShadow(QFrame.Plain)
        self.mgaScrollArea.setLineWidth(0)
        self.mgaScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
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
        self.gestaltPageContent.setEnabled(True)
        self.verticalLayout_8 = QVBoxLayout(self.gestaltPageContent)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.gestaltPageContent)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_8.addWidget(self.label_9)

        self.dynamicIslandDrp = QComboBox(self.gestaltPageContent)
        self.dynamicIslandDrp.addItem(u"None")
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
        self.dynamicIslandDrp.setCurrentText(u"None")
        self.dynamicIslandDrp.setMaxVisibleItems(15)
        self.dynamicIslandDrp.setProperty(u"placeholderText", u"")

        self.verticalLayout_8.addWidget(self.dynamicIslandDrp)

        self.rdarFixChk = QCheckBox(self.gestaltPageContent)
        self.rdarFixChk.setObjectName(u"rdarFixChk")
        self.rdarFixChk.setText(u"Fix RDAR (modifies resolution)")

        self.verticalLayout_8.addWidget(self.rdarFixChk)

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

        self.line_7 = QFrame(self.gestaltPageContent)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_7.setFrameShadow(QFrame.Plain)
        self.line_7.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_8.addWidget(self.line_7)

        self.stageManagerChk = QCheckBox(self.gestaltPageContent)
        self.stageManagerChk.setObjectName(u"stageManagerChk")

        self.verticalLayout_8.addWidget(self.stageManagerChk)

        self.enableMedusaChk = QCheckBox(self.gestaltPageContent)
        self.enableMedusaChk.setObjectName(u"enableMedusaChk")

        self.verticalLayout_8.addWidget(self.enableMedusaChk)

        self.ipadAppsChk = QCheckBox(self.gestaltPageContent)
        self.ipadAppsChk.setObjectName(u"ipadAppsChk")

        self.verticalLayout_8.addWidget(self.ipadAppsChk)

        self.shutterChk = QCheckBox(self.gestaltPageContent)
        self.shutterChk.setObjectName(u"shutterChk")

        self.verticalLayout_8.addWidget(self.shutterChk)

        self.findMyFriendsChk = QCheckBox(self.gestaltPageContent)
        self.findMyFriendsChk.setObjectName(u"findMyFriendsChk")

        self.verticalLayout_8.addWidget(self.findMyFriendsChk)

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
        self.line_9.setFrameShape(QFrame.Shape.HLine)

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
        self.line_10.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_8.addWidget(self.line_10)

        self.collisionSOSChk = QCheckBox(self.gestaltPageContent)
        self.collisionSOSChk.setObjectName(u"collisionSOSChk")

        self.verticalLayout_8.addWidget(self.collisionSOSChk)

        self.aodChk = QCheckBox(self.gestaltPageContent)
        self.aodChk.setObjectName(u"aodChk")

        self.verticalLayout_8.addWidget(self.aodChk)

        self.aodVibrancyChk = QCheckBox(self.gestaltPageContent)
        self.aodVibrancyChk.setObjectName(u"aodVibrancyChk")

        self.verticalLayout_8.addWidget(self.aodVibrancyChk)

        self.line_22 = QFrame(self.gestaltPageContent)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_22.setFrameShadow(QFrame.Plain)
        self.line_22.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_8.addWidget(self.line_22)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, -1, -1, 0)
        self.label_10 = QLabel(self.gestaltPageContent)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setEnabled(True)

        self.horizontalLayout_11.addWidget(self.label_10)

        self.addGestaltKeyBtn = QToolButton(self.gestaltPageContent)
        self.addGestaltKeyBtn.setObjectName(u"addGestaltKeyBtn")
        self.addGestaltKeyBtn.setEnabled(True)
        icon19 = QIcon()
        icon19.addFile(u":/icon/plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addGestaltKeyBtn.setIcon(icon19)
        self.addGestaltKeyBtn.setCheckable(False)
        self.addGestaltKeyBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_11.addWidget(self.addGestaltKeyBtn)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)

        self.label_12 = QLabel(self.gestaltPageContent)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_8.addWidget(self.label_12)

        self.line_23 = QFrame(self.gestaltPageContent)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_23.setFrameShadow(QFrame.Plain)
        self.line_23.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_8.addWidget(self.line_23)

        self.customKeysCnt = QWidget(self.gestaltPageContent)
        self.customKeysCnt.setObjectName(u"customKeysCnt")
        self.customKeysCnt.setEnabled(True)
        self.verticalLayout_32 = QVBoxLayout(self.customKeysCnt)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.customKeysLayout = QVBoxLayout()
        self.customKeysLayout.setObjectName(u"customKeysLayout")

        self.verticalLayout_32.addLayout(self.customKeysLayout)


        self.verticalLayout_8.addWidget(self.customKeysCnt)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)


        self.verticalLayout_9.addWidget(self.gestaltPageContent)

        self.mgaScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.mgaScrollArea)

        self.pages.addWidget(self.gestaltPage)
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
        self.toolButton_10.setIcon(icon5)

        self.horizontalLayout_20.addWidget(self.toolButton_10)

        self.verticalWidget_4 = QWidget(self.horizontalWidget_5)
        self.verticalWidget_4.setObjectName(u"verticalWidget_4")
        self.verticalLayout_12 = QVBoxLayout(self.verticalWidget_4)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.internalOptionsLbl = QLabel(self.verticalWidget_4)
        self.internalOptionsLbl.setObjectName(u"internalOptionsLbl")
        self.internalOptionsLbl.setFont(font)

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
        self.line_12.setFrameShape(QFrame.Shape.HLine)

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
        self.div.setFrameShape(QFrame.Shape.HLine)

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
        self.toolButton_11.setIcon(icon6)

        self.horizontalLayout_21.addWidget(self.toolButton_11)

        self.verticalWidget_5 = QWidget(self.horizontalWidget_6)
        self.verticalWidget_5.setObjectName(u"verticalWidget_5")
        self.verticalLayout_15 = QVBoxLayout(self.verticalWidget_5)
        self.verticalLayout_15.setSpacing(6)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.eligibilityLbl = QLabel(self.verticalWidget_5)
        self.eligibilityLbl.setObjectName(u"eligibilityLbl")
        self.eligibilityLbl.setFont(font)

        self.verticalLayout_15.addWidget(self.eligibilityLbl)

        self.verticalSpacer_20 = QSpacerItem(20, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_15.addItem(self.verticalSpacer_20)


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
        self.line_13.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_17.addWidget(self.line_13)

        self.scrollArea_2 = QScrollArea(self.euEnablerPage)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 619, 535))
        self.verticalLayout_37 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.euEnablerPageContent = QWidget(self.scrollAreaWidgetContents_2)
        self.euEnablerPageContent.setObjectName(u"euEnablerPageContent")
        self.euEnablerPageContent.setEnabled(False)
        self.verticalLayout_16 = QVBoxLayout(self.euEnablerPageContent)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.euEnablerContent = QWidget(self.euEnablerPageContent)
        self.euEnablerContent.setObjectName(u"euEnablerContent")
        self.verticalLayout_36 = QVBoxLayout(self.euEnablerContent)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.euEnablerEnabledChk = QCheckBox(self.euEnablerContent)
        self.euEnablerEnabledChk.setObjectName(u"euEnablerEnabledChk")

        self.verticalLayout_36.addWidget(self.euEnablerEnabledChk)

        self.label_5 = QLabel(self.euEnablerContent)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_36.addWidget(self.label_5)

        self.methodChoiceDrp = QComboBox(self.euEnablerContent)
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

        self.verticalLayout_36.addWidget(self.methodChoiceDrp)

        self.label_6 = QLabel(self.euEnablerContent)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_36.addWidget(self.label_6)

        self.regionCodeTxt = QLineEdit(self.euEnablerContent)
        self.regionCodeTxt.setObjectName(u"regionCodeTxt")

        self.verticalLayout_36.addWidget(self.regionCodeTxt)

        self.line_16 = QFrame(self.euEnablerContent)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setEnabled(False)
        self.line_16.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_16.setFrameShadow(QFrame.Plain)
        self.line_16.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_36.addWidget(self.line_16)


        self.verticalLayout_16.addWidget(self.euEnablerContent)

        self.mgaWarningLbl2 = QLabel(self.euEnablerPageContent)
        self.mgaWarningLbl2.setObjectName(u"mgaWarningLbl2")
        self.mgaWarningLbl2.setFont(font)

        self.verticalLayout_16.addWidget(self.mgaWarningLbl2)

        self.enableAIChk = QCheckBox(self.euEnablerPageContent)
        self.enableAIChk.setObjectName(u"enableAIChk")

        self.verticalLayout_16.addWidget(self.enableAIChk)

        self.aiEnablerContent = QWidget(self.euEnablerPageContent)
        self.aiEnablerContent.setObjectName(u"aiEnablerContent")
        self.verticalLayout_34 = QVBoxLayout(self.aiEnablerContent)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 5, 0, 5)
        self.eligFileChk = QCheckBox(self.aiEnablerContent)
        self.eligFileChk.setObjectName(u"eligFileChk")

        self.verticalLayout_34.addWidget(self.eligFileChk)

        self.languageLbl = QLabel(self.aiEnablerContent)
        self.languageLbl.setObjectName(u"languageLbl")

        self.verticalLayout_34.addWidget(self.languageLbl)

        self.languageTxt = QLineEdit(self.aiEnablerContent)
        self.languageTxt.setObjectName(u"languageTxt")

        self.verticalLayout_34.addWidget(self.languageTxt)

        self.line_21 = QFrame(self.aiEnablerContent)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_21.setFrameShadow(QFrame.Plain)
        self.line_21.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_34.addWidget(self.line_21)

        self.aiInfoLabel = QLabel(self.aiEnablerContent)
        self.aiInfoLabel.setObjectName(u"aiInfoLabel")
        sizePolicy1.setHeightForWidth(self.aiInfoLabel.sizePolicy().hasHeightForWidth())
        self.aiInfoLabel.setSizePolicy(sizePolicy1)
        self.aiInfoLabel.setMaximumSize(QSize(16777215, 16777215))
        self.aiInfoLabel.setTextFormat(Qt.AutoText)
        self.aiInfoLabel.setScaledContents(False)

        self.verticalLayout_34.addWidget(self.aiInfoLabel)

        self.label_8 = QLabel(self.aiEnablerContent)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_34.addWidget(self.label_8)

        self.spoofedModelDrp = QComboBox(self.aiEnablerContent)
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.addItem("")
        self.spoofedModelDrp.setObjectName(u"spoofedModelDrp")
        self.spoofedModelDrp.setMaximumSize(QSize(325, 16777215))
        self.spoofedModelDrp.setStyleSheet(u"QComboBox {\n"
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

        self.verticalLayout_34.addWidget(self.spoofedModelDrp)

        self.spoofHardwareChk = QCheckBox(self.aiEnablerContent)
        self.spoofHardwareChk.setObjectName(u"spoofHardwareChk")
        self.spoofHardwareChk.setChecked(True)

        self.verticalLayout_34.addWidget(self.spoofHardwareChk)

        self.spoofCPUChk = QCheckBox(self.aiEnablerContent)
        self.spoofCPUChk.setObjectName(u"spoofCPUChk")
        self.spoofCPUChk.setChecked(True)

        self.verticalLayout_34.addWidget(self.spoofCPUChk)


        self.verticalLayout_16.addWidget(self.aiEnablerContent)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_7)


        self.verticalLayout_37.addWidget(self.euEnablerPageContent)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_17.addWidget(self.scrollArea_2)

        self.pages.addWidget(self.euEnablerPage)
        self.statusBarPage = QWidget()
        self.statusBarPage.setObjectName(u"statusBarPage")
        self.verticalLayout_41 = QVBoxLayout(self.statusBarPage)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.statusBarPageHeader1 = QWidget(self.statusBarPage)
        self.statusBarPageHeader1.setObjectName(u"statusBarPageHeader1")
        self.horizontalLayout_51 = QHBoxLayout(self.statusBarPageHeader1)
        self.horizontalLayout_51.setSpacing(10)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, -1, 0, -1)
        self.toolButton_81 = QToolButton(self.statusBarPageHeader1)
        self.toolButton_81.setObjectName(u"toolButton_81")
        self.toolButton_81.setEnabled(False)
        self.toolButton_81.setStyleSheet(u"QToolButton {\n"
"    icon-size: 24px;\n"
"    background-color: transparent;\n"
"    padding-left: 0px;\n"
"    padding-right: 5px;\n"
"    border-radius: 0px;\n"
"}")
        self.toolButton_81.setIcon(icon7)

        self.horizontalLayout_51.addWidget(self.toolButton_81)

        self.verticalWidget_22 = QWidget(self.statusBarPageHeader1)
        self.verticalWidget_22.setObjectName(u"verticalWidget_22")
        self.verticalLayout_51 = QVBoxLayout(self.verticalWidget_22)
        self.verticalLayout_51.setSpacing(6)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.statusBarLbl1 = QLabel(self.verticalWidget_22)
        self.statusBarLbl1.setObjectName(u"statusBarLbl1")
        self.statusBarLbl1.setFont(font)

        self.verticalLayout_51.addWidget(self.statusBarLbl1)

        self.statusBarEnabledChk = QCheckBox(self.verticalWidget_22)
        self.statusBarEnabledChk.setObjectName(u"statusBarEnabledChk")

        self.verticalLayout_51.addWidget(self.statusBarEnabledChk)


        self.horizontalLayout_51.addWidget(self.verticalWidget_22)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_51.addItem(self.horizontalSpacer_41)


        self.verticalLayout_41.addWidget(self.statusBarPageHeader1)

        self.line_81 = QFrame(self.statusBarPage)
        self.line_81.setObjectName(u"line_81")
        self.line_81.setStyleSheet(u"QFrame {\n"
"    color: #414141;\n"
"}")
        self.line_81.setFrameShadow(QFrame.Plain)
        self.line_81.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_41.addWidget(self.line_81)

        self.sbScrollArea = QScrollArea(self.statusBarPage)
        self.sbScrollArea.setObjectName(u"sbScrollArea")
        self.sbScrollArea.setFrameShape(QFrame.NoFrame)
        self.sbScrollArea.setFrameShadow(QFrame.Plain)
        self.sbScrollArea.setLineWidth(0)
        self.sbScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollAreaWidgetContents1 = QWidget()
        self.scrollAreaWidgetContents1.setObjectName(u"scrollAreaWidgetContents1")
        self.scrollAreaWidgetContents1.setGeometry(QRect(0, 0, 650, 2000))
        self.scrollAreaWidgetContents1.setMinimumSize(QSize(650, 2000))
        self.scrollAreaWidgetContents1.setMaximumSize(QSize(650, 2000))
        self.verticalLayout_91 = QVBoxLayout(self.scrollAreaWidgetContents1)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.verticalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.statusBarPageContent = QWidget(self.scrollAreaWidgetContents1)
        self.statusBarPageContent.setObjectName(u"statusBarPageContent")
        self.statusBarPageContent.setEnabled(False)
        self.verticalLayout_81 = QVBoxLayout(self.statusBarPageContent)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.label_91 = QLabel(self.statusBarPageContent)
        self.label_91.setObjectName(u"label_91")

        self.verticalLayout_81.addWidget(self.label_91)

        self.horizontalWidget4 = QWidget(self.statusBarPageContent)
        self.horizontalWidget4.setObjectName(u"horizontalWidget4")
        sizePolicy4.setHeightForWidth(self.horizontalWidget4.sizePolicy().hasHeightForWidth())
        self.horizontalWidget4.setSizePolicy(sizePolicy4)
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalWidget4)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pDefaultRdo = QRadioButton(self.horizontalWidget4)
        self.pDefaultRdo.setObjectName(u"pDefaultRdo")
        self.pDefaultRdo.setChecked(True)

        self.horizontalLayout_7.addWidget(self.pDefaultRdo)

        self.pShowRdo = QRadioButton(self.horizontalWidget4)
        self.pShowRdo.setObjectName(u"pShowRdo")

        self.horizontalLayout_7.addWidget(self.pShowRdo)

        self.pHideRdo = QRadioButton(self.horizontalWidget4)
        self.pHideRdo.setObjectName(u"pHideRdo")

        self.horizontalLayout_7.addWidget(self.pHideRdo)

        self.horizontalSpacer1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer1)


        self.verticalLayout_81.addWidget(self.horizontalWidget4)

        self.pCarrierChk = QCheckBox(self.statusBarPageContent)
        self.pCarrierChk.setObjectName(u"pCarrierChk")

        self.verticalLayout_81.addWidget(self.pCarrierChk)

        self.pCarrierTxt = QLineEdit(self.statusBarPageContent)
        self.pCarrierTxt.setObjectName(u"pCarrierTxt")

        self.verticalLayout_81.addWidget(self.pCarrierTxt)

        self.pBadgeChk = QCheckBox(self.statusBarPageContent)
        self.pBadgeChk.setObjectName(u"pBadgeChk")

        self.verticalLayout_81.addWidget(self.pBadgeChk)

        self.pBadgeTxt = QLineEdit(self.statusBarPageContent)
        self.pBadgeTxt.setObjectName(u"pBadgeTxt")

        self.verticalLayout_81.addWidget(self.pBadgeTxt)

        self.pTypeChk = QCheckBox(self.statusBarPageContent)
        self.pTypeChk.setObjectName(u"pTypeChk")

        self.verticalLayout_81.addWidget(self.pTypeChk)

        self.pTypeDrp = QComboBox(self.statusBarPageContent)
        self.pTypeDrp.addItem("")
        self.pTypeDrp.addItem("")
        self.pTypeDrp.addItem("")
        self.pTypeDrp.addItem("")
        self.pTypeDrp.addItem("")
        self.pTypeDrp.addItem("")
        self.pTypeDrp.addItem("")
        self.pTypeDrp.addItem(u"1x")
        self.pTypeDrp.addItem("")
        self.pTypeDrp.addItem("")
        self.pTypeDrp.addItem("")
        self.pTypeDrp.addItem("")
        self.pTypeDrp.addItem("")
        self.pTypeDrp.addItem("")
        self.pTypeDrp.addItem("")
        self.pTypeDrp.setObjectName(u"pTypeDrp")
        self.pTypeDrp.setMinimumSize(QSize(0, 0))
        self.pTypeDrp.setMaximumSize(QSize(150, 16777215))
        self.pTypeDrp.setStyleSheet(u"QComboBox {\n"
"    background-color: #3b3b3b;\n"
"    border: none;\n"
"    color: #e8e8e8;\n"
"    font-size: 14px;\n"
"    padding-left: 8px;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    image: url(:/icon/caret-down-fill.svg);\n"
"    icon-size: 16px;\n"
"    subcontrol-position: right center;\n"
"    margin-right: 8px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #3b3b3b;\n"
"    outline: none;\n"
"    margin-top: 1px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    background-color: #3b3b3b;\n"
"    color: #e8e8e8;\n"
"    padding-left: 8px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #535353;\n"
"    color: #ffffff;\n"
"}")
        self.pTypeDrp.setMaxVisibleItems(15)

        self.verticalLayout_81.addWidget(self.pTypeDrp)

        self.pStrengthChk = QCheckBox(self.statusBarPageContent)
        self.pStrengthChk.setObjectName(u"pStrengthChk")

        self.verticalLayout_81.addWidget(self.pStrengthChk)

        self.horizontalWidget5 = QWidget(self.statusBarPageContent)
        self.horizontalWidget5.setObjectName(u"horizontalWidget5")
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalWidget5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.pStrengthLbl = QLabel(self.horizontalWidget5)
        self.pStrengthLbl.setObjectName(u"pStrengthLbl")
        self.pStrengthLbl.setMinimumSize(QSize(50, 0))
        self.pStrengthLbl.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_9.addWidget(self.pStrengthLbl)

        self.pStrengthSld = QSlider(self.horizontalWidget5)
        self.pStrengthSld.setObjectName(u"pStrengthSld")
        self.pStrengthSld.setMaximum(4)
        self.pStrengthSld.setSingleStep(0)
        self.pStrengthSld.setPageStep(0)
        self.pStrengthSld.setOrientation(Qt.Horizontal)

        self.horizontalLayout_9.addWidget(self.pStrengthSld)


        self.verticalLayout_81.addWidget(self.horizontalWidget5)

        self.line_91 = QFrame(self.statusBarPageContent)
        self.line_91.setObjectName(u"line_91")
        self.line_91.setStyleSheet(u"QFrame {\n"
"    color: #414141;\n"
"}")
        self.line_91.setFrameShadow(QFrame.Plain)
        self.line_91.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_81.addWidget(self.line_91)

        self.label_101 = QLabel(self.statusBarPageContent)
        self.label_101.setObjectName(u"label_101")

        self.verticalLayout_81.addWidget(self.label_101)

        self.horizontalWidget6 = QWidget(self.statusBarPageContent)
        self.horizontalWidget6.setObjectName(u"horizontalWidget6")
        self.horizontalLayout_81 = QHBoxLayout(self.horizontalWidget6)
        self.horizontalLayout_81.setSpacing(20)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.sDefaultRdo = QRadioButton(self.horizontalWidget6)
        self.sDefaultRdo.setObjectName(u"sDefaultRdo")
        self.sDefaultRdo.setChecked(True)

        self.horizontalLayout_81.addWidget(self.sDefaultRdo)

        self.sShowRdo = QRadioButton(self.horizontalWidget6)
        self.sShowRdo.setObjectName(u"sShowRdo")

        self.horizontalLayout_81.addWidget(self.sShowRdo)

        self.sHideRdo = QRadioButton(self.horizontalWidget6)
        self.sHideRdo.setObjectName(u"sHideRdo")

        self.horizontalLayout_81.addWidget(self.sHideRdo)

        self.horizontalSpacer_51 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_81.addItem(self.horizontalSpacer_51)


        self.verticalLayout_81.addWidget(self.horizontalWidget6)

        self.sCarrierChk = QCheckBox(self.statusBarPageContent)
        self.sCarrierChk.setObjectName(u"sCarrierChk")

        self.verticalLayout_81.addWidget(self.sCarrierChk)

        self.sCarrierTxt = QLineEdit(self.statusBarPageContent)
        self.sCarrierTxt.setObjectName(u"sCarrierTxt")

        self.verticalLayout_81.addWidget(self.sCarrierTxt)

        self.sBadgeChk = QCheckBox(self.statusBarPageContent)
        self.sBadgeChk.setObjectName(u"sBadgeChk")

        self.verticalLayout_81.addWidget(self.sBadgeChk)

        self.sBadgeTxt = QLineEdit(self.statusBarPageContent)
        self.sBadgeTxt.setObjectName(u"sBadgeTxt")

        self.verticalLayout_81.addWidget(self.sBadgeTxt)

        self.sTypeChk = QCheckBox(self.statusBarPageContent)
        self.sTypeChk.setObjectName(u"sTypeChk")

        self.verticalLayout_81.addWidget(self.sTypeChk)

        self.sTypeDrp = QComboBox(self.statusBarPageContent)
        self.sTypeDrp.addItem("")
        self.sTypeDrp.addItem("")
        self.sTypeDrp.addItem("")
        self.sTypeDrp.addItem("")
        self.sTypeDrp.addItem("")
        self.sTypeDrp.addItem("")
        self.sTypeDrp.addItem("")
        self.sTypeDrp.addItem("")
        self.sTypeDrp.addItem("")
        self.sTypeDrp.addItem("")
        self.sTypeDrp.addItem("")
        self.sTypeDrp.addItem("")
        self.sTypeDrp.addItem("")
        self.sTypeDrp.addItem("")
        self.sTypeDrp.addItem("")
        self.sTypeDrp.setObjectName(u"sTypeDrp")
        self.sTypeDrp.setMinimumSize(QSize(0, 0))
        self.sTypeDrp.setMaximumSize(QSize(150, 16777215))
        self.sTypeDrp.setStyleSheet(u"QComboBox {\n"
"    background-color: #3b3b3b;\n"
"    border: none;\n"
"    color: #e8e8e8;\n"
"    font-size: 14px;\n"
"    padding-left: 8px;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    image: url(:/icon/caret-down-fill.svg);\n"
"    icon-size: 16px;\n"
"    subcontrol-position: right center;\n"
"    margin-right: 8px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #3b3b3b;\n"
"    outline: none;\n"
"    margin-top: 1px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    background-color: #3b3b3b;\n"
"    color: #e8e8e8;\n"
"    padding-left: 8px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #535353;\n"
"    color: #ffffff;\n"
"}")
        self.sTypeDrp.setMaxVisibleItems(15)

        self.verticalLayout_81.addWidget(self.sTypeDrp)

        self.sStrengthChk = QCheckBox(self.statusBarPageContent)
        self.sStrengthChk.setObjectName(u"sStrengthChk")

        self.verticalLayout_81.addWidget(self.sStrengthChk)

        self.horizontalWidget7 = QWidget(self.statusBarPageContent)
        self.horizontalWidget7.setObjectName(u"horizontalWidget7")
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalWidget7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.sStrengthLbl = QLabel(self.horizontalWidget7)
        self.sStrengthLbl.setObjectName(u"sStrengthLbl")
        self.sStrengthLbl.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_10.addWidget(self.sStrengthLbl)

        self.sStrengthSld = QSlider(self.horizontalWidget7)
        self.sStrengthSld.setObjectName(u"sStrengthSld")
        self.sStrengthSld.setMaximum(4)
        self.sStrengthSld.setSingleStep(0)
        self.sStrengthSld.setPageStep(0)
        self.sStrengthSld.setOrientation(Qt.Horizontal)

        self.horizontalLayout_10.addWidget(self.sStrengthSld)


        self.verticalLayout_81.addWidget(self.horizontalWidget7)

        self.line_71 = QFrame(self.statusBarPageContent)
        self.line_71.setObjectName(u"line_71")
        self.line_71.setStyleSheet(u"QFrame {\n"
"    color: #414141;\n"
"}")
        self.line_71.setFrameShadow(QFrame.Plain)
        self.line_71.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_81.addWidget(self.line_71)

        self.timeChk = QCheckBox(self.statusBarPageContent)
        self.timeChk.setObjectName(u"timeChk")

        self.verticalLayout_81.addWidget(self.timeChk)

        self.timeTxt = QLineEdit(self.statusBarPageContent)
        self.timeTxt.setObjectName(u"timeTxt")

        self.verticalLayout_81.addWidget(self.timeTxt)

        self.dateChk = QCheckBox(self.statusBarPageContent)
        self.dateChk.setObjectName(u"dateChk")

        self.verticalLayout_81.addWidget(self.dateChk)

        self.dateTxt = QLineEdit(self.statusBarPageContent)
        self.dateTxt.setObjectName(u"dateTxt")

        self.verticalLayout_81.addWidget(self.dateTxt)

        self.breadcrumbChk = QCheckBox(self.statusBarPageContent)
        self.breadcrumbChk.setObjectName(u"breadcrumbChk")

        self.verticalLayout_81.addWidget(self.breadcrumbChk)

        self.breadcrumbTxt = QLineEdit(self.statusBarPageContent)
        self.breadcrumbTxt.setObjectName(u"breadcrumbTxt")

        self.verticalLayout_81.addWidget(self.breadcrumbTxt)

        self.batteryDetailChk = QCheckBox(self.statusBarPageContent)
        self.batteryDetailChk.setObjectName(u"batteryDetailChk")

        self.verticalLayout_81.addWidget(self.batteryDetailChk)

        self.batteryDetailTxt = QLineEdit(self.statusBarPageContent)
        self.batteryDetailTxt.setObjectName(u"batteryDetailTxt")

        self.verticalLayout_81.addWidget(self.batteryDetailTxt)

        self.batteryCapacityChk = QCheckBox(self.statusBarPageContent)
        self.batteryCapacityChk.setObjectName(u"batteryCapacityChk")

        self.verticalLayout_81.addWidget(self.batteryCapacityChk)

        self.horizontalWidget8 = QWidget(self.statusBarPageContent)
        self.horizontalWidget8.setObjectName(u"horizontalWidget8")
        self.horizontalLayout_111 = QHBoxLayout(self.horizontalWidget8)
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.horizontalLayout_111.setContentsMargins(0, 0, 0, 0)
        self.batteryCapacityLbl = QLabel(self.horizontalWidget8)
        self.batteryCapacityLbl.setObjectName(u"batteryCapacityLbl")
        self.batteryCapacityLbl.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_111.addWidget(self.batteryCapacityLbl)

        self.batteryCapacitySld = QSlider(self.horizontalWidget8)
        self.batteryCapacitySld.setObjectName(u"batteryCapacitySld")
        self.batteryCapacitySld.setMaximum(100)
        self.batteryCapacitySld.setSingleStep(0)
        self.batteryCapacitySld.setPageStep(0)
        self.batteryCapacitySld.setTracking(True)
        self.batteryCapacitySld.setOrientation(Qt.Horizontal)
        self.batteryCapacitySld.setInvertedAppearance(False)
        self.batteryCapacitySld.setInvertedControls(False)
        self.batteryCapacitySld.setTickInterval(5)

        self.horizontalLayout_111.addWidget(self.batteryCapacitySld)


        self.verticalLayout_81.addWidget(self.horizontalWidget8)

        self.wifiStrengthChk = QCheckBox(self.statusBarPageContent)
        self.wifiStrengthChk.setObjectName(u"wifiStrengthChk")

        self.verticalLayout_81.addWidget(self.wifiStrengthChk)

        self.horizontalWidget9 = QWidget(self.statusBarPageContent)
        self.horizontalWidget9.setObjectName(u"horizontalWidget9")
        self.horizontalLayout_12 = QHBoxLayout(self.horizontalWidget9)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.wifiStrengthLbl = QLabel(self.horizontalWidget9)
        self.wifiStrengthLbl.setObjectName(u"wifiStrengthLbl")
        self.wifiStrengthLbl.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_12.addWidget(self.wifiStrengthLbl)

        self.wifiStrengthSld = QSlider(self.horizontalWidget9)
        self.wifiStrengthSld.setObjectName(u"wifiStrengthSld")
        self.wifiStrengthSld.setMaximum(3)
        self.wifiStrengthSld.setSingleStep(0)
        self.wifiStrengthSld.setPageStep(0)
        self.wifiStrengthSld.setOrientation(Qt.Horizontal)

        self.horizontalLayout_12.addWidget(self.wifiStrengthSld)


        self.verticalLayout_81.addWidget(self.horizontalWidget9)

        self.numericWifiChk = QCheckBox(self.statusBarPageContent)
        self.numericWifiChk.setObjectName(u"numericWifiChk")

        self.verticalLayout_81.addWidget(self.numericWifiChk)

        self.numericCellChk = QCheckBox(self.statusBarPageContent)
        self.numericCellChk.setObjectName(u"numericCellChk")

        self.verticalLayout_81.addWidget(self.numericCellChk)

        self.label_51 = QLabel(self.statusBarPageContent)
        self.label_51.setObjectName(u"label_51")

        self.verticalLayout_81.addWidget(self.label_51)

        self.line_101 = QFrame(self.statusBarPageContent)
        self.line_101.setObjectName(u"line_101")
        self.line_101.setStyleSheet(u"QFrame {\n"
"    color: #414141;\n"
"}")
        self.line_101.setFrameShadow(QFrame.Plain)
        self.line_101.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_81.addWidget(self.line_101)

        self.label_18 = QLabel(self.statusBarPageContent)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_81.addWidget(self.label_18)

        self.dndRdo = QWidget(self.statusBarPageContent)
        self.dndRdo.setObjectName(u"dndRdo")
        self.horizontalLayout_32 = QHBoxLayout(self.dndRdo)
        self.horizontalLayout_32.setSpacing(20)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.dndDefaultRdo = QRadioButton(self.dndRdo)
        self.dndDefaultRdo.setObjectName(u"dndDefaultRdo")
        self.dndDefaultRdo.setChecked(True)

        self.horizontalLayout_32.addWidget(self.dndDefaultRdo)

        self.dndShowRdo = QRadioButton(self.dndRdo)
        self.dndShowRdo.setObjectName(u"dndShowRdo")

        self.horizontalLayout_32.addWidget(self.dndShowRdo)

        self.dndHideRdo = QRadioButton(self.dndRdo)
        self.dndHideRdo.setObjectName(u"dndHideRdo")

        self.horizontalLayout_32.addWidget(self.dndHideRdo)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_20)


        self.verticalLayout_81.addWidget(self.dndRdo)

        self.label_181 = QLabel(self.statusBarPageContent)
        self.label_181.setObjectName(u"label_181")

        self.verticalLayout_81.addWidget(self.label_181)

        self.airplaneRdo = QWidget(self.statusBarPageContent)
        self.airplaneRdo.setObjectName(u"airplaneRdo")
        self.horizontalLayout_321 = QHBoxLayout(self.airplaneRdo)
        self.horizontalLayout_321.setSpacing(20)
        self.horizontalLayout_321.setObjectName(u"horizontalLayout_321")
        self.horizontalLayout_321.setContentsMargins(0, 0, 0, 0)
        self.airplaneDefaultRdo = QRadioButton(self.airplaneRdo)
        self.airplaneDefaultRdo.setObjectName(u"airplaneDefaultRdo")
        self.airplaneDefaultRdo.setChecked(True)

        self.horizontalLayout_321.addWidget(self.airplaneDefaultRdo)

        self.airplaneShowRdo = QRadioButton(self.airplaneRdo)
        self.airplaneShowRdo.setObjectName(u"airplaneShowRdo")

        self.horizontalLayout_321.addWidget(self.airplaneShowRdo)

        self.airplaneHideRdo = QRadioButton(self.airplaneRdo)
        self.airplaneHideRdo.setObjectName(u"airplaneHideRdo")

        self.horizontalLayout_321.addWidget(self.airplaneHideRdo)

        self.horizontalSpacer_201 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_321.addItem(self.horizontalSpacer_201)


        self.verticalLayout_81.addWidget(self.airplaneRdo)

        self.label_182 = QLabel(self.statusBarPageContent)
        self.label_182.setObjectName(u"label_182")

        self.verticalLayout_81.addWidget(self.label_182)

        self.wifiRdo = QWidget(self.statusBarPageContent)
        self.wifiRdo.setObjectName(u"wifiRdo")
        self.horizontalLayout_322 = QHBoxLayout(self.wifiRdo)
        self.horizontalLayout_322.setSpacing(20)
        self.horizontalLayout_322.setObjectName(u"horizontalLayout_322")
        self.horizontalLayout_322.setContentsMargins(0, 0, 0, 0)
        self.wifiDefaultRdo = QRadioButton(self.wifiRdo)
        self.wifiDefaultRdo.setObjectName(u"wifiDefaultRdo")
        self.wifiDefaultRdo.setChecked(True)

        self.horizontalLayout_322.addWidget(self.wifiDefaultRdo)

        self.wifiShowRdo = QRadioButton(self.wifiRdo)
        self.wifiShowRdo.setObjectName(u"wifiShowRdo")

        self.horizontalLayout_322.addWidget(self.wifiShowRdo)

        self.wifiHideRdo = QRadioButton(self.wifiRdo)
        self.wifiHideRdo.setObjectName(u"wifiHideRdo")

        self.horizontalLayout_322.addWidget(self.wifiHideRdo)

        self.horizontalSpacer_202 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_322.addItem(self.horizontalSpacer_202)


        self.verticalLayout_81.addWidget(self.wifiRdo)

        self.label_121 = QLabel(self.statusBarPageContent)
        self.label_121.setObjectName(u"label_121")

        self.verticalLayout_81.addWidget(self.label_121)

        self.label_183 = QLabel(self.statusBarPageContent)
        self.label_183.setObjectName(u"label_183")

        self.verticalLayout_81.addWidget(self.label_183)

        self.batteryRdo = QWidget(self.statusBarPageContent)
        self.batteryRdo.setObjectName(u"batteryRdo")
        self.horizontalLayout_323 = QHBoxLayout(self.batteryRdo)
        self.horizontalLayout_323.setSpacing(20)
        self.horizontalLayout_323.setObjectName(u"horizontalLayout_323")
        self.horizontalLayout_323.setContentsMargins(0, 0, 0, 0)
        self.batteryDefaultRdo = QRadioButton(self.batteryRdo)
        self.batteryDefaultRdo.setObjectName(u"batteryDefaultRdo")
        self.batteryDefaultRdo.setChecked(True)

        self.horizontalLayout_323.addWidget(self.batteryDefaultRdo)

        self.batteryShowRdo = QRadioButton(self.batteryRdo)
        self.batteryShowRdo.setObjectName(u"batteryShowRdo")

        self.horizontalLayout_323.addWidget(self.batteryShowRdo)

        self.batteryHideRdo = QRadioButton(self.batteryRdo)
        self.batteryHideRdo.setObjectName(u"batteryHideRdo")

        self.horizontalLayout_323.addWidget(self.batteryHideRdo)

        self.horizontalSpacer_203 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_323.addItem(self.horizontalSpacer_203)


        self.verticalLayout_81.addWidget(self.batteryRdo)

        self.label_184 = QLabel(self.statusBarPageContent)
        self.label_184.setObjectName(u"label_184")

        self.verticalLayout_81.addWidget(self.label_184)

        self.bluetoothRdo = QWidget(self.statusBarPageContent)
        self.bluetoothRdo.setObjectName(u"bluetoothRdo")
        self.horizontalLayout_324 = QHBoxLayout(self.bluetoothRdo)
        self.horizontalLayout_324.setSpacing(20)
        self.horizontalLayout_324.setObjectName(u"horizontalLayout_324")
        self.horizontalLayout_324.setContentsMargins(0, 0, 0, 0)
        self.bluetoothDefaultRdo = QRadioButton(self.bluetoothRdo)
        self.bluetoothDefaultRdo.setObjectName(u"bluetoothDefaultRdo")
        self.bluetoothDefaultRdo.setChecked(True)

        self.horizontalLayout_324.addWidget(self.bluetoothDefaultRdo)

        self.bluetoothShowRdo = QRadioButton(self.bluetoothRdo)
        self.bluetoothShowRdo.setObjectName(u"bluetoothShowRdo")

        self.horizontalLayout_324.addWidget(self.bluetoothShowRdo)

        self.bluetoothHideRdo = QRadioButton(self.bluetoothRdo)
        self.bluetoothHideRdo.setObjectName(u"bluetoothHideRdo")

        self.horizontalLayout_324.addWidget(self.bluetoothHideRdo)

        self.horizontalSpacer_204 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_324.addItem(self.horizontalSpacer_204)


        self.verticalLayout_81.addWidget(self.bluetoothRdo)

        self.label_185 = QLabel(self.statusBarPageContent)
        self.label_185.setObjectName(u"label_185")

        self.verticalLayout_81.addWidget(self.label_185)

        self.alarmRdo = QWidget(self.statusBarPageContent)
        self.alarmRdo.setObjectName(u"alarmRdo")
        self.horizontalLayout_325 = QHBoxLayout(self.alarmRdo)
        self.horizontalLayout_325.setSpacing(20)
        self.horizontalLayout_325.setObjectName(u"horizontalLayout_325")
        self.horizontalLayout_325.setContentsMargins(0, 0, 0, 0)
        self.alarmDefaultRdo = QRadioButton(self.alarmRdo)
        self.alarmDefaultRdo.setObjectName(u"alarmDefaultRdo")
        self.alarmDefaultRdo.setChecked(True)

        self.horizontalLayout_325.addWidget(self.alarmDefaultRdo)

        self.alarmShowRdo = QRadioButton(self.alarmRdo)
        self.alarmShowRdo.setObjectName(u"alarmShowRdo")

        self.horizontalLayout_325.addWidget(self.alarmShowRdo)

        self.alarmHideRdo = QRadioButton(self.alarmRdo)
        self.alarmHideRdo.setObjectName(u"alarmHideRdo")

        self.horizontalLayout_325.addWidget(self.alarmHideRdo)

        self.horizontalSpacer_205 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_325.addItem(self.horizontalSpacer_205)


        self.verticalLayout_81.addWidget(self.alarmRdo)

        self.label_186 = QLabel(self.statusBarPageContent)
        self.label_186.setObjectName(u"label_186")

        self.verticalLayout_81.addWidget(self.label_186)

        self.locationRdo = QWidget(self.statusBarPageContent)
        self.locationRdo.setObjectName(u"locationRdo")
        self.horizontalLayout_326 = QHBoxLayout(self.locationRdo)
        self.horizontalLayout_326.setSpacing(20)
        self.horizontalLayout_326.setObjectName(u"horizontalLayout_326")
        self.horizontalLayout_326.setContentsMargins(0, 0, 0, 0)
        self.locationDefaultRdo = QRadioButton(self.locationRdo)
        self.locationDefaultRdo.setObjectName(u"locationDefaultRdo")
        self.locationDefaultRdo.setChecked(True)

        self.horizontalLayout_326.addWidget(self.locationDefaultRdo)

        self.locationShowRdo = QRadioButton(self.locationRdo)
        self.locationShowRdo.setObjectName(u"locationShowRdo")

        self.horizontalLayout_326.addWidget(self.locationShowRdo)

        self.locationHideRdo = QRadioButton(self.locationRdo)
        self.locationHideRdo.setObjectName(u"locationHideRdo")

        self.horizontalLayout_326.addWidget(self.locationHideRdo)

        self.horizontalSpacer_206 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_326.addItem(self.horizontalSpacer_206)


        self.verticalLayout_81.addWidget(self.locationRdo)

        self.label_187 = QLabel(self.statusBarPageContent)
        self.label_187.setObjectName(u"label_187")

        self.verticalLayout_81.addWidget(self.label_187)

        self.rotationRdo = QWidget(self.statusBarPageContent)
        self.rotationRdo.setObjectName(u"rotationRdo")
        self.horizontalLayout_327 = QHBoxLayout(self.rotationRdo)
        self.horizontalLayout_327.setSpacing(20)
        self.horizontalLayout_327.setObjectName(u"horizontalLayout_327")
        self.horizontalLayout_327.setContentsMargins(0, 0, 0, 0)
        self.rotationDefaultRdo = QRadioButton(self.rotationRdo)
        self.rotationDefaultRdo.setObjectName(u"rotationDefaultRdo")
        self.rotationDefaultRdo.setChecked(True)

        self.horizontalLayout_327.addWidget(self.rotationDefaultRdo)

        self.rotationShowRdo = QRadioButton(self.rotationRdo)
        self.rotationShowRdo.setObjectName(u"rotationShowRdo")

        self.horizontalLayout_327.addWidget(self.rotationShowRdo)

        self.rotationHideRdo = QRadioButton(self.rotationRdo)
        self.rotationHideRdo.setObjectName(u"rotationHideRdo")

        self.horizontalLayout_327.addWidget(self.rotationHideRdo)

        self.horizontalSpacer_207 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_327.addItem(self.horizontalSpacer_207)


        self.verticalLayout_81.addWidget(self.rotationRdo)

        self.label_188 = QLabel(self.statusBarPageContent)
        self.label_188.setObjectName(u"label_188")

        self.verticalLayout_81.addWidget(self.label_188)

        self.airplayRdo = QWidget(self.statusBarPageContent)
        self.airplayRdo.setObjectName(u"airplayRdo")
        self.horizontalLayout_328 = QHBoxLayout(self.airplayRdo)
        self.horizontalLayout_328.setSpacing(20)
        self.horizontalLayout_328.setObjectName(u"horizontalLayout_328")
        self.horizontalLayout_328.setContentsMargins(0, 0, 0, 0)
        self.airplayDefaultRdo = QRadioButton(self.airplayRdo)
        self.airplayDefaultRdo.setObjectName(u"airplayDefaultRdo")
        self.airplayDefaultRdo.setChecked(True)

        self.horizontalLayout_328.addWidget(self.airplayDefaultRdo)

        self.airplayShowRdo = QRadioButton(self.airplayRdo)
        self.airplayShowRdo.setObjectName(u"airplayShowRdo")

        self.horizontalLayout_328.addWidget(self.airplayShowRdo)

        self.airplayHideRdo = QRadioButton(self.airplayRdo)
        self.airplayHideRdo.setObjectName(u"airplayHideRdo")

        self.horizontalLayout_328.addWidget(self.airplayHideRdo)

        self.horizontalSpacer_208 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_328.addItem(self.horizontalSpacer_208)


        self.verticalLayout_81.addWidget(self.airplayRdo)

        self.label_189 = QLabel(self.statusBarPageContent)
        self.label_189.setObjectName(u"label_189")

        self.verticalLayout_81.addWidget(self.label_189)

        self.carplayRdo = QWidget(self.statusBarPageContent)
        self.carplayRdo.setObjectName(u"carplayRdo")
        self.horizontalLayout_329 = QHBoxLayout(self.carplayRdo)
        self.horizontalLayout_329.setSpacing(20)
        self.horizontalLayout_329.setObjectName(u"horizontalLayout_329")
        self.horizontalLayout_329.setContentsMargins(0, 0, 0, 0)
        self.carplayDefaultRdo = QRadioButton(self.carplayRdo)
        self.carplayDefaultRdo.setObjectName(u"carplayDefaultRdo")
        self.carplayDefaultRdo.setChecked(True)

        self.horizontalLayout_329.addWidget(self.carplayDefaultRdo)

        self.carplayShowRdo = QRadioButton(self.carplayRdo)
        self.carplayShowRdo.setObjectName(u"carplayShowRdo")

        self.horizontalLayout_329.addWidget(self.carplayShowRdo)

        self.carplayHideRdo = QRadioButton(self.carplayRdo)
        self.carplayHideRdo.setObjectName(u"carplayHideRdo")

        self.horizontalLayout_329.addWidget(self.carplayHideRdo)

        self.horizontalSpacer_209 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_329.addItem(self.horizontalSpacer_209)


        self.verticalLayout_81.addWidget(self.carplayRdo)

        self.label_1810 = QLabel(self.statusBarPageContent)
        self.label_1810.setObjectName(u"label_1810")

        self.verticalLayout_81.addWidget(self.label_1810)

        self.vpnRdo = QWidget(self.statusBarPageContent)
        self.vpnRdo.setObjectName(u"vpnRdo")
        self.horizontalLayout_3210 = QHBoxLayout(self.vpnRdo)
        self.horizontalLayout_3210.setSpacing(20)
        self.horizontalLayout_3210.setObjectName(u"horizontalLayout_3210")
        self.horizontalLayout_3210.setContentsMargins(0, 0, 0, 0)
        self.vpnDefaultRdo = QRadioButton(self.vpnRdo)
        self.vpnDefaultRdo.setObjectName(u"vpnDefaultRdo")
        self.vpnDefaultRdo.setChecked(True)

        self.horizontalLayout_3210.addWidget(self.vpnDefaultRdo)

        self.vpnShowRdo = QRadioButton(self.vpnRdo)
        self.vpnShowRdo.setObjectName(u"vpnShowRdo")

        self.horizontalLayout_3210.addWidget(self.vpnShowRdo)

        self.vpnHideRdo = QRadioButton(self.vpnRdo)
        self.vpnHideRdo.setObjectName(u"vpnHideRdo")

        self.horizontalLayout_3210.addWidget(self.vpnHideRdo)

        self.horizontalSpacer_2010 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3210.addItem(self.horizontalSpacer_2010)


        self.verticalLayout_81.addWidget(self.vpnRdo)

        self.label_19 = QLabel(self.statusBarPageContent)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_81.addWidget(self.label_19)

        self.studentRdo = QWidget(self.statusBarPageContent)
        self.studentRdo.setObjectName(u"studentRdo")
        self.horizontalLayout_34 = QHBoxLayout(self.studentRdo)
        self.horizontalLayout_34.setSpacing(20)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.studentDefaultRdo = QRadioButton(self.studentRdo)
        self.studentDefaultRdo.setObjectName(u"studentDefaultRdo")
        self.studentDefaultRdo.setChecked(True)

        self.horizontalLayout_34.addWidget(self.studentDefaultRdo)

        self.studentShowRdo = QRadioButton(self.studentRdo)
        self.studentShowRdo.setObjectName(u"studentShowRdo")

        self.horizontalLayout_34.addWidget(self.studentShowRdo)

        self.studentHideRdo = QRadioButton(self.studentRdo)
        self.studentHideRdo.setObjectName(u"studentHideRdo")

        self.horizontalLayout_34.addWidget(self.studentHideRdo)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_22)


        self.verticalLayout_81.addWidget(self.studentRdo)

        self.label_20 = QLabel(self.statusBarPageContent)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_81.addWidget(self.label_20)

        self.waterRdo = QWidget(self.statusBarPageContent)
        self.waterRdo.setObjectName(u"waterRdo")
        self.horizontalLayout_35 = QHBoxLayout(self.waterRdo)
        self.horizontalLayout_35.setSpacing(20)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.waterDefaultRdo = QRadioButton(self.waterRdo)
        self.waterDefaultRdo.setObjectName(u"waterDefaultRdo")
        self.waterDefaultRdo.setChecked(True)

        self.horizontalLayout_35.addWidget(self.waterDefaultRdo)

        self.waterShowRdo = QRadioButton(self.waterRdo)
        self.waterShowRdo.setObjectName(u"waterShowRdo")

        self.horizontalLayout_35.addWidget(self.waterShowRdo)

        self.waterHideRdo = QRadioButton(self.waterRdo)
        self.waterHideRdo.setObjectName(u"waterHideRdo")

        self.horizontalLayout_35.addWidget(self.waterHideRdo)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_23)


        self.verticalLayout_81.addWidget(self.waterRdo)

        self.label_21 = QLabel(self.statusBarPageContent)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_81.addWidget(self.label_21)

        self.vcRdo = QWidget(self.statusBarPageContent)
        self.vcRdo.setObjectName(u"vcRdo")
        self.horizontalLayout_36 = QHBoxLayout(self.vcRdo)
        self.horizontalLayout_36.setSpacing(20)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.vcDefaultRdo = QRadioButton(self.vcRdo)
        self.vcDefaultRdo.setObjectName(u"vcDefaultRdo")
        self.vcDefaultRdo.setChecked(True)

        self.horizontalLayout_36.addWidget(self.vcDefaultRdo)

        self.vcShowRdo = QRadioButton(self.vcRdo)
        self.vcShowRdo.setObjectName(u"vcShowRdo")

        self.horizontalLayout_36.addWidget(self.vcShowRdo)

        self.vcHideRdo = QRadioButton(self.vcRdo)
        self.vcHideRdo.setObjectName(u"vcHideRdo")

        self.horizontalLayout_36.addWidget(self.vcHideRdo)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_24)


        self.verticalLayout_81.addWidget(self.vcRdo)

        self.sillyModeChk = QCheckBox(self.statusBarPageContent)
        self.sillyModeChk.setObjectName(u"sillyModeChk")

        self.verticalLayout_81.addWidget(self.sillyModeChk)

        self.verticalSpacer_31 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_81.addItem(self.verticalSpacer_31)


        self.verticalLayout_91.addWidget(self.statusBarPageContent)

        self.sbScrollArea.setWidget(self.scrollAreaWidgetContents1)

        self.verticalLayout_41.addWidget(self.sbScrollArea)

        self.pages.addWidget(self.statusBarPage)
        self.springboardOptionsPage = QWidget()
        self.springboardOptionsPage.setObjectName(u"springboardOptionsPage")
        self.verticalLayout_10 = QVBoxLayout(self.springboardOptionsPage)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_4 = QWidget(self.springboardOptionsPage)
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
        icon20 = QIcon()
        icon20.addFile(u":/icon/app-indicator.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_7.setIcon(icon20)

        self.horizontalLayout_13.addWidget(self.toolButton_7)

        self.verticalWidget_3 = QWidget(self.horizontalWidget_4)
        self.verticalWidget_3.setObjectName(u"verticalWidget_3")
        self.verticalLayout_7 = QVBoxLayout(self.verticalWidget_3)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.springboardOptionsLbl = QLabel(self.verticalWidget_3)
        self.springboardOptionsLbl.setObjectName(u"springboardOptionsLbl")
        self.springboardOptionsLbl.setFont(font)

        self.verticalLayout_7.addWidget(self.springboardOptionsLbl)

        self.verticalSpacer_19 = QSpacerItem(20, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_19)


        self.horizontalLayout_13.addWidget(self.verticalWidget_3)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_6)


        self.verticalLayout_10.addWidget(self.horizontalWidget_4)

        self.line_11 = QFrame(self.springboardOptionsPage)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_11.setFrameShadow(QFrame.Plain)
        self.line_11.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_10.addWidget(self.line_11)

        self.springboardOptionsPageContent = QWidget(self.springboardOptionsPage)
        self.springboardOptionsPageContent.setObjectName(u"springboardOptionsPageContent")
        self.springboardOptionsPageContent.setEnabled(False)
        self.springboardOptionsPageContent.setMaximumSize(QSize(650, 16777215))
        self._2 = QVBoxLayout(self.springboardOptionsPageContent)
        self._2.setObjectName(u"_2")
        self._2.setContentsMargins(0, 0, 0, 0)
        self.footnoteLbl = QLabel(self.springboardOptionsPageContent)
        self.footnoteLbl.setObjectName(u"footnoteLbl")

        self._2.addWidget(self.footnoteLbl)

        self.footnoteTxt = QLineEdit(self.springboardOptionsPageContent)
        self.footnoteTxt.setObjectName(u"footnoteTxt")

        self._2.addWidget(self.footnoteTxt)

        self.footnoteLine = QFrame(self.springboardOptionsPageContent)
        self.footnoteLine.setObjectName(u"footnoteLine")
        self.footnoteLine.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.footnoteLine.setFrameShadow(QFrame.Plain)
        self.footnoteLine.setFrameShape(QFrame.Shape.HLine)

        self._2.addWidget(self.footnoteLine)

        self.disableLockRespringChk = QCheckBox(self.springboardOptionsPageContent)
        self.disableLockRespringChk.setObjectName(u"disableLockRespringChk")

        self._2.addWidget(self.disableLockRespringChk)

        self.disableDimmingChk = QCheckBox(self.springboardOptionsPageContent)
        self.disableDimmingChk.setObjectName(u"disableDimmingChk")

        self._2.addWidget(self.disableDimmingChk)

        self.disableBatteryAlertsChk = QCheckBox(self.springboardOptionsPageContent)
        self.disableBatteryAlertsChk.setObjectName(u"disableBatteryAlertsChk")

        self._2.addWidget(self.disableBatteryAlertsChk)

        self.disableCrumbChk = QCheckBox(self.springboardOptionsPageContent)
        self.disableCrumbChk.setObjectName(u"disableCrumbChk")

        self._2.addWidget(self.disableCrumbChk)

        self.enableSupervisionTextChk = QCheckBox(self.springboardOptionsPageContent)
        self.enableSupervisionTextChk.setObjectName(u"enableSupervisionTextChk")

        self._2.addWidget(self.enableSupervisionTextChk)

        self.enableAirPlayChk = QCheckBox(self.springboardOptionsPageContent)
        self.enableAirPlayChk.setObjectName(u"enableAirPlayChk")

        self._2.addWidget(self.enableAirPlayChk)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self._2.addItem(self.verticalSpacer_5)


        self.verticalLayout_10.addWidget(self.springboardOptionsPageContent)

        self.pages.addWidget(self.springboardOptionsPage)
        self.internalOptionsPage = QWidget()
        self.internalOptionsPage.setObjectName(u"internalOptionsPage")
        self.verticalLayout_141 = QVBoxLayout(self.internalOptionsPage)
        self.verticalLayout_141.setObjectName(u"verticalLayout_141")
        self.verticalLayout_141.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_51 = QWidget(self.internalOptionsPage)
        self.horizontalWidget_51.setObjectName(u"horizontalWidget_51")
        self.horizontalLayout_201 = QHBoxLayout(self.horizontalWidget_51)
        self.horizontalLayout_201.setSpacing(10)
        self.horizontalLayout_201.setObjectName(u"horizontalLayout_201")
        self.horizontalLayout_201.setContentsMargins(0, 9, 0, 9)
        self.toolButton_101 = QToolButton(self.horizontalWidget_51)
        self.toolButton_101.setObjectName(u"toolButton_101")
        self.toolButton_101.setEnabled(False)
        self.toolButton_101.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        icon21 = QIcon()
        icon21.addFile(u":/icon/hdd.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_101.setIcon(icon21)

        self.horizontalLayout_201.addWidget(self.toolButton_101)

        self.verticalWidget_41 = QWidget(self.horizontalWidget_51)
        self.verticalWidget_41.setObjectName(u"verticalWidget_41")
        self.verticalLayout_121 = QVBoxLayout(self.verticalWidget_41)
        self.verticalLayout_121.setSpacing(6)
        self.verticalLayout_121.setObjectName(u"verticalLayout_121")
        self.verticalLayout_121.setContentsMargins(0, 0, 0, 0)
        self.internalOptionsLbl1 = QLabel(self.verticalWidget_41)
        self.internalOptionsLbl1.setObjectName(u"internalOptionsLbl1")
        self.internalOptionsLbl1.setFont(font)

        self.verticalLayout_121.addWidget(self.internalOptionsLbl1)

        self.verticalSpacer_18 = QSpacerItem(20, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_121.addItem(self.verticalSpacer_18)


        self.horizontalLayout_201.addWidget(self.verticalWidget_41)

        self.horizontalSpacer_71 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_201.addItem(self.horizontalSpacer_71)


        self.verticalLayout_141.addWidget(self.horizontalWidget_51)

        self.line_121 = QFrame(self.internalOptionsPage)
        self.line_121.setObjectName(u"line_121")
        self.line_121.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_121.setFrameShadow(QFrame.Plain)
        self.line_121.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_141.addWidget(self.line_121)

        self.internalOptionsPageContent = QWidget(self.internalOptionsPage)
        self.internalOptionsPageContent.setObjectName(u"internalOptionsPageContent")
        self.internalOptionsPageContent.setEnabled(False)
        self.verticalLayout_131 = QVBoxLayout(self.internalOptionsPageContent)
        self.verticalLayout_131.setObjectName(u"verticalLayout_131")
        self.verticalLayout_131.setContentsMargins(0, 0, 0, 0)
        self.buildVersionChk = QCheckBox(self.internalOptionsPageContent)
        self.buildVersionChk.setObjectName(u"buildVersionChk")

        self.verticalLayout_131.addWidget(self.buildVersionChk)

        self.RTLChk = QCheckBox(self.internalOptionsPageContent)
        self.RTLChk.setObjectName(u"RTLChk")

        self.verticalLayout_131.addWidget(self.RTLChk)

        self.div1 = QFrame(self.internalOptionsPageContent)
        self.div1.setObjectName(u"div1")
        self.div1.setEnabled(False)
        self.div1.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.div1.setFrameShadow(QFrame.Plain)
        self.div1.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_131.addWidget(self.div1)

        self.metalHUDChk = QCheckBox(self.internalOptionsPageContent)
        self.metalHUDChk.setObjectName(u"metalHUDChk")

        self.verticalLayout_131.addWidget(self.metalHUDChk)

        self.iMessageChk = QCheckBox(self.internalOptionsPageContent)
        self.iMessageChk.setObjectName(u"iMessageChk")

        self.verticalLayout_131.addWidget(self.iMessageChk)

        self.IDSChk = QCheckBox(self.internalOptionsPageContent)
        self.IDSChk.setObjectName(u"IDSChk")

        self.verticalLayout_131.addWidget(self.IDSChk)

        self.VCChk = QCheckBox(self.internalOptionsPageContent)
        self.VCChk.setObjectName(u"VCChk")

        self.verticalLayout_131.addWidget(self.VCChk)

        self.line_17 = QFrame(self.internalOptionsPageContent)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_17.setFrameShadow(QFrame.Plain)
        self.line_17.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_131.addWidget(self.line_17)

        self.appStoreChk = QCheckBox(self.internalOptionsPageContent)
        self.appStoreChk.setObjectName(u"appStoreChk")

        self.verticalLayout_131.addWidget(self.appStoreChk)

        self.notesChk = QCheckBox(self.internalOptionsPageContent)
        self.notesChk.setObjectName(u"notesChk")

        self.verticalLayout_131.addWidget(self.notesChk)

        self.line_18 = QFrame(self.internalOptionsPageContent)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_18.setFrameShadow(QFrame.Plain)
        self.line_18.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_131.addWidget(self.line_18)

        self.showTouchesChk = QCheckBox(self.internalOptionsPageContent)
        self.showTouchesChk.setObjectName(u"showTouchesChk")

        self.verticalLayout_131.addWidget(self.showTouchesChk)

        self.hideRespringChk = QCheckBox(self.internalOptionsPageContent)
        self.hideRespringChk.setObjectName(u"hideRespringChk")

        self.verticalLayout_131.addWidget(self.hideRespringChk)

        self.enableWakeVibrateChk = QCheckBox(self.internalOptionsPageContent)
        self.enableWakeVibrateChk.setObjectName(u"enableWakeVibrateChk")

        self.verticalLayout_131.addWidget(self.enableWakeVibrateChk)

        self.line_19 = QFrame(self.internalOptionsPageContent)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_19.setFrameShadow(QFrame.Plain)
        self.line_19.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_131.addWidget(self.line_19)

        self.pasteSoundChk = QCheckBox(self.internalOptionsPageContent)
        self.pasteSoundChk.setObjectName(u"pasteSoundChk")

        self.verticalLayout_131.addWidget(self.pasteSoundChk)

        self.notifyPastesChk = QCheckBox(self.internalOptionsPageContent)
        self.notifyPastesChk.setObjectName(u"notifyPastesChk")

        self.verticalLayout_131.addWidget(self.notifyPastesChk)

        self.verticalSpacer_61 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_131.addItem(self.verticalSpacer_61)


        self.verticalLayout_141.addWidget(self.internalOptionsPageContent)

        self.pages.addWidget(self.internalOptionsPage)
        self.daemonsPage = QWidget()
        self.daemonsPage.setObjectName(u"daemonsPage")
        self.verticalLayout_142 = QVBoxLayout(self.daemonsPage)
        self.verticalLayout_142.setObjectName(u"verticalLayout_142")
        self.verticalLayout_142.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_52 = QWidget(self.daemonsPage)
        self.horizontalWidget_52.setObjectName(u"horizontalWidget_52")
        self.horizontalLayout_202 = QHBoxLayout(self.horizontalWidget_52)
        self.horizontalLayout_202.setSpacing(10)
        self.horizontalLayout_202.setObjectName(u"horizontalLayout_202")
        self.horizontalLayout_202.setContentsMargins(0, 9, 0, 9)
        self.toolButton_102 = QToolButton(self.horizontalWidget_52)
        self.toolButton_102.setObjectName(u"toolButton_102")
        self.toolButton_102.setEnabled(True)
        self.toolButton_102.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        icon22 = QIcon()
        icon22.addFile(u":/icon/toggles.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_102.setIcon(icon22)

        self.horizontalLayout_202.addWidget(self.toolButton_102)

        self.verticalWidget_42 = QWidget(self.horizontalWidget_52)
        self.verticalWidget_42.setObjectName(u"verticalWidget_42")
        self.verticalLayout_122 = QVBoxLayout(self.verticalWidget_42)
        self.verticalLayout_122.setSpacing(6)
        self.verticalLayout_122.setObjectName(u"verticalLayout_122")
        self.verticalLayout_122.setContentsMargins(0, 0, 0, 0)
        self.daemonsLbl = QLabel(self.verticalWidget_42)
        self.daemonsLbl.setObjectName(u"daemonsLbl")
        self.daemonsLbl.setFont(font)

        self.verticalLayout_122.addWidget(self.daemonsLbl)

        self.modifyDaemonsChk = QCheckBox(self.verticalWidget_42)
        self.modifyDaemonsChk.setObjectName(u"modifyDaemonsChk")

        self.verticalLayout_122.addWidget(self.modifyDaemonsChk)


        self.horizontalLayout_202.addWidget(self.verticalWidget_42)

        self.horizontalSpacer_72 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_202.addItem(self.horizontalSpacer_72)


        self.verticalLayout_142.addWidget(self.horizontalWidget_52)

        self.line_122 = QFrame(self.daemonsPage)
        self.line_122.setObjectName(u"line_122")
        self.line_122.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_122.setFrameShadow(QFrame.Plain)
        self.line_122.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_142.addWidget(self.line_122)

        self.regularDomainsLbl = QLabel(self.daemonsPage)
        self.regularDomainsLbl.setObjectName(u"regularDomainsLbl")

        self.verticalLayout_142.addWidget(self.regularDomainsLbl)

        self.daemonsPageContent = QWidget(self.daemonsPage)
        self.daemonsPageContent.setObjectName(u"daemonsPageContent")
        self.daemonsPageContent.setEnabled(False)
        self.verticalLayout_132 = QVBoxLayout(self.daemonsPageContent)
        self.verticalLayout_132.setObjectName(u"verticalLayout_132")
        self.verticalLayout_132.setContentsMargins(0, 0, 0, 0)
        self.otadChk = QCheckBox(self.daemonsPageContent)
        self.otadChk.setObjectName(u"otadChk")

        self.verticalLayout_132.addWidget(self.otadChk)

        self.usageTrackingAgentChk = QCheckBox(self.daemonsPageContent)
        self.usageTrackingAgentChk.setObjectName(u"usageTrackingAgentChk")

        self.verticalLayout_132.addWidget(self.usageTrackingAgentChk)

        self.screenTimeChk = QCheckBox(self.daemonsPageContent)
        self.screenTimeChk.setObjectName(u"screenTimeChk")

        self.verticalLayout_132.addWidget(self.screenTimeChk)

        self.clearScreenTimeAgentChk = QCheckBox(self.daemonsPageContent)
        self.clearScreenTimeAgentChk.setObjectName(u"clearScreenTimeAgentChk")

        self.verticalLayout_132.addWidget(self.clearScreenTimeAgentChk)

        self.crashReportsChk = QCheckBox(self.daemonsPageContent)
        self.crashReportsChk.setObjectName(u"crashReportsChk")

        self.verticalLayout_132.addWidget(self.crashReportsChk)

        self.atwakeupChk = QCheckBox(self.daemonsPageContent)
        self.atwakeupChk.setObjectName(u"atwakeupChk")

        self.verticalLayout_132.addWidget(self.atwakeupChk)

        self.line_25 = QFrame(self.daemonsPageContent)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_25.setFrameShadow(QFrame.Plain)
        self.line_25.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_132.addWidget(self.line_25)

        self.gameCenterChk = QCheckBox(self.daemonsPageContent)
        self.gameCenterChk.setObjectName(u"gameCenterChk")

        self.verticalLayout_132.addWidget(self.gameCenterChk)

        self.tipsChk = QCheckBox(self.daemonsPageContent)
        self.tipsChk.setObjectName(u"tipsChk")

        self.verticalLayout_132.addWidget(self.tipsChk)

        self.vpndChk = QCheckBox(self.daemonsPageContent)
        self.vpndChk.setObjectName(u"vpndChk")

        self.verticalLayout_132.addWidget(self.vpndChk)

        self.wapicChk = QCheckBox(self.daemonsPageContent)
        self.wapicChk.setObjectName(u"wapicChk")

        self.verticalLayout_132.addWidget(self.wapicChk)

        self.healthdChk = QCheckBox(self.daemonsPageContent)
        self.healthdChk.setObjectName(u"healthdChk")

        self.verticalLayout_132.addWidget(self.healthdChk)

        self.line_26 = QFrame(self.daemonsPageContent)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_26.setFrameShadow(QFrame.Plain)
        self.line_26.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_132.addWidget(self.line_26)

        self.airprintChk = QCheckBox(self.daemonsPageContent)
        self.airprintChk.setObjectName(u"airprintChk")

        self.verticalLayout_132.addWidget(self.airprintChk)

        self.assistiveTouchChk = QCheckBox(self.daemonsPageContent)
        self.assistiveTouchChk.setObjectName(u"assistiveTouchChk")

        self.verticalLayout_132.addWidget(self.assistiveTouchChk)

        self.icloudChk = QCheckBox(self.daemonsPageContent)
        self.icloudChk.setObjectName(u"icloudChk")

        self.verticalLayout_132.addWidget(self.icloudChk)

        self.hotspotChk = QCheckBox(self.daemonsPageContent)
        self.hotspotChk.setObjectName(u"hotspotChk")

        self.verticalLayout_132.addWidget(self.hotspotChk)

        self.passbookChk = QCheckBox(self.daemonsPageContent)
        self.passbookChk.setObjectName(u"passbookChk")

        self.verticalLayout_132.addWidget(self.passbookChk)

        self.spotlightChk = QCheckBox(self.daemonsPageContent)
        self.spotlightChk.setObjectName(u"spotlightChk")

        self.verticalLayout_132.addWidget(self.spotlightChk)

        self.voiceControlChk = QCheckBox(self.daemonsPageContent)
        self.voiceControlChk.setObjectName(u"voiceControlChk")

        self.verticalLayout_132.addWidget(self.voiceControlChk)

        self.verticalSpacer_62 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_132.addItem(self.verticalSpacer_62)


        self.verticalLayout_142.addWidget(self.daemonsPageContent)

        self.pages.addWidget(self.daemonsPage)
        self.posterboardPage = QWidget()
        self.posterboardPage.setObjectName(u"posterboardPage")
        self.verticalLayout_143 = QVBoxLayout(self.posterboardPage)
        self.verticalLayout_143.setObjectName(u"verticalLayout_143")
        self.verticalLayout_143.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_7 = QWidget(self.posterboardPage)
        self.horizontalWidget_7.setObjectName(u"horizontalWidget_7")
        self.horizontalLayout_203 = QHBoxLayout(self.horizontalWidget_7)
        self.horizontalLayout_203.setSpacing(10)
        self.horizontalLayout_203.setObjectName(u"horizontalLayout_203")
        self.horizontalLayout_203.setContentsMargins(0, 9, 0, 0)
        self.toolButton_103 = QToolButton(self.horizontalWidget_7)
        self.toolButton_103.setObjectName(u"toolButton_103")
        self.toolButton_103.setEnabled(True)
        self.toolButton_103.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_103.setIcon(icon3)

        self.horizontalLayout_203.addWidget(self.toolButton_103)

        self.verticalWidget_43 = QWidget(self.horizontalWidget_7)
        self.verticalWidget_43.setObjectName(u"verticalWidget_43")
        self.verticalLayout_123 = QVBoxLayout(self.verticalWidget_43)
        self.verticalLayout_123.setSpacing(6)
        self.verticalLayout_123.setObjectName(u"verticalLayout_123")
        self.verticalLayout_123.setContentsMargins(0, 0, 0, 0)
        self.posterboardLbl = QLabel(self.verticalWidget_43)
        self.posterboardLbl.setObjectName(u"posterboardLbl")
        self.posterboardLbl.setFont(font)

        self.verticalLayout_123.addWidget(self.posterboardLbl)

        self.verticalSpacer_23 = QSpacerItem(20, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_123.addItem(self.verticalSpacer_23)


        self.horizontalLayout_203.addWidget(self.verticalWidget_43)

        self.horizontalSpacer_73 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_203.addItem(self.horizontalSpacer_73)

        self.findPBBtn = QToolButton(self.horizontalWidget_7)
        self.findPBBtn.setObjectName(u"findPBBtn")
        icon23 = QIcon()
        icon23.addFile(u":/icon/globe.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.findPBBtn.setIcon(icon23)
        self.findPBBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_203.addWidget(self.findPBBtn)

        self.pbHelpBtn = QToolButton(self.horizontalWidget_7)
        self.pbHelpBtn.setObjectName(u"pbHelpBtn")
        self.pbHelpBtn.setMinimumSize(QSize(35, 35))
        self.pbHelpBtn.setMaximumSize(QSize(35, 35))
        icon24 = QIcon()
        icon24.addFile(u":/icon/questionmark.circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pbHelpBtn.setIcon(icon24)
        self.pbHelpBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_203.addWidget(self.pbHelpBtn)


        self.verticalLayout_143.addWidget(self.horizontalWidget_7)

        self.pbPagePicker = QWidget(self.posterboardPage)
        self.pbPagePicker.setObjectName(u"pbPagePicker")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pbPagePicker.sizePolicy().hasHeightForWidth())
        self.pbPagePicker.setSizePolicy(sizePolicy5)
        self.pbPagePicker.setMinimumSize(QSize(0, 30))
        self.pbPagePicker.setMaximumSize(QSize(16777215, 35))
        self.pbPagePicker.setStyleSheet(u"QToolButton {\n"
"	min-height: 25px;\n"
"	border-radius: 5px;\n"
"}")
        self.horizontalLayout_14 = QHBoxLayout(self.pbPagePicker)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 0, -1, 0)
        self.tendiesPageBtn = QToolButton(self.pbPagePicker)
        self.tendiesPageBtn.setObjectName(u"tendiesPageBtn")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.tendiesPageBtn.sizePolicy().hasHeightForWidth())
        self.tendiesPageBtn.setSizePolicy(sizePolicy6)
        self.tendiesPageBtn.setMinimumSize(QSize(0, 25))
        icon25 = QIcon()
        icon25.addFile(u":/icon/file-earmark-zip.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tendiesPageBtn.setIcon(icon25)
        self.tendiesPageBtn.setCheckable(True)
        self.tendiesPageBtn.setChecked(True)
        self.tendiesPageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_14.addWidget(self.tendiesPageBtn)

        self.templatePageBtn = QToolButton(self.pbPagePicker)
        self.templatePageBtn.setObjectName(u"templatePageBtn")
        self.templatePageBtn.setIcon(icon8)
        self.templatePageBtn.setCheckable(True)
        self.templatePageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_14.addWidget(self.templatePageBtn)

        self.videoPageBtn = QToolButton(self.pbPagePicker)
        self.videoPageBtn.setObjectName(u"videoPageBtn")
        self.videoPageBtn.setMinimumSize(QSize(0, 25))
        icon26 = QIcon()
        icon26.addFile(u":/icon/photo.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.videoPageBtn.setIcon(icon26)
        self.videoPageBtn.setCheckable(True)
        self.videoPageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_14.addWidget(self.videoPageBtn)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_21)

        self.label = QLabel(self.pbPagePicker)
        self.label.setObjectName(u"label")

        self.horizontalLayout_14.addWidget(self.label)


        self.verticalLayout_143.addWidget(self.pbPagePicker)

        self.line_123 = QFrame(self.posterboardPage)
        self.line_123.setObjectName(u"line_123")
        self.line_123.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_123.setFrameShadow(QFrame.Plain)
        self.line_123.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_143.addWidget(self.line_123)

        self.pbPages = QStackedWidget(self.posterboardPage)
        self.pbPages.setObjectName(u"pbPages")
        self.pbPages.setEnabled(False)
        self.pbTendiesPage = QWidget()
        self.pbTendiesPage.setObjectName(u"pbTendiesPage")
        self.verticalLayout_38 = QVBoxLayout(self.pbTendiesPage)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_121 = QHBoxLayout()
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.horizontalLayout_121.setContentsMargins(-1, -1, -1, 3)
        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_121.addItem(self.horizontalSpacer_18)

        self.importTendiesBtn = QToolButton(self.pbTendiesPage)
        self.importTendiesBtn.setObjectName(u"importTendiesBtn")
        self.importTendiesBtn.setLayoutDirection(Qt.RightToLeft)
        icon27 = QIcon()
        icon27.addFile(u":/icon/import.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.importTendiesBtn.setIcon(icon27)
        self.importTendiesBtn.setIconSize(QSize(20, 20))
        self.importTendiesBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_121.addWidget(self.importTendiesBtn)


        self.verticalLayout_38.addLayout(self.horizontalLayout_121)

        self.line_27 = QFrame(self.pbTendiesPage)
        self.line_27.setObjectName(u"line_27")
        self.line_27.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_27.setFrameShadow(QFrame.Plain)
        self.line_27.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_38.addWidget(self.line_27)

        self.pbFilesList = QWidget(self.pbTendiesPage)
        self.pbFilesList.setObjectName(u"pbFilesList")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.pbFilesList.sizePolicy().hasHeightForWidth())
        self.pbFilesList.setSizePolicy(sizePolicy7)
        self.pbFilesList.setMinimumSize(QSize(200, 35))

        self.verticalLayout_38.addWidget(self.pbFilesList)

        self.pbPages.addWidget(self.pbTendiesPage)
        self.pbTemplatesPage = QWidget()
        self.pbTemplatesPage.setObjectName(u"pbTemplatesPage")
        self.verticalLayout_381 = QVBoxLayout(self.pbTemplatesPage)
        self.verticalLayout_381.setObjectName(u"verticalLayout_381")
        self.verticalLayout_381.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_122 = QHBoxLayout()
        self.horizontalLayout_122.setObjectName(u"horizontalLayout_122")
        self.horizontalLayout_122.setContentsMargins(-1, -1, -1, 3)
        self.horizontalSpacer_181 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_122.addItem(self.horizontalSpacer_181)

        self.importTemplateBtn = QToolButton(self.pbTemplatesPage)
        self.importTemplateBtn.setObjectName(u"importTemplateBtn")
        self.importTemplateBtn.setLayoutDirection(Qt.RightToLeft)
        self.importTemplateBtn.setIcon(icon27)
        self.importTemplateBtn.setIconSize(QSize(20, 20))
        self.importTemplateBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_122.addWidget(self.importTemplateBtn)


        self.verticalLayout_381.addLayout(self.horizontalLayout_122)

        self.line_28 = QFrame(self.pbTemplatesPage)
        self.line_28.setObjectName(u"line_28")
        self.line_28.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_28.setFrameShadow(QFrame.Plain)
        self.line_28.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_381.addWidget(self.line_28)

        self.pbTemplatesList = QWidget(self.pbTemplatesPage)
        self.pbTemplatesList.setObjectName(u"pbTemplatesList")
        sizePolicy7.setHeightForWidth(self.pbTemplatesList.sizePolicy().hasHeightForWidth())
        self.pbTemplatesList.setSizePolicy(sizePolicy7)
        self.pbTemplatesList.setMinimumSize(QSize(200, 35))

        self.verticalLayout_381.addWidget(self.pbTemplatesList)

        self.pbPages.addWidget(self.pbTemplatesPage)
        self.pbVideoPage = QWidget()
        self.pbVideoPage.setObjectName(u"pbVideoPage")
        self.verticalLayout_39 = QVBoxLayout(self.pbVideoPage)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.caVideoChk = QCheckBox(self.pbVideoPage)
        self.caVideoChk.setObjectName(u"caVideoChk")
        self.caVideoChk.setChecked(True)

        self.verticalLayout_39.addWidget(self.caVideoChk)

        self.reverseLoopChk = QCheckBox(self.pbVideoPage)
        self.reverseLoopChk.setObjectName(u"reverseLoopChk")

        self.verticalLayout_39.addWidget(self.reverseLoopChk)

        self.useForegroundChk = QCheckBox(self.pbVideoPage)
        self.useForegroundChk.setObjectName(u"useForegroundChk")

        self.verticalLayout_39.addWidget(self.useForegroundChk)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.chooseThumbBtn = QToolButton(self.pbVideoPage)
        self.chooseThumbBtn.setObjectName(u"chooseThumbBtn")

        self.horizontalLayout_30.addWidget(self.chooseThumbBtn)

        self.chooseVideoBtn = QToolButton(self.pbVideoPage)
        self.chooseVideoBtn.setObjectName(u"chooseVideoBtn")

        self.horizontalLayout_30.addWidget(self.chooseVideoBtn)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_19)


        self.verticalLayout_39.addLayout(self.horizontalLayout_30)

        self.pbVideoThumbLbl = QLabel(self.pbVideoPage)
        self.pbVideoThumbLbl.setObjectName(u"pbVideoThumbLbl")
        self.pbVideoThumbLbl.setText(u"Current Thumbnail: None")

        self.verticalLayout_39.addWidget(self.pbVideoThumbLbl)

        self.pbVideoLbl = QLabel(self.pbVideoPage)
        self.pbVideoLbl.setObjectName(u"pbVideoLbl")
        self.pbVideoLbl.setText(u"Current Video: None")

        self.verticalLayout_39.addWidget(self.pbVideoLbl)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_39.addItem(self.verticalSpacer_22)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.advancedOptionsBtn = QToolButton(self.pbVideoPage)
        self.advancedOptionsBtn.setObjectName(u"advancedOptionsBtn")
        self.advancedOptionsBtn.setIcon(icon9)
        self.advancedOptionsBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_16.addWidget(self.advancedOptionsBtn)

        self.exportPBVideoBtn = QToolButton(self.pbVideoPage)
        self.exportPBVideoBtn.setObjectName(u"exportPBVideoBtn")
        self.exportPBVideoBtn.setEnabled(False)
        icon28 = QIcon()
        icon28.addFile(u":/icon/export.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.exportPBVideoBtn.setIcon(icon28)
        self.exportPBVideoBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_16.addWidget(self.exportPBVideoBtn)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_10)


        self.verticalLayout_39.addLayout(self.horizontalLayout_16)

        self.pbPages.addWidget(self.pbVideoPage)

        self.verticalLayout_143.addWidget(self.pbPages)

        self.pages.addWidget(self.posterboardPage)
        self.templatesPage = QWidget()
        self.templatesPage.setObjectName(u"templatesPage")
        self.verticalLayout_144 = QVBoxLayout(self.templatesPage)
        self.verticalLayout_144.setObjectName(u"verticalLayout_144")
        self.verticalLayout_144.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_53 = QWidget(self.templatesPage)
        self.horizontalWidget_53.setObjectName(u"horizontalWidget_53")
        self.horizontalLayout_204 = QHBoxLayout(self.horizontalWidget_53)
        self.horizontalLayout_204.setSpacing(10)
        self.horizontalLayout_204.setObjectName(u"horizontalLayout_204")
        self.horizontalLayout_204.setContentsMargins(0, 9, 0, 0)
        self.toolButton_104 = QToolButton(self.horizontalWidget_53)
        self.toolButton_104.setObjectName(u"toolButton_104")
        self.toolButton_104.setEnabled(True)
        self.toolButton_104.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_104.setIcon(icon8)

        self.horizontalLayout_204.addWidget(self.toolButton_104)

        self.verticalWidget_44 = QWidget(self.horizontalWidget_53)
        self.verticalWidget_44.setObjectName(u"verticalWidget_44")
        self.verticalLayout_124 = QVBoxLayout(self.verticalWidget_44)
        self.verticalLayout_124.setSpacing(6)
        self.verticalLayout_124.setObjectName(u"verticalLayout_124")
        self.verticalLayout_124.setContentsMargins(0, 0, 0, 0)
        self.templatesLbl = QLabel(self.verticalWidget_44)
        self.templatesLbl.setObjectName(u"templatesLbl")
        self.templatesLbl.setFont(font)

        self.verticalLayout_124.addWidget(self.templatesLbl)

        self.verticalSpacer_24 = QSpacerItem(20, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_124.addItem(self.verticalSpacer_24)


        self.horizontalLayout_204.addWidget(self.verticalWidget_44)

        self.horizontalSpacer_74 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_204.addItem(self.horizontalSpacer_74)


        self.verticalLayout_144.addWidget(self.horizontalWidget_53)

        self.line_124 = QFrame(self.templatesPage)
        self.line_124.setObjectName(u"line_124")
        self.line_124.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_124.setFrameShadow(QFrame.Plain)
        self.line_124.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_144.addWidget(self.line_124)

        self.verticalLayout_382 = QVBoxLayout()
        self.verticalLayout_382.setObjectName(u"verticalLayout_382")
        self.verticalLayout_382.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_123 = QHBoxLayout()
        self.horizontalLayout_123.setObjectName(u"horizontalLayout_123")
        self.horizontalLayout_123.setContentsMargins(-1, -1, -1, 3)
        self.horizontalSpacer_182 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_123.addItem(self.horizontalSpacer_182)

        self.importTemplatesBtn = QToolButton(self.templatesPage)
        self.importTemplatesBtn.setObjectName(u"importTemplatesBtn")
        self.importTemplatesBtn.setLayoutDirection(Qt.RightToLeft)
        self.importTemplatesBtn.setIcon(icon27)
        self.importTemplatesBtn.setIconSize(QSize(20, 20))
        self.importTemplatesBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_123.addWidget(self.importTemplatesBtn)


        self.verticalLayout_382.addLayout(self.horizontalLayout_123)

        self.line_281 = QFrame(self.templatesPage)
        self.line_281.setObjectName(u"line_281")
        self.line_281.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_281.setFrameShadow(QFrame.Plain)
        self.line_281.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_382.addWidget(self.line_281)

        self.templatesList = QWidget(self.templatesPage)
        self.templatesList.setObjectName(u"templatesList")
        sizePolicy7.setHeightForWidth(self.templatesList.sizePolicy().hasHeightForWidth())
        self.templatesList.setSizePolicy(sizePolicy7)
        self.templatesList.setMinimumSize(QSize(200, 35))

        self.verticalLayout_382.addWidget(self.templatesList)


        self.verticalLayout_144.addLayout(self.verticalLayout_382)

        self.pages.addWidget(self.templatesPage)
        self.advancedOptionsPage = QWidget()
        self.advancedOptionsPage.setObjectName(u"advancedOptionsPage")
        self.verticalLayout_145 = QVBoxLayout(self.advancedOptionsPage)
        self.verticalLayout_145.setObjectName(u"verticalLayout_145")
        self.verticalLayout_145.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_54 = QWidget(self.advancedOptionsPage)
        self.horizontalWidget_54.setObjectName(u"horizontalWidget_54")
        self.horizontalLayout_205 = QHBoxLayout(self.horizontalWidget_54)
        self.horizontalLayout_205.setSpacing(10)
        self.horizontalLayout_205.setObjectName(u"horizontalLayout_205")
        self.horizontalLayout_205.setContentsMargins(0, 9, 0, 9)
        self.toolButton_105 = QToolButton(self.horizontalWidget_54)
        self.toolButton_105.setObjectName(u"toolButton_105")
        self.toolButton_105.setEnabled(False)
        self.toolButton_105.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_105.setIcon(icon14)

        self.horizontalLayout_205.addWidget(self.toolButton_105)

        self.verticalWidget_45 = QWidget(self.horizontalWidget_54)
        self.verticalWidget_45.setObjectName(u"verticalWidget_45")
        self.verticalLayout_125 = QVBoxLayout(self.verticalWidget_45)
        self.verticalLayout_125.setSpacing(6)
        self.verticalLayout_125.setObjectName(u"verticalLayout_125")
        self.verticalLayout_125.setContentsMargins(0, 0, 0, 0)
        self.advancedOptionsLbl = QLabel(self.verticalWidget_45)
        self.advancedOptionsLbl.setObjectName(u"advancedOptionsLbl")
        self.advancedOptionsLbl.setFont(font)

        self.verticalLayout_125.addWidget(self.advancedOptionsLbl)

        self.verticalSpacer_181 = QSpacerItem(20, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_125.addItem(self.verticalSpacer_181)


        self.horizontalLayout_205.addWidget(self.verticalWidget_45)

        self.horizontalSpacer_75 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_205.addItem(self.horizontalSpacer_75)


        self.verticalLayout_145.addWidget(self.horizontalWidget_54)

        self.line_125 = QFrame(self.advancedOptionsPage)
        self.line_125.setObjectName(u"line_125")
        self.line_125.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_125.setFrameShadow(QFrame.Plain)
        self.line_125.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_145.addWidget(self.line_125)

        self.advancedOptionsPageContent = QWidget(self.advancedOptionsPage)
        self.advancedOptionsPageContent.setObjectName(u"advancedOptionsPageContent")
        self.advancedOptionsPageContent.setEnabled(True)
        self.verticalLayout_133 = QVBoxLayout(self.advancedOptionsPageContent)
        self.verticalLayout_133.setObjectName(u"verticalLayout_133")
        self.verticalLayout_133.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.advancedOptionsPageContent)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_133.addWidget(self.label_17)

        self.line_191 = QFrame(self.advancedOptionsPageContent)
        self.line_191.setObjectName(u"line_191")
        self.line_191.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_191.setFrameShadow(QFrame.Plain)
        self.line_191.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_133.addWidget(self.line_191)

        self.disableOTAChk = QCheckBox(self.advancedOptionsPageContent)
        self.disableOTAChk.setObjectName(u"disableOTAChk")

        self.verticalLayout_133.addWidget(self.disableOTAChk)

        self.thermalmonitordChk = QCheckBox(self.advancedOptionsPageContent)
        self.thermalmonitordChk.setObjectName(u"thermalmonitordChk")

        self.verticalLayout_133.addWidget(self.thermalmonitordChk)

        self.line_181 = QFrame(self.advancedOptionsPageContent)
        self.line_181.setObjectName(u"line_181")
        self.line_181.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_181.setFrameShadow(QFrame.Plain)
        self.line_181.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_133.addWidget(self.line_181)

        self.enableResolutionChk = QCheckBox(self.advancedOptionsPageContent)
        self.enableResolutionChk.setObjectName(u"enableResolutionChk")

        self.verticalLayout_133.addWidget(self.enableResolutionChk)

        self.resChangerContent = QWidget(self.advancedOptionsPageContent)
        self.resChangerContent.setObjectName(u"resChangerContent")
        self.resChangerContent.setEnabled(True)
        self.verticalLayout_35 = QVBoxLayout(self.resChangerContent)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.resHeightLbl = QLabel(self.resChangerContent)
        self.resHeightLbl.setObjectName(u"resHeightLbl")
        self.resHeightLbl.setEnabled(False)

        self.verticalLayout_35.addWidget(self.resHeightLbl)

        self.horizontalLayout_91 = QHBoxLayout()
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalLayout_91.setContentsMargins(-1, -1, -1, 5)
        self.resHeightTxt = QLineEdit(self.resChangerContent)
        self.resHeightTxt.setObjectName(u"resHeightTxt")
        self.resHeightTxt.setEnabled(True)

        self.horizontalLayout_91.addWidget(self.resHeightTxt)

        self.resHeightWarningLbl = QLabel(self.resChangerContent)
        self.resHeightWarningLbl.setObjectName(u"resHeightWarningLbl")
        self.resHeightWarningLbl.setMinimumSize(QSize(22, 0))
        self.resHeightWarningLbl.setStyleSheet(u"QLabel {\n"
"		border: 2px solid red;\n"
"		border-radius: 25px;\n"
"		color: red;\n"
"}")
        self.resHeightWarningLbl.setFrameShape(QFrame.NoFrame)
        self.resHeightWarningLbl.setFrameShadow(QFrame.Plain)
        self.resHeightWarningLbl.setText(u"!")
        self.resHeightWarningLbl.setScaledContents(False)
        self.resHeightWarningLbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_91.addWidget(self.resHeightWarningLbl)


        self.verticalLayout_35.addLayout(self.horizontalLayout_91)

        self.resWidthLbl = QLabel(self.resChangerContent)
        self.resWidthLbl.setObjectName(u"resWidthLbl")

        self.verticalLayout_35.addWidget(self.resWidthLbl)

        self.resolutionContent = QVBoxLayout()
        self.resolutionContent.setObjectName(u"resolutionContent")
        self.resolutionContent.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_101 = QHBoxLayout()
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.horizontalLayout_101.setContentsMargins(-1, -1, -1, 5)
        self.resWidthTxt = QLineEdit(self.resChangerContent)
        self.resWidthTxt.setObjectName(u"resWidthTxt")

        self.horizontalLayout_101.addWidget(self.resWidthTxt)

        self.resWidthWarningLbl = QLabel(self.resChangerContent)
        self.resWidthWarningLbl.setObjectName(u"resWidthWarningLbl")
        self.resWidthWarningLbl.setMinimumSize(QSize(22, 0))
        self.resWidthWarningLbl.setStyleSheet(u"QLabel {\n"
"		border: 2px solid red;\n"
"		border-radius: 25px;\n"
"		color: red;\n"
"}")
        self.resWidthWarningLbl.setText(u"!")
        self.resWidthWarningLbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_101.addWidget(self.resWidthWarningLbl)


        self.resolutionContent.addLayout(self.horizontalLayout_101)


        self.verticalLayout_35.addLayout(self.resolutionContent)


        self.verticalLayout_133.addWidget(self.resChangerContent)

        self.verticalSpacer_63 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_133.addItem(self.verticalSpacer_63)


        self.verticalLayout_145.addWidget(self.advancedOptionsPageContent)

        self.pages.addWidget(self.advancedOptionsPage)
        self.miscOptionsPage = QWidget()
        self.miscOptionsPage.setObjectName(u"miscOptionsPage")
        self.verticalLayout_6 = QVBoxLayout(self.miscOptionsPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget2 = QWidget(self.miscOptionsPage)
        self.verticalWidget2.setObjectName(u"verticalWidget2")
        self.verticalLayout_24 = QVBoxLayout(self.verticalWidget2)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.statusBarPageHeader_2 = QWidget(self.verticalWidget2)
        self.statusBarPageHeader_2.setObjectName(u"statusBarPageHeader_2")
        self.horizontalLayout_33 = QHBoxLayout(self.statusBarPageHeader_2)
        self.horizontalLayout_33.setSpacing(10)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, -1, 0, -1)
        self.toolButton_18 = QToolButton(self.statusBarPageHeader_2)
        self.toolButton_18.setObjectName(u"toolButton_18")
        self.toolButton_18.setEnabled(True)
        self.toolButton_18.setStyleSheet(u"QToolButton {\n"
"    icon-size: 24px;\n"
"    background-color: transparent;\n"
"    padding-left: 0px;\n"
"    padding-right: 5px;\n"
"    border-radius: 0px;\n"
"}")
        self.toolButton_18.setIcon(icon9)

        self.horizontalLayout_33.addWidget(self.toolButton_18)

        self.verticalWidget_11 = QWidget(self.statusBarPageHeader_2)
        self.verticalWidget_11.setObjectName(u"verticalWidget_11")
        self.verticalLayout_33 = QVBoxLayout(self.verticalWidget_11)
        self.verticalLayout_33.setSpacing(6)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.statusBarLbl_5 = QLabel(self.verticalWidget_11)
        self.statusBarLbl_5.setObjectName(u"statusBarLbl_5")
        self.statusBarLbl_5.setFont(font)

        self.verticalLayout_33.addWidget(self.statusBarLbl_5)

        self.label_16 = QLabel(self.verticalWidget_11)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_33.addWidget(self.label_16)


        self.horizontalLayout_33.addWidget(self.verticalWidget_11)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_15)


        self.verticalLayout_24.addWidget(self.statusBarPageHeader_2)

        self.line_5 = QFrame(self.verticalWidget2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"QFrame {\n"
"    color: #414141;\n"
"}")
        self.line_5.setFrameShadow(QFrame.Plain)
        self.line_5.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_24.addWidget(self.line_5)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_10)

        self.gridOptions_2 = QWidget(self.verticalWidget2)
        self.gridOptions_2.setObjectName(u"gridOptions_2")
        sizePolicy1.setHeightForWidth(self.gridOptions_2.sizePolicy().hasHeightForWidth())
        self.gridOptions_2.setSizePolicy(sizePolicy1)
        self.gridOptions_2.setStyleSheet(u"QToolButton {\n"
"    background-color: #3b3b3b;\n"
"    border: none;\n"
"    color: #e8e8e8;\n"
"    font-size: 16px;\n"
"	min-width: 100px;\n"
"	min-height: 80px;\n"
"	icon-size: 40px;\n"
"	padding-left: 8px;\n"
"	padding-right: 8px;\n"
"	padding-top: 8px;\n"
"	padding-bottom: 8px;\n"
"	border-radius: 12px;\n"
"}")
        self.gridOptions = QGridLayout(self.gridOptions_2)
        self.gridOptions.setObjectName(u"gridOptions")
        self.gridOptions.setContentsMargins(200, 5, 200, 5)
        self.springboardOptionsPageBtn = QToolButton(self.gridOptions_2)
        self.springboardOptionsPageBtn.setObjectName(u"springboardOptionsPageBtn")
        sizePolicy.setHeightForWidth(self.springboardOptionsPageBtn.sizePolicy().hasHeightForWidth())
        self.springboardOptionsPageBtn.setSizePolicy(sizePolicy)
        self.springboardOptionsPageBtn.setMinimumSize(QSize(116, 96))
        self.springboardOptionsPageBtn.setIcon(icon20)
        self.springboardOptionsPageBtn.setIconSize(QSize(36, 36))
        self.springboardOptionsPageBtn.setCheckable(False)
        self.springboardOptionsPageBtn.setAutoExclusive(False)
        self.springboardOptionsPageBtn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.springboardOptionsPageBtn.setProperty(u"cls", u"miscBtn")

        self.gridOptions.addWidget(self.springboardOptionsPageBtn, 0, 0, 1, 1)

        self.internalOptionsPageBtn = QToolButton(self.gridOptions_2)
        self.internalOptionsPageBtn.setObjectName(u"internalOptionsPageBtn")
        sizePolicy.setHeightForWidth(self.internalOptionsPageBtn.sizePolicy().hasHeightForWidth())
        self.internalOptionsPageBtn.setSizePolicy(sizePolicy)
        self.internalOptionsPageBtn.setIcon(icon21)
        self.internalOptionsPageBtn.setCheckable(False)
        self.internalOptionsPageBtn.setAutoExclusive(False)
        self.internalOptionsPageBtn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.internalOptionsPageBtn.setProperty(u"cls", u"miscBtn")

        self.gridOptions.addWidget(self.internalOptionsPageBtn, 0, 1, 1, 1)

        self.daemonsPageBtn = QToolButton(self.gridOptions_2)
        self.daemonsPageBtn.setObjectName(u"daemonsPageBtn")
        self.daemonsPageBtn.setEnabled(True)
        sizePolicy.setHeightForWidth(self.daemonsPageBtn.sizePolicy().hasHeightForWidth())
        self.daemonsPageBtn.setSizePolicy(sizePolicy)
        self.daemonsPageBtn.setIcon(icon22)
        self.daemonsPageBtn.setCheckable(False)
        self.daemonsPageBtn.setAutoExclusive(False)
        self.daemonsPageBtn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.daemonsPageBtn.setProperty(u"cls", u"miscBtn")

        self.gridOptions.addWidget(self.daemonsPageBtn, 1, 0, 1, 1)

        self.advancedPageBtn = QToolButton(self.gridOptions_2)
        self.advancedPageBtn.setObjectName(u"advancedPageBtn")
        sizePolicy.setHeightForWidth(self.advancedPageBtn.sizePolicy().hasHeightForWidth())
        self.advancedPageBtn.setSizePolicy(sizePolicy)
        self.advancedPageBtn.setIcon(icon14)
        self.advancedPageBtn.setCheckable(False)
        self.advancedPageBtn.setAutoExclusive(False)
        self.advancedPageBtn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.advancedPageBtn.setProperty(u"cls", u"miscBtn")

        self.gridOptions.addWidget(self.advancedPageBtn, 1, 1, 1, 1)


        self.verticalLayout_24.addWidget(self.gridOptions_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_2)


        self.verticalLayout_6.addWidget(self.verticalWidget2)

        self.pages.addWidget(self.miscOptionsPage)
        self.applyPage = QWidget()
        self.applyPage.setObjectName(u"applyPage")
        self.verticalLayout_61 = QVBoxLayout(self.applyPage)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget3 = QWidget(self.applyPage)
        self.verticalWidget3.setObjectName(u"verticalWidget3")
        self.verticalLayout_241 = QVBoxLayout(self.verticalWidget3)
        self.verticalLayout_241.setObjectName(u"verticalLayout_241")
        self.verticalLayout_241.setContentsMargins(0, 0, 0, 0)
        self.locSimPageHeader_2 = QWidget(self.verticalWidget3)
        self.locSimPageHeader_2.setObjectName(u"locSimPageHeader_2")
        self.horizontalLayout_331 = QHBoxLayout(self.locSimPageHeader_2)
        self.horizontalLayout_331.setSpacing(10)
        self.horizontalLayout_331.setObjectName(u"horizontalLayout_331")
        self.horizontalLayout_331.setContentsMargins(0, -1, 0, -1)
        self.toolButton_181 = QToolButton(self.locSimPageHeader_2)
        self.toolButton_181.setObjectName(u"toolButton_181")
        self.toolButton_181.setEnabled(False)
        self.toolButton_181.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_181.setIcon(icon10)

        self.horizontalLayout_331.addWidget(self.toolButton_181)

        self.verticalWidget_111 = QWidget(self.locSimPageHeader_2)
        self.verticalWidget_111.setObjectName(u"verticalWidget_111")
        self.verticalLayout_331 = QVBoxLayout(self.verticalWidget_111)
        self.verticalLayout_331.setSpacing(6)
        self.verticalLayout_331.setObjectName(u"verticalLayout_331")
        self.verticalLayout_331.setContentsMargins(0, 0, 0, 0)
        self.statusBarLbl_51 = QLabel(self.verticalWidget_111)
        self.statusBarLbl_51.setObjectName(u"statusBarLbl_51")
        self.statusBarLbl_51.setFont(font)

        self.verticalLayout_331.addWidget(self.statusBarLbl_51)

        self.label_161 = QLabel(self.verticalWidget_111)
        self.label_161.setObjectName(u"label_161")

        self.verticalLayout_331.addWidget(self.label_161)


        self.horizontalLayout_331.addWidget(self.verticalWidget_111)

        self.horizontalSpacer_151 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_331.addItem(self.horizontalSpacer_151)


        self.verticalLayout_241.addWidget(self.locSimPageHeader_2)

        self.line_51 = QFrame(self.verticalWidget3)
        self.line_51.setObjectName(u"line_51")
        self.line_51.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_51.setFrameShadow(QFrame.Plain)
        self.line_51.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_241.addWidget(self.line_51)

        self.verticalSpacer_101 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_241.addItem(self.verticalSpacer_101)

        self.gestaltLocationTitleLbl = QLabel(self.verticalWidget3)
        self.gestaltLocationTitleLbl.setObjectName(u"gestaltLocationTitleLbl")
        self.gestaltLocationTitleLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_241.addWidget(self.gestaltLocationTitleLbl)

        self.gestaltLocationLbl = QLabel(self.verticalWidget3)
        self.gestaltLocationLbl.setObjectName(u"gestaltLocationLbl")
        self.gestaltLocationLbl.setText(u"None")
        self.gestaltLocationLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_241.addWidget(self.gestaltLocationLbl)

        self.horizontalLayout_71 = QHBoxLayout()
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(-1, 10, -1, 0)
        self.chooseGestaltBtn = QToolButton(self.verticalWidget3)
        self.chooseGestaltBtn.setObjectName(u"chooseGestaltBtn")
        icon29 = QIcon()
        icon29.addFile(u":/icon/folder.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.chooseGestaltBtn.setIcon(icon29)
        self.chooseGestaltBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_71.addWidget(self.chooseGestaltBtn)


        self.verticalLayout_241.addLayout(self.horizontalLayout_71)

        self.horizontalWidget10 = QWidget(self.verticalWidget3)
        self.horizontalWidget10.setObjectName(u"horizontalWidget10")
        self.horizontalLayout_17 = QHBoxLayout(self.horizontalWidget10)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.applyTweaksBtn = QToolButton(self.horizontalWidget10)
        self.applyTweaksBtn.setObjectName(u"applyTweaksBtn")
        self.applyTweaksBtn.setIcon(icon10)
        self.applyTweaksBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_17.addWidget(self.applyTweaksBtn)


        self.verticalLayout_241.addWidget(self.horizontalWidget10)

        self.statusLbl = QLabel(self.verticalWidget3)
        self.statusLbl.setObjectName(u"statusLbl")
        self.statusLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_241.addWidget(self.statusLbl)

        self.restoreProgressBar = QProgressBar(self.verticalWidget3)
        self.restoreProgressBar.setObjectName(u"restoreProgressBar")
        sizePolicy.setHeightForWidth(self.restoreProgressBar.sizePolicy().hasHeightForWidth())
        self.restoreProgressBar.setSizePolicy(sizePolicy)
        self.restoreProgressBar.setMinimumSize(QSize(150, 0))
        self.restoreProgressBar.setValue(0)
        self.restoreProgressBar.setAlignment(Qt.AlignCenter)

        self.verticalLayout_241.addWidget(self.restoreProgressBar, 0, Qt.AlignHCenter)

        self.skipSetupOnLbl = QLabel(self.verticalWidget3)
        self.skipSetupOnLbl.setObjectName(u"skipSetupOnLbl")
        self.skipSetupOnLbl.setFont(font)
        self.skipSetupOnLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_241.addWidget(self.skipSetupOnLbl)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_241.addItem(self.verticalSpacer_21)

        self.horizontalWidget11 = QWidget(self.verticalWidget3)
        self.horizontalWidget11.setObjectName(u"horizontalWidget11")
        self.horizontalLayout_25 = QHBoxLayout(self.horizontalWidget11)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_14)

        self.removeTweaksBtn = QToolButton(self.horizontalWidget11)
        self.removeTweaksBtn.setObjectName(u"removeTweaksBtn")

        self.horizontalLayout_25.addWidget(self.removeTweaksBtn)

        self.resetGestaltBtn = QToolButton(self.horizontalWidget11)
        self.resetGestaltBtn.setObjectName(u"resetGestaltBtn")

        self.horizontalLayout_25.addWidget(self.resetGestaltBtn)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_16)


        self.verticalLayout_241.addWidget(self.horizontalWidget11)


        self.verticalLayout_61.addWidget(self.verticalWidget3)

        self.pages.addWidget(self.applyPage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.verticalLayout_101 = QVBoxLayout(self.settingsPage)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.verticalLayout_101.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_41 = QWidget(self.settingsPage)
        self.horizontalWidget_41.setObjectName(u"horizontalWidget_41")
        self.horizontalLayout_131 = QHBoxLayout(self.horizontalWidget_41)
        self.horizontalLayout_131.setSpacing(10)
        self.horizontalLayout_131.setObjectName(u"horizontalLayout_131")
        self.horizontalLayout_131.setContentsMargins(0, 9, 0, 9)
        self.toolButton_71 = QToolButton(self.horizontalWidget_41)
        self.toolButton_71.setObjectName(u"toolButton_71")
        self.toolButton_71.setEnabled(False)
        self.toolButton_71.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_71.setIcon(icon11)

        self.horizontalLayout_131.addWidget(self.toolButton_71)

        self.verticalWidget_31 = QWidget(self.horizontalWidget_41)
        self.verticalWidget_31.setObjectName(u"verticalWidget_31")
        self.verticalLayout_71 = QVBoxLayout(self.verticalWidget_31)
        self.verticalLayout_71.setSpacing(6)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.springboardOptionsLbl1 = QLabel(self.verticalWidget_31)
        self.springboardOptionsLbl1.setObjectName(u"springboardOptionsLbl1")
        self.springboardOptionsLbl1.setFont(font)

        self.verticalLayout_71.addWidget(self.springboardOptionsLbl1)

        self.verticalSpacer_17 = QSpacerItem(20, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_71.addItem(self.verticalSpacer_17)


        self.horizontalLayout_131.addWidget(self.verticalWidget_31)

        self.horizontalSpacer_61 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_131.addItem(self.horizontalSpacer_61)


        self.verticalLayout_101.addWidget(self.horizontalWidget_41)

        self.line_111 = QFrame(self.settingsPage)
        self.line_111.setObjectName(u"line_111")
        self.line_111.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_111.setFrameShadow(QFrame.Plain)
        self.line_111.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_101.addWidget(self.line_111)

        self.settingsPageContent = QWidget(self.settingsPage)
        self.settingsPageContent.setObjectName(u"settingsPageContent")
        self.settingsPageContent.setEnabled(True)
        self.settingsPageContent.setMaximumSize(QSize(650, 16777215))
        self._21 = QVBoxLayout(self.settingsPageContent)
        self._21.setObjectName(u"_21")
        self._21.setContentsMargins(0, 0, 0, 0)
        self.languageWidget = QWidget(self.settingsPageContent)
        self.languageWidget.setObjectName(u"languageWidget")
        self.languageWidget.setMinimumSize(QSize(0, 25))
        self.horizontalLayout_3 = QHBoxLayout(self.languageWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.langIcn = QToolButton(self.languageWidget)
        self.langIcn.setObjectName(u"langIcn")
        self.langIcn.setMinimumSize(QSize(0, 35))
        self.langIcn.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.langIcn.setText(u"")
        icon30 = QIcon()
        icon30.addFile(u":/icon/translate.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.langIcn.setIcon(icon30)
        self.langIcn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.langIcn)

        self.langLbl = QLabel(self.languageWidget)
        self.langLbl.setObjectName(u"langLbl")
        self.langLbl.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.langLbl)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)

        self.label_4 = QLabel(self.languageWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setText(u"")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.langDrp = QComboBox(self.languageWidget)
        self.langDrp.setObjectName(u"langDrp")
        self.langDrp.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_3.addWidget(self.langDrp)


        self._21.addWidget(self.languageWidget)

        self.allowWifiApplyingChk = QCheckBox(self.settingsPageContent)
        self.allowWifiApplyingChk.setObjectName(u"allowWifiApplyingChk")
        self.allowWifiApplyingChk.setChecked(False)

        self._21.addWidget(self.allowWifiApplyingChk)

        self.autoRebootChk = QCheckBox(self.settingsPageContent)
        self.autoRebootChk.setObjectName(u"autoRebootChk")
        self.autoRebootChk.setChecked(True)

        self._21.addWidget(self.autoRebootChk)

        self.showRiskyChk = QCheckBox(self.settingsPageContent)
        self.showRiskyChk.setObjectName(u"showRiskyChk")

        self._21.addWidget(self.showRiskyChk)

        self.showAllSpoofableChk = QCheckBox(self.settingsPageContent)
        self.showAllSpoofableChk.setObjectName(u"showAllSpoofableChk")

        self._21.addWidget(self.showAllSpoofableChk)

        self.ignorePBFrameLimitChk = QCheckBox(self.settingsPageContent)
        self.ignorePBFrameLimitChk.setObjectName(u"ignorePBFrameLimitChk")

        self._21.addWidget(self.ignorePBFrameLimitChk)

        self.disableTendiesLimitChk = QCheckBox(self.settingsPageContent)
        self.disableTendiesLimitChk.setObjectName(u"disableTendiesLimitChk")

        self._21.addWidget(self.disableTendiesLimitChk)

        self.line_24 = QFrame(self.settingsPageContent)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_24.setFrameShadow(QFrame.Plain)
        self.line_24.setFrameShape(QFrame.Shape.HLine)

        self._21.addWidget(self.line_24)

        self.revertRdarChk = QCheckBox(self.settingsPageContent)
        self.revertRdarChk.setObjectName(u"revertRdarChk")

        self._21.addWidget(self.revertRdarChk)

        self.revertRdarLine = QFrame(self.settingsPageContent)
        self.revertRdarLine.setObjectName(u"revertRdarLine")
        self.revertRdarLine.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.revertRdarLine.setFrameShadow(QFrame.Plain)
        self.revertRdarLine.setFrameShape(QFrame.Shape.HLine)

        self._21.addWidget(self.revertRdarLine)

        self.trustStoreChk = QCheckBox(self.settingsPageContent)
        self.trustStoreChk.setObjectName(u"trustStoreChk")
        self.trustStoreChk.setChecked(False)

        self._21.addWidget(self.trustStoreChk)

        self.skipSetupChk = QCheckBox(self.settingsPageContent)
        self.skipSetupChk.setObjectName(u"skipSetupChk")
        self.skipSetupChk.setChecked(True)

        self._21.addWidget(self.skipSetupChk)

        self.supervisionChk = QCheckBox(self.settingsPageContent)
        self.supervisionChk.setObjectName(u"supervisionChk")
        self.supervisionChk.setEnabled(True)
        self.supervisionChk.setChecked(False)

        self._21.addWidget(self.supervisionChk)

        self.supervisionOrganization = QLineEdit(self.settingsPageContent)
        self.supervisionOrganization.setObjectName(u"supervisionOrganization")

        self._21.addWidget(self.supervisionOrganization)

        self.verticalSpacer_211 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self._21.addItem(self.verticalSpacer_211)

        self.label_15 = QLabel(self.settingsPageContent)
        self.label_15.setObjectName(u"label_15")

        self._21.addWidget(self.label_15)

        self.line_20 = QFrame(self.settingsPageContent)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_20.setFrameShadow(QFrame.Plain)
        self.line_20.setFrameShape(QFrame.Shape.HLine)

        self._21.addWidget(self.line_20)

        self.deviceSettingsBtns = QHBoxLayout()
        self.deviceSettingsBtns.setObjectName(u"deviceSettingsBtns")
        self.deviceSettingsBtns.setContentsMargins(-1, -1, -1, 0)
        self.resetPairBtn = QToolButton(self.settingsPageContent)
        self.resetPairBtn.setObjectName(u"resetPairBtn")

        self.deviceSettingsBtns.addWidget(self.resetPairBtn)


        self._21.addLayout(self.deviceSettingsBtns)

        self.horizontalLayout_3211 = QHBoxLayout()
        self.horizontalLayout_3211.setObjectName(u"horizontalLayout_3211")
        self.horizontalLayout_3211.setContentsMargins(-1, -1, -1, 0)
        self.pocketPosterHelperBtn = QToolButton(self.settingsPageContent)
        self.pocketPosterHelperBtn.setObjectName(u"pocketPosterHelperBtn")

        self.horizontalLayout_3211.addWidget(self.pocketPosterHelperBtn)


        self._21.addLayout(self.horizontalLayout_3211)

        self.verticalSpacer_51 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self._21.addItem(self.verticalSpacer_51)


        self.verticalLayout_101.addWidget(self.settingsPageContent)

        self.pages.addWidget(self.settingsPage)

        self._3.addWidget(self.pages)


        self.horizontalLayout_18.addWidget(self.main)


        self.verticalLayout_11.addWidget(self.body)

        Nugget.setCentralWidget(self.centralwidget)

        self.retranslateUi(Nugget)

        self.devicePicker.setCurrentIndex(-1)
        self.pages.setCurrentIndex(8)
        self.dynamicIslandDrp.setCurrentIndex(0)
        self.spoofedModelDrp.setCurrentIndex(0)
        self.pTypeDrp.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Nugget)
    # setupUi

    def retranslateUi(self, Nugget):
        self.homePageBtn.setText(QCoreApplication.translate("Nugget", u"    Home", None))
        self.posterboardPageBtn.setText(QCoreApplication.translate("Nugget", u"    Posterboard", None))
        self.gestaltPageBtn.setText(QCoreApplication.translate("Nugget", u"     Mobile Gestalt", None))
        self.featureFlagsPageBtn.setText(QCoreApplication.translate("Nugget", u"    Feature Flags", None))
        self.euEnablerPageBtn.setText(QCoreApplication.translate("Nugget", u"    Eligibility", None))
        self.statusBarPageBtn.setText(QCoreApplication.translate("Nugget", u"    Status Bar", None))
        self.templatesPageBtn.setText(QCoreApplication.translate("Nugget", u"    Templates", None))
        self.miscOptionsBtn.setText(QCoreApplication.translate("Nugget", u"    Miscellaneous", None))
        self.applyPageBtn.setText(QCoreApplication.translate("Nugget", u"    Apply", None))
        self.settingsPageBtn.setText(QCoreApplication.translate("Nugget", u"    Settings", None))
        self.bigNuggetBtn.setText(QCoreApplication.translate("Nugget", u"...", None))
        self.discordBtn.setText(QCoreApplication.translate("Nugget", u"  Join the Discord", None))
        self.starOnGithubBtn.setText(QCoreApplication.translate("Nugget", u" Star on Github", None))
#if QT_CONFIG(tooltip)
        self.leminBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.leminBtn.setText(QCoreApplication.translate("Nugget", u"  LeminLimez", None))
        self.leminTwitterBtn.setText(QCoreApplication.translate("Nugget", u"...", None))
        self.leminGithubBtn.setText(QCoreApplication.translate("Nugget", u"...", None))
        self.leminKoFiBtn.setText(QCoreApplication.translate("Nugget", u"...", None))
        self.toolButton_14.setText(QCoreApplication.translate("Nugget", u"Main Developer", None))
        self.helpFromBtn.setText(QCoreApplication.translate("Nugget", u"With Help From", None))
#if QT_CONFIG(tooltip)
        self.posterRestoreBtn.setToolTip(QCoreApplication.translate("Nugget", u"dootskyre, dulark, forcequitOS, pengubow, Middo, and SerStars", None))
#endif // QT_CONFIG(tooltip)
        self.posterRestoreBtn.setText(QCoreApplication.translate("Nugget", u"PosterRestore Team\n"
"Posterboard", None))
        self.snoolieBtn.setText(QCoreApplication.translate("Nugget", u"Snoolie\n"
".aar Handling", None))
        self.disfordottieBtn.setText(QCoreApplication.translate("Nugget", u"disfordottie\n"
"Feature Flags", None))
        self.mikasaBtn.setText(QCoreApplication.translate("Nugget", u"Mikasa\n"
"Quiet Daemon", None))
        self.toolButton_15.setText(QCoreApplication.translate("Nugget", u"Additional Thanks", None))
        self.translatorsBtn.setText(QCoreApplication.translate("Nugget", u"Translators", None))
        self.libiBtn.setText(QCoreApplication.translate("Nugget", u"pymobiledevice3", None))
        self.jjtechBtn.setText(QCoreApplication.translate("Nugget", u"JJTech\n"
"Sparserestore", None))
        self.qtBtn.setText(QCoreApplication.translate("Nugget", u"Qt Creator", None))
        self.appVersionLbl.setText(QCoreApplication.translate("Nugget", u"Nugget GUI - Version %VERSION %BETATAG", None))
        self.statusBarLbl.setText(QCoreApplication.translate("Nugget", u"Mobile Gestalt", None))
        self.mgaWarningLbl.setText(QCoreApplication.translate("Nugget", u"! You will need a MobileGestalt file for this feature. Please select it in the Apply page !", None))
        self.label_9.setText(QCoreApplication.translate("Nugget", u"Device Subtype Preset", None))
        self.dynamicIslandDrp.setItemText(1, QCoreApplication.translate("Nugget", u"2436 (iPhone X Gestures for SE phones)", None))
        self.dynamicIslandDrp.setItemText(2, QCoreApplication.translate("Nugget", u"2556 (iPhone 14 Pro Dynamic Island)", None))
        self.dynamicIslandDrp.setItemText(3, QCoreApplication.translate("Nugget", u"2796 (iPhone 14 Pro Max Dynamic Island)", None))
        self.dynamicIslandDrp.setItemText(4, QCoreApplication.translate("Nugget", u"2976 (iPhone 15 Pro Max Dynamic Island)", None))
        self.dynamicIslandDrp.setItemText(5, QCoreApplication.translate("Nugget", u"2622 (iPhone 16 Pro Dynamic Island)", None))
        self.dynamicIslandDrp.setItemText(6, QCoreApplication.translate("Nugget", u"2868 (iPhone 16 Pro Max Dynamic Island)", None))

#if QT_CONFIG(tooltip)
        self.rdarFixChk.setToolTip(QCoreApplication.translate("Nugget", u"Modifies the resolution to improve functionality of the changed device subtype. May cause weird visual bugs.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.modelNameChk.setToolTip(QCoreApplication.translate("Nugget", u"Changes the model name in the 'About' page in the Settings app.", None))
#endif // QT_CONFIG(tooltip)
        self.modelNameChk.setText(QCoreApplication.translate("Nugget", u"Change Device Model Name", None))
        self.modelNameTxt.setPlaceholderText(QCoreApplication.translate("Nugget", u"Model Name", None))
#if QT_CONFIG(tooltip)
        self.bootChimeChk.setToolTip(QCoreApplication.translate("Nugget", u"Plays a sound when the device shuts down.\n"
"\n"
"After enabling, you can find the option to enable it in 'Accessibility' settings.", None))
#endif // QT_CONFIG(tooltip)
        self.bootChimeChk.setText(QCoreApplication.translate("Nugget", u"Enable Boot Chime", None))
#if QT_CONFIG(tooltip)
        self.chargeLimitChk.setToolTip(QCoreApplication.translate("Nugget", u"Shows the charge limit menu in Settings. Actual limiting may not be functional.", None))
#endif // QT_CONFIG(tooltip)
        self.chargeLimitChk.setText(QCoreApplication.translate("Nugget", u"Enable Charge Limit", None))
        self.tapToWakeChk.setText(QCoreApplication.translate("Nugget", u"Enable Tap to Wake (for iPhone SEs)", None))
#if QT_CONFIG(tooltip)
        self.iphone16SettingsChk.setToolTip(QCoreApplication.translate("Nugget", u"Enables Camera Control menu in Settings app and allows for downloading A17 Pro-exclusive apps (when spoofed).", None))
#endif // QT_CONFIG(tooltip)
        self.iphone16SettingsChk.setText(QCoreApplication.translate("Nugget", u"Enable iPhone 16 Settings", None))
#if QT_CONFIG(tooltip)
        self.parallaxChk.setToolTip(QCoreApplication.translate("Nugget", u"Disables the motion of the wallpaper.", None))
#endif // QT_CONFIG(tooltip)
        self.parallaxChk.setText(QCoreApplication.translate("Nugget", u"Disable Wallpaper Parallax", None))
        self.stageManagerChk.setText(QCoreApplication.translate("Nugget", u"Enable Stage Manager Supported", None))
        self.enableMedusaChk.setText(QCoreApplication.translate("Nugget", u"Enable Medusa (iPad Multitasking)", None))
        self.ipadAppsChk.setText(QCoreApplication.translate("Nugget", u"Allow iPad Apps on iPhone", None))
#if QT_CONFIG(tooltip)
        self.shutterChk.setToolTip(QCoreApplication.translate("Nugget", u"Sets the device's region to LL/A to bypass certain region restrictions like the forced shutter sound.", None))
#endif // QT_CONFIG(tooltip)
        self.shutterChk.setText(QCoreApplication.translate("Nugget", u"Disable Region Restrictions (ie. Shutter Sound)", None))
        self.findMyFriendsChk.setText(QCoreApplication.translate("Nugget", u"Enable Find My Friends", None))
        self.pencilChk.setText(QCoreApplication.translate("Nugget", u"Enable Apple Pencil Settings Tab", None))
        self.actionButtonChk.setText(QCoreApplication.translate("Nugget", u"Enable Action Button Settings Tab", None))
#if QT_CONFIG(tooltip)
        self.internalInstallChk.setToolTip(QCoreApplication.translate("Nugget", u"Use the Metal HUD in any app. Enable Metal HUD through Springboard Options.\n"
"\n"
"Note: OTA updates will be broken until this is disabled.", None))
#endif // QT_CONFIG(tooltip)
        self.internalInstallChk.setText(QCoreApplication.translate("Nugget", u"Set as Apple Internal Install (ie Metal HUD in any app)", None))
#if QT_CONFIG(tooltip)
        self.internalStorageChk.setToolTip(QCoreApplication.translate("Nugget", u"Shows internal files in storage settings.\n"
"\n"
"Note: OTA updates will be broken until this is disabled.", None))
#endif // QT_CONFIG(tooltip)
        self.internalStorageChk.setText(QCoreApplication.translate("Nugget", u"Enable Internal Storage (WARNING: risky for some devices, mainly iPads)", None))
#if QT_CONFIG(tooltip)
        self.collisionSOSChk.setToolTip(QCoreApplication.translate("Nugget", u"Shows collision detection in the SOS page in Settings.", None))
#endif // QT_CONFIG(tooltip)
        self.collisionSOSChk.setText(QCoreApplication.translate("Nugget", u"Enable Collision SOS", None))
#if QT_CONFIG(tooltip)
        self.aodChk.setToolTip(QCoreApplication.translate("Nugget", u"Enable AOD on unsupported devices. May cause burn in, use with caution.", None))
#endif // QT_CONFIG(tooltip)
        self.aodChk.setText(QCoreApplication.translate("Nugget", u"Enable Always On Display", None))
#if QT_CONFIG(tooltip)
        self.aodVibrancyChk.setToolTip(QCoreApplication.translate("Nugget", u"Enable this if something is wonky when using the above toggle.", None))
#endif // QT_CONFIG(tooltip)
        self.aodVibrancyChk.setText(QCoreApplication.translate("Nugget", u"Enable AOD Vibrancy", None))
        self.label_10.setText(QCoreApplication.translate("Nugget", u"Custom Gestalt Keys", None))
        self.addGestaltKeyBtn.setText(QCoreApplication.translate("Nugget", u"  Add Key", None))
        self.label_12.setText(QCoreApplication.translate("Nugget", u"Warning: Using this feature incorrectly can lead to bootloops and data loss. Only use if you know\n"
"what you are doing.", None))
        self.internalOptionsLbl.setText(QCoreApplication.translate("Nugget", u"Feature Flags", None))
#if QT_CONFIG(tooltip)
        self.clockAnimChk.setToolTip(QCoreApplication.translate("Nugget", u"Enables an animation when the lock screen clock changes time or style.", None))
#endif // QT_CONFIG(tooltip)
        self.clockAnimChk.setText(QCoreApplication.translate("Nugget", u"Enable Lockscreen Clock Animation", None))
#if QT_CONFIG(tooltip)
        self.lockscreenChk.setToolTip(QCoreApplication.translate("Nugget", u"Enables a button to duplicate the lock screen page in edit mode.\n"
"Enables quickly switching lock screens by holding down and swiping.", None))
#endif // QT_CONFIG(tooltip)
        self.lockscreenChk.setText(QCoreApplication.translate("Nugget", u"Enable Duplicate Lockscreen Button and Lockscreen Quickswitch", None))
#if QT_CONFIG(tooltip)
        self.photosChk.setToolTip(QCoreApplication.translate("Nugget", u"Revert the photos app to the iOS 17 style.\n"
"\n"
"Does not work on iOS 18.0 RC.", None))
#endif // QT_CONFIG(tooltip)
        self.photosChk.setText(QCoreApplication.translate("Nugget", u"Enable Old Photo UI", None))
#if QT_CONFIG(tooltip)
        self.aiChk.setToolTip(QCoreApplication.translate("Nugget", u"Enable the new Siri UI.\n"
"\n"
"Only works on iOS 18.0 beta 1-2.", None))
#endif // QT_CONFIG(tooltip)
        self.aiChk.setText(QCoreApplication.translate("Nugget", u"Enable Apple Intelligence", None))
        self.eligibilityLbl.setText(QCoreApplication.translate("Nugget", u"Eligibility Tweaks", None))
        self.euEnablerEnabledChk.setText(QCoreApplication.translate("Nugget", u"Enable EU Enabler", None))
        self.label_5.setText(QCoreApplication.translate("Nugget", u"Method Type", None))
        self.methodChoiceDrp.setItemText(0, QCoreApplication.translate("Nugget", u"Method 1", None))
        self.methodChoiceDrp.setItemText(1, QCoreApplication.translate("Nugget", u"Method 2", None))

        self.label_6.setText(QCoreApplication.translate("Nugget", u"Region Code (Should be 2 letters)", None))
        self.regionCodeTxt.setPlaceholderText(QCoreApplication.translate("Nugget", u"Region Code (Default: US)", None))
        self.mgaWarningLbl2.setText(QCoreApplication.translate("Nugget", u"! You will need a MobileGestalt file for this feature. Please select it in the Apply page !", None))
        self.enableAIChk.setText(QCoreApplication.translate("Nugget", u"Enable Apple Intelligence (for Unsupported Devices)", None))
        self.eligFileChk.setText(QCoreApplication.translate("Nugget", u"Enable Eligibility File", None))
        self.languageLbl.setText(QCoreApplication.translate("Nugget", u"Language Code (not needed for English)", None))
        self.languageTxt.setPlaceholderText(QCoreApplication.translate("Nugget", u"Language Code (i.e. en)", None))
        self.aiInfoLabel.setText(QCoreApplication.translate("Nugget", u"In order to download the AI models, you must spoof your device model. However, this may break \n"
"Face ID until you revert back. \n"
"\n"
"WARNING: Do not go to the Apple Intelligence menu in the Settings app after unspoofing.\n"
"\n"
"Entering the menu on your original device model will cause a re-download and may require a full\n"
"restore to fix. Furthermore, if you switch between model groups, like spoofing from the iPhone 16s\n"
"to the iPhone 15 Pro series, a re-download may also occur. \n"
"Please be careful!", None))
        self.label_8.setText(QCoreApplication.translate("Nugget", u"Spoofed Device Model", None))
        self.spoofedModelDrp.setItemText(0, QCoreApplication.translate("Nugget", u"Original", None))
        self.spoofedModelDrp.setItemText(1, QCoreApplication.translate("Nugget", u"iPhone 15 Pro (iPhone16,1)", None))
        self.spoofedModelDrp.setItemText(2, QCoreApplication.translate("Nugget", u"iPhone 15 Pro Max (iPhone16,2)", None))
        self.spoofedModelDrp.setItemText(3, QCoreApplication.translate("Nugget", u"iPhone 16 (iPhone17,3)", None))
        self.spoofedModelDrp.setItemText(4, QCoreApplication.translate("Nugget", u"iPhone 16 Plus (iPhone17,4)", None))
        self.spoofedModelDrp.setItemText(5, QCoreApplication.translate("Nugget", u"iPhone 16 Pro (iPhone17,1)", None))
        self.spoofedModelDrp.setItemText(6, QCoreApplication.translate("Nugget", u"iPhone 16 Pro Max (iPhone17,2)", None))
        self.spoofedModelDrp.setItemText(7, QCoreApplication.translate("Nugget", u"iPad Mini (A17 Pro) (W) (iPad16,1)", None))
        self.spoofedModelDrp.setItemText(8, QCoreApplication.translate("Nugget", u"iPad Mini (A17 Pro) (C) (iPad16,2)", None))
        self.spoofedModelDrp.setItemText(9, QCoreApplication.translate("Nugget", u"iPad Pro (13-inch) (M4) (W) (iPad16,5)", None))
        self.spoofedModelDrp.setItemText(10, QCoreApplication.translate("Nugget", u"iPad Pro (13-inch) (M4) (C) (iPad16,6)", None))
        self.spoofedModelDrp.setItemText(11, QCoreApplication.translate("Nugget", u"iPad Pro (11-inch) (M4) (W) (iPad16,3)", None))
        self.spoofedModelDrp.setItemText(12, QCoreApplication.translate("Nugget", u"iPad Pro (11-inch) (M4) (C) (iPad16,4)", None))
        self.spoofedModelDrp.setItemText(13, QCoreApplication.translate("Nugget", u"iPad Pro (12.9-inch) (M2) (W) (iPad14,5)", None))
        self.spoofedModelDrp.setItemText(14, QCoreApplication.translate("Nugget", u"iPad Pro (12.9-inch) (M2) (C) (iPad14,6)", None))
        self.spoofedModelDrp.setItemText(15, QCoreApplication.translate("Nugget", u"iPad Pro (11-inch) (M2) (W) (iPad14,3)", None))
        self.spoofedModelDrp.setItemText(16, QCoreApplication.translate("Nugget", u"iPad Pro (11-inch) (M2) (C) (iPad14,4)", None))
        self.spoofedModelDrp.setItemText(17, QCoreApplication.translate("Nugget", u"iPad Air (13-inch) (M2) (W) (iPad14,10)", None))
        self.spoofedModelDrp.setItemText(18, QCoreApplication.translate("Nugget", u"iPad Air (13-inch) (M2) (C) (iPad14,11)", None))
        self.spoofedModelDrp.setItemText(19, QCoreApplication.translate("Nugget", u"iPad Air (11-inch) (M2) (W) (iPad14,8)", None))
        self.spoofedModelDrp.setItemText(20, QCoreApplication.translate("Nugget", u"iPad Air (11-inch) (M2) (C) (iPad14,9)", None))
        self.spoofedModelDrp.setItemText(21, QCoreApplication.translate("Nugget", u"iPad Pro (11-inch) (M1) (W) (iPad13,4)", None))
        self.spoofedModelDrp.setItemText(22, QCoreApplication.translate("Nugget", u"iPad Pro (11-inch) (M1) (C) (iPad13,5)", None))
        self.spoofedModelDrp.setItemText(23, QCoreApplication.translate("Nugget", u"iPad Pro (12.9-inch) (M1) (W) (iPad13,8)", None))
        self.spoofedModelDrp.setItemText(24, QCoreApplication.translate("Nugget", u"iPad Pro (12.9-inch) (M1) (C) (iPad13,9)", None))
        self.spoofedModelDrp.setItemText(25, QCoreApplication.translate("Nugget", u"iPad Air (M1) (W) (iPad13,16)", None))
        self.spoofedModelDrp.setItemText(26, QCoreApplication.translate("Nugget", u"iPad Air (M1) (C) (iPad13,17)", None))

        self.spoofedModelDrp.setCurrentText(QCoreApplication.translate("Nugget", u"Original", None))
#if QT_CONFIG(tooltip)
        self.spoofHardwareChk.setToolTip(QCoreApplication.translate("Nugget", u"Spoofs the device hardware model (ie D83AP)", None))
#endif // QT_CONFIG(tooltip)
        self.spoofHardwareChk.setText(QCoreApplication.translate("Nugget", u"Spoof Hardware Model", None))
#if QT_CONFIG(tooltip)
        self.spoofCPUChk.setToolTip(QCoreApplication.translate("Nugget", u"Spoofs the device CPU model (ie t8130)", None))
#endif // QT_CONFIG(tooltip)
        self.spoofCPUChk.setText(QCoreApplication.translate("Nugget", u"Spoof CPU Model", None))
        self.statusBarLbl1.setText(QCoreApplication.translate("Nugget", u"Status Bar", None))
        self.statusBarEnabledChk.setText(QCoreApplication.translate("Nugget", u"Modify", None))
        self.label_91.setText(QCoreApplication.translate("Nugget", u"Primary Cellular", None))
        self.pDefaultRdo.setText(QCoreApplication.translate("Nugget", u"Default", None))
        self.pShowRdo.setText(QCoreApplication.translate("Nugget", u"Force Show", None))
        self.pHideRdo.setText(QCoreApplication.translate("Nugget", u"Force Hide", None))
        self.pCarrierChk.setText(QCoreApplication.translate("Nugget", u"Change Carrier Text", None))
        self.pCarrierTxt.setPlaceholderText(QCoreApplication.translate("Nugget", u"Carrier Text", None))
        self.pBadgeChk.setText(QCoreApplication.translate("Nugget", u"Change Service Badge Text", None))
        self.pBadgeTxt.setPlaceholderText(QCoreApplication.translate("Nugget", u"Service Badge Text", None))
        self.pTypeChk.setText(QCoreApplication.translate("Nugget", u"Change Data Network Type", None))
        self.pTypeDrp.setItemText(0, QCoreApplication.translate("Nugget", u"GPRS", None))
        self.pTypeDrp.setItemText(1, QCoreApplication.translate("Nugget", u"EDGE", None))
        self.pTypeDrp.setItemText(2, QCoreApplication.translate("Nugget", u"3G", None))
        self.pTypeDrp.setItemText(3, QCoreApplication.translate("Nugget", u"4G", None))
        self.pTypeDrp.setItemText(4, QCoreApplication.translate("Nugget", u"LTE", None))
        self.pTypeDrp.setItemText(5, QCoreApplication.translate("Nugget", u"Wi-Fi", None))
        self.pTypeDrp.setItemText(6, QCoreApplication.translate("Nugget", u"Personal Hotspot", None))
        self.pTypeDrp.setItemText(8, QCoreApplication.translate("Nugget", u"5G\u1d07", None))
        self.pTypeDrp.setItemText(9, QCoreApplication.translate("Nugget", u"LTE-A", None))
        self.pTypeDrp.setItemText(10, QCoreApplication.translate("Nugget", u"LTE+", None))
        self.pTypeDrp.setItemText(11, QCoreApplication.translate("Nugget", u"5G", None))
        self.pTypeDrp.setItemText(12, QCoreApplication.translate("Nugget", u"5G+", None))
        self.pTypeDrp.setItemText(13, QCoreApplication.translate("Nugget", u"5GUW", None))
        self.pTypeDrp.setItemText(14, QCoreApplication.translate("Nugget", u"5GUC", None))

        self.pStrengthChk.setText(QCoreApplication.translate("Nugget", u"Change Signal Strength", None))
        self.pStrengthLbl.setText(QCoreApplication.translate("Nugget", u"0 Bars", None))
        self.label_101.setText(QCoreApplication.translate("Nugget", u"Secondary Cellular", None))
        self.sDefaultRdo.setText(QCoreApplication.translate("Nugget", u"Default", None))
        self.sShowRdo.setText(QCoreApplication.translate("Nugget", u"Force Show", None))
        self.sHideRdo.setText(QCoreApplication.translate("Nugget", u"Force Hide", None))
        self.sCarrierChk.setText(QCoreApplication.translate("Nugget", u"Change Carrier Text", None))
        self.sCarrierTxt.setPlaceholderText(QCoreApplication.translate("Nugget", u"Carrier Text", None))
        self.sBadgeChk.setText(QCoreApplication.translate("Nugget", u"Change Service Badge Text", None))
        self.sBadgeTxt.setPlaceholderText(QCoreApplication.translate("Nugget", u"Service Badge Text", None))
        self.sTypeChk.setText(QCoreApplication.translate("Nugget", u"Change Data Network Type", None))
        self.sTypeDrp.setItemText(0, QCoreApplication.translate("Nugget", u"GPRS", None))
        self.sTypeDrp.setItemText(1, QCoreApplication.translate("Nugget", u"EDGE", None))
        self.sTypeDrp.setItemText(2, QCoreApplication.translate("Nugget", u"3G", None))
        self.sTypeDrp.setItemText(3, QCoreApplication.translate("Nugget", u"4G", None))
        self.sTypeDrp.setItemText(4, QCoreApplication.translate("Nugget", u"LTE", None))
        self.sTypeDrp.setItemText(5, QCoreApplication.translate("Nugget", u"Wi-Fi", None))
        self.sTypeDrp.setItemText(6, QCoreApplication.translate("Nugget", u"Personal Hotspot", None))
        self.sTypeDrp.setItemText(7, QCoreApplication.translate("Nugget", u"1x", None))
        self.sTypeDrp.setItemText(8, QCoreApplication.translate("Nugget", u"5G\u1d07", None))
        self.sTypeDrp.setItemText(9, QCoreApplication.translate("Nugget", u"LTE-A", None))
        self.sTypeDrp.setItemText(10, QCoreApplication.translate("Nugget", u"LTE+", None))
        self.sTypeDrp.setItemText(11, QCoreApplication.translate("Nugget", u"5G", None))
        self.sTypeDrp.setItemText(12, QCoreApplication.translate("Nugget", u"5G+", None))
        self.sTypeDrp.setItemText(13, QCoreApplication.translate("Nugget", u"5GUW", None))
        self.sTypeDrp.setItemText(14, QCoreApplication.translate("Nugget", u"5GUC", None))

        self.sStrengthChk.setText(QCoreApplication.translate("Nugget", u"Change Signal Strength", None))
        self.sStrengthLbl.setText(QCoreApplication.translate("Nugget", u"0 Bars", None))
        self.timeChk.setText(QCoreApplication.translate("Nugget", u"Change Status Bar Time Text*", None))
        self.timeTxt.setPlaceholderText(QCoreApplication.translate("Nugget", u"Status Bar Time Text", None))
        self.dateChk.setText(QCoreApplication.translate("Nugget", u"Change Status Bar Date Text", None))
        self.dateTxt.setPlaceholderText(QCoreApplication.translate("Nugget", u"Status Bar Date Text", None))
        self.breadcrumbChk.setText(QCoreApplication.translate("Nugget", u"Change Breadcrumb Text", None))
        self.breadcrumbTxt.setPlaceholderText(QCoreApplication.translate("Nugget", u"Breadcrumb Text", None))
        self.batteryDetailChk.setText(QCoreApplication.translate("Nugget", u"Change Battery Detail Text", None))
        self.batteryDetailTxt.setPlaceholderText(QCoreApplication.translate("Nugget", u"Battery Detail Text", None))
        self.batteryCapacityChk.setText(QCoreApplication.translate("Nugget", u"Change Battery Icon Capacity", None))
        self.batteryCapacityLbl.setText(QCoreApplication.translate("Nugget", u"0%", None))
        self.wifiStrengthChk.setText(QCoreApplication.translate("Nugget", u"Change Wi-Fi Signal Strength", None))
        self.wifiStrengthLbl.setText(QCoreApplication.translate("Nugget", u"0 Bars", None))
        self.numericWifiChk.setText(QCoreApplication.translate("Nugget", u"Show Numeric Wi-Fi Strength", None))
        self.numericCellChk.setText(QCoreApplication.translate("Nugget", u"Show Numeric Cellular Strength", None))
        self.label_51.setText(QCoreApplication.translate("Nugget", u"*When set to blank on notched devices, this will display the carrier name.", None))
        self.label_18.setText(QCoreApplication.translate("Nugget", u"Focus Mode Icon", None))
        self.dndDefaultRdo.setText(QCoreApplication.translate("Nugget", u"Default", None))
        self.dndShowRdo.setText(QCoreApplication.translate("Nugget", u"Always Show", None))
        self.dndHideRdo.setText(QCoreApplication.translate("Nugget", u"Always Hide", None))
        self.label_181.setText(QCoreApplication.translate("Nugget", u"Airplane Mode", None))
        self.airplaneDefaultRdo.setText(QCoreApplication.translate("Nugget", u"Default", None))
        self.airplaneShowRdo.setText(QCoreApplication.translate("Nugget", u"Always Show", None))
        self.airplaneHideRdo.setText(QCoreApplication.translate("Nugget", u"Always Hide", None))
        self.label_182.setText(QCoreApplication.translate("Nugget", u"Wi-Fi Icon", None))
        self.wifiDefaultRdo.setText(QCoreApplication.translate("Nugget", u"Default", None))
        self.wifiShowRdo.setText(QCoreApplication.translate("Nugget", u"Always Show", None))
        self.wifiHideRdo.setText(QCoreApplication.translate("Nugget", u"Always Hide", None))
        self.label_121.setText(QCoreApplication.translate("Nugget", u"^Will also hide cellular data indicator.", None))
        self.label_183.setText(QCoreApplication.translate("Nugget", u"Battery Icon", None))
        self.batteryDefaultRdo.setText(QCoreApplication.translate("Nugget", u"Default", None))
        self.batteryShowRdo.setText(QCoreApplication.translate("Nugget", u"Always Show", None))
        self.batteryHideRdo.setText(QCoreApplication.translate("Nugget", u"Always Hide", None))
        self.label_184.setText(QCoreApplication.translate("Nugget", u"Bluetooth Icon", None))
        self.bluetoothDefaultRdo.setText(QCoreApplication.translate("Nugget", u"Default", None))
        self.bluetoothShowRdo.setText(QCoreApplication.translate("Nugget", u"Always Show", None))
        self.bluetoothHideRdo.setText(QCoreApplication.translate("Nugget", u"Always Hide", None))
        self.label_185.setText(QCoreApplication.translate("Nugget", u"Alarm Icon", None))
        self.alarmDefaultRdo.setText(QCoreApplication.translate("Nugget", u"Default", None))
        self.alarmShowRdo.setText(QCoreApplication.translate("Nugget", u"Always Show", None))
        self.alarmHideRdo.setText(QCoreApplication.translate("Nugget", u"Always Hide", None))
        self.label_186.setText(QCoreApplication.translate("Nugget", u"Location Icon", None))
        self.locationDefaultRdo.setText(QCoreApplication.translate("Nugget", u"Default", None))
        self.locationShowRdo.setText(QCoreApplication.translate("Nugget", u"Always Show", None))
        self.locationHideRdo.setText(QCoreApplication.translate("Nugget", u"Always Hide", None))
        self.label_187.setText(QCoreApplication.translate("Nugget", u"Rotation Lock Icon", None))
        self.rotationDefaultRdo.setText(QCoreApplication.translate("Nugget", u"Default", None))
        self.rotationShowRdo.setText(QCoreApplication.translate("Nugget", u"Always Show", None))
        self.rotationHideRdo.setText(QCoreApplication.translate("Nugget", u"Always Hide", None))
        self.label_188.setText(QCoreApplication.translate("Nugget", u"AirPlay Icon", None))
        self.airplayDefaultRdo.setText(QCoreApplication.translate("Nugget", u"Default", None))
        self.airplayShowRdo.setText(QCoreApplication.translate("Nugget", u"Always Show", None))
        self.airplayHideRdo.setText(QCoreApplication.translate("Nugget", u"Always Hide", None))
        self.label_189.setText(QCoreApplication.translate("Nugget", u"CarPlay Icon", None))
        self.carplayDefaultRdo.setText(QCoreApplication.translate("Nugget", u"Default", None))
        self.carplayShowRdo.setText(QCoreApplication.translate("Nugget", u"Always Show", None))
        self.carplayHideRdo.setText(QCoreApplication.translate("Nugget", u"Always Hide", None))
        self.label_1810.setText(QCoreApplication.translate("Nugget", u"VPN Icon", None))
        self.vpnDefaultRdo.setText(QCoreApplication.translate("Nugget", u"Default", None))
        self.vpnShowRdo.setText(QCoreApplication.translate("Nugget", u"Always Show", None))
        self.vpnHideRdo.setText(QCoreApplication.translate("Nugget", u"Always Hide", None))
        self.label_19.setText(QCoreApplication.translate("Nugget", u"Classroom Icon", None))
        self.studentDefaultRdo.setText(QCoreApplication.translate("Nugget", u"Default", None))
        self.studentShowRdo.setText(QCoreApplication.translate("Nugget", u"Always Show", None))
        self.studentHideRdo.setText(QCoreApplication.translate("Nugget", u"Always Hide", None))
        self.label_20.setText(QCoreApplication.translate("Nugget", u"Liquid Detection Warning Icon", None))
        self.waterDefaultRdo.setText(QCoreApplication.translate("Nugget", u"Default", None))
        self.waterShowRdo.setText(QCoreApplication.translate("Nugget", u"Always Show", None))
        self.waterHideRdo.setText(QCoreApplication.translate("Nugget", u"Always Hide", None))
        self.label_21.setText(QCoreApplication.translate("Nugget", u"Voice Control Icon", None))
        self.vcDefaultRdo.setText(QCoreApplication.translate("Nugget", u"Default", None))
        self.vcShowRdo.setText(QCoreApplication.translate("Nugget", u"Always Show", None))
        self.vcHideRdo.setText(QCoreApplication.translate("Nugget", u"Always Hide", None))
#if QT_CONFIG(tooltip)
        self.sillyModeChk.setToolTip(QCoreApplication.translate("Nugget", u"Force enables everything", None))
#endif // QT_CONFIG(tooltip)
        self.sillyModeChk.setText(QCoreApplication.translate("Nugget", u"Silly Mode", None))
        self.springboardOptionsLbl.setText(QCoreApplication.translate("Nugget", u"Springboard Options", None))
        self.footnoteLbl.setText(QCoreApplication.translate("Nugget", u"Lock Screen Footnote Text", None))
        self.footnoteTxt.setPlaceholderText(QCoreApplication.translate("Nugget", u"Footnote Text", None))
        self.disableLockRespringChk.setText(QCoreApplication.translate("Nugget", u"Disable Lock After Respring", None))
        self.disableDimmingChk.setText(QCoreApplication.translate("Nugget", u"Disable Screen Dimming While Charging", None))
        self.disableBatteryAlertsChk.setText(QCoreApplication.translate("Nugget", u"Disable Low Battery Alerts", None))
#if QT_CONFIG(tooltip)
        self.disableCrumbChk.setToolTip(QCoreApplication.translate("Nugget", u"Removes '< PreviousAppName' glyph in Status Bar when being forwarded to another app.", None))
#endif // QT_CONFIG(tooltip)
        self.disableCrumbChk.setText(QCoreApplication.translate("Nugget", u"Disable Breadcrumbs", None))
#if QT_CONFIG(tooltip)
        self.enableSupervisionTextChk.setToolTip(QCoreApplication.translate("Nugget", u"Shows info about the device supervision status and organization at the bottom of the lock screen.", None))
#endif // QT_CONFIG(tooltip)
        self.enableSupervisionTextChk.setText(QCoreApplication.translate("Nugget", u"Show Supervision Text on Lock Screen", None))
        self.enableAirPlayChk.setText(QCoreApplication.translate("Nugget", u"Enable AirPlay support for Stage Manager", None))
        self.internalOptionsLbl1.setText(QCoreApplication.translate("Nugget", u"Internal Options", None))
        self.buildVersionChk.setText(QCoreApplication.translate("Nugget", u"Show Build Version in Status Bar", None))
        self.RTLChk.setText(QCoreApplication.translate("Nugget", u"Force Right-to-Left Layout", None))
        self.metalHUDChk.setText(QCoreApplication.translate("Nugget", u"Enable Metal HUD Debug", None))
        self.iMessageChk.setText(QCoreApplication.translate("Nugget", u"Enable iMessage Debugging", None))
        self.IDSChk.setText(QCoreApplication.translate("Nugget", u"Enable Continuity Debugging", None))
        self.VCChk.setText(QCoreApplication.translate("Nugget", u"Enable FaceTime Debugging", None))
        self.appStoreChk.setText(QCoreApplication.translate("Nugget", u"Enable App Store Debug Gesture", None))
        self.notesChk.setText(QCoreApplication.translate("Nugget", u"Enable Notes Debug Mode", None))
        self.showTouchesChk.setText(QCoreApplication.translate("Nugget", u"Show Touches With Debug Info", None))
        self.hideRespringChk.setText(QCoreApplication.translate("Nugget", u"Hide Respring Icon", None))
        self.enableWakeVibrateChk.setText(QCoreApplication.translate("Nugget", u"Vibrate on Raise-to-Wake", None))
        self.pasteSoundChk.setText(QCoreApplication.translate("Nugget", u"Play Sound on Paste", None))
        self.notifyPastesChk.setText(QCoreApplication.translate("Nugget", u"Show Notifications for System Pastes", None))
        self.daemonsLbl.setText(QCoreApplication.translate("Nugget", u"Daemons", None))
        self.modifyDaemonsChk.setText(QCoreApplication.translate("Nugget", u"Modify", None))
        self.regularDomainsLbl.setText(QCoreApplication.translate("Nugget", u"Note: Even on Sparserestore versions, this uses regular domains. Skip Setup will be applied if you have\n"
"it enabled.", None))
#if QT_CONFIG(tooltip)
        self.otadChk.setToolTip(QCoreApplication.translate("Nugget", u"Stops over-the-air updates to prevent auto-downloads.", None))
#endif // QT_CONFIG(tooltip)
        self.otadChk.setText(QCoreApplication.translate("Nugget", u"Disable OTA", None))
#if QT_CONFIG(tooltip)
        self.usageTrackingAgentChk.setToolTip(QCoreApplication.translate("Nugget", u"Disables usage tracking for improved privacy.", None))
#endif // QT_CONFIG(tooltip)
        self.usageTrackingAgentChk.setText(QCoreApplication.translate("Nugget", u"Disable UsageTrackingAgent", None))
#if QT_CONFIG(tooltip)
        self.screenTimeChk.setToolTip(QCoreApplication.translate("Nugget", u"Disables Screen Time monitoring features.", None))
#endif // QT_CONFIG(tooltip)
        self.screenTimeChk.setText(QCoreApplication.translate("Nugget", u"Disable Screen Time Agent", None))
#if QT_CONFIG(tooltip)
        self.clearScreenTimeAgentChk.setToolTip(QCoreApplication.translate("Nugget", u"Deletes the Screen Time Agent preferences file to prevent app lockout set via iCloud.\n"
"\n"
"To work properly, also disable the daemon using the toggle above.", None))
#endif // QT_CONFIG(tooltip)
        self.clearScreenTimeAgentChk.setText(QCoreApplication.translate("Nugget", u"Clear ScreenTimeAgent.plist file", None))
#if QT_CONFIG(tooltip)
        self.crashReportsChk.setToolTip(QCoreApplication.translate("Nugget", u"Stops logs, dumps, and crash reports collection.", None))
#endif // QT_CONFIG(tooltip)
        self.crashReportsChk.setText(QCoreApplication.translate("Nugget", u"Disable Logs, Dumps, and Crash Reports", None))
#if QT_CONFIG(tooltip)
        self.atwakeupChk.setToolTip(QCoreApplication.translate("Nugget", u"Disables pinging to sleeping bluetooth devices for improved battery life.", None))
#endif // QT_CONFIG(tooltip)
        self.atwakeupChk.setText(QCoreApplication.translate("Nugget", u"Disable ATWAKEUP", None))
#if QT_CONFIG(tooltip)
        self.gameCenterChk.setToolTip(QCoreApplication.translate("Nugget", u"Turns off Game Center background services.", None))
#endif // QT_CONFIG(tooltip)
        self.gameCenterChk.setText(QCoreApplication.translate("Nugget", u"Disable Game Center", None))
#if QT_CONFIG(tooltip)
        self.tipsChk.setToolTip(QCoreApplication.translate("Nugget", u"Disables the Tips service and notifications.", None))
#endif // QT_CONFIG(tooltip)
        self.tipsChk.setText(QCoreApplication.translate("Nugget", u"Disable Tips Services", None))
#if QT_CONFIG(tooltip)
        self.vpndChk.setToolTip(QCoreApplication.translate("Nugget", u"Disables the Virtual Private Network service.", None))
#endif // QT_CONFIG(tooltip)
        self.vpndChk.setText(QCoreApplication.translate("Nugget", u"Disable VPN Service", None))
#if QT_CONFIG(tooltip)
        self.wapicChk.setToolTip(QCoreApplication.translate("Nugget", u"Disables the service that deals with errors with WiFi networks with Chinese characters in the name.", None))
#endif // QT_CONFIG(tooltip)
        self.wapicChk.setText(QCoreApplication.translate("Nugget", u"Disable Chinese WLAN Service", None))
#if QT_CONFIG(tooltip)
        self.healthdChk.setToolTip(QCoreApplication.translate("Nugget", u"Disables HealthKit services used by the health app.", None))
#endif // QT_CONFIG(tooltip)
        self.healthdChk.setText(QCoreApplication.translate("Nugget", u"Disable HealthKit", None))
        self.airprintChk.setText(QCoreApplication.translate("Nugget", u"Disable AirPrint", None))
        self.assistiveTouchChk.setText(QCoreApplication.translate("Nugget", u"Disable Assistive Touch", None))
        self.icloudChk.setText(QCoreApplication.translate("Nugget", u"Disable iCloud", None))
        self.hotspotChk.setText(QCoreApplication.translate("Nugget", u"Disable Internet Tethering (Hotspot)", None))
        self.passbookChk.setText(QCoreApplication.translate("Nugget", u"Disable Passbook", None))
        self.spotlightChk.setText(QCoreApplication.translate("Nugget", u"Disable Spotlight", None))
        self.voiceControlChk.setText(QCoreApplication.translate("Nugget", u"Disable Voice Control", None))
        self.posterboardLbl.setText(QCoreApplication.translate("Nugget", u"Posterboard", None))
        self.findPBBtn.setText(QCoreApplication.translate("Nugget", u"   Discover Wallpapers", None))
        self.pbHelpBtn.setText(QCoreApplication.translate("Nugget", u"...", None))
        self.tendiesPageBtn.setText(QCoreApplication.translate("Nugget", u"  Tendies", None))
        self.templatePageBtn.setText(QCoreApplication.translate("Nugget", u"   Templates", None))
        self.videoPageBtn.setText(QCoreApplication.translate("Nugget", u"   Video", None))
        self.label.setText(QCoreApplication.translate("Nugget", u"Clear Action:", None))
#if QT_CONFIG(tooltip)
        self.importTendiesBtn.setToolTip(QCoreApplication.translate("Nugget", u"Select a wallpaper file with the .tendies extension.", None))
#endif // QT_CONFIG(tooltip)
        self.importTendiesBtn.setText(QCoreApplication.translate("Nugget", u"  Import Files (.tendies)", None))
#if QT_CONFIG(tooltip)
        self.importTemplateBtn.setToolTip(QCoreApplication.translate("Nugget", u"Select a wallpaper file with the .tendies extension.", None))
#endif // QT_CONFIG(tooltip)
        self.importTemplateBtn.setText(QCoreApplication.translate("Nugget", u"  Import Templates (.batter)", None))
#if QT_CONFIG(tooltip)
        self.caVideoChk.setToolTip(QCoreApplication.translate("Nugget", u"Uses the CoreAnimation file to play the video (300 fps limit)\n"
"Will show up in Collections", None))
#endif // QT_CONFIG(tooltip)
        self.caVideoChk.setText(QCoreApplication.translate("Nugget", u"Loop (use CoreAnimation method)", None))
        self.reverseLoopChk.setText(QCoreApplication.translate("Nugget", u"Reverse on Loop", None))
        self.useForegroundChk.setText(QCoreApplication.translate("Nugget", u"Make Foreground (hides clock)", None))
#if QT_CONFIG(tooltip)
        self.chooseThumbBtn.setToolTip(QCoreApplication.translate("Nugget", u"Choose a photo for the wallpaper to freeze on when finished (.heic files only)", None))
#endif // QT_CONFIG(tooltip)
        self.chooseThumbBtn.setText(QCoreApplication.translate("Nugget", u"Choose Freeze Frame (.HEIC)", None))
#if QT_CONFIG(tooltip)
        self.chooseVideoBtn.setToolTip(QCoreApplication.translate("Nugget", u"Choose a video file for the wallpaper (.mov or .mp4)", None))
#endif // QT_CONFIG(tooltip)
        self.chooseVideoBtn.setText(QCoreApplication.translate("Nugget", u"Choose Video", None))
        self.advancedOptionsBtn.setText(QCoreApplication.translate("Nugget", u"   Advanced Options", None))
        self.exportPBVideoBtn.setText(QCoreApplication.translate("Nugget", u"   Export Video as Descriptor", None))
        self.templatesLbl.setText(QCoreApplication.translate("Nugget", u"Templates", None))
#if QT_CONFIG(tooltip)
        self.importTemplatesBtn.setToolTip(QCoreApplication.translate("Nugget", u"Select a wallpaper file with the .tendies extension.", None))
#endif // QT_CONFIG(tooltip)
        self.importTemplatesBtn.setText(QCoreApplication.translate("Nugget", u"  Import Templates (.batter)", None))
        self.advancedOptionsLbl.setText(QCoreApplication.translate("Nugget", u"Risky Options", None))
        self.label_17.setText(QCoreApplication.translate("Nugget", u"Disclaimer:\n"
"\n"
"The options on this page may be unsafe for your device. Use these options at your own risk. Changing\n"
"your device resolution has the potential to brick your device when used improperly.\n"
"\n"
"Nugget is not responsible if you mess up your device, especially with resolution changer.", None))
#if QT_CONFIG(tooltip)
        self.disableOTAChk.setToolTip(QCoreApplication.translate("Nugget", u"Uses the file method. Recommended to disable the daemon instead in the Daemons tab.", None))
#endif // QT_CONFIG(tooltip)
        self.disableOTAChk.setText(QCoreApplication.translate("Nugget", u"Disable OTA Updates (file)", None))
#if QT_CONFIG(tooltip)
        self.thermalmonitordChk.setToolTip(QCoreApplication.translate("Nugget", u"Disables temperature monitoring daemon to reduce system checks.\n"
"\n"
"Warning: Disabling will cause the battery to show \"Unknown Part\" or \"Unverified\" in Settings.", None))
#endif // QT_CONFIG(tooltip)
        self.thermalmonitordChk.setText(QCoreApplication.translate("Nugget", u"Disable thermalmonitord", None))
#if QT_CONFIG(tooltip)
        self.enableResolutionChk.setToolTip(QCoreApplication.translate("Nugget", u"Set a custom device screen resolution.", None))
#endif // QT_CONFIG(tooltip)
        self.enableResolutionChk.setText(QCoreApplication.translate("Nugget", u"Set a Custom Device Resolution", None))
        self.resHeightLbl.setText(QCoreApplication.translate("Nugget", u"Height:", None))
        self.resHeightTxt.setPlaceholderText(QCoreApplication.translate("Nugget", u"Resolution Height", None))
        self.resWidthLbl.setText(QCoreApplication.translate("Nugget", u"Width:", None))
        self.resWidthTxt.setPlaceholderText(QCoreApplication.translate("Nugget", u"Resolution Width", None))
        self.statusBarLbl_5.setText(QCoreApplication.translate("Nugget", u"Miscellaneous Options", None))
        self.label_16.setText("")
        self.springboardOptionsPageBtn.setText(QCoreApplication.translate("Nugget", u"Springboard", None))
        self.internalOptionsPageBtn.setText(QCoreApplication.translate("Nugget", u"Internal", None))
        self.daemonsPageBtn.setText(QCoreApplication.translate("Nugget", u"Daemons", None))
        self.advancedPageBtn.setText(QCoreApplication.translate("Nugget", u"Risky", None))
        self.statusBarLbl_51.setText(QCoreApplication.translate("Nugget", u"Apply", None))
        self.label_161.setText("")
        self.gestaltLocationTitleLbl.setText(QCoreApplication.translate("Nugget", u"Current gestalt file location:", None))
        self.chooseGestaltBtn.setText(QCoreApplication.translate("Nugget", u"  Choose Gestalt File", None))
        self.applyTweaksBtn.setText(QCoreApplication.translate("Nugget", u"  Apply Changes", None))
        self.statusLbl.setText(QCoreApplication.translate("Nugget", u"Ready!", None))
        self.skipSetupOnLbl.setText(QCoreApplication.translate("Nugget", u"Note: Skip Setup is currently turned on.", None))
        self.removeTweaksBtn.setText(QCoreApplication.translate("Nugget", u"Remove All Tweaks", None))
        self.resetGestaltBtn.setText(QCoreApplication.translate("Nugget", u"Reset Mobile Gestalt", None))
        self.springboardOptionsLbl1.setText(QCoreApplication.translate("Nugget", u"Nugget Settings", None))
        self.langLbl.setText(QCoreApplication.translate("Nugget", u"App Language", None))
        self.allowWifiApplyingChk.setText(QCoreApplication.translate("Nugget", u"Allow Applying Over WiFi", None))
        self.autoRebootChk.setText(QCoreApplication.translate("Nugget", u"Auto Reboot After Applying", None))
        self.showRiskyChk.setText(QCoreApplication.translate("Nugget", u"Show Risky Tweak Options", None))
#if QT_CONFIG(tooltip)
        self.showAllSpoofableChk.setToolTip(QCoreApplication.translate("Nugget", u"Show models for other device types in the AI device spoofing tab.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.showAllSpoofableChk.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.showAllSpoofableChk.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.showAllSpoofableChk.setText(QCoreApplication.translate("Nugget", u"Show All Spoofable Models", None))
        self.ignorePBFrameLimitChk.setText(QCoreApplication.translate("Nugget", u"Ignore Posterboard Frame Limit", None))
#if QT_CONFIG(tooltip)
        self.disableTendiesLimitChk.setToolTip(QCoreApplication.translate("Nugget", u"Disables the tendies file limit of 2. There is still the descriptor limit.\n"
"\n"
"DO NOT unplug your device during restores.", None))
#endif // QT_CONFIG(tooltip)
        self.disableTendiesLimitChk.setText(QCoreApplication.translate("Nugget", u"Disable Tendies Limit", None))
#if QT_CONFIG(tooltip)
        self.line_24.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.revertRdarChk.setToolTip(QCoreApplication.translate("Nugget", u"If you used the rdar/status bar fix in a previous iOS version, this will revert that.", None))
#endif // QT_CONFIG(tooltip)
        self.revertRdarChk.setText(QCoreApplication.translate("Nugget", u"Revert rdar Fix (reset resolution)", None))
#if QT_CONFIG(tooltip)
        self.trustStoreChk.setToolTip(QCoreApplication.translate("Nugget", u"Restores the SSL config that does something idk", None))
#endif // QT_CONFIG(tooltip)
        self.trustStoreChk.setText(QCoreApplication.translate("Nugget", u"Restore TrustStore (SSL Configuration Profiles)", None))
        self.skipSetupChk.setText(QCoreApplication.translate("Nugget", u"Skip Setup * (non-exploit files only)", None))
        self.supervisionChk.setText(QCoreApplication.translate("Nugget", u"Enable Supervision * (requires Skip Setup)", None))
        self.supervisionOrganization.setPlaceholderText(QCoreApplication.translate("Nugget", u"Enter Organization Name", None))
        self.label_15.setText(QCoreApplication.translate("Nugget", u"* Note: Skip Setup may cause issues with configuration profiles. Turn it off if you need that.", None))
        self.resetPairBtn.setText(QCoreApplication.translate("Nugget", u"Reset Device Pairing", None))
        self.pocketPosterHelperBtn.setText(QCoreApplication.translate("Nugget", u"Pocket Poster Helper", None))
        pass
    # retranslateUi

