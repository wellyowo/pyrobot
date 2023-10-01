#!/usr/bin/env python

# Copyright (c) Facebook, Inc. and its affiliates.

# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import subprocess
import time

p = subprocess.Popen(["roslaunch", "realsense2_camera", "rs_camera.launch"])
time.sleep(3)
genP = subprocess.Popen(["roslaunch", "orb_slam2_ros", "gen_cfg.launch"])
time.sleep(3)
p.terminate()
genP.terminate()
p.wait()
genP.wait()
