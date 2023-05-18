#!/usr/bin/python3
"""
    validates if a data set contains a valid UTF-8
    encoding.
"""


def validUTF8(data):
  """
  Determines if a given data set represents a valid UTF-8 encoding.

  Args:
    data: A list of integers representing the data.

  Returns:
    True if data is a valid UTF-8 encoding, else return False.
  """
  
  remaining_bytes = 0

  for integer in data:
        # Check utf-8 first Byte header
        if remaining_bytes == 0:
            #check 2 bytes
            if integer >> 5 == 0b110 or integer >> 5 == 0b1110:
                remaining_bytes = 1
            #check 3 bytes
            elif integer >> 4 == 0b1110:
                remaining_bytes = 2
            elif integer >> 3 == 0b11110:
                remaining_bytes = 3
            elif integer >> 7 == 0b1:
                return False
        #check other bytes
        else:
            if integer >> 6 != 0b10:
                return False
            remaining_bytes -= 1
  return remaining_bytes == 0