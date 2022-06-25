import gdb
import sys
import inspect

from mag.command import disassemble
from mag.command import register
from mag.command import stack

class Command(gdb.Command):
    def __init__(self):
        super().__init__('mag', gdb.COMMAND_NONE, gdb.COMPLETE_COMMAND, True)

    def invoke(self, argument, from_tty):
        return

for module_name in sys.modules.keys():
    if module_name.startswith('mag.command'):
        inspect.getmembers(sys.modules[module_name], inspect.isclass)[0][1]()
