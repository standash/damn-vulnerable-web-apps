#!/usr/bin/env python3

import sys, os.path
from modules.Engine import Engine

app_name = "honeypot"

def print_usage():
    print("\nUSAGE: ./run.py [app_name] [guest_port] [host_port]")
    print("EXAMPLE: ./run.py xssstored 8888 80\n")
    sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv[1:]) != 3:
        print_usage()

    app_name = sys.argv[1]
    guest_port = sys.argv[2]
    host_port = sys.argv[3]

    engine = Engine(app_name, guest_port, host_port)
    try:
        engine.run()
    except Exception as e:
        print("[ERROR]: {}".format(e))
