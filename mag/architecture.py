import gdb
import sys
import struct

STRUCT_FORMATS = {('little', 32): '<L', ('little', 64): '<Q', ('big', 32): '>Q', ('big', 64): '>Q'}

name = None
bits = None
endianness = None

def update():
    module = sys.modules[__name__]

    gdb_inferior = gdb.selected_inferior()
    gdb_architecture = gdb_inferior.architecture()

    if gdb_architecture.name() == 'i386':
        module.name = 'x86'
        module.bits = 32
        module.endianness = 'little'
    elif gdb_architecture.name() == 'i386:x86-64':
        module.name = 'x64'
        module.bits = 64
        module.endianness = 'little'
    else:
        clear()

def clear():
    module = sys.modules[__name__]
    module.name = None
    module.bits = None
    module.endianness = None

def disassemble(start_address, end_address):
    gdb_frame = gdb.selected_frame()
    gdb_architecture = gdb_frame.architecture()
    return gdb_architecture.disassemble(start_address, end_address)

def pack(value):
    return struct.pack(STRUCT_FORMATS[(endianness, bits)], value)

def unpack(value):
    return struct.unpack(STRUCT_FORMATS[(endianness, bits)], value)[0]
