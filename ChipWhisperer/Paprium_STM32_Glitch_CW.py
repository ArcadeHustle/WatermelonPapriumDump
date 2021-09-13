#!/opt/homebrew/bin/python3

PLATFORM = 'CW308_STM32F0'
#PLATFORM = 'CW308_STM32F1'
#PLATFORM = 'CW308_STM32F2'
#PLATFORM = 'CW308_STM32F3'
#PLATFORM = 'CW308_STM32F4'
SCOPETYPE = 'OPENADC'

import chipwhisperer as cw
import usb
from chipwhisperer.hardware.naeusb.programmer_stm32fserial import supported_stm32f

try:
    try:
        if not scope.connectStatus:
            scope.con()
    except NameError:
        scope = cw.scope()

    target_type = cw.targets.SimpleSerial2

    try:
        target = cw.target(scope, target_type)
    except IOError:
        print("INFO: Caught exception on reconnecting to target - attempting to reconnect to scope first.")
        print("INFO: This is a work-around when USB has died without Python knowing. Ignore errors above this line.")
        scope = cw.scope()
        target = cw.target(scope, target_type)
except:
    if usb.__version__ < '1.1.0':
        print("-----------------------------------")
        print("Unable to connect to chipwhisperer. pyusb {} detected (>= 1.1.0 required)".format(usb.__version))
        print("-----------------------------------")
    raise

print("INFO: Connected to ChipWhispererp")

# Check for presence of STM32 chipset
if (PLATFORM == 'CW308_STM32F0' or PLATFORM == 'CW308_STM32F1' or PLATFORM == 'CW308_STM32F2'  or PLATFORM == 'CW308_STM32F3' or PLATFORM == 'CW308_STM32F4' ):
    try:
        target = cw.target(scope, cw.targets.SimpleSerial)
        scope.default_setup()

        prog = cw.programmers.STM32FProgrammer()
        prog.scope = scope
        prog._logging = None
        prog.open()
        prog.find()
    except e:
        print("fail gracefully " + e)
# Disconnect, and allow reuse by another instance
scope.dis()
target.dis()

