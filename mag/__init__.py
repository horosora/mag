import gdb

from mag import command
from mag import event
from mag import color

gdb.execute('set confirm off')
gdb.execute('set pagination off')
gdb.execute('set print repeats 0')
gdb.execute('set disassembly-flavor intel')
gdb.execute(f'set prompt {color.CYAN + "GDB$ " + color.RESET}')
