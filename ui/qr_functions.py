import qrcode
from dataclasses import dataclass
from qrcode.image.pure import PyPNGImage

from ui.qr_bankInfo import Ui_BankInfo
import ui.validators
import ui.css
from PySide6 import QtCore, QtWidgets, QtGui


class QrBankInfo_frontend(QtWidgets.QWidget):
    def __init__(self, db, parent=None):
        super().__init__(parent)

        self.ui = Ui_BankInfo()
        self.ui.setupUi(self)
        self.db = db  # db-connector

        # переменные класса
        self.css = ui.css  # для красоты

        self.initUi()

    def initUi(self):
        """Инициализация интерфейса"""
        self.setFixedWidth(400)

        # валидаторы
        self.ui.PersonalAcc_lineEdit.setValidator(ui.validators.onlyNumValidator())
        self.ui.BIC_lineEdit.setValidator(ui.validators.onlyNumValidator())
        self.ui.CorrespAcc_lineEdit.setValidator(ui.validators.onlyNumValidator())
        self.ui.PayeeINN_lineEdit.setValidator(ui.validators.onlyNumValidator())
        self.ui.KPP_lineEdit.setValidator(ui.validators.onlyNumValidator())

        # add a little bit of spice
        self.css.SetIcon.icon(self, window_icon=1)


Name = 'Всеволжская районная организация общественной организации ВОА'
PersonalAcc = '40703810655410003535'
BankName = 'СЕВЕРО-ЗАПАДНЫЙ БАНК ПАО СБЕРБАНК'
BIC = '044030653'
CorrespAcc = '30101810500000000653'

LastName = 'Елизоветенков'
FirstName = 'Никита'
MiddleName = 'Александрович'
# {LastName} {FirstName} {MiddleName},
Sum = 10000  # сумма в копейках (рубли * 100)
Purpose = f'ПО 31,ряд №гараж, за 2020'
PayeeINN = '4703035967'
KPP = '470301001'

qr = f'ST00011|Name={Name}|PersonalAcc={PersonalAcc}|BankName={BankName}|BIC={BIC}\
|CorrespAcc={CorrespAcc}|PayeeINN={PayeeINN}|LastName={LastName}|FirstName={FirstName}|MiddleName\
={MiddleName}|Purpose={Purpose}||Sum={Sum}'

img = qrcode.make(qr, image_factory=PyPNGImage)
img.save("qr.png")


@dataclass
class paymentInfo:
    id: str = ''
    Name: str = ''
    PersonalAcc: str = ''
    BankName: str = ''
    BIC: str = ''
    CorrespAcc: str = ''
    PayeeINN: str = ''
    KPP: str = ''
