import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from ui.UI import Ui_MainWindow
import app.GenerateName as gn


def username_edited(UN_Name_Line):
    lgn = gn.convert(UN_Name_Line)
    lgn = gn.genlogin(lgn)
    ui.RC_Login_Line.setText(lgn)
    pwd = gn.convertPwd(UN_Name_Line)
    ui.RC_Pass_Line.setText(pwd)

def un_checkbox(RC_Login_CheckBox):
    if (RC_Login_CheckBox == 0):
        ui.RC_Login_Line.setReadOnly(True)
    else:
        ui.RC_Login_Line.setReadOnly(False)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.UN_Name_Line.textChanged.connect(username_edited)
    ui.RC_Login_CheckBox.stateChanged.connect(un_checkbox)


    sys.exit(app.exec_())
