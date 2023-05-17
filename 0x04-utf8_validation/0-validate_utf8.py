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

  # Check if the data is empty.
  if not data:
    return False

  # Check if the first byte is a valid start byte.
  start_byte = data[0]
  if not (start_byte & 0x80):
    return False

  # Check if the remaining bytes are valid continuation bytes.
  for byte in data[1:]:
    if not (byte & 0xc0):
      return False

  return True