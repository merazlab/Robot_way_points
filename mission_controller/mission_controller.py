
import numpy as np
import time
from threading import Thread


class MissionController:

    def __init__(self, robot):
        print("Creating MissionController!")

        thread_poll_position = Thread(target=self._poll_position, daemon=True)

        thread_poll_position.start()

        self.robot = robot
        self.current_waypoint_idx = 0
        self.trajectory = ()
        
    def set_trajectory(self, trajectory):
        self.current_waypoint_idx = 0
        self.trajectory = trajectory

    def _poll_position(self):

        time.sleep(1)

        position = self.robot.get_position()
        # print("Robot current Pose-", position)
        # if self.trajectory == None:
        #     pass
        if len(self.trajectory) == 0:
            print("Robot Stop")
            
        elif self.current_waypoint_idx == 0:
            self._send_navigation_command()
            self.current_waypoint_idx += 1

        elif np.all(position == self.trajectory[0]) and self.current_waypoint_idx == 1  :
            self._send_navigation_command()
            self.current_waypoint_idx += 1

        self._poll_position()

    def _send_navigation_command(self):

        print(f"Sending waypoint {self.current_waypoint_idx}")
        self.robot.set_navigation_command(self.trajectory[self.current_waypoint_idx])
        
