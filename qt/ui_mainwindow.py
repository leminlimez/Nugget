# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QToolButton, QVBoxLayout,
    QWidget)
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
        icon.addFile(u":/icon/phone.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        icon1.addFile(u":/icon/arrow-clockwise.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        icon2.addFile(u":/icon/house.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.homePageBtn.setIcon(icon2)
        self.homePageBtn.setCheckable(True)
        self.homePageBtn.setChecked(True)
        self.homePageBtn.setAutoExclusive(True)
        self.homePageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

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

        self.verticalLayout.addWidget(self.gestaltPageBtn)

        self.featureFlagsPageBtn = QToolButton(self.sidebar)
        self.featureFlagsPageBtn.setObjectName(u"featureFlagsPageBtn")
        sizePolicy2.setHeightForWidth(self.featureFlagsPageBtn.sizePolicy().hasHeightForWidth())
        self.featureFlagsPageBtn.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setFamilies([u".AppleSystemUIFont"])
        self.featureFlagsPageBtn.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u":/icon/flag.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.featureFlagsPageBtn.setIcon(icon5)
        self.featureFlagsPageBtn.setCheckable(True)
        self.featureFlagsPageBtn.setAutoExclusive(True)
        self.featureFlagsPageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

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

        self.verticalLayout.addWidget(self.euEnablerPageBtn)

        self.springboardOptionsPageBtn = QToolButton(self.sidebar)
        self.springboardOptionsPageBtn.setObjectName(u"springboardOptionsPageBtn")
        sizePolicy2.setHeightForWidth(self.springboardOptionsPageBtn.sizePolicy().hasHeightForWidth())
        self.springboardOptionsPageBtn.setSizePolicy(sizePolicy2)
        icon7 = QIcon()
        icon7.addFile(u":/icon/app-indicator.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.springboardOptionsPageBtn.setIcon(icon7)
        self.springboardOptionsPageBtn.setCheckable(True)
        self.springboardOptionsPageBtn.setAutoExclusive(True)
        self.springboardOptionsPageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.springboardOptionsPageBtn)

        self.internalOptionsPageBtn = QToolButton(self.sidebar)
        self.internalOptionsPageBtn.setObjectName(u"internalOptionsPageBtn")
        sizePolicy2.setHeightForWidth(self.internalOptionsPageBtn.sizePolicy().hasHeightForWidth())
        self.internalOptionsPageBtn.setSizePolicy(sizePolicy2)
        icon8 = QIcon()
        icon8.addFile(u":/icon/hdd.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.internalOptionsPageBtn.setIcon(icon8)
        self.internalOptionsPageBtn.setCheckable(True)
        self.internalOptionsPageBtn.setAutoExclusive(True)
        self.internalOptionsPageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.internalOptionsPageBtn)

        self.daemonsPageBtn = QToolButton(self.sidebar)
        self.daemonsPageBtn.setObjectName(u"daemonsPageBtn")
        self.daemonsPageBtn.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.daemonsPageBtn.sizePolicy().hasHeightForWidth())
        self.daemonsPageBtn.setSizePolicy(sizePolicy2)
        icon9 = QIcon()
        icon9.addFile(u":/icon/toggles.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.daemonsPageBtn.setIcon(icon9)
        self.daemonsPageBtn.setCheckable(True)
        self.daemonsPageBtn.setAutoExclusive(True)
        self.daemonsPageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.daemonsPageBtn)

        self.templatesPageBtn = QToolButton(self.sidebar)
        self.templatesPageBtn.setObjectName(u"templatesPageBtn")
        self.templatesPageBtn.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.templatesPageBtn.sizePolicy().hasHeightForWidth())
        self.templatesPageBtn.setSizePolicy(sizePolicy2)
        icon10 = QIcon()
        icon10.addFile(u":/icon/pencil.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.templatesPageBtn.setIcon(icon10)
        self.templatesPageBtn.setCheckable(True)
        self.templatesPageBtn.setAutoExclusive(True)
        self.templatesPageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.templatesPageBtn)

        self.advancedPageBtn = QToolButton(self.sidebar)
        self.advancedPageBtn.setObjectName(u"advancedPageBtn")
        sizePolicy2.setHeightForWidth(self.advancedPageBtn.sizePolicy().hasHeightForWidth())
        self.advancedPageBtn.setSizePolicy(sizePolicy2)
        icon11 = QIcon()
        icon11.addFile(u":/icon/star.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.advancedPageBtn.setIcon(icon11)
        self.advancedPageBtn.setCheckable(True)
        self.advancedPageBtn.setAutoExclusive(True)
        self.advancedPageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.advancedPageBtn)

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
        icon12 = QIcon()
        icon12.addFile(u":/icon/check-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.applyPageBtn.setIcon(icon12)
        self.applyPageBtn.setCheckable(True)
        self.applyPageBtn.setAutoExclusive(True)
        self.applyPageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.applyPageBtn)

        self.settingsPageBtn = QToolButton(self.sidebar)
        self.settingsPageBtn.setObjectName(u"settingsPageBtn")
        sizePolicy2.setHeightForWidth(self.settingsPageBtn.sizePolicy().hasHeightForWidth())
        self.settingsPageBtn.setSizePolicy(sizePolicy2)
        icon13 = QIcon()
        icon13.addFile(u":/icon/gear.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsPageBtn.setIcon(icon13)
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
        self.homePage.setFont(font)
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
        self.phoneVersionLbl.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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
        icon14 = QIcon()
        icon14.addFile(u":/credits/big_nugget.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bigNuggetBtn.setIcon(icon14)
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

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, -1, 0, 0)
        self.discordBtn = QToolButton(self.verticalWidget1)
        self.discordBtn.setObjectName(u"discordBtn")
        icon15 = QIcon()
        icon15.addFile(u":/icon/discord.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.discordBtn.setIcon(icon15)
        self.discordBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_8.addWidget(self.discordBtn)

        self.starOnGithubBtn = QToolButton(self.verticalWidget1)
        self.starOnGithubBtn.setObjectName(u"starOnGithubBtn")
        self.starOnGithubBtn.setIcon(icon11)
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
        icon16 = QIcon()
        icon16.addFile(u":/credits/LeminLimez.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.leminBtn.setIcon(icon16)
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
        icon17 = QIcon()
        icon17.addFile(u":/icon/twitter.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.leminTwitterBtn.setIcon(icon17)

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
        icon18 = QIcon()
        icon18.addFile(u":/icon/github.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.leminGithubBtn.setIcon(icon18)

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
        icon19 = QIcon()
        icon19.addFile(u":/icon/currency-dollar.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.leminKoFiBtn.setIcon(icon19)

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
        self.line_8.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_4.addWidget(self.line_8)

        self.mgaWarningLbl = QLabel(self.gestaltPage)
        self.mgaWarningLbl.setObjectName(u"mgaWarningLbl")
        self.mgaWarningLbl.setFont(font2)

        self.verticalLayout_4.addWidget(self.mgaWarningLbl)

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
        self.gestaltPageContent.setEnabled(True)
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

        self.rdarFixChk = QCheckBox(self.gestaltPageContent)
        self.rdarFixChk.setObjectName(u"rdarFixChk")

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
        icon20 = QIcon()
        icon20.addFile(u":/icon/plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addGestaltKeyBtn.setIcon(icon20)
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

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)

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
        self.eligibilityLbl.setFont(font1)

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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 660, 573))
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
        self.mgaWarningLbl2.setFont(font2)

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
        self.toolButton_7.setIcon(icon7)

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
        self.label_13 = QLabel(self.springboardOptionsPageContent)
        self.label_13.setObjectName(u"label_13")

        self._2.addWidget(self.label_13)

        self.footnoteTxt = QLineEdit(self.springboardOptionsPageContent)
        self.footnoteTxt.setObjectName(u"footnoteTxt")

        self._2.addWidget(self.footnoteTxt)

        self.line_6 = QFrame(self.springboardOptionsPageContent)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_6.setFrameShadow(QFrame.Plain)
        self.line_6.setFrameShape(QFrame.Shape.HLine)

        self._2.addWidget(self.line_6)

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
        self.toolButton_101.setIcon(icon8)

        self.horizontalLayout_201.addWidget(self.toolButton_101)

        self.verticalWidget_41 = QWidget(self.horizontalWidget_51)
        self.verticalWidget_41.setObjectName(u"verticalWidget_41")
        self.verticalLayout_121 = QVBoxLayout(self.verticalWidget_41)
        self.verticalLayout_121.setSpacing(6)
        self.verticalLayout_121.setObjectName(u"verticalLayout_121")
        self.verticalLayout_121.setContentsMargins(0, 0, 0, 0)
        self.internalOptionsLbl1 = QLabel(self.verticalWidget_41)
        self.internalOptionsLbl1.setObjectName(u"internalOptionsLbl1")
        self.internalOptionsLbl1.setFont(font1)

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
        self.toolButton_102.setIcon(icon9)

        self.horizontalLayout_202.addWidget(self.toolButton_102)

        self.verticalWidget_42 = QWidget(self.horizontalWidget_52)
        self.verticalWidget_42.setObjectName(u"verticalWidget_42")
        self.verticalLayout_122 = QVBoxLayout(self.verticalWidget_42)
        self.verticalLayout_122.setSpacing(6)
        self.verticalLayout_122.setObjectName(u"verticalLayout_122")
        self.verticalLayout_122.setContentsMargins(0, 0, 0, 0)
        self.daemonsLbl = QLabel(self.verticalWidget_42)
        self.daemonsLbl.setObjectName(u"daemonsLbl")
        self.daemonsLbl.setFont(font1)

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
        self.horizontalWidget_53 = QWidget(self.posterboardPage)
        self.horizontalWidget_53.setObjectName(u"horizontalWidget_53")
        self.horizontalLayout_203 = QHBoxLayout(self.horizontalWidget_53)
        self.horizontalLayout_203.setSpacing(10)
        self.horizontalLayout_203.setObjectName(u"horizontalLayout_203")
        self.horizontalLayout_203.setContentsMargins(0, 9, 0, 0)
        self.toolButton_103 = QToolButton(self.horizontalWidget_53)
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

        self.verticalWidget_43 = QWidget(self.horizontalWidget_53)
        self.verticalWidget_43.setObjectName(u"verticalWidget_43")
        self.verticalLayout_123 = QVBoxLayout(self.verticalWidget_43)
        self.verticalLayout_123.setSpacing(6)
        self.verticalLayout_123.setObjectName(u"verticalLayout_123")
        self.verticalLayout_123.setContentsMargins(0, 0, 0, 0)
        self.posterboardLbl = QLabel(self.verticalWidget_43)
        self.posterboardLbl.setObjectName(u"posterboardLbl")
        self.posterboardLbl.setFont(font1)

        self.verticalLayout_123.addWidget(self.posterboardLbl)

        self.verticalSpacer_23 = QSpacerItem(20, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_123.addItem(self.verticalSpacer_23)


        self.horizontalLayout_203.addWidget(self.verticalWidget_43)

        self.horizontalSpacer_73 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_203.addItem(self.horizontalSpacer_73)

        self.findPBBtn = QToolButton(self.horizontalWidget_53)
        self.findPBBtn.setObjectName(u"findPBBtn")
        icon21 = QIcon()
        icon21.addFile(u":/icon/globe.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.findPBBtn.setIcon(icon21)
        self.findPBBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_203.addWidget(self.findPBBtn)

        self.pbHelpBtn = QToolButton(self.horizontalWidget_53)
        self.pbHelpBtn.setObjectName(u"pbHelpBtn")
        self.pbHelpBtn.setMinimumSize(QSize(35, 35))
        self.pbHelpBtn.setMaximumSize(QSize(35, 35))
        icon22 = QIcon()
        icon22.addFile(u":/icon/questionmark.circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pbHelpBtn.setIcon(icon22)
        self.pbHelpBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_203.addWidget(self.pbHelpBtn)


        self.verticalLayout_143.addWidget(self.horizontalWidget_53)

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
        icon23 = QIcon()
        icon23.addFile(u":/icon/file-earmark-zip.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tendiesPageBtn.setIcon(icon23)
        self.tendiesPageBtn.setCheckable(True)
        self.tendiesPageBtn.setChecked(True)
        self.tendiesPageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_14.addWidget(self.tendiesPageBtn)

        self.templatePageBtn = QToolButton(self.pbPagePicker)
        self.templatePageBtn.setObjectName(u"templatePageBtn")
        self.templatePageBtn.setIcon(icon10)
        self.templatePageBtn.setCheckable(True)
        self.templatePageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_14.addWidget(self.templatePageBtn)

        self.videoPageBtn = QToolButton(self.pbPagePicker)
        self.videoPageBtn.setObjectName(u"videoPageBtn")
        self.videoPageBtn.setMinimumSize(QSize(0, 25))
        icon24 = QIcon()
        icon24.addFile(u":/icon/photo.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.videoPageBtn.setIcon(icon24)
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
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, -1, -1, 3)
        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_18)

        self.importTendiesBtn = QToolButton(self.pbTendiesPage)
        self.importTendiesBtn.setObjectName(u"importTendiesBtn")
        self.importTendiesBtn.setLayoutDirection(Qt.RightToLeft)
        icon25 = QIcon()
        icon25.addFile(u":/icon/import.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.importTendiesBtn.setIcon(icon25)
        self.importTendiesBtn.setIconSize(QSize(20, 20))
        self.importTendiesBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_12.addWidget(self.importTendiesBtn)


        self.verticalLayout_38.addLayout(self.horizontalLayout_12)

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
        self.horizontalLayout_121 = QHBoxLayout()
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.horizontalLayout_121.setContentsMargins(-1, -1, -1, 3)
        self.horizontalSpacer_181 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_121.addItem(self.horizontalSpacer_181)

        self.importTemplateBtn = QToolButton(self.pbTemplatesPage)
        self.importTemplateBtn.setObjectName(u"importTemplateBtn")
        self.importTemplateBtn.setLayoutDirection(Qt.RightToLeft)
        self.importTemplateBtn.setIcon(icon25)
        self.importTemplateBtn.setIconSize(QSize(20, 20))
        self.importTemplateBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_121.addWidget(self.importTemplateBtn)


        self.verticalLayout_381.addLayout(self.horizontalLayout_121)

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

        self.exportPBVideoBtn = QToolButton(self.pbVideoPage)
        self.exportPBVideoBtn.setObjectName(u"exportPBVideoBtn")
        icon26 = QIcon()
        icon26.addFile(u":/icon/export.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.exportPBVideoBtn.setIcon(icon26)
        self.exportPBVideoBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_30.addWidget(self.exportPBVideoBtn)


        self.verticalLayout_39.addLayout(self.horizontalLayout_30)

        self.pbVideoThumbLbl = QLabel(self.pbVideoPage)
        self.pbVideoThumbLbl.setObjectName(u"pbVideoThumbLbl")

        self.verticalLayout_39.addWidget(self.pbVideoThumbLbl)

        self.pbVideoLbl = QLabel(self.pbVideoPage)
        self.pbVideoLbl.setObjectName(u"pbVideoLbl")

        self.verticalLayout_39.addWidget(self.pbVideoLbl)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_39.addItem(self.verticalSpacer_22)

        self.pbPages.addWidget(self.pbVideoPage)

        self.verticalLayout_143.addWidget(self.pbPages)

        self.pages.addWidget(self.posterboardPage)
        self.templatesPage = QWidget()
        self.templatesPage.setObjectName(u"templatesPage")
        self.verticalLayout_144 = QVBoxLayout(self.templatesPage)
        self.verticalLayout_144.setObjectName(u"verticalLayout_144")
        self.verticalLayout_144.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_54 = QWidget(self.templatesPage)
        self.horizontalWidget_54.setObjectName(u"horizontalWidget_54")
        self.horizontalLayout_204 = QHBoxLayout(self.horizontalWidget_54)
        self.horizontalLayout_204.setSpacing(10)
        self.horizontalLayout_204.setObjectName(u"horizontalLayout_204")
        self.horizontalLayout_204.setContentsMargins(0, 9, 0, 0)
        self.toolButton_104 = QToolButton(self.horizontalWidget_54)
        self.toolButton_104.setObjectName(u"toolButton_104")
        self.toolButton_104.setEnabled(True)
        self.toolButton_104.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_104.setIcon(icon10)

        self.horizontalLayout_204.addWidget(self.toolButton_104)

        self.verticalWidget_44 = QWidget(self.horizontalWidget_54)
        self.verticalWidget_44.setObjectName(u"verticalWidget_44")
        self.verticalLayout_124 = QVBoxLayout(self.verticalWidget_44)
        self.verticalLayout_124.setSpacing(6)
        self.verticalLayout_124.setObjectName(u"verticalLayout_124")
        self.verticalLayout_124.setContentsMargins(0, 0, 0, 0)
        self.templatesLbl = QLabel(self.verticalWidget_44)
        self.templatesLbl.setObjectName(u"templatesLbl")
        self.templatesLbl.setFont(font1)

        self.verticalLayout_124.addWidget(self.templatesLbl)

        self.verticalSpacer_24 = QSpacerItem(20, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_124.addItem(self.verticalSpacer_24)


        self.horizontalLayout_204.addWidget(self.verticalWidget_44)

        self.horizontalSpacer_74 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_204.addItem(self.horizontalSpacer_74)


        self.verticalLayout_144.addWidget(self.horizontalWidget_54)

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
        self.horizontalLayout_122 = QHBoxLayout()
        self.horizontalLayout_122.setObjectName(u"horizontalLayout_122")
        self.horizontalLayout_122.setContentsMargins(-1, -1, -1, 3)
        self.horizontalSpacer_182 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_122.addItem(self.horizontalSpacer_182)

        self.importTemplatesBtn = QToolButton(self.templatesPage)
        self.importTemplatesBtn.setObjectName(u"importTemplatesBtn")
        self.importTemplatesBtn.setLayoutDirection(Qt.RightToLeft)
        self.importTemplatesBtn.setIcon(icon25)
        self.importTemplatesBtn.setIconSize(QSize(20, 20))
        self.importTemplatesBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_122.addWidget(self.importTemplatesBtn)


        self.verticalLayout_382.addLayout(self.horizontalLayout_122)

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
        self.horizontalWidget_55 = QWidget(self.advancedOptionsPage)
        self.horizontalWidget_55.setObjectName(u"horizontalWidget_55")
        self.horizontalLayout_205 = QHBoxLayout(self.horizontalWidget_55)
        self.horizontalLayout_205.setSpacing(10)
        self.horizontalLayout_205.setObjectName(u"horizontalLayout_205")
        self.horizontalLayout_205.setContentsMargins(0, 9, 0, 9)
        self.toolButton_105 = QToolButton(self.horizontalWidget_55)
        self.toolButton_105.setObjectName(u"toolButton_105")
        self.toolButton_105.setEnabled(False)
        self.toolButton_105.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_105.setIcon(icon11)

        self.horizontalLayout_205.addWidget(self.toolButton_105)

        self.verticalWidget_45 = QWidget(self.horizontalWidget_55)
        self.verticalWidget_45.setObjectName(u"verticalWidget_45")
        self.verticalLayout_125 = QVBoxLayout(self.verticalWidget_45)
        self.verticalLayout_125.setSpacing(6)
        self.verticalLayout_125.setObjectName(u"verticalLayout_125")
        self.verticalLayout_125.setContentsMargins(0, 0, 0, 0)
        self.advancedOptionsLbl = QLabel(self.verticalWidget_45)
        self.advancedOptionsLbl.setObjectName(u"advancedOptionsLbl")
        self.advancedOptionsLbl.setFont(font1)

        self.verticalLayout_125.addWidget(self.advancedOptionsLbl)

        self.verticalSpacer_181 = QSpacerItem(20, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_125.addItem(self.verticalSpacer_181)


        self.horizontalLayout_205.addWidget(self.verticalWidget_45)

        self.horizontalSpacer_75 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_205.addItem(self.horizontalSpacer_75)


        self.verticalLayout_145.addWidget(self.horizontalWidget_55)

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

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, -1, -1, 5)
        self.resHeightTxt = QLineEdit(self.resChangerContent)
        self.resHeightTxt.setObjectName(u"resHeightTxt")
        self.resHeightTxt.setEnabled(True)

        self.horizontalLayout_9.addWidget(self.resHeightTxt)

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
        self.resHeightWarningLbl.setScaledContents(False)
        self.resHeightWarningLbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.resHeightWarningLbl)


        self.verticalLayout_35.addLayout(self.horizontalLayout_9)

        self.resWidthLbl = QLabel(self.resChangerContent)
        self.resWidthLbl.setObjectName(u"resWidthLbl")

        self.verticalLayout_35.addWidget(self.resWidthLbl)

        self.resolutionContent = QVBoxLayout()
        self.resolutionContent.setObjectName(u"resolutionContent")
        self.resolutionContent.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 5)
        self.resWidthTxt = QLineEdit(self.resChangerContent)
        self.resWidthTxt.setObjectName(u"resWidthTxt")

        self.horizontalLayout_10.addWidget(self.resWidthTxt)

        self.resWidthWarningLbl = QLabel(self.resChangerContent)
        self.resWidthWarningLbl.setObjectName(u"resWidthWarningLbl")
        self.resWidthWarningLbl.setMinimumSize(QSize(22, 0))
        self.resWidthWarningLbl.setStyleSheet(u"QLabel {\n"
"		border: 2px solid red;\n"
"		border-radius: 25px;\n"
"		color: red;\n"
"}")
        self.resWidthWarningLbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.resWidthWarningLbl)


        self.resolutionContent.addLayout(self.horizontalLayout_10)


        self.verticalLayout_35.addLayout(self.resolutionContent)


        self.verticalLayout_133.addWidget(self.resChangerContent)

        self.verticalSpacer_63 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_133.addItem(self.verticalSpacer_63)


        self.verticalLayout_145.addWidget(self.advancedOptionsPageContent)

        self.pages.addWidget(self.advancedOptionsPage)
        self.applyPage = QWidget()
        self.applyPage.setObjectName(u"applyPage")
        self.verticalLayout_6 = QVBoxLayout(self.applyPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget2 = QWidget(self.applyPage)
        self.verticalWidget2.setObjectName(u"verticalWidget2")
        self.verticalLayout_24 = QVBoxLayout(self.verticalWidget2)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.locSimPageHeader_2 = QWidget(self.verticalWidget2)
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
        self.toolButton_18.setIcon(icon12)

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

        self.line_5 = QFrame(self.verticalWidget2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_5.setFrameShadow(QFrame.Plain)
        self.line_5.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_24.addWidget(self.line_5)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_10)

        self.gestaltLocationTitleLbl = QLabel(self.verticalWidget2)
        self.gestaltLocationTitleLbl.setObjectName(u"gestaltLocationTitleLbl")
        self.gestaltLocationTitleLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.gestaltLocationTitleLbl)

        self.gestaltLocationLbl = QLabel(self.verticalWidget2)
        self.gestaltLocationLbl.setObjectName(u"gestaltLocationLbl")
        self.gestaltLocationLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.gestaltLocationLbl)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 10, -1, 0)
        self.chooseGestaltBtn = QToolButton(self.verticalWidget2)
        self.chooseGestaltBtn.setObjectName(u"chooseGestaltBtn")
        icon27 = QIcon()
        icon27.addFile(u":/icon/folder.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.chooseGestaltBtn.setIcon(icon27)
        self.chooseGestaltBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_7.addWidget(self.chooseGestaltBtn)


        self.verticalLayout_24.addLayout(self.horizontalLayout_7)

        self.horizontalWidget4 = QWidget(self.verticalWidget2)
        self.horizontalWidget4.setObjectName(u"horizontalWidget4")
        self.horizontalLayout_17 = QHBoxLayout(self.horizontalWidget4)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.applyTweaksBtn = QToolButton(self.horizontalWidget4)
        self.applyTweaksBtn.setObjectName(u"applyTweaksBtn")
        self.applyTweaksBtn.setIcon(icon12)
        self.applyTweaksBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_17.addWidget(self.applyTweaksBtn)


        self.verticalLayout_24.addWidget(self.horizontalWidget4)

        self.statusLbl = QLabel(self.verticalWidget2)
        self.statusLbl.setObjectName(u"statusLbl")
        self.statusLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.statusLbl)

        self.restoreProgressBar = QProgressBar(self.verticalWidget2)
        self.restoreProgressBar.setObjectName(u"restoreProgressBar")
        sizePolicy.setHeightForWidth(self.restoreProgressBar.sizePolicy().hasHeightForWidth())
        self.restoreProgressBar.setSizePolicy(sizePolicy)
        self.restoreProgressBar.setMinimumSize(QSize(150, 0))
        self.restoreProgressBar.setValue(0)
        self.restoreProgressBar.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.restoreProgressBar, 0, Qt.AlignHCenter)

        self.skipSetupOnLbl = QLabel(self.verticalWidget2)
        self.skipSetupOnLbl.setObjectName(u"skipSetupOnLbl")
        self.skipSetupOnLbl.setFont(font1)
        self.skipSetupOnLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.skipSetupOnLbl)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_2)

        self.horizontalWidget5 = QWidget(self.verticalWidget2)
        self.horizontalWidget5.setObjectName(u"horizontalWidget5")
        self.horizontalLayout_25 = QHBoxLayout(self.horizontalWidget5)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_14)

        self.removeTweaksBtn = QToolButton(self.horizontalWidget5)
        self.removeTweaksBtn.setObjectName(u"removeTweaksBtn")

        self.horizontalLayout_25.addWidget(self.removeTweaksBtn)

        self.resetGestaltBtn = QToolButton(self.horizontalWidget5)
        self.resetGestaltBtn.setObjectName(u"resetGestaltBtn")

        self.horizontalLayout_25.addWidget(self.resetGestaltBtn)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_16)


        self.verticalLayout_24.addWidget(self.horizontalWidget5)


        self.verticalLayout_6.addWidget(self.verticalWidget2)

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
        self.toolButton_71.setIcon(icon13)

        self.horizontalLayout_131.addWidget(self.toolButton_71)

        self.verticalWidget_31 = QWidget(self.horizontalWidget_41)
        self.verticalWidget_31.setObjectName(u"verticalWidget_31")
        self.verticalLayout_71 = QVBoxLayout(self.verticalWidget_31)
        self.verticalLayout_71.setSpacing(6)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.springboardOptionsLbl1 = QLabel(self.verticalWidget_31)
        self.springboardOptionsLbl1.setObjectName(u"springboardOptionsLbl1")
        self.springboardOptionsLbl1.setFont(font1)

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

        self.verticalSpacer_21 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self._21.addItem(self.verticalSpacer_21)

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

        self.verticalSpacer_51 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self._21.addItem(self.verticalSpacer_51)


        self.verticalLayout_101.addWidget(self.settingsPageContent)

        self.pages.addWidget(self.settingsPage)
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
        self.toolButton_13.setIcon(icon6)

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
        self.line_2.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_28.addWidget(self.line_2)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer_14)

        self.locSimCnt = QWidget(self.locSimPage)
        self.locSimCnt.setObjectName(u"locSimCnt")
        self.locSimPageContent = QVBoxLayout(self.locSimCnt)
        self.locSimPageContent.setObjectName(u"locSimPageContent")
        self.locSimPageContent.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget3 = QWidget(self.locSimCnt)
        self.verticalWidget3.setObjectName(u"verticalWidget3")
        self.verticalLayout_29 = QVBoxLayout(self.verticalWidget3)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.verticalWidget3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_7)

        self.latitudeTxt = QLineEdit(self.verticalWidget3)
        self.latitudeTxt.setObjectName(u"latitudeTxt")
        self.latitudeTxt.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.latitudeTxt)

        self.label_11 = QLabel(self.verticalWidget3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_11)

        self.longitudeTxt = QLineEdit(self.verticalWidget3)
        self.longitudeTxt.setObjectName(u"longitudeTxt")
        self.longitudeTxt.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.longitudeTxt)

        self.horizontalWidget6 = QWidget(self.verticalWidget3)
        self.horizontalWidget6.setObjectName(u"horizontalWidget6")
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalWidget6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.setLocationBtn = QToolButton(self.horizontalWidget6)
        self.setLocationBtn.setObjectName(u"setLocationBtn")

        self.horizontalLayout_3.addWidget(self.setLocationBtn)


        self.verticalLayout_29.addWidget(self.horizontalWidget6)

        self.horizontalWidget_22 = QWidget(self.verticalWidget3)
        self.horizontalWidget_22.setObjectName(u"horizontalWidget_22")
        self.horizontalLayout_29 = QHBoxLayout(self.horizontalWidget_22)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.resetLocationBtn = QToolButton(self.horizontalWidget_22)
        self.resetLocationBtn.setObjectName(u"resetLocationBtn")

        self.horizontalLayout_29.addWidget(self.resetLocationBtn)


        self.verticalLayout_29.addWidget(self.horizontalWidget_22)


        self.locSimPageContent.addWidget(self.verticalWidget3)


        self.verticalLayout_28.addWidget(self.locSimCnt)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer_13)

        self.pages.addWidget(self.locSimPage)
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
        self.toolButton_12.setIcon(icon10)
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
        self.line_14.setFrameShape(QFrame.Shape.HLine)

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
        self.importOperationBtn.setIcon(icon25)
        self.importOperationBtn.setIconSize(QSize(20, 20))
        self.importOperationBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.customOpsTopBtns.addWidget(self.importOperationBtn, 0, Qt.AlignLeft)

        self.newOperationBtn = QToolButton(self.customOperationsPageContent)
        self.newOperationBtn.setObjectName(u"newOperationBtn")
        self.newOperationBtn.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.newOperationBtn.sizePolicy().hasHeightForWidth())
        self.newOperationBtn.setSizePolicy(sizePolicy2)
        self.newOperationBtn.setMinimumSize(QSize(0, 35))
        self.newOperationBtn.setIcon(icon20)
        self.newOperationBtn.setIconSize(QSize(16, 16))
        self.newOperationBtn.setCheckable(False)
        self.newOperationBtn.setAutoExclusive(True)
        self.newOperationBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.customOpsTopBtns.addWidget(self.newOperationBtn, 0, Qt.AlignLeft)


        self.verticalLayout_19.addLayout(self.customOpsTopBtns)

        self.operationsCnt = QWidget(self.customOperationsPageContent)
        self.operationsCnt.setObjectName(u"operationsCnt")
        self.operationsCnt.setEnabled(True)
        sizePolicy7.setHeightForWidth(self.operationsCnt.sizePolicy().hasHeightForWidth())
        self.operationsCnt.setSizePolicy(sizePolicy7)

        self.verticalLayout_19.addWidget(self.operationsCnt)


        self.verticalLayout_20.addWidget(self.customOperationsPageContent)

        self.pages.addWidget(self.customOperationsPage)
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
        icon28 = QIcon()
        icon28.addFile(u":/icon/compass.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_16.setIcon(icon28)

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
        self.line_3.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_31.addWidget(self.line_3)

        self.exploreThemesCnt = QWidget(self.explorePage)
        self.exploreThemesCnt.setObjectName(u"exploreThemesCnt")
        sizePolicy7.setHeightForWidth(self.exploreThemesCnt.sizePolicy().hasHeightForWidth())
        self.exploreThemesCnt.setSizePolicy(sizePolicy7)

        self.verticalLayout_31.addWidget(self.exploreThemesCnt)

        self.pages.addWidget(self.explorePage)
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
        self.themesBtn.setIcon(icon4)
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

        self.horizontalWidget7 = QWidget(self.horizontalWidget_8)
        self.horizontalWidget7.setObjectName(u"horizontalWidget7")
        self.horizontalLayout_26 = QHBoxLayout(self.horizontalWidget7)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.importThemeBtn = QToolButton(self.horizontalWidget7)
        self.importThemeBtn.setObjectName(u"importThemeBtn")
        self.importThemeBtn.setEnabled(False)
        self.importThemeBtn.setStyleSheet(u"QToolButton {\n"
"	background: none;\n"
"}")

        self.horizontalLayout_26.addWidget(self.importThemeBtn)

        self.importThemeFolderBtn = QToolButton(self.horizontalWidget7)
        self.importThemeFolderBtn.setObjectName(u"importThemeFolderBtn")
        self.importThemeFolderBtn.setIcon(icon27)

        self.horizontalLayout_26.addWidget(self.importThemeFolderBtn)

        self.importThemeZipBtn = QToolButton(self.horizontalWidget7)
        self.importThemeZipBtn.setObjectName(u"importThemeZipBtn")
        self.importThemeZipBtn.setIcon(icon23)

        self.horizontalLayout_26.addWidget(self.importThemeZipBtn)


        self.horizontalLayout_23.addWidget(self.horizontalWidget7)


        self.verticalLayout_23.addWidget(self.horizontalWidget_8)

        self.line_15 = QFrame(self.themingPage)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_15.setFrameShadow(QFrame.Plain)
        self.line_15.setFrameShape(QFrame.Shape.HLine)

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
        self.line.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_22.addWidget(self.line)

        self.label_3 = QLabel(self.themesPageContent)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_22.addWidget(self.label_3)

        self.iconsCnt = QWidget(self.themesPageContent)
        self.iconsCnt.setObjectName(u"iconsCnt")

        self.verticalLayout_22.addWidget(self.iconsCnt)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_9)

        self.horizontalWidget8 = QWidget(self.themesPageContent)
        self.horizontalWidget8.setObjectName(u"horizontalWidget8")
        self.horizontalLayout_16 = QHBoxLayout(self.horizontalWidget8)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.hideNamesBtn = QToolButton(self.horizontalWidget8)
        self.hideNamesBtn.setObjectName(u"hideNamesBtn")
        sizePolicy2.setHeightForWidth(self.hideNamesBtn.sizePolicy().hasHeightForWidth())
        self.hideNamesBtn.setSizePolicy(sizePolicy2)

        self.horizontalLayout_16.addWidget(self.hideNamesBtn)

        self.borderAllBtn = QToolButton(self.horizontalWidget8)
        self.borderAllBtn.setObjectName(u"borderAllBtn")
        sizePolicy2.setHeightForWidth(self.borderAllBtn.sizePolicy().hasHeightForWidth())
        self.borderAllBtn.setSizePolicy(sizePolicy2)

        self.horizontalLayout_16.addWidget(self.borderAllBtn)

        self.addAllBtn = QToolButton(self.horizontalWidget8)
        self.addAllBtn.setObjectName(u"addAllBtn")
        sizePolicy2.setHeightForWidth(self.addAllBtn.sizePolicy().hasHeightForWidth())
        self.addAllBtn.setSizePolicy(sizePolicy2)

        self.horizontalLayout_16.addWidget(self.addAllBtn)


        self.verticalLayout_22.addWidget(self.horizontalWidget8)


        self.verticalLayout_23.addWidget(self.themesPageContent)

        self.pages.addWidget(self.themingPage)

        self._3.addWidget(self.pages)


        self.horizontalLayout_18.addWidget(self.main)


        self.verticalLayout_11.addWidget(self.body)

        Nugget.setCentralWidget(self.centralwidget)

        self.retranslateUi(Nugget)

        self.devicePicker.setCurrentIndex(-1)
        self.pages.setCurrentIndex(0)
        self.dynamicIslandDrp.setCurrentIndex(0)
        self.spoofedModelDrp.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Nugget)
    # setupUi

    def retranslateUi(self, Nugget):
        Nugget.setWindowTitle(QCoreApplication.translate("Nugget", u"Nugget", None))
        self.centralwidget.setProperty(u"cls", QCoreApplication.translate("Nugget", u"central", None))
        self.devicePicker.setPlaceholderText(QCoreApplication.translate("Nugget", u"None", None))
        self.refreshBtn.setProperty(u"cls", QCoreApplication.translate("Nugget", u"btn", None))
        self.titleBar.setText(QCoreApplication.translate("Nugget", u"Nugget", None))
        self.homePageBtn.setText(QCoreApplication.translate("Nugget", u"    Home", None))
        self.homePageBtn.setProperty(u"cls", QCoreApplication.translate("Nugget", u"sidebarBtn", None))
        self.posterboardPageBtn.setText(QCoreApplication.translate("Nugget", u"    Posterboard", None))
        self.posterboardPageBtn.setProperty(u"cls", QCoreApplication.translate("Nugget", u"sidebarBtn", None))
        self.gestaltPageBtn.setText(QCoreApplication.translate("Nugget", u"     Mobile Gestalt", None))
        self.gestaltPageBtn.setProperty(u"cls", QCoreApplication.translate("Nugget", u"sidebarBtn", None))
        self.featureFlagsPageBtn.setText(QCoreApplication.translate("Nugget", u"    Feature Flags", None))
        self.featureFlagsPageBtn.setProperty(u"cls", QCoreApplication.translate("Nugget", u"sidebarBtn", None))
        self.euEnablerPageBtn.setText(QCoreApplication.translate("Nugget", u"    Eligibility", None))
        self.euEnablerPageBtn.setProperty(u"cls", QCoreApplication.translate("Nugget", u"sidebarBtn", None))
        self.springboardOptionsPageBtn.setText(QCoreApplication.translate("Nugget", u"    Springboard Options", None))
        self.springboardOptionsPageBtn.setProperty(u"cls", QCoreApplication.translate("Nugget", u"sidebarBtn", None))
        self.internalOptionsPageBtn.setText(QCoreApplication.translate("Nugget", u"    Internal Options", None))
        self.internalOptionsPageBtn.setProperty(u"cls", QCoreApplication.translate("Nugget", u"sidebarBtn", None))
        self.daemonsPageBtn.setText(QCoreApplication.translate("Nugget", u"    Daemons", None))
        self.daemonsPageBtn.setProperty(u"cls", QCoreApplication.translate("Nugget", u"sidebarBtn", None))
        self.templatesPageBtn.setText(QCoreApplication.translate("Nugget", u"    Templates", None))
        self.templatesPageBtn.setProperty(u"cls", QCoreApplication.translate("Nugget", u"sidebarBtn", None))
        self.advancedPageBtn.setText(QCoreApplication.translate("Nugget", u"    Risky Options", None))
        self.advancedPageBtn.setProperty(u"cls", QCoreApplication.translate("Nugget", u"sidebarBtn", None))
        self.applyPageBtn.setText(QCoreApplication.translate("Nugget", u"    Apply", None))
        self.applyPageBtn.setProperty(u"cls", QCoreApplication.translate("Nugget", u"sidebarBtn", None))
        self.settingsPageBtn.setText(QCoreApplication.translate("Nugget", u"    Settings", None))
        self.settingsPageBtn.setProperty(u"cls", QCoreApplication.translate("Nugget", u"sidebarBtn", None))
        self.phoneNameLbl.setText(QCoreApplication.translate("Nugget", u"Phone", None))
        self.phoneVersionLbl.setText(QCoreApplication.translate("Nugget", u"<a style=\"text-decoration:none; color: white\" href=\"#\">Version</a>", None))
        self.bigNuggetBtn.setText(QCoreApplication.translate("Nugget", u"...", None))
        self.label_2.setText(QCoreApplication.translate("Nugget", u"Nugget", None))
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
        self.libiBtn.setText(QCoreApplication.translate("Nugget", u"pymobiledevice3", None))
        self.jjtechBtn.setText(QCoreApplication.translate("Nugget", u"JJTech\n"
"Sparserestore", None))
        self.qtBtn.setText(QCoreApplication.translate("Nugget", u"Qt Creator", None))
        self.appVersionLbl.setText(QCoreApplication.translate("Nugget", u"Nugget GUI - Version %VERSION %BETATAG", None))
        self.statusBarLbl.setText(QCoreApplication.translate("Nugget", u"Mobile Gestalt", None))
        self.mgaWarningLbl.setText(QCoreApplication.translate("Nugget", u"! You will need a MobileGestalt file for this feature. Please select it in the Apply page !", None))
        self.label_9.setText(QCoreApplication.translate("Nugget", u"Device Subtype Preset", None))
        self.dynamicIslandDrp.setItemText(0, QCoreApplication.translate("Nugget", u"None", None))
        self.dynamicIslandDrp.setItemText(1, QCoreApplication.translate("Nugget", u"2436 (iPhone X Gestures for SE phones)", None))
        self.dynamicIslandDrp.setItemText(2, QCoreApplication.translate("Nugget", u"2556 (iPhone 14 Pro Dynamic Island)", None))
        self.dynamicIslandDrp.setItemText(3, QCoreApplication.translate("Nugget", u"2796 (iPhone 14 Pro Max Dynamic Island)", None))
        self.dynamicIslandDrp.setItemText(4, QCoreApplication.translate("Nugget", u"2976 (iPhone 15 Pro Max Dynamic Island)", None))
        self.dynamicIslandDrp.setItemText(5, QCoreApplication.translate("Nugget", u"2622 (iPhone 16 Pro Dynamic Island)", None))
        self.dynamicIslandDrp.setItemText(6, QCoreApplication.translate("Nugget", u"2868 (iPhone 16 Pro Max Dynamic Island)", None))

        self.dynamicIslandDrp.setCurrentText(QCoreApplication.translate("Nugget", u"None", None))
#if QT_CONFIG(tooltip)
        self.rdarFixChk.setToolTip(QCoreApplication.translate("Nugget", u"Modifies the resolution to improve functionality of the changed device subtype. May cause weird visual bugs.", None))
#endif // QT_CONFIG(tooltip)
        self.rdarFixChk.setText(QCoreApplication.translate("Nugget", u"Fix RDAR (modifies resolution)", None))
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
        self.springboardOptionsLbl.setText(QCoreApplication.translate("Nugget", u"Springboard Options", None))
        self.label_13.setText(QCoreApplication.translate("Nugget", u"Lock Screen Footnote Text", None))
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
        self.exportPBVideoBtn.setText(QCoreApplication.translate("Nugget", u"   Export Video as Descriptor", None))
        self.pbVideoThumbLbl.setText(QCoreApplication.translate("Nugget", u"Current Thumbnail: None", None))
        self.pbVideoLbl.setText(QCoreApplication.translate("Nugget", u"Current Video: None", None))
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
        self.resHeightWarningLbl.setText(QCoreApplication.translate("Nugget", u"!", None))
        self.resWidthLbl.setText(QCoreApplication.translate("Nugget", u"Width:", None))
        self.resWidthTxt.setPlaceholderText(QCoreApplication.translate("Nugget", u"Resolution Width", None))
        self.resWidthWarningLbl.setText(QCoreApplication.translate("Nugget", u"!", None))
        self.statusBarLbl_5.setText(QCoreApplication.translate("Nugget", u"Apply", None))
        self.label_16.setText("")
        self.gestaltLocationTitleLbl.setText(QCoreApplication.translate("Nugget", u"Current gestalt file location:", None))
        self.gestaltLocationLbl.setText(QCoreApplication.translate("Nugget", u"None", None))
        self.chooseGestaltBtn.setText(QCoreApplication.translate("Nugget", u"  Choose Gestalt File", None))
        self.applyTweaksBtn.setText(QCoreApplication.translate("Nugget", u"  Apply Changes", None))
        self.statusLbl.setText(QCoreApplication.translate("Nugget", u"Ready!", None))
        self.skipSetupOnLbl.setText(QCoreApplication.translate("Nugget", u"Note: Skip Setup is currently turned on.", None))
        self.removeTweaksBtn.setText(QCoreApplication.translate("Nugget", u"Remove All Tweaks", None))
        self.resetGestaltBtn.setText(QCoreApplication.translate("Nugget", u"Reset Mobile Gestalt", None))
        self.springboardOptionsLbl1.setText(QCoreApplication.translate("Nugget", u"Nugget Settings", None))
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
        self.line_24.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.revertRdarChk.setToolTip(QCoreApplication.translate("Nugget", u"If you used the rdar/status bar fix in a previous iOS version, this will revert that.", None))
#endif // QT_CONFIG(tooltip)
        self.revertRdarChk.setText(QCoreApplication.translate("Nugget", u"Revert rdar Fix (reset resolution)", None))
        self.skipSetupChk.setText(QCoreApplication.translate("Nugget", u"Skip Setup * (non-exploit files only)", None))
        self.supervisionChk.setText(QCoreApplication.translate("Nugget", u"Enable Supervision * (requires Skip Setup)", None))
        self.supervisionOrganization.setPlaceholderText(QCoreApplication.translate("Nugget", u"Enter Organization Name", None))
        self.label_15.setText(QCoreApplication.translate("Nugget", u"* Note: Skip Setup may cause issues with configuration profiles. Turn it off if you need that.", None))
        self.resetPairBtn.setText(QCoreApplication.translate("Nugget", u"Reset Device Pairing", None))
        self.statusBarLbl_2.setText(QCoreApplication.translate("Nugget", u"Location Simulation", None))
        self.label_4.setText("")
        self.loadLocSimBtn.setText(QCoreApplication.translate("Nugget", u"Start Location Simulation", None))
        self.label_7.setText(QCoreApplication.translate("Nugget", u"Latitude", None))
        self.latitudeTxt.setPlaceholderText(QCoreApplication.translate("Nugget", u"XXX.XXXXX", None))
        self.label_11.setText(QCoreApplication.translate("Nugget", u"Longitude", None))
        self.longitudeTxt.setPlaceholderText(QCoreApplication.translate("Nugget", u"XXX.XXXXX", None))
        self.setLocationBtn.setText(QCoreApplication.translate("Nugget", u"Set Location", None))
        self.resetLocationBtn.setText(QCoreApplication.translate("Nugget", u"Reset Location", None))
        self.customOperationsLbl.setText(QCoreApplication.translate("Nugget", u"Custom Operations", None))
        self.label_14.setText("")
        self.importOperationBtn.setText(QCoreApplication.translate("Nugget", u"  Import .cowperation", None))
        self.newOperationBtn.setText(QCoreApplication.translate("Nugget", u"  New Operation", None))
        self.exploreLbl.setText(QCoreApplication.translate("Nugget", u"Explore", None))
        self.exploreSubLbl.setText("")
        self.themesLbl.setText(QCoreApplication.translate("Nugget", u"Mobile Gestalt Modifications", None))
        self.importThemeBtn.setText(QCoreApplication.translate("Nugget", u"Import Theme:", None))
        self.importThemeFolderBtn.setText(QCoreApplication.translate("Nugget", u"...", None))
        self.importThemeZipBtn.setText(QCoreApplication.translate("Nugget", u"...", None))
        self.label_3.setText(QCoreApplication.translate("Nugget", u"Customize Individual Apps", None))
        self.hideNamesBtn.setText(QCoreApplication.translate("Nugget", u"Hide/Show All App Names", None))
        self.borderAllBtn.setText(QCoreApplication.translate("Nugget", u"Toggle All \"Border\"", None))
        self.addAllBtn.setText(QCoreApplication.translate("Nugget", u"Toggle All \"Add to Device\"", None))
    # retranslateUi

