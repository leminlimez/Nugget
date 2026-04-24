import asyncio
import sqlite3

from PySide6.QtWidgets import QWizard, QWizardPage, QLabel, QVBoxLayout, QProgressBar, QSizePolicy, QCheckBox
from PySide6.QtCore import QSize, Qt, QStandardPaths

from os import path, makedirs
from pymobiledevice3.lockdown import create_using_usbmux
from pymobiledevice3.services.mobilebackup2 import Mobilebackup2Service
from shutil import rmtree

from src.exceptions.nugget_exception import NuggetException
from src.gui.thread_workers.pb_worker import PBDBThread
from src.tweaks.tweaks import tweaks, TweakID

class PosterBoardDBWizard(QWizard):
    def __init__(self, udid: str, pbDBLbl: QLabel, update_savedIds_list=lambda x: None):
        super().__init__()
        self.udid = udid
        self.pbDBLbl = pbDBLbl
        self.backup_in_progress = False
        self.delete_backup_when_done = False
        self.backup_successful = False
        self.update_savedIds_list = update_savedIds_list

        # only show cancel and next/finish buttons
        self.setOption(QWizard.WizardOption.NoBackButtonOnStartPage, True)
        self.setOption(QWizard.WizardOption.NoBackButtonOnLastPage, True)
        self.setButtonLayout([QWizard.WizardButton.CancelButton, QWizard.WizardButton.Stretch, QWizard.WizardButton.NextButton])

        # progress bar for the backup progress
        self.backupInfoLbl = QLabel("Please enter your password on your device to continue")
        self.progressBar = QProgressBar()
        sizePolicy = QSizePolicy()
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QSize(250, 0))
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)

        self.addPage(self.createPage1())
        self.addPage(self.createBackupProgPage())
        self.addPage(self.createFinalPage())

        self.setWindowTitle("Fetch Database File")

    # PAGES
    def on_deleteBackupChk_toggled(self, enabled: bool):
        self.delete_backup_when_done = enabled
    def createPage1(self) -> QWizardPage:
        # information page telling the user about backing up
        page = QWizardPage()
        page.setTitle("Notice")
        message = QLabel("In order to get the file, Nugget needs to back up your device.")
        delBkLbl = QLabel("If you do not delete the backup, this process will be faster when getting the file again.")
        delBkChk = QCheckBox("Delete Backup When Complete")
        delBkChk.toggled.connect(self.on_deleteBackupChk_toggled)
        contLbl = QLabel("\nWould you like to continue?")
        layout = QVBoxLayout(page)
        layout.addWidget(message)
        layout.addWidget(delBkLbl)
        layout.addWidget(delBkChk)
        layout.addWidget(contLbl)
        page.setLayout(layout)
        return page
    
    def createFinalPage(self) -> QWizardPage:
        # just say whether backup was successful
        page = QWizardPage()
        page.setTitle("Backup Complete")
        message = QLabel("Successfully got the file")
        layout = QVBoxLayout(page)
        layout.addWidget(message)
        page.setLayout(layout)
        return page
    
    def createBackupProgPage(self) -> QWizardPage:
        # show the progress bar of the backup
        page = QWizardPage()
        page.setTitle("Backing Up Device...")
        layout = QVBoxLayout(page)
        layout.addWidget(self.backupInfoLbl)
        layout.addWidget(self.progressBar)
        page.setLayout(layout)
        return page
    
    def update_progress_bar(self, percent):
        print(f'backup progress: {percent}')
        if percent == 0.0:
            self.backupInfoLbl.setText("Preparing device for backup...")
        else:
            self.progressBar.setValue(int(percent))
            self.backupInfoLbl.setText(f'Backing up...  {percent:6.1f}%')

    def update_progress_lbl(self, txt: str):
        # hacky workaround
        if txt.startswith('sqlite'):
            self.pbDBLbl.setText(txt)
        else:
            self.backupInfoLbl.setText(txt)

    def finish_backup_thread(self):
        if self.backup_successful:
            self.update_savedIds_list()
            self.setButtonLayout([QWizard.WizardButton.Stretch, QWizard.WizardButton.NextButton])
        self.backup_in_progress = False
        # self.next()
    
    def start_device_backup(self, update_label=lambda x: None, update_progress=lambda x: None):
        asyncio.run(self._start_device_backup(update_label, update_progress))
    async def _start_device_backup(self, update_label=lambda x: None, update_progress=lambda x: None):
        try:
            app_data_path = path.join(QStandardPaths.writableLocation(QStandardPaths.AppDataLocation), 'Backups')
            if not path.exists(app_data_path):
                makedirs(app_data_path)
            service_provider = await create_using_usbmux(serial=self.udid)
            backup_client = Mobilebackup2Service(service_provider)
            backup_folder = path.join(app_data_path, self.udid)
            # check if a full backup is needed (makes it faster)
            needs_full = False
            if path.exists(backup_folder):
                files_to_verify = ["Info.plist", "Manifest.db", "Manifest.plist", "Status.plist"]
                for file in files_to_verify:
                    if not path.exists(path.join(backup_folder, file)):
                        needs_full = True
                        break
            await backup_client.backup(full=needs_full, backup_directory=app_data_path, progress_callback=update_progress)
            await service_provider.close()

            # get the file, reading the sqlite db first to get the file id
            update_label("Getting the file...")
            db_path = path.join(backup_folder, "Manifest.db")
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute(
                "SELECT fileID FROM Files WHERE domain = ? AND relativePath = ?",
                ("AppDomain-com.apple.PosterBoard",
                    "Library/Application Support/PRBPosterExtensionDataStore/61/PBFPosterExtensionDataStoreSQLiteDatabase.sqlite3"))
            fileID = cursor.fetchone()
            conn.close()
            if fileID is None or len(fileID) == 0:
                raise NuggetException("Could not find sqlite database in the backup!")
            fileID = fileID[0]
            db_file_path = path.join(backup_folder, fileID[:2], fileID)
            if not path.exists(db_file_path):
                raise NuggetException("The database file doesn't exist!")
            if not tweaks[TweakID.PosterBoard].config_manager.update_database_file(db_file_path, self.udid):
                raise NuggetException("The database is not of the correct format!")
            update_label("sqlite: Selected")

            # delete backup files if wanted
            if self.delete_backup_when_done:
                update_label("Deleting backup...")
                rmtree(backup_folder)

            # re-enable next button
            self.backup_successful = True
            update_label("Success!") # TODO: Place this somewhere else so that we can call self.next()
            # self.setButtonLayout([QWizard.WizardButton.Stretch, QWizard.WizardButton.NextButton])
        except Exception as e:
            update_label("Backup Failed!")
            print(repr(e))
    
    # OVERWRITTEN FUNCTIONS
    def initializePage(self, id):
        if id == 1:
            # start the backup
            # disable next button until backup is done
            self.setButtonLayout([QWizard.WizardButton.CancelButton, QWizard.WizardButton.Stretch])
            self.backup_in_progress = True
            self.worker_thread = PBDBThread(backup_function=self.start_device_backup)
            self.worker_thread.progress.connect(self.update_progress_bar)
            self.worker_thread.infoLbl.connect(self.update_progress_lbl)
            # self.worker_thread.alert.connect(self.alert_message)
            self.worker_thread.finished.connect(self.finish_backup_thread)
            self.worker_thread.finished.connect(self.worker_thread.deleteLater)
            self.worker_thread.start()
        return super().initializePage(id)
    
    # def isComplete(self):
    #     # need to emit completeChanged() every time a different value is returned
    #     # this should be for the page not the QWizard itself
    #     return not self.backup_started or self.backup_complete