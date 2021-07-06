import sys
import signal


class RobotKiller:
    shutdown = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.set_shutdown)
        signal.signal(signal.SIGTERM, self.set_shutdown)

    def set_shutdown(self, sig, frame):
        self.shutdown = True
