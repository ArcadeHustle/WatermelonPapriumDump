echo "reset halt" | nc localhost 4444
echo "stm32f1x lock 0" | nc localhost 4444
echo "reset halt" | nc localhost 4444
echo "exit" | nc localhost 4444
