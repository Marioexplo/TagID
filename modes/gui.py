import eyed3
from os import path as Path, scandir
from PySide6.QtWidgets import (QApplication, QScrollArea, QWidget, QVBoxLayout, QFrame, 
                               QHBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog)
from PySide6.QtCore import Qt, QTimer
import PySide6.QtGui as Gui
from subprocess import Popen as process

app = QApplication([])

scroller = QScrollArea(widgetResizable=True)
scroller.setFixedWidth(1195)
main = QWidget()
m_lay = QVBoxLayout()
m_lay.setAlignment(Qt.AlignmentFlag.AlignTop)

class Item(QFrame):
    empty = False

    def __init__(self, path: str):
        self.is_file = Path.isfile(path)
        if self.is_file:
            tag = eyed3.load(path)
            if tag == None:
                self.empty = True
                return
            tag = tag.tag
        super().__init__()
        self.setFixedHeight(40)
        self.set_white()
        self.path = path
        lay = QHBoxLayout()
        lay.setAlignment(Qt.AlignmentFlag.AlignLeft)
        lay.addWidget(QLabel(pixmap=Gui.QPixmap(Gui.QIcon.fromTheme(
                        "folder" if not self.is_file else "audio-x-generic"
                    ).pixmap(20, 20))))
        lay.addWidget(self.Label(Path.basename(path), 300))
        if self.is_file:
            lay.addWidget(Item.Label(Item.check_tag(tag.title), 200))
            lay.addWidget(Item.Label(Item.check_tag(tag.artist), 200))
            lay.addWidget(Item.Label(Item.check_tag(tag.album), 200))
        self.setLayout(lay)

    def set_white(self):
        self.setStyleSheet("background: white")

    class Label(QLabel):
        def __init__(self, text: str, width: int):
            super().__init__(text, alignment=Qt.AlignmentFlag.AlignLeft)
            self.setToolTip(text)
            self.setFixedWidth(width)
            self.setStyleSheet("color: black")

    def check_tag(tag: str | None) -> str:
        if tag is None:
            tag = ""
        return tag
    
    def enterEvent(self, _):
        self.setStyleSheet("background: #e4e4e4")
    
    def leaveEvent(self, _):
        self.set_white()
    
    def mousePressEvent(self, _):
        global last_pressed
        if not last_pressed is None:
            last_pressed.set_white()
        self.setStyleSheet("background: #0073e6")
        last_pressed = self

    def mouseDoubleClickEvent(self, _):
        if self.is_file:
            process(["xdg-open", self.path])
        else:
            Item.set_list(self.path)

    def set_list(path: str):
        win_lay.text.setText(path)
        while m_lay.count():
            m_lay.takeAt(0).widget().setParent(None)
        paths = [file.path for file in scandir(path)]
        paths.sort()
        for path in paths:
            if Path.basename(path)[0] == ".":
                continue
            item = Item(path)
            if not item.empty:
                m_lay.addWidget(item, alignment=Qt.AlignmentFlag.AlignTop)
last_pressed: Item = None

lay_header = QWidget()
lay_header.setStyleSheet("background: white")
lay_header.setFixedWidth(1080)
lay_header_lay = QHBoxLayout()
lay_header_lay.setAlignment(Qt.AlignmentFlag.AlignLeft)
lay_header_lay.addWidget(Item.Label("", 28))
lay_header_lay.addWidget(Item.Label("Name", 300))
lay_header_lay.addWidget(Item.Label("Title", 200))
lay_header_lay.addWidget(Item.Label("Artist", 200))
lay_header_lay.addWidget(Item.Label("Album", 200))
lay_header.setLayout(lay_header_lay)
m_lay.setMenuBar(lay_header)

class MainLayout(QVBoxLayout):
    text: QLineEdit
    timer = QTimer(interval=1000, singleShot=True)

    def __init__(self):
        super().__init__()
        self.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.timer.timeout.connect(self.de_path_error)
        lay = QHBoxLayout()
        def add_button(theme: str, desc: str, func, align: Qt.AlignmentFlag):
            button = QPushButton(Gui.QIcon.fromTheme(theme).pixmap(75, 75), "")
            button.setToolTip(desc)
            button.pressed.connect(func)
            lay.addWidget(button, alignment=align)
        add_button("go-up",
                   "Go to the upper folder",
                   lambda: Item.set_list(Path.dirname(self.text.text())),
                   Qt.AlignmentFlag.AlignLeft)

        self.text = QLineEdit("", maxLength=480)
        self.text.returnPressed.connect(self.set_path)
        lay.addWidget(self.text, Qt.AlignmentFlag.AlignCenter)
        self.text_back = self.text.palette().color(Gui.QPalette.ColorRole.Base).name(Gui.QColor.NameFormat.HexRgb)

        add_button(
            "system-file-manager",
            "Search with file manager",
            self.get_path,
            Qt.AlignmentFlag.AlignRight
        )
        self.addLayout(lay)

    def set_path(self):
        if Path.isdir(self.text.text()):
            Item.set_list(self.text.text())
            self.text.focusOutEvent()
        else:
            self.text.setStyleSheet("background: #ff3737")
            self.timer.start()
    
    def de_path_error(self):
        self.text.setStyleSheet("background: " + self.text_back)

    def get_path(self):
        Item.set_list(QFileDialog.getExistingDirectory(dir=self.text.text(), options=QFileDialog.Option.ShowDirsOnly))

main.setLayout(m_lay)
win = QWidget()
win.setWindowTitle("TagID     ")
win_lay = MainLayout()
scroller.setWidget(main)
win_lay.addWidget(scroller, alignment=Qt.AlignmentFlag.AlignHCenter)
win.setLayout(win_lay)

Item.set_list(Path.expanduser("~"))
win.show()
app.exec()
