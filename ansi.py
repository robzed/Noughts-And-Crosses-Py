# ASCII Sequences based on Peter Jakacki's Tachyon Extensions for Mecrisp
# MIT License


def ESC(ch, more=''):
  print(f'\x1b{ch}{more}', end='')


# ESC [
def ESCbracket(more=''):
  ESC("[", more)


# ESC [ ch
def CSI(ch):
  ESCbracket(ch)


def HOME():
  CSI('0;0H')


# Erase the screen from the current location
def ERSCN():
  CSI('2J')


# Erase the current line
def ERLINE():
  CSI('2K')


def CLS():
  ERSCN()
  HOME()
