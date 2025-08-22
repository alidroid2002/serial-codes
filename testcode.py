import time, sys
import serial

def read_for(ser, seconds=2.0):
    """Read and print any lines available for up to `seconds`."""
    end = time.time() + seconds
    while time.time() < end:
        print(f"[DEBUG] Waiting for line... (time left: {round(end - time.time(),2)}s)")
        
        line = ser.readline()  # waits until newline or timeout
        print(type(line))
        print(f"[DEBUG] Raw bytes read: {line}")   # show raw data

        if not line:
            print("[DEBUG] No data received, retrying...")
            continue

        try:
            decoded = line.decode("utf-8", errors="replace").rstrip()
            print(f"[DEBUG] Decoded line: {decoded}")
        except UnicodeDecodeError as e:
            print(f"[ERROR] Decode failed: {e}")
            print("[DEBUG] Fallback raw line:", line)


def main():
    ser = serial.Serial('COM6',9600, timeout=0.1)
    print(ser)
    read_for(ser, 10.0)

    while True:
        try:
            s = input("> ")
        except KeyboardInterrupt:
            print(KeyboardInterrupt)
            break

if __name__ == "__main__":
    main()