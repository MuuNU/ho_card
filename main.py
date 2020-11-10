import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from ui.UI import Ui_MainWindow
import app.GenerateName as gn
import app.userOptions as uo
import pprint
import app.rc_api as rcapi

def init_list(token, id):
    gname, gid, gcount = rcapi.channels_list(token, id)
    for i in range(gcount):
        ui.RC_Groups_List.addItem(gname[i])

def binds():
    ui.RC_Login_Line.setEnabled(False)
    ui.RC_Pass_Line.setEnabled(False)
    ui.UN_Name_Line.textChanged.connect(username_edited)
    ui.RC_Login_CheckBox.stateChanged.connect(rc_un_checkbox)
    ui.RC_Password_checkBox.stateChanged.connect(rc_pw_checkbox)
    ui.RC_Add_Button.clicked.connect(group_add)
    ui.RC_Delete_Button.clicked.connect(group_delete)
    ui.RC_Create_Button.clicked.connect(rc_create_user)
    return True

def group_add():
    itemR = ui.RC_Groups_List.currentRow()
    Item = ui.RC_Groups_List.currentItem()
    ui.RC_Groups_List.takeItem(itemR)
    ui.RC_Groups_List_2.addItem(Item)

def group_delete():
    itemR = ui.RC_Groups_List_2.currentRow()
    Item = ui.RC_Groups_List_2.currentItem()
    ui.RC_Groups_List_2.takeItem(itemR)
    ui.RC_Groups_List.addItem(Item)

def current_groups():
    list = []
    for i in range(ui.RC_Groups_List_2.count()):
        list.append(ui.RC_Groups_List_2.item(i).text())
    return list

def rc_create_user():
    new_login = ui.RC_Login_Line.text()
    new_username = ui.UN_Name_Line.text()
    new_password = ui.RC_Pass_Line.text()
    new_email = ui.EM_Line.text()
    grup_list = current_groups()
    print(token)
    print(id)
    rcapi.new_user(token, id, new_username, new_email, new_password, new_login)


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
    token, id = rcapi.login('testA', 'testAdmin123')
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    init_list(token, id)
    bnd = binds()
    sys.exit(app.exec_())
