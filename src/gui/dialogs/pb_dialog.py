import sqlite3

from PySide6.QtWidgets import QWizard, QWizardPage, QLabel, QVBoxLayout, QProgressBar, QSizePolicy
from PySide6.QtGui import QFont, QIcon, QPixmap
from PySide6.QtCore import QSize, Qt, QStandardPaths

from os import path, makedirs
from pymobiledevice3.lockdown import LockdownClient
from pymobiledevice3.services.mobilebackup2 import Mobilebackup2Service

from src.exceptions.nugget_exception import NuggetException
from src.tweaks.tweaks import tweaks, TweakID

class PosterBoardDBWizard(QWizard):
    def __init__(self, service_provider: LockdownClient, pbDBLbl: QLabel):
        super().__init__()
        self.service_provider = service_provider
        self.pbDBLbl = pbDBLbl
        self.backup_in_progress = False
        self.backup_complete = False

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
    def createPage1(self) -> QWizardPage:
        # information page telling the user about backing up
        page = QWizardPage()
        page.setTitle("Notice")
        # TODO: Option to not save backup
        message = QLabel("In order to get the file, Nugget needs to back up your device.\nThe backup will be deleted after Nugget finishes (NOT IMPLEMENTED YET).\n\nWould you like to continue?")
        layout = QVBoxLayout(page)
        layout.addWidget(message)
        page.setLayout(layout)
        return page
    
    def update_progress_bar(self, percent):
        print(f'backup progress: {percent}')
        self.progressBar.setValue(int(percent))
        self.backupInfoLbl.setText(f'Backing up...  {percent:6.1f}%')
    
    def createBackupProgPage(self) -> QWizardPage:
        # show the progress bar of the backup
        page = QWizardPage()
        page.setTitle("Backing Up Device...")
        layout = QVBoxLayout(page)
        layout.addWidget(self.backupInfoLbl)
        layout.addWidget(self.progressBar)
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
    
    # OVERWRITTEN FUNCTIONS
    def initializePage(self, id):
        if id == 1:
            # start the backup
            try:
                # disable next button until backup is done
                self.setButtonLayout([QWizard.WizardButton.CancelButton, QWizard.WizardButton.Stretch])
                self.backup_in_progress = True

                app_data_path = path.join(QStandardPaths.writableLocation(QStandardPaths.AppDataLocation), 'Backups')
                if not path.exists(app_data_path):
                    makedirs(app_data_path)
                backup_client = Mobilebackup2Service(self.service_provider)
                backup_folder = path.join(app_data_path, self.service_provider.udid)
                # check if a full backup is needed (makes it faster)
                needs_full = False
                if path.exists(backup_folder):
                    files_to_verify = ["Info.plist", "Manifest.db", "Manifest.plist", "Status.plist"]
                    for file in files_to_verify:
                        if not path.exists(path.join(backup_folder, file)):
                            needs_full = True
                            break
                backup_client.backup(full=needs_full, backup_directory=app_data_path, progress_callback=self.update_progress_bar)

                # get the file, reading the sqlite db first to get the file id
                self.backupInfoLbl.setText("Getting the file...")
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
                if not tweaks[TweakID.PosterBoard].config_manager.update_database_file(db_file_path, self.service_provider.udid):
                    raise NuggetException("The database is not of the correct format!")
                self.pbDBLbl.setText("sqlite: Selected")

                # re-enable next button
                self.backupInfoLbl.setText("Success!") # TODO: Place this somewhere else so that we can call self.next()
                self.setButtonLayout([QWizard.WizardButton.Stretch, QWizard.WizardButton.NextButton])
            except Exception as e:
                self.backupInfoLbl.setText("Backup Failed!")
                print(repr(e))
        return super().initializePage(id)
    
    # def isComplete(self):
    #     # need to emit completeChanged() every time a different value is returned
    #     # this should be for the page not the QWizard itself
    #     return not self.backup_started or self.backup_complete