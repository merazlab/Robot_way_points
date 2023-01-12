# Robot_way_points

This is a code debugging/refactoring exercise, it is meant to take 1-2 hours.

The program is intended as a simple service to release waypoints one at a time to a robot in a way that allows changes/cancellations. 

For example, the process could be:

* The robot begins with coordinates (2, 1). 
* We submit a trajectory with points ((4, 3), (5, 3)).
* The robot starts to move to (4, 3).
* We submit a trajectory with points ((3, 3), (5, 4)).
* The robot starts to move to (3, 3) instead of (4, 3).
* The robot arrives at (3, 3), and starts to move towards (5, 4).
* The robot receives a trajectory with points ().
* The robot stops.

(In the real world this might be done with something like ROS, but we minimized external dependencies for this exercise.)

Task:

* Expand the test set as needed.
* Debug the program to resolve inconsistencies.
* Add basic input validation to improve robustness.
* Refactor the code to improve readability, maintainability.


Scoring is based on:

* How many bugs/other issues are fixed.
* Overall structure of the final code.

It does not depend on adding new features, using a particular testing framework, adding very detailed documentation etc.


Notes:

* Currently it is based on python threading (with many bugs added), but you can rewrite using whatever methodology 
  you're comfortable with (e.g. async python).

* If you are unfamiliar with python, feel free to write an equivalent program in a language of your choosing.

————————————————————————————————————————————————————————————————

# Contributions

## MissionController (mission_controller.py)

1. Inside __init__: During the constructor call, the trajectory variable was not initialised. I have initialised it to empty tuple in order to handle a case where from user is slow, so ROBOT should not move.

2.	Inside set_trajectory: When set_trajectory() function is called, current_waypoint_idx should be initialised to 0 as the ROBOT need to take values from beginning in the list of trajectory points.

3. Inside _poll_position: The poll position conditions are modified. New conditions are given below:

	1.	Added a condition to handle empty tuple so the ROBOT will stay static when no trajectory coordinates are defined.

	2.	Added a condition to check if the current waypoint is beginning of trajectory coordinates.

	3.	Added a condition to check if the ROBOT has reached the first coordinate of previous point successfully or not. If it has reached then only will proceed to next point in the trajectory coordinates.

## SimulatedRobot (simulated_robot.py)
	
1.	In this class, the threads are updated with new Target worker functions, but none of them were started due to that the position of the ROBOT was not changing. I have added the thread_update.start() command in the below functions:

	1.	SimulatedRobot —> set_navigation_command —> update()
	2.	SimulatedRobotWithCommunicationDelay —> set_position —> update()
	3.	SimulatedRobotWithCommunicationDelay —> set_navigation_command —> update()

## Test
	
1.	We have created three test files(test.py, test2.py, test3.py) with different scenarios. Each test file is covering one tescase with different number of time.sleep() param.
