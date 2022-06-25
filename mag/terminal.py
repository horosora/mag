from mag import color

def info(message):
    print(f'{color.GREEN}[+]{color.RESET} {message}')

def warning(message):
    print(f'{color.YELLOW}[-]{color.RESET} {message}')

def error(message):
    print(f'{color.RED}[x]{color.RESET} {message}')
