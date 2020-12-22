from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from pymysql import *
from main_ui import *


class myApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        Ui_MainWindow.setupUi(self, self)
        try:
            self.db = connect(
                host="54.180.32.208",
                user="dev8_1",
                password="1234",
                db="dev8",
            )
            print("OK!")
        except:
            print("ERROR!")
            exit(1)

        self.cur = self.db.cursor()
        self.main()

    def main(self):
        self.cmd = "select * from command1"
        self.cur.execute(self.cmd)
        self.db.commit()
        self.data = self.cur.fetchall()
        for i in range(len(self.data)):
            print(self.data[i][0], self.data[i][1], self.data[i][2], self.data[i][3])

        self.tm = QTimer()
        self.tm.setInterval(500)
        self.tm.timeout.connect(self.run)
        self.tm.start()

    def closeEvent(self, event):
        self.db.close()

    def clickedGo(self):
        print("Go")
        nt = self.dt
        self.cmd = "update command1 set is_finish=0, time='" + nt + "' where cmd_string='go'"
        self.cur.execute(self.cmd)
        self.db.commit()
        self.text.appendPlainText("Datetime: {0}, Dir: {1}".format(nt, self.data[1][1]))

    def clickedMid(self):
        print("Mid")
        nt = self.dt
        self.cmd = "update command1 set is_finish=0, time='" + nt + "' where cmd_string='mid'"
        self.cur.execute(self.cmd)
        self.db.commit()
        self.text.appendPlainText("Datetime: {0}, Dir: {1}".format(nt, self.data[4][1]))

    def clickedLeft(self):
        print("Left")
        nt = self.dt
        self.cmd = "update command1 set is_finish=0, time='" + nt + "' where cmd_string='left'"
        self.cur.execute(self.cmd)
        self.db.commit()
        self.text.appendPlainText("Datetime: {0}, Dir: {1}".format(nt, self.data[5][1]))

    def clickedRight(self):
        print("Right")
        nt = self.dt
        self.cmd = "update command1 set is_finish=0, time='" + nt + "' where cmd_string='right'"
        self.cur.execute(self.cmd)
        self.db.commit()
        self.text.appendPlainText("Datetime: {0}, Dir: {1}".format(nt, self.data[0][1]))

    def clickedBack(self):
        print("Back")
        nt = self.dt
        self.cmd = "update command1 set is_finish=0, time='" + nt + "' where cmd_string='back'"
        self.cur.execute(self.cmd)
        self.db.commit()
        self.text.appendPlainText("Datetime: {0}, Dir: {1}".format(nt, self.data[2][1]))

    def run(self):
        qdt = QDateTime().currentDateTime()
        self.dt = qdt.toString("yyyy-MM-dd HH:mm:ss")

        self.sens = "select * from sensing1 order by time desc limit 1"
        self.cur.execute(self.sens)
        self.db.commit()
        sens_data = self.cur.fetchall()

        temp = sens_data[0][1]
        humi = sens_data[0][2]
        dist = sens_data[0][3]
        is_finish = sens_data[0][5]

        if is_finish == 0:
            self.sens = "update sensing1 set is_finish=1 where is_finish=0"
            self.cur.execute(self.sens)
            self.db.commit()
            sens_str = "Temp: {0}, Humi: {1}, Dist: {2}".format(temp, humi, dist)
            self.sens_text.appendPlainText(sens_str)

        print("#")


app = QApplication()
win = myApp()
win.show()
app.exec_()
