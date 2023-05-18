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
  count = 0

  for integer in data:
        if count == 0:
            if integer >> 5 == 0b110 or integer >> 5 == 0b1110:
                count = 1
            elif integer >> 4 == 0b1110:
                count = 2
            elif integer >> 3 == 0b11110:
                count = 3
            elif integer >> 7 == 0b1:
                return False
        else:
            if integer >> 6 != 0b10:
                return False
            count -= 1
  return count == 0