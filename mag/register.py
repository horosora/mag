import gdb
import sys

from mag import architecture

ip = None
bp = None
sp = None

def update():
    module = sys.modules[__name__]

    gdb_inferior = gdb.selected_inferior()
    gdb_architecture = gdb_inferior.architecture()

    if gdb_architecture.name() == 'i386':
        module.ip = 'eip'
        module.bp = 'ebp'
        module.sp = 'esp'
    elif gdb_architecture.name() == 'i386:x86-64':
        module.ip = 'rip'
        module.bp = 'rbp'
        module.sp = 'rsp'
    else:
        clear()

def clear():
    module = sys.modules[__name__]
    module.ip = None
    module.bp = None
    module.sp = None

def read(register):
    gdb_frame = gdb.selected_frame()
    gdb_architecture = gdb_frame.architecture()
    return int(gdb_frame.read_register(register).cast(gdb_architecture.integer_type(architecture.bits, False)))
