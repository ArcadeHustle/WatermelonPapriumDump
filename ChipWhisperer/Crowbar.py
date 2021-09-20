#!/opt/homebrew/bin/python3
# https://circuitcellar.com/research-design-hub/design-solutions/voltage-fault-injection-on-a-modern-rpi-sbc/
#
# Simple crowbar example from Colin O'Flynn

import sys
import chipwhisperer as cw
scope = cw.scope()

scope.clock.clkgen_freq = 100E6
scope.glitch.output = "enable_only"
scope.glitch.clk_src = "clkgen"
scope.io.glitch_hp = True
scope.clock.reset_dcms()

# Set glitch width here
scope.glitch.repeat = int(sys.argv[1])

# Call this to insert glitches
while 1==1:
	scope.glitch.manual_trigger()
	print("xX",end = '', flush=True)

