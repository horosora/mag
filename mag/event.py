import gdb

from mag import process
from mag import architecture
from mag import register
from mag import color

def stop_handler(event):
    print(color.CYAN + '### Register ###' + color.RESET)
    gdb.execute('mag register')
    print(color.CYAN + '### Disassemble ###' + color.RESET)
    gdb.execute('mag disassemble')
    print(color.CYAN + '### Stack ###' + color.RESET)
    gdb.execute('mag stack')

def new_objfile_handler(event):
    if process.name is None:
        process.update(event.new_objfile.filename)
        architecture.update()
        register.update()

def clear_objfiles_handler(event):
    process.clear()
    architecture.clear()
    register.clear()

gdb.events.stop.connect(stop_handler)
gdb.events.new_objfile.connect(new_objfile_handler)
gdb.events.clear_objfiles.connect(clear_objfiles_handler)
