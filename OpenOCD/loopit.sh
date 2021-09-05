while true 
do
	FILE=/tmp/file # Firmware will dump here if successful. 
	if test -f "$FILE"; then
	    echo "$FILE exists."
	    exit
	else
	    ./getFlash.sh
	fi
done
