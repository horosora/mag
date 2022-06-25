import gdb
import sys

from mag import terminal

name = None

def update(name):
    module = sys.modules[__name__]

    gdb_inferior = gdb.selected_inferior()
    gdb_architecture = gdb_inferior.architecture()

    if gdb_architecture.name() in ['i386', 'i386:x86-64']:
        module.name = name
    else:
        terminal.warning('This architecture is not supported by mag.')
        clear()

def clear():
    module = sys.modules[__name__]
    module.name = None

def is_alive():
    gdb_inferior = gdb.selected_inferior()
    return gdb_inferior.pid > 0
