import sys
from gui import Gui

def main():
    configfile = sys.argv[1] if len(sys.argv) > 1 \
                             else 'default.layout'
    gui = Gui(configfile)


if __name__ == '__main__':
    main()
