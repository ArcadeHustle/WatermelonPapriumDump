import sys
PapriumNoXOR = bytearray(open("S29GL064N90BFI03@BGA48_20210924_142237_DECODED.BIN", 'rb').read())
size = len(PapriumNoXOR) 
FlippedBitPaprium = bytearray(size)

for i in range(size):
	FlippedBitPaprium[i] = PapriumNoXOR[i] ^ 0xff

open("S29GL064N90BFI03@BGA48_20210924_142237_DECODED_FLIPPED.BIN", 'wb').write(FlippedBitPaprium)


