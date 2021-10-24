import sys
import webbrowser

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QMessageBox
from PyQt5.QtGui import QIcon
from designer.de_ui import Ui_MainWindow

import core
import config


class MyLabel(QLabel):
    def __init__(self, parent=None):
        super(MyLabel, self).__init__(parent)
        self.pos_value = (0, 0)

    def mousePressEvent(self, event):
        pos = event.pos()
        global_pos = self.mapToGlobal(pos)
        self.pos_value = (global_pos.x(), global_pos.y())
        self.setText(f'{self.pos_value[0]}, {self.pos_value[1]}')


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowIcon(QIcon(config.TITLE_ICON))   # set windows icon
        self._init_ui()
        self.my_thread = None   # Thread

    def _init_ui(self):
        self.setupUi(self)
        self.coordinate_label = MyLabel()
        self.add_layout.addWidget(self.coordinate_label)
        self.add_layout.setStretch(1, 10)

        # connect
        self.start_btn.clicked.connect(self.start)

        # menu
        self.menu_deam_help.triggered.connect(lambda: self.open_help(config.WEB_HELP))

    def start(self):
        print("%02d" % self.hour.value())
        user_set_time = f'{"%02d" % self.hour.value()}:{"%02d" % self.minute.value()}:{"%02d" % self.second.value()}'
        self.my_thread = core.MyThread(user_set_time, self.coordinate_label.pos_value)
        # set thread event
        self.my_thread.started.connect(lambda: self.start_btn.setText("在监控时间中...."))
        self.my_thread.finished.connect(lambda: QMessageBox.information(self, '点击成功', '点击成功', QMessageBox.Yes))
        self.my_thread.finished.connect(lambda: self.start_btn.setText("开始"))
        # start thread
        self.my_thread.start()

    @staticmethod
    def open_help(web_path):
        webbrowser.open_new(web_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())