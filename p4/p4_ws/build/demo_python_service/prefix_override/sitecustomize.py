import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/lhc/fishros-/p4/p4_ws/install/demo_python_service'
