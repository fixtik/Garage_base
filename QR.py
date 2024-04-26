#!/usr/bin/env python3
# подключаем модуль
import qrcode
from qrcode.image.pure import PyPNGImage

Name = 'Всеволжская районная организация общественной организации ВОА'
PersonalAcc = '40703810655410003535'
BankName = 'СЕВЕРО-ЗАПАДНЫЙ БАНК ПАО СБЕРБАНК'
BIC = '044030653'
CorrespAcc = '30101810500000000653'

LastName = 'Елизоветенков'
FirstName = 'Никита'
MiddleName = 'Александрович'

Sum = 10000  # сумма в копейках (рубли * 100)
Purpose = f'ПО 31, {LastName} {FirstName} {MiddleName}, ряд №гараж, за 2020'
PayeeINN = '4703035967'
KPP = '470301001'

qr = f'ST00011|Name={Name}|PersonalAcc={PersonalAcc}|BankName={BankName}|BIC={BIC}\
|CorrespAcc={CorrespAcc}|PayeeINN={PayeeINN}|LastName={LastName}|FirstName={FirstName}|MiddleName\
={MiddleName}|Purpose={Purpose}||Sum={Sum}'

img = qrcode.make(qr, image_factory=PyPNGImage)
img.save("qr.png")
