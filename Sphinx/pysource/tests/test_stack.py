#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Basic module
import unittest

# The module to manipulate the search path
import sys
from pathlib import Path

# Insert path in which the module locates
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# Other necessary module






# Main entry point
if __name__ == '__main__':
    unittest.main()