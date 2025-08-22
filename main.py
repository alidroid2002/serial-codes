import argparse, sys, time
import serial
from serial.tools import list_ports

def list_serial_ports():
    ports = list_ports.comports()
    for i, p in enumerate(ports):
        print(f"[{i}] {p.device}  {p.description}")
    return ports

def read_for(ser, seconds=2.0):
    """Read and print any lines available for up to `seconds`."""
    end = time.time() + seconds
    while time.time() < end:
        line = ser.readline()  # reads until \n or timeout
        if not line:
            continue
        try:
            print(line.decode("utf-8", errors="replace").rstrip())
        except UnicodeDecodeError:
            print(line)

def main():
    parser = argparse.ArgumentParser(description="Simple serial CLI")
    parser.add_argument("--port", help="COM port, e.g., COM5 or /dev/ttyUSB0")
    parser.add_argument("--baud", type=int, default=9600)
    args = parser.parse_args()

    ports = list_serial_ports()
    if not ports and not args.port:
        print("No serial ports found. Plug in your Arduino and try again.")
        sys.exit(1)

    port = args.port
    if not port:
        idx = input("Select port index: ").strip()
        try:
            port = ports[int(idx)].device
        except Exception:
            print("Invalid selection.")
            sys.exit(1)

    try:
        ser = serial.Serial(port, args.baud, timeout=0.1)
        print(f"Opened {port} @ {args.baud}. Type commands, blank line to just read, 'quit' to exit.")
        # Read initial banner lines (like "READY")
        read_for(ser, 1.0)

        while True:
            try:
                s = input("> ")
            except (EOFError, KeyboardInterrupt):
                break
            if s.lower() in ("quit", "exit"):
                break
            if s.strip():
                ser.write((s.strip() + "\n").encode("utf-8"))
            # After sending (or blank), harvest anything for a bit:
            read_for(ser, 1.0)

    except serial.SerialException as e:
        print(f"Serial error: {e}")
    finally:
        try:
            ser.close()
            print("Port closed.")
        except:
            pass

if __name__ == "__main__":
    main()
