import tkinter as tk

from configparser import parse_config
from rpntokenizer import tokenize_rpn
from shuntingyard import shunting_yard
from calculator import calculation



# Constant definitions. Unit in trailing comment.
# Units:
#     C: in characters.
#     W: In widgets.

TITLE_TEXT = 'Calculator GUI v1.0'
TITLE_WIDTH = 4  # W

DISPLAY_WELCOME_MESSAGE = 'Hello!'
DISPLAY_WIDTH = 16  # C
DISPLAY_HEIGHT = 1  # C
DISPLAY_BG_COLOR = '#ffffff'
DISPLAY_FONT_SIZE = 15

SYMBOL_BACKSPACE = '\u232b'
SYMBOL_ENTER = '\u23ce'

BUTTON_WIDTH = 2 # C
BUTTON_HEIGHT = 1 # C

KEYBOARD_X_OFFSET = 0  # W
KEYBOARD_Y_OFFSET = 3  # W


class Gui:
    def __init__(self, settings_file: str) -> None:
        self.root = tk.Tk()
        self.title = tk.Label(self.root, text=TITLE_TEXT)
        self.title.grid(row=0, column=0, columnspan=TITLE_WIDTH, sticky='w')
        self.display = tk.Label(self.root,
                            text=DISPLAY_WELCOME_MESSAGE,
                            width=DISPLAY_WIDTH,
                            height=DISPLAY_HEIGHT,
                            bg=DISPLAY_BG_COLOR,
                            font=DISPLAY_FONT_SIZE,
                            anchor=tk.E)
        self.display.grid(row=1, column=0, columnspan=4)

        self.buttons = {

            # Display control buttons.
            'BUTTON_AC': self.createGuiButton('AC', self.emptyInput),
            'BUTTON_BACKSPACE': self.createGuiButton(SYMBOL_BACKSPACE, self.backspace),
            'BUTTON_ENTER': self.createGuiButton(SYMBOL_ENTER, self.calculate),

            # Numeric buttons.
            'BUTTON_0': self.createGuiButton('0', self.getCharCallbackFunction('0')),
            'BUTTON_1': self.createGuiButton('1', self.getCharCallbackFunction('1')),
            'BUTTON_2': self.createGuiButton('2', self.getCharCallbackFunction('2')),
            'BUTTON_3': self.createGuiButton('3', self.getCharCallbackFunction('3')),
            'BUTTON_4': self.createGuiButton('4', self.getCharCallbackFunction('4')),
            'BUTTON_5': self.createGuiButton('5', self.getCharCallbackFunction('5')),
            'BUTTON_6': self.createGuiButton('6', self.getCharCallbackFunction('6')),
            'BUTTON_7': self.createGuiButton('7', self.getCharCallbackFunction('7')),
            'BUTTON_8': self.createGuiButton('8', self.getCharCallbackFunction('8')),
            'BUTTON_9': self.createGuiButton('9', self.getCharCallbackFunction('9')),

            # Operator buttons.
            'BUTTON_ADD': self.createGuiButton('+', self.getCharCallbackFunction('+')),
            'BUTTON_SUB': self.createGuiButton('-', self.getCharCallbackFunction('-')),
            'BUTTON_MUL': self.createGuiButton('*', self.getCharCallbackFunction('*')),
            'BUTTON_DIV': self.createGuiButton('/', self.getCharCallbackFunction('/')),
            'BUTTON_EXP': self.createGuiButton('^', self.getCharCallbackFunction('^')),
            'BUTTON_MOD': self.createGuiButton('%', self.getCharCallbackFunction('%')),
            'BUTTON_LEFT_PAREN': self.createGuiButton('(', self.getCharCallbackFunction('(')),
            'BUTTON_RIGHT_PAREN': self.createGuiButton(')', self.getCharCallbackFunction(')')),
            'BUTTON_DECIMAL_POINT': self.createGuiButton('.', self.getCharCallbackFunction('.')),

            # Memory operation buttons. TBI
            'MEMORY_ADD': None,
            'MEMORY_SUB': None,
            'MEMORY_SAVE': None,
            'MEMORY_FETCH': None,
        }
        
        self.character_buffer = []

        self.createLayout(settings_file)
        self.root.mainloop()


    def createGuiButton(self,
                     text: str,
                     callback,
                     height=BUTTON_HEIGHT,
                     width=BUTTON_WIDTH) -> None:

        button = tk.Button(self.root,
                           text=text,
                           height=height,
                           width=width,
                           justify=tk.CENTER,
                           command=lambda: callback())
        return button


    def backspace(self) -> None:
        if len(self.character_buffer):
            del self.character_buffer[-1]

        # Acts as the AC-button if input buffer is empty.
        # e.g. When an answer is displayed.
        self.updateDisplay()


    def calculate(self) -> None:
        result = str(
                 calculation(
                 shunting_yard(
                 tokenize_rpn(self.character_buffer))))

        self.updateDisplay(str(result))
        self.character_buffer = []


    def createLayout(self, settings_file: str) -> None:
        with open(settings_file, 'r') as file:
            self.settings = parse_config(file.read())
        
        for (setting_name, setting_value) in self.settings.items():
            if len(setting_value) == 1 and setting_value[0] == 'None':
                continue
            
            if setting_name in self.buttons:
                self.gridButton(self.buttons[setting_name], setting_value)


    def emptyInput(self) -> None:
        self.character_buffer = []
        self.updateDisplay()


    def gridButton(self, button, coordinate_pair: tuple) -> None:
        # Offset coordinates by the amount of other widgets.
        x, y = coordinate_pair
        x += KEYBOARD_X_OFFSET
        y += KEYBOARD_Y_OFFSET

        button.grid(row=y, column=x, padx=0)


    def updateDisplay(self, text=False) -> None:
        if not text:
            text = ''.join(self.character_buffer)

        # Trim text to Display width so that it doesn't render
        # characters out of bounds.
        self.display.config(text=text[-DISPLAY_WIDTH:])


    def getCharCallbackFunction(self, char: str) -> None:
        def addToDisplay() -> None:
            self.character_buffer.append(char)
            self.updateDisplay()
        return addToDisplay
