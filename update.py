from os import path, mkdir
from editor import ProgramPath, GetBeta, currentSystem
from shutil import move, rmtree
from dirsync import sync
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from update_ui import Ui_Update
from subprocess import Popen
from requests import get, ConnectionError, Timeout
from zipfile import ZipFile

class Progress():
    def update(self, op_code, cur_count, max_count=None, message=''):
        if(op_code > 10): UpdateThread.progress.emit(cur_count/max_count*100)

class Download(QThread):
    progress = pyqtSignal(int)
    done = pyqtSignal()
    version = "null"

    def run(self):
        directory = ProgramPath+"/tmp"
        if(not path.exists(directory)): mkdir(directory)
        file = open(directory+"/downloaded.zip", "wb")
        with get("https://github.com/BenjaminHalko/WiiMusicEditorPlus/releases/download/"+self.version+"/WiiMusicEditorPlus-"+currentSystem+".zip",stream=True) as response:
            total =  int(response.headers['content-length'])
            downloaded = 0
            for i in response.iter_content(1024):
                downloaded+=len(i)
                file.write(i)
                UpdateThread.progress.emit(downloaded/total*100)

        file.close()

        zip = ZipFile(directory+"/downloaded.zip")
        zip.extractall(directory+"/downloaded")
        zip.close()

        move(directory+"/downloaded/WiiMusicEditorPlus.exe",directory+"/downloaded/Helper/Update/NewProgram.exe")
        sync(directory+"/downloaded",ProgramPath,"sync",purge=True,ignore=(r"settings.ini",r"Helper/Backup",r"WiiMusicEditorPlus.exe",r"Helper/Update/Version.txt",r"tmp"))
        rmtree(directory)
        UpdateThread.done.emit()

class UpdateWindow(QDialog,Ui_Update):
    def __init__(self,otherWindow,check):
        global UpdateThread
        super().__init__(None)
        self.otherWindow = otherWindow
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint,False)
        self.setWindowModality(Qt.ApplicationModal)

        if(check == False):
            check = CheckForUpdate()
            if(check == "null"):
                self.MainWidget.setCurrentIndex(2)

        self.version = check
        self.NewUpdate_Update.clicked.connect(self.startupdate)
        self.NewUpdate_Cancel.clicked.connect(self.close)
        self.NoUpdate_Button.clicked.connect(self.close)

        self.show()
        self.exec()
        
    def startupdate(self):
        global UpdateThread
        self.MainWidget.setCurrentIndex(1)
        UpdateThread = Download()
        UpdateThread.version = self.version
        UpdateThread.progress.connect(self.reportProgress)
        UpdateThread.done.connect(self.restart)
        UpdateThread.start()

    def reportProgress(self,value):
        self.Update_Progress.setValue(value)

    def restart(self):
        file = open(ProgramPath+"/Helper/Update/Version.txt","w")
        file.write(self.version)
        file.close()
        if(currentSystem == "Windows"):
            Popen(ProgramPath+'/Helper/Update/Update.bat')
        else:
            Popen(ProgramPath+'/Helper/Update/Update.sh')
        self.close()
        self.otherWindow.close()

def CheckForUpdate():
    if(path.exists(ProgramPath+"/Helper/Update/Version.txt")):
        file = open(ProgramPath+"/Helper/Update/Version.txt")
        version = file.read()
        file.close()
        try:
            tag = GetReleaseTag()
            if(tag != version): return tag
            else: return "null"
        except (ConnectionError, Timeout):
            return "null"
    else:
        try:
            file = open(ProgramPath+"/Helper/Update/Version.txt","w")
            file.write(GetReleaseTag())
            file.close()
            return "null"
        except (ConnectionError, Timeout):
            return "null"
        
def GetReleaseTag():
    data = get("https://api.github.com/repos/BenjaminHalko/WiiMusicEditorPlus/releases").json()
    i = 0
    if(not GetBeta()):
        while (data[i]["prerelease"]): i += 1
    return data[i]["tag_name"]