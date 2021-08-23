#!/usr/bin/env python3

import shutil
import sys
import os

def check_reboot():
  """Return True if the compter has a pending rebott"""
  return os.path.exists("/run/reboot/required")

def check_disk_usage(disk, min_gb, min_percent):
  '''Return True is there is enough free disk space, false otherwise'''
  du = shutil.disk_usage(disk)
  # Calculate the ercentage of free space
  percent_free = 100 * du.free / du.total
  # Calculate how many fre gigabytes
  gigabytes_free = du.free / 2**30
  if percent_free < min_percent or gigabytes_free < min_gb:
    return True
  return False


def main():
  if check_reboot():
    print("Pending reboot.")
    sys.exit(1)
  if check_disk_usage(disk = "/", min_gb = 2, min_percent = 10):
    print("Disk Full")
    sys.exit(1)

  print("Everything ok.")
  sys.exit(0)

main()
