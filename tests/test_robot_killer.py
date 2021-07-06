import pytest
import os
import signal
from src.robot_killer import RobotKiller


def test__robot_killer_init():
    robot_killer = RobotKiller()
    assert robot_killer.shutdown is False


@pytest.mark.parametrize("signal_sent", [signal.SIGINT, signal.SIGTERM])
def test__robot_killer_signal(signal_sent):
    robot_killer = RobotKiller()
    pid = os.getpid()
    os.kill(pid, signal_sent)
    assert robot_killer.shutdown is True
