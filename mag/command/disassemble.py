import gdb

from mag import process
from mag import architecture
from mag import register
from mag import terminal

class Command(gdb.Command):
    def __init__(self):
        super().__init__('mag disassemble', gdb.COMMAND_NONE, gdb.COMPLETE_NONE, False)

    def invoke(self, argument, from_tty):
        if process.name is None:
            terminal.warning('This architecture is not supported by mag.')
            return

        if not process.is_alive():
            terminal.warning('Program is not running.')
            return

        ip = register.read(register.ip)
        instructions = architecture.disassemble(ip - 150, ip + 165)
        current_position = [instruction['addr'] for instruction in instructions].index(ip)

        for instruction in instructions[current_position-10:current_position+11]:
            if instruction['addr'] == ip:
                print(f'=> {format(instruction["addr"], "#0" + str((architecture.bits // 4) + 2) + "x")}: {instruction["asm"]}')
            else:
                print(f'   {format(instruction["addr"], "#0" + str((architecture.bits // 4) + 2) + "x")}: {instruction["asm"]}')
