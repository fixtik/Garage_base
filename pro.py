import usb.util


def checker(title: str):
    idVendor, idProduct = title.split(':')
    try:
        devices = usb.core.find(find_all=True)
        for device in devices:
            try:
                if f"{device.idVendor:04x}:{device.idProduct:04x}" == title:
                    return True
            except:
                continue
    finally:
        pass
    # dev = usb.core.find(idVendor=idVendor, idProduct=idProduct)
    return False

# devices = usb.core.find(find_all=True)
#
# # Iterate through the devices and print their information
# for device in devices:
#     try:
#         print(f"Device ID: {device.idVendor:04x}:{device.idProduct:04x}")
#         print(f"Serial Number: {usb.util.get_string(device, device.iSerialNumber)}")
#     except:
#         print()
#

# DEVICE ID :cb20
# 048d:04d2
