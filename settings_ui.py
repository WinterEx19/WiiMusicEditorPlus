# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.setWindowModality(QtCore.Qt.ApplicationModal)
        Settings.resize(443, 324)
        Settings.setStyleSheet("QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: white;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: white;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(:images/images/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: #121212;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"    padding-left: 1px;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(:images/images/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QRadioButton:disabled\n"
"{\n"
"    background-color: #404040;\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(:images/images/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}\n"
"\n"
"QWidget[error=\"true\"]\n"
"{\n"
"    border: 1px solid red;\n"
"}\n"
"\n"
"QWidget[error=\"true\"]\n"
"{\n"
"    border: 1px solid red;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Settings)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MainWidget = QtWidgets.QTabWidget(Settings)
        self.MainWidget.setObjectName("MainWidget")
        self.Tab_General = QtWidgets.QWidget()
        self.Tab_General.setObjectName("Tab_General")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Tab_General)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Appearence = QtWidgets.QGroupBox(self.Tab_General)
        self.Appearence.setObjectName("Appearence")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.Appearence)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.LanguageLayout = QtWidgets.QHBoxLayout()
        self.LanguageLayout.setObjectName("LanguageLayout")
        self.LanguageLabel = QtWidgets.QLabel(self.Appearence)
        self.LanguageLabel.setObjectName("LanguageLabel")
        self.LanguageLayout.addWidget(self.LanguageLabel)
        self.LanguageBox = QtWidgets.QComboBox(self.Appearence)
        self.LanguageBox.setObjectName("LanguageBox")
        self.LanguageBox.addItem("")
        self.LanguageBox.setItemText(0, "English")
        self.LanguageBox.addItem("")
        self.LanguageBox.setItemText(1, "Français")
        self.LanguageBox.addItem("")
        self.LanguageBox.setItemText(2, "Español")
        self.LanguageBox.addItem("")
        self.LanguageBox.setItemText(3, "Deutsch")
        self.LanguageBox.addItem("")
        self.LanguageBox.setItemText(4, "Italiano")
        self.LanguageBox.addItem("")
        self.LanguageBox.setItemText(5, "日本")
        self.LanguageBox.addItem("")
        self.LanguageBox.setItemText(6, "한국인")
        self.LanguageLayout.addWidget(self.LanguageBox)
        self.verticalLayout_10.addLayout(self.LanguageLayout)
        self.verticalLayout_3.addWidget(self.Appearence)
        self.groupBox = QtWidgets.QGroupBox(self.Tab_General)
        self.groupBox.setTitle("Discord")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.Discord = QtWidgets.QCheckBox(self.groupBox)
        self.Discord.setChecked(True)
        self.Discord.setObjectName("Discord")
        self.verticalLayout_12.addWidget(self.Discord)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.Updates = QtWidgets.QGroupBox(self.Tab_General)
        self.Updates.setObjectName("Updates")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Updates)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.CheckForUpdates = QtWidgets.QCheckBox(self.Updates)
        self.CheckForUpdates.setChecked(True)
        self.CheckForUpdates.setObjectName("CheckForUpdates")
        self.horizontalLayout.addWidget(self.CheckForUpdates)
        self.SwitchBeta = QtWidgets.QPushButton(self.Updates)
        self.SwitchBeta.setObjectName("SwitchBeta")
        self.horizontalLayout.addWidget(self.SwitchBeta)
        self.verticalLayout_3.addWidget(self.Updates)
        self.Debug = QtWidgets.QGroupBox(self.Tab_General)
        self.Debug.setObjectName("Debug")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.Debug)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.UnsafeMode = QtWidgets.QCheckBox(self.Debug)
        self.UnsafeMode.setEnabled(True)
        self.UnsafeMode.setObjectName("UnsafeMode")
        self.verticalLayout_9.addWidget(self.UnsafeMode)
        self.verticalLayout_3.addWidget(self.Debug)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.MainWidget.addTab(self.Tab_General, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.Rom = QtWidgets.QGroupBox(self.tab)
        self.Rom.setObjectName("Rom")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.Rom)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Region = QtWidgets.QHBoxLayout()
        self.Region.setObjectName("Region")
        self.RegionLabel = QtWidgets.QLabel(self.Rom)
        self.RegionLabel.setObjectName("RegionLabel")
        self.Region.addWidget(self.RegionLabel)
        self.RegionBox = QtWidgets.QComboBox(self.Rom)
        self.RegionBox.setMinimumSize(QtCore.QSize(60, 20))
        self.RegionBox.setObjectName("RegionBox")
        self.RegionBox.addItem("")
        self.RegionBox.addItem("")
        self.RegionBox.addItem("")
        self.RegionBox.addItem("")
        self.Region.addWidget(self.RegionBox)
        self.verticalLayout_8.addLayout(self.Region)
        self.RomLanguage = QtWidgets.QHBoxLayout()
        self.RomLanguage.setObjectName("RomLanguage")
        self.label = QtWidgets.QLabel(self.Rom)
        self.label.setObjectName("label")
        self.RomLanguage.addWidget(self.label)
        self.RomLanguageBox = QtWidgets.QComboBox(self.Rom)
        self.RomLanguageBox.setObjectName("RomLanguageBox")
        self.RomLanguage.addWidget(self.RomLanguageBox)
        self.verticalLayout_8.addLayout(self.RomLanguage)
        self.RevertChanges = QtWidgets.QCheckBox(self.Rom)
        self.RevertChanges.setChecked(True)
        self.RevertChanges.setObjectName("RevertChanges")
        self.verticalLayout_8.addWidget(self.RevertChanges)
        self.verticalLayout_11.addWidget(self.Rom)
        self.SongEditor = QtWidgets.QGroupBox(self.tab)
        self.SongEditor.setObjectName("SongEditor")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.SongEditor)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.SongScoreCheckbox = QtWidgets.QCheckBox(self.SongEditor)
        self.SongScoreCheckbox.setObjectName("SongScoreCheckbox")
        self.verticalLayout_4.addWidget(self.SongScoreCheckbox)
        self.RapperFix = QtWidgets.QCheckBox(self.SongEditor)
        self.RapperFix.setChecked(True)
        self.RapperFix.setObjectName("RapperFix")
        self.verticalLayout_4.addWidget(self.RapperFix)
        self.Normalize = QtWidgets.QCheckBox(self.SongEditor)
        self.Normalize.setObjectName("Normalize")
        self.verticalLayout_4.addWidget(self.Normalize)
        self.verticalLayout_11.addWidget(self.SongEditor)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem1)
        self.MainWidget.addTab(self.tab, "")
        self.Tab_Dolphin = QtWidgets.QWidget()
        self.Tab_Dolphin.setObjectName("Tab_Dolphin")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Tab_Dolphin)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.DolphinPath_Title = QtWidgets.QGroupBox(self.Tab_Dolphin)
        self.DolphinPath_Title.setObjectName("DolphinPath_Title")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.DolphinPath_Title)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.DolphinPath_Label = QtWidgets.QLabel(self.DolphinPath_Title)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.DolphinPath_Label.setFont(font)
        self.DolphinPath_Label.setStyleSheet("QLabel\n"
"{\n"
"padding: 1px;\n"
"border: 1px solid;\n"
"border-color: #1e1e1e;\n"
"background-color: #242424;\n"
"padding-top: 6px;\n"
"padding-bottom: 6px;\n"
"}")
        self.DolphinPath_Label.setObjectName("DolphinPath_Label")
        self.verticalLayout_5.addWidget(self.DolphinPath_Label)
        self.DolphinPath_Browse = QtWidgets.QPushButton(self.DolphinPath_Title)
        self.DolphinPath_Browse.setObjectName("DolphinPath_Browse")
        self.verticalLayout_5.addWidget(self.DolphinPath_Browse)
        self.verticalLayout_2.addWidget(self.DolphinPath_Title)
        self.DolphinSave_Title = QtWidgets.QGroupBox(self.Tab_Dolphin)
        self.DolphinSave_Title.setObjectName("DolphinSave_Title")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.DolphinSave_Title)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.DolphinSave_Label = QtWidgets.QLabel(self.DolphinSave_Title)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.DolphinSave_Label.setFont(font)
        self.DolphinSave_Label.setStyleSheet("QLabel\n"
"{\n"
"padding: 1px;\n"
"border: 1px solid;\n"
"border-color: #1e1e1e;\n"
"background-color: #242424;\n"
"padding-top: 6px;\n"
"padding-bottom: 6px;\n"
"}")
        self.DolphinSave_Label.setObjectName("DolphinSave_Label")
        self.verticalLayout_6.addWidget(self.DolphinSave_Label)
        self.DolphinSave_Buttons = QtWidgets.QHBoxLayout()
        self.DolphinSave_Buttons.setObjectName("DolphinSave_Buttons")
        self.DolphinSave_Browse = QtWidgets.QPushButton(self.DolphinSave_Title)
        self.DolphinSave_Browse.setObjectName("DolphinSave_Browse")
        self.DolphinSave_Buttons.addWidget(self.DolphinSave_Browse)
        self.DolphinSave_Default = QtWidgets.QPushButton(self.DolphinSave_Title)
        self.DolphinSave_Default.setObjectName("DolphinSave_Default")
        self.DolphinSave_Buttons.addWidget(self.DolphinSave_Default)
        self.verticalLayout_6.addLayout(self.DolphinSave_Buttons)
        self.verticalLayout_2.addWidget(self.DolphinSave_Title)
        self.Dolphin_Geckocodes_Title = QtWidgets.QGroupBox(self.Tab_Dolphin)
        self.Dolphin_Geckocodes_Title.setObjectName("Dolphin_Geckocodes_Title")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.Dolphin_Geckocodes_Title)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.Dolphon_Geckocodes = QtWidgets.QCheckBox(self.Dolphin_Geckocodes_Title)
        self.Dolphon_Geckocodes.setChecked(True)
        self.Dolphon_Geckocodes.setObjectName("Dolphon_Geckocodes")
        self.verticalLayout_7.addWidget(self.Dolphon_Geckocodes)
        self.DolphinEnableCheats = QtWidgets.QCheckBox(self.Dolphin_Geckocodes_Title)
        self.DolphinEnableCheats.setChecked(True)
        self.DolphinEnableCheats.setObjectName("DolphinEnableCheats")
        self.verticalLayout_7.addWidget(self.DolphinEnableCheats)
        self.verticalLayout_2.addWidget(self.Dolphin_Geckocodes_Title)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.MainWidget.addTab(self.Tab_Dolphin, "Dolphin")
        self.verticalLayout.addWidget(self.MainWidget)

        self.retranslateUi(Settings)
        self.MainWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Settings"))
        self.Appearence.setTitle(_translate("Settings", "Appearence"))
        self.LanguageLabel.setText(_translate("Settings", "Language:"))
        self.Discord.setText(_translate("Settings", "Discord Rich Presence"))
        self.Updates.setTitle(_translate("Settings", "Updates"))
        self.CheckForUpdates.setText(_translate("Settings", "Check for Updates on Startup"))
        self.SwitchBeta.setText(_translate("Settings", "Switch to Beta"))
        self.Debug.setTitle(_translate("Settings", "Debug Options"))
        self.UnsafeMode.setText(_translate("Settings", "Unsafe mode (Enables options that might crash the game)"))
        self.MainWidget.setTabText(self.MainWidget.indexOf(self.Tab_General), _translate("Settings", "General"))
        self.Rom.setTitle(_translate("Settings", "Rom Settings"))
        self.RegionLabel.setText(_translate("Settings", "Fallback Region (Used if rom region can\'t be determinded):"))
        self.RegionBox.setItemText(0, _translate("Settings", "U.S."))
        self.RegionBox.setItemText(1, _translate("Settings", "Europe"))
        self.RegionBox.setItemText(2, _translate("Settings", "Japan"))
        self.RegionBox.setItemText(3, _translate("Settings", "Korea"))
        self.label.setText(_translate("Settings", "Rom Language:"))
        self.RevertChanges.setText(_translate("Settings", "Remove changes from Changes.ini when reverting changes"))
        self.SongEditor.setTitle(_translate("Settings", "Song Editor"))
        self.SongScoreCheckbox.setText(_translate("Settings", "Load Song and Score separately"))
        self.RapperFix.setText(_translate("Settings", "Add the Rapper Crash fix to Gecko codes"))
        self.Normalize.setText(_translate("Settings", "Normalize Midi (Makes Midis more Wii Music friendly)"))
        self.MainWidget.setTabText(self.MainWidget.indexOf(self.tab), _translate("Settings", "Editor"))
        self.DolphinPath_Title.setTitle(_translate("Settings", "Dolphin Path"))
        self.DolphinPath_Label.setText(_translate("Settings", "No Specified Path"))
        self.DolphinPath_Browse.setText(_translate("Settings", "Browse"))
        self.DolphinSave_Title.setTitle(_translate("Settings", "Dolphin Save Path"))
        self.DolphinSave_Label.setText(_translate("Settings", "Default Path"))
        self.DolphinSave_Browse.setText(_translate("Settings", "Browse"))
        self.DolphinSave_Default.setText(_translate("Settings", "Set as Default"))
        self.Dolphin_Geckocodes_Title.setTitle(_translate("Settings", "Gecko Codes"))
        self.Dolphon_Geckocodes.setText(_translate("Settings", "Copy Gecko codes to Dolphin save directory"))
        self.DolphinEnableCheats.setText(_translate("Settings", "Force Enable Cheats when launching Dolphin"))
import resources_rc
