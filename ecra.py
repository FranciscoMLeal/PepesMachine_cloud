import sys
import time
import os
import DFRobot_RPi_Eink_Display

# Peripheral params
RASPBERRY_SPI_BUS = 0
RASPBERRY_SPI_DEV = 0
RASPBERRY_PIN_CS = 27
RASPBERRY_PIN_CD = 17
RASPBERRY_PIN_BUSY = 4
RASPBERRY_PIN_RST = 26

terminal_input = []
fast_terminal_input = []  # Move this to the global scope
fontFilePath = "./resources/wqydkzh.ttf"  # fonts file

eink_display = DFRobot_RPi_Eink_Display.DFRobot_RPi_Eink_Display(
    RASPBERRY_SPI_BUS, RASPBERRY_SPI_DEV, RASPBERRY_PIN_CS,
    RASPBERRY_PIN_CD, RASPBERRY_PIN_BUSY, RASPBERRY_PIN_RST
)

def pad_text(text):
    if len(text) < 19:
        return text.ljust(19)
    return text

def pad_text35(text):
    if len(text) < 35:
        return text.ljust(35)
    return text

def initialize_display(clear=True):
    eink_display.begin()
    if clear:
        eink_display.clear_screen()

    ft = DFRobot_RPi_Eink_Display.FreetypeHelper(fontFilePath)
    ft.set_dis_lower_limit(112)
    eink_display.set_ex_fonts(ft)
    eink_display.set_text_format(1, eink_display.BLACK, eink_display.WHITE, 1, 1)

def write_to_fast_terminal(text):
    global fast_terminal_input  # Add this line to use the global variable
    if len(fast_terminal_input) > 5:
        fast_terminal_input = []
    if len(text) > 35:
        # Write the first 19 characters
        current_text = text[:35]
        fast_terminal_input.append(current_text)
        x = len(fast_terminal_input) - 1
        eink_display.set_ex_fonts_fmt(12, 12)
        eink_display.set_text_cursor(0, 48 + (x * 12))
        eink_display.print_str(current_text)
        eink_display.flush(eink_display.PART)
        # Recursively call with the remaining text
        return write_to_fast_terminal(text[35:])
    fast_terminal_input.append(text)
    x = len(fast_terminal_input) - 1
    eink_display.set_ex_fonts_fmt(12, 12)
    eink_display.set_text_cursor(0, 48 + (x * 12))
    text = pad_text35(text)
    eink_display.print_str(text)
    eink_display.flush(eink_display.PART)

def write_to_terminal(text):
    global terminal_input  # Add this line to use the global variable
    terminal_input.append(text)
    if len(terminal_input) > 6:
        terminal_input.pop(0)
    x = len(terminal_input) - 1
    print(f"terminal Input :", terminal_input)
    while x >= 0:
        eink_display.set_ex_fonts_fmt(12, 12)
        eink_display.set_text_cursor(0, 108 - (x*12))
        terminal_input[x] = pad_text35(terminal_input[x])
        eink_display.print_str(terminal_input[x])
        eink_display.flush(eink_display.PART)
        x = x - 1

    #time.sleep(1)


def write_to_display(text, col=0 , clear=False):
    if len(text) > 19:
        # Write the first 19 characters
        current_text = text[:19]
        col = write_to_display(current_text, col, clear)
        # Recursively call with the remaining text
        return write_to_display(text[19:], col, False)

    text = pad_text(text)
    initialize_display(clear)
    if col > 96:
        col = 24
    eink_display.set_ex_fonts_fmt(24, 24)

    eink_display.set_text_cursor(0, col)
    eink_display.print_str(text)
    eink_display.flush(eink_display.PART)
    #time.sleep(1)
    col = col + 24
    return col

def write_to_display_mini(text, col=0 , clear=False):
    text = pad_text(text)
    initialize_display(clear)
    if col > 96:
        col = 24
    eink_display.set_ex_fonts_fmt(12, 12)

    eink_display.set_text_cursor(0, col)
    eink_display.print_str(text)
    eink_display.flush(eink_display.PART)
    #time.sleep(1)
    col = col + 24
    return col

def clear_screen():
    eink_display.clear_screen()