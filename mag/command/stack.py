import gdb

from mag import process
from mag import architecture
from mag import register
from mag import memory
from mag import terminal

class Command(gdb.Command):
    def __init__(self):
        super().__init__('mag stack', gdb.COMMAND_NONE, gdb.COMPLETE_NONE, False)

    def invoke(self, argument, from_tty):
        if process.name is None:
            terminal.warning('This architecture is not supported by mag.')
            return

        if not process.is_alive():
            terminal.warning('Program is not running.')
            return

        sp = register.read(register.sp)

        for i in range(10):
            address = sp + i * architecture.bits // 8
            value = architecture.unpack(memory.read(address, architecture.bits // 8))
            data = f'{format(address, "#0" + str(architecture.bits // 4 + 2) + "x")}: {format(value, "#0" + str(architecture.bits // 4 + 2) + "x")}'
            try:
                value = architecture.unpack(memory.read(value, architecture.bits // 8))
                data += f' -> {format(value, "#0" + str(architecture.bits // 4 + 2) + "x")}'
            except gdb.MemoryError:
                pass
            print(data)
