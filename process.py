from state import ProcessState
import random
import time

class Process:
    def __init__(self, pid):
        self.pid = pid
        self.state = ProcessState.NEW
        print(f"Process {self.pid} created and is in {self.state.name} state.")

    def transition(self, new_state):
        print(f"Process {self.pid} transitioning from {self.state.name} to {new_state.name}.")
        self.state = new_state

    def run(self):
        self.transition(ProcessState.READY)
        time.sleep(random.uniform(0.1, 0.5))
        self.transition(ProcessState.RUNNING)
        time.sleep(random.uniform(0.2, 0.6))
        if random.choice([True, False]):
            self.transition(ProcessState.WAITING)
            time.sleep(random.uniform(0.3, 0.7))
            self.transition(ProcessState.READY)
        self.transition(ProcessState.TERMINATED)