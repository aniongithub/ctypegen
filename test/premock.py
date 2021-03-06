# Copyright (c) 2020 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.
#
# DON'T EDIT THIS FILE. It was generated by
# ./PreMockTest.py
# Please see AID/3558 for details on the contents of this file
#
from ctypes import * # pylint: disable=wildcard-import
from CTypeGenRun import * # pylint: disable=wildcard-import
# pylint: disable=unnecessary-pass,protected-access



class Globals(object):
   def __init__(self, dll):
      pass
def decorateFunctions( lib ):
   lib.preEntry.restype = None
   lib.preEntry.argtypes = []

   lib.preRecurse.restype = None
   lib.preRecurse.argtypes = [
      c_int ]

   lib.preF.restype = c_int
   lib.preF.argtypes = [
      c_int,
      c_char_p,
      POINTER( c_int ) ]

   lib.preRecurseEntry.restype = None
   lib.preRecurseEntry.argtypes = [
      c_int ]

   pass

functionTypes = {
   'preEntry': CFUNCTYPE( None),
   'preRecurse': CFUNCTYPE( None, c_int
      ),
   'preF': CFUNCTYPE( c_int, c_int
      , c_char_p
      , POINTER( c_int )
      ),
   'preRecurseEntry': CFUNCTYPE( None, c_int
      ),
}


if __name__ == "__main__":
   test_classes()
