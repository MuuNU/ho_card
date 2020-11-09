import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from ui.UI import Ui_MainWindow
import app.GenerateName as gn
import app.userOptions as uo


def binds():
    ui.RC_Login_Line.setEnabled(False)
    ui.RC_Pass_Line.setEnabled(False)
    ui.UN_Name_Line.textChanged.connect(username_edited)
    ui.RC_Login_CheckBox.stateChanged.connect(rc_un_checkbox)
    ui.RC_Password_checkBox.stateChanged.connect(rc_pw_checkbox)
    ui.RC_Create_Button.clicked.connect(rc_create_user)
    return True


def rc_create_user():
    new_login = ui.RC_Login_Line.text()
    print(new_login)
    new_username = ui.UN_Name_Line.text()
    print(new_username)
    new_password = ui.RC_Pass_Line.text()
    print(new_password)
    new_email = ui.EM_Line.text()
    print(new_email)
    uo.new(new_login, new_username, new_password, new_email)


def username_edited(UN_Name_Line):
    lgn = gn.convert(UN_Name_Line)
    lgn = gn.genlogin(lgn)
    ui.RC_Login_Line.setText(lgn)
    pwd = gn.convertPwd(UN_Name_Line)
    ui.RC_Pass_Line.setText(pwd)
    eml = (lgn + '@7-time.ru')
    ui.EM_Line.setText(eml)
    ui.EM_Pass_Line.setText(pwd)

def rc_un_checkbox(RC_Login_CheckBox):
    if (RC_Login_CheckBox == 0):
        ui.RC_Login_Line.setEnabled(False)
    else:
        ui.RC_Login_Line.setEnabled(True)

def rc_pw_checkbox(RC_Password_checkBox):
    if (RC_Password_checkBox == 0):
        ui.RC_Pass_Line.setEnabled(False)
    else:
        ui.RC_Pass_Line.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    bnd = binds()

    sys.exit(app.exec_())
