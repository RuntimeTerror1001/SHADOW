import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/redpaladin/shadow_project/ros2_ws/install/shadow_robot'
