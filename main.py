from process import Process
from state import ProcessState
import random
import time

def simulate_process_lifecycle(process_id):
    proc = Process(process_id)
    proc.run()

if __name__ == "__main__":
    for i in range(3):  # Simulating 3 processes
        simulate_process_lifecycle(i)