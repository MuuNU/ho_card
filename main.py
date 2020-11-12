import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from ui.UI import Ui_MainWindow
import app.GenerateName as gn
import app.userOptions as uo
import app.rc_api as rc


def rocket_chat_init(rocket_chat_domain):
    admin_login = 'admin'
    admin_password = '19852001Ff'
    admin_token, admin_id = rc.login(admin_login, admin_password, rocket_chat_domain)
    return admin_token, admin_id


def init_list(admin_token, admin_id):
    group_name, group_id, group_count = rc.channels_list(admin_token, admin_id, rocket_chat_domain)
    global group_dict
    group_dict = {}
    for i in range(group_count):
        ui.RC_Groups_List.addItem(group_name[i])
        group_dict.update({group_name[i]:group_id[i]})


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
    current_item_row = ui.RC_Groups_List.currentRow()
    current_item_name = ui.RC_Groups_List.currentItem()
    ui.RC_Groups_List.takeItem(current_item_row)
    ui.RC_Groups_List_2.addItem(current_item_name)


def group_delete():
    current_item_row = ui.RC_Groups_List_2.currentRow()
    current_item_name = ui.RC_Groups_List_2.currentItem()
    ui.RC_Groups_List_2.takeItem(current_item_row)
    ui.RC_Groups_List.addItem(current_item_name)


def current_groups():
    groups_to_add_list = []
    for i in range (ui.RC_Groups_List_2.count()):
        current_name = ui.RC_Groups_List_2.item(i).text()
        groups_to_add_list.append(group_dict[current_name])
    return groups_to_add_list


def rc_create_user():
    new_user_login = ui.RC_Login_Line.text()
    new_user_name = ui.UN_Name_Line.text()
    new_user_password = ui.RC_Pass_Line.text()
    new_user_email = ui.EM_Line.text()
    user_id, user_name = rc.new_user(admin_token, admin_id, new_user_name, new_user_email, new_user_password, new_user_login, rocket_chat_domain)
    groups_to_add_list = current_groups()
    rc.add_to_groups(admin_token, admin_id, groups_to_add_list, user_id, rocket_chat_domain)


def username_edited():
    new_user_login = gn.genlogin(ui.UN_Name_Line.text())
    new_user_password = gn.convertPwd(ui.UN_Name_Line.text())
    ui.RC_Login_Line.setText(new_user_login)
    ui.RC_Pass_Line.setText(new_user_password)
    ui.EM_Line.setText(new_user_login + '@7-time.ru')
    ui.EM_Pass_Line.setText(new_user_password)


def rc_un_checkbox():
    if (ui.RC_Login_CheckBox.isChecked()):
        ui.RC_Login_Line.setEnabled(True)
    else:
        ui.RC_Login_Line.setEnabled(False)


def rc_pw_checkbox():
    if (ui.RC_Password_checkBox.isChecked()):
        ui.RC_Pass_Line.setEnabled(True)
    else:
        ui.RC_Pass_Line.setEnabled(False)


def rd_init():



if __name__ == "__main__":
    rocket_chat_domain = 'https://muunull.rocket.chat'
    admin_token, admin_id = rocket_chat_init(rocket_chat_domain)
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    init_list(admin_token, admin_id)
    bnd = binds()
    rd_init()
    sys.exit(app.exec_())
