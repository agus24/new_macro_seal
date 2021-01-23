from sty import fg, bg, ef, rs

def black(text):
    print('\033[30m', text, '\033[0m', sep='')

def red(text):
    print(fg(255, 10, 10) + text)

def green(text):
    print('\033[32m', text, '\033[0m', sep='')

def yellow(text):
    print('\033[33m', text, '\033[0m', sep='')

def blue(text):
    print('\033[34m', text, '\033[0m', sep='')

def magenta(text):
    print('\033[35m', text, '\033[0m', sep='')

def cyan(text):
    print('\033[36m', text, '\033[0m', sep='')

def gray(text):
    print('\033[90m', text, '\033[0m', sep='')