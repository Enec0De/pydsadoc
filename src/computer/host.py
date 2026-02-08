#!/usr/bin/env python

# The Main Memory Hardware.
class MemoryArray:
    ...


class MainMemory:

    def __init__(self) -> None:
        self.memory_unit = MemoryArray()
        self.mar = b''
        self.mdr = b''


# The CPU Hardware.
class CU:
    ...

class ALU:
    ...

class Calculator:
    
    def __init__(self) -> None:
        self.alu = ALU()
        self.acc = b''
        self.mq = b''
        self.x = b''

class Controller:

    def __init__(self) -> None:
        self.cu = CU()
        self.pc = b''
        self.ir = b''

class CPU:

    def __init__(self) -> None:
        self.controller = Controller()
        self.calculator = Calculator()


class Host:

    def __init__(self) -> None:
        self.cpu = CPU()
        self.memory = MainMemory()

    def run(self) -> None:
        ...
