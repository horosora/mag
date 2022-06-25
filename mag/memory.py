import gdb

def read(address, length):
    gdb_inferior = gdb.selected_inferior()
    return bytes(gdb_inferior.read_memory(address, length))
