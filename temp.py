import serial, time

try:
    ser = serial.Serial("COM6", 9600, timeout=0.1)
    print(f"{ser.name} found.")
    
    while True:
        line = ser.readline()
        print(line)

        if line:
            linestr = line.decode("utf-8").strip()
            print("Decoded: ", linestr)

        else:
            print("Nothing")
        time.sleep(0.1)

except serial.SerialException as e:
    print("Port error: ",e)
except KeyboardInterrupt:
    print("Terminated")
finally:
    if ser in locals() and ser.is_open:
        ser.close()
        print("Port closed.")