from uuid import getnode as get_mac
import subprocess
import sys
import os

def format_mac_adress():
  mac = get_mac()
  return ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))

def get_path():
  return '{0}\\test.bat'.format(os.path.dirname(os.path.abspath(__file__)))


def execute_bat():
  fullpath = get_path()
  test = subprocess.call([r'{0}'.format(fullpath)])
  

execute_bat()


