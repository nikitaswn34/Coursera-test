import usb.core
import usb.util

# find our device
dev = usb.core.find(idVendor=0x12D1, idProduct=0x107E)
#dev = usb.core.find(iSerialNumber="BRB3Y18721005288")
#USB\VID_12D1&PID_107E&MI_00
print (dev)
# was it found?
if dev is None:
    raise ValueError('Device not found')

# set the active configuration. With no arguments, the first
# configuration will be the active one
dev.set_configuration()

# get an endpoint instance
cfg = dev.get_active_configuration()
intf = cfg[(0,0)]

ep = usb.util.find_descriptor(
    intf,
    # match the first OUT endpoint
    custom_match = \
    lambda e: \
        usb.util.endpoint_direction(e.bEndpointAddress) == \
        usb.util.ENDPOINT_OUT)

assert ep is not None

# write the data
ep.write('test')
