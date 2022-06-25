import gdb

from mag import process
from mag import architecture
from mag import register
from mag import memory
from mag import terminal

class Register(gdb.Command):
    def __init__(self):
        super().__init__('mag register', gdb.COMMAND_NONE, gdb.COMPLETE_NONE, False)

    def invoke(self, argument, from_tty):
        if process.name is None:
            terminal.warning('This architecture is not supported by mag.')
            return

        if not process.is_alive():
            terminal.warning('Program is not running.')
            return

        if architecture.name == 'x86':
            regs = ['eax', 'ebx', 'ecx', 'edx', 'esi', 'edi', 'esp', 'ebp', 'eip']
        elif architecture.name == 'x64':
            regs = ['rax', 'rbx', 'rcx', 'rdx', 'rsi', 'rdi', 'rsp', 'rbp', 'r8', 'r9', 'r10', 'r11', 'r12', 'r13', 'r14', 'r15', 'rip']
        else:
            return

        for reg in regs:
            value = register.read(reg)
            data = f'{format(reg, " >3")}: {format(value, "#0" + str(architecture.bits // 4 + 2) + "x")}'
            try:
                value = architecture.unpack(memory.read(value, architecture.bits // 8))
                data += f' -> {format(value, "#0" + str(architecture.bits // 4 + 2) + "x")}'
            except gdb.MemoryError:
                pass
            print(data)
