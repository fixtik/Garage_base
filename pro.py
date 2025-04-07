import libusb_package
import usb.core
import usb.backend.libusb1


def checker(title: str):
    idVendor, idProduct = title.split(':')
    try:
        libusb1_backend = usb.backend.libusb1.get_backend(find_library=libusb_package.find_library)
        devices = usb.core.find(find_all=True, backend=libusb1_backend)
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

# libusb1_backend = usb.backend.libusb1.get_backend(find_library=libusb_package.find_library)
# # devices = usb.core.find(find_all=True)
#
# # Iterate through the devices and print their information
# for device in usb.core.find(find_all=True, backend=libusb1_backend):
#     try:
#         print(f"Device ID: {device.idVendor:04x}:{device.idProduct:04x}")
#         print(f"Serial Number: {usb.ut    il.get_string(device, device.iSerialNumber)}")
#     except:
#         print()

#
# DEVICE ID :cb20
# 048d:04d2
