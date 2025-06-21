import webbrowser
from PySide6.QtCore import QCoreApplication

from ..page import Page
from qt.ui_mainwindow import Ui_Nugget

from devicemanagement.constants import Version

class HomePage(Page):
    def __init__(self, window, ui: Ui_Nugget):
        super().__init__()
        self.window = window
        self.ui = ui
        self.show_uuid = False

    def load_page(self):
        ## HOME PAGE ACTIONS
        self.ui.phoneVersionLbl.linkActivated.connect(self.toggle_version_label)

        ## HOME PAGE LINKS
        self.ui.bigNuggetBtn.clicked.connect(self.on_bigNuggetBtn_clicked)
        self.ui.starOnGithubBtn.clicked.connect(self.on_githubBtn_clicked)

        self.ui.leminGithubBtn.clicked.connect(self.on_leminGitHubBtn_clicked)
        self.ui.leminTwitterBtn.clicked.connect(self.on_leminTwitterBtn_clicked)
        self.ui.leminKoFiBtn.clicked.connect(self.on_leminKoFiBtn_clicked)
        
        self.ui.posterRestoreBtn.clicked.connect(self.on_posterRestoreBtn_clicked)
        self.ui.snoolieBtn.clicked.connect(self.on_snoolieBtn_clicked)
        self.ui.disfordottieBtn.clicked.connect(self.on_disfordottieBtn_clicked)
        self.ui.mikasaBtn.clicked.connect(self.on_mikasaBtn_clicked)

        self.ui.libiBtn.clicked.connect(self.on_libiBtn_clicked)
        self.ui.jjtechBtn.clicked.connect(self.on_jjtechBtn_clicked)
        self.ui.qtBtn.clicked.connect(self.on_qtBtn_clicked)
        self.ui.translatorsBtn.clicked.connect(self.on_translatorsBtn_clicked)

        self.ui.discordBtn.clicked.connect(self.on_discordBtn_clicked)

    ## ACTIONS
    def updatePhoneInfo(self):
        # name label
        self.ui.phoneNameLbl.setText(self.window.device_manager.get_current_device_name())
        # version label
        ver = self.window.device_manager.get_current_device_version()
        build = self.window.device_manager.get_current_device_build()
        self.show_uuid = False
        if ver != "":
            self.show_version_text(version=ver, build=build)
        else:
            self.ui.phoneVersionLbl.setText(QCoreApplication.tr("Please connect a device."))

    def toggle_version_label(self):
        if self.show_uuid:
            self.show_uuid = False
            ver = self.window.device_manager.get_current_device_version()
            build = self.window.device_manager.get_current_device_build()
            if ver != "":
                self.show_version_text(version=ver, build=build)
        else:
            self.show_uuid = True
            uuid = self.window.device_manager.get_current_device_uuid()
            if uuid != "":
                self.ui.phoneVersionLbl.setText(f"<a style=\"text-decoration:none; color: white\" href=\"#\">{uuid}</a>")

    def show_version_text(self, version: str, build: str):
        support_str: str = "<span style=\"color: #32d74b;\">" + QCoreApplication.tr("Supported!") + "</span></a>"
        if Version(version) < Version("17.0"):
            support_str = "<span style=\"color: #ff0000;\">" + QCoreApplication.tr("Not Supported.") + "</span></a>"
        elif self.window.device_manager.get_current_device_patched():
            # sparserestore fully patched
            support_str = "<span style=\"color: #ffff00;\">"+ QCoreApplication.tr("Partially Supported.") + "</span></a>"
        self.ui.phoneVersionLbl.setText(f"<a style=\"text-decoration:none; color: white;\" href=\"#\">iOS {version} ({build}) {support_str}")

    ## HOME PAGE LINKS
    def on_bigMilkBtn_clicked(self):
        webbrowser.open_new_tab("https://cowabun.ga")

    def on_leminGitHubBtn_clicked(self):
        webbrowser.open_new_tab("https://github.com/leminlimez")
    def on_leminTwitterBtn_clicked(self):
        webbrowser.open_new_tab("https://twitter.com/LeminLimez")
    def on_leminKoFiBtn_clicked(self):
        webbrowser.open_new_tab("https://ko-fi.com/leminlimez")

    def on_posterRestoreBtn_clicked(self):
        webbrowser.open_new_tab("https://discord.gg/gWtzTVhMvh")
    def on_snoolieBtn_clicked(self):
        webbrowser.open_new_tab("https://github.com/0xilis/python-aar-stuff")
    def on_disfordottieBtn_clicked(self):
        webbrowser.open_new_tab("https://twitter.com/disfordottie")
    def on_mikasaBtn_clicked(self):
        webbrowser.open_new_tab("https://github.com/Mikasa-san/QuietDaemon")

    def on_libiBtn_clicked(self):
        webbrowser.open_new_tab("https://github.com/doronz88/pymobiledevice3")
    def on_jjtechBtn_clicked(self):
        webbrowser.open_new_tab("https://github.com/JJTech0130/TrollRestore")
    def on_qtBtn_clicked(self):
        webbrowser.open_new_tab("https://www.qt.io/product/development-tools")
    def on_translatorsBtn_clicked(self):
        webbrowser.open_new_tab("https://poeditor.com/join/project/UTqpVSE2UD")

    def on_discordBtn_clicked(self):
        webbrowser.open_new_tab("https://discord.gg/MN8JgqSAqT")
    def on_githubBtn_clicked(self):
        webbrowser.open_new_tab("https://github.com/leminlimez/Nugget")
    def on_bigNuggetBtn_clicked(self):
        webbrowser.open_new_tab("https://cowabun.ga")