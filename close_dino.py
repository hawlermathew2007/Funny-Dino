import os

def create_close_signal():
    with open("close_signal.txt", "w") as f:
        f.write("close")

if os.path.exists('signal_activated.txt'):
    create_close_signal()