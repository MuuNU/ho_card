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



if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.UN_Name_Line.textChanged.connect(username_edited)


    sys.exit(app.exec_())
