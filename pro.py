import libusb_package
import usb.core
import usb.backend.libusb1

def checker(title: str):
    try:
        libusb1_backend = usb.backend.libusb1.get_backend(find_library=libusb_package.find_library)
        devices = usb.core.find(find_all=True, backend=libusb1_backend)
        for device in devices:
            try:
                if f"{device.idVendor:04x}:{device.idProduct:04x}" == title:
                    return True
            except:
                continue
    except Exception as e:
        print(e)

    return False

