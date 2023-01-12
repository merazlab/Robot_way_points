
import time
import numpy as np

from mission_controller.mission_controller import MissionController
from mission_controller.simulated_robot import SimulatedRobot, SimulatedRobotWithCommunicationDelay


def test_normal_operation():

    simulated_robot = SimulatedRobotWithCommunicationDelay(np.array([2.0, 1.0]))

    controller = MissionController(simulated_robot)

    # set the first trajectory
    time.sleep(1)
    controller.set_trajectory(np.array([[4.0, 3.0], [5.0, 3.0]]))

    time.sleep(5)

    # now set a different trajectory before the first trajectory completes

    controller.set_trajectory(np.array([[3.0, 3.0], [5.0, 4.0]]))

    time.sleep(8)

    print("Test complete")

    exit(0)


if __name__ == "__main__":
    test_normal_operation()
