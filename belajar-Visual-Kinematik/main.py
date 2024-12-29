#!/usr/bin/env python3

from visual_kinematics.RobotSerial import *
import numpy as np
from math import pi
import math


def main():
    np.set_printoptions(precision=3, suppress=True)

    # Parameter DH untuk robot 3 DOF
    dh_params = np.array(
        object=[[0.2, 0., 0.5 * pi, 0.],
                [0., 0.3, pi, 0.5 * pi],
                [0., 0.5, pi, 0.]])

    robot = RobotSerial(dh_params)

    # =====================================
    # inverse
    # =====================================

    xyz = np.array([[0.2], [0.3], [0.9]])
    abc = np.array([0, 0., 0])
    end = Frame.from_euler_3(abc, xyz)
    robot.inverse(end)

    print("inverse is successful: {0}".format(robot.is_reachable_inverse))
    print("axis values: \n{0}".format(robot.axis_values))
    print(
        f"sudut\ntheta 1 {math.degrees(robot.axis_values[0])},\ntheta 2 {math.degrees(robot.axis_values[1])}\ntheta 3 {math.degrees(robot.axis_values[2])}")
    robot.show()

    # ================================
    # forward
    # ===============================
    f = robot.forward(robot.axis_values)
    print("-------forward-------")
    print("end frame t_4_4:")
    print(f.t_4_4)
    print("end frame xyz:")
    print(f.t_3_1.reshape([3, ]))
    print("end frame abc:")
    print(f.euler_3)
    print("end frame rotational matrix:")
    print(f.r_3_3)
    print("end frame quaternion:")
    print(f.q_4)
    print("end frame angle-axis:")
    print(f.r_3)


if __name__ == "__main__":
    main()
