echo "reset halt" | nc localhost 4444
echo "flash read_bank 0 /tmp/file" | nc localhost 4444
