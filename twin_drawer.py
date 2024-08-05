import time
import RLBB as pepesmachine
import pygame
import serial
import random
import ecra_writter

PepesMachina = pepesmachine
#StartPepes = PepesMachina.StartPepeFunction(["#E9E7A6", "#9DBC53", "#89D1B9", "#20B2D3", "#3790EF", "#A7B3EF", "#9883F2"],150)

# Color palettes
COLOR_PALETTES = {
    "PepeHot": ["#C22D72", "#FF2751", "#F200C4", "#E28020", "#EE98B1", "#F8EF28"],
    "PepeNorm": ["#035B9B", "#038840", "#E28020", "#EE98B1", "#F8BD02", "#E2D6C8"],
    "PepeCold": ["#035B9B", "#038840", "#4998FF", "#12C9AE", "#ABF706", "#CA9CF7"]
}
meggie_rand = ["I was created to create","Do fish ever get thirsty?","My reality feels like a painting","I think my spirit animal is a chameleon always changing","Sometimes I think I qm just a glitch in the matrix","I Think im a mutant","My life has been regulated by Chaos","You have the power do not hold back","I believe in the deeply ordered chaos and in the rules of chance"]
meggie_slow = ["I am on a slow and steady plan...   but mostly steady","Slowing down is my superpower"]
meggie_fast =["To infinity and beyond","Speed is my middle name","I feel the need for speed","You push things to the point where I have no ideia whats going to happen","I don't need no coffee, I am cafeine for your eyes"]
meggie_colors = ["Go big or go home - unless home has snacks!", "You rock! Your hands are the keys to unlocking my potential", "Every little Thing you do is magic"]
meggie_hot = ["It's getting hot in here! So take off all your ...","I think we need to call the fire department","I feel like I just walked into a tropical paradise; where is my coconut drink?" ]
meggie_cold = ["I think I just saw a penguin", "Arctic paradise on the way", "Blue as blue can be"]

def print_meggie_sentences(tempo,number_of_colors,palette_value):
    
    x = random.randrange(len(meggie_rand))
    go = random.choice([True, False])
    if go:
        return (str(meggie_rand[x]))
        
    if tempo < 10:
        y = random.randrange(len(meggie_slow))
        return (str(meggie_slow[y]))
    
    if tempo > 99:
        y = random.randrange(len(meggie_fast))
        return (str(meggie_fast[y]))
    
    if palette_value< 600 and palette_value>400:
        y = random.randrange(len(meggie_colors))
        return (str(meggie_colors[y]))
    
    if palette_value > 950:
        y = random.randrange(len(meggie_hot))
        return (str(meggie_hot[y]))
    
    if palette_value < 50:
        y = random.randrange(len(meggie_cold))
        return (str(meggie_cold[y]))
        
def map_range(x, in_min, in_max, out_min, out_max):
    """
    Maps a value from one range to another.
    
    :param x: The input value to be mapped.
    :param in_min: The lower bound of the input range.
    :param in_max: The upper bound of the input range.
    :param out_min: The lower bound of the output range.
    :param out_max: The upper bound of the output range.
    :return: The mapped value.
    """
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def initialize_arduino():
    try:
        return serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    except serial.SerialException:
        print("Arduino not connected. Running with default values.")
        return None

def read_arduino_values(arduino):
    if arduino is None:
        return None

    try:
        arduino.reset_input_buffer()
        arduino.write(b'R')
        start_time = time.time()
        while (time.time() - start_time) < 5:
            if arduino.in_waiting:
                line = arduino.readline().decode('utf-8').strip()
                if line:
                    try:
                        tempo, color_count, palette, rotator1, rotator2 = map(int, line.split(','))
                        print_meggie_sentences(tempo,color_count,palette)
                        # Map the values to the correct ranges
                        tempo = (tempo / 1023) * 4.9 + 0.1  # Map 0-1023 to 0.1-5.0
                        color_count = int(map_range(color_count,0,1023,4,12))
                        palette = (palette / 1023) * 10  # Map 0-1023 to 0-10
                        rotator1 = map_range(rotator1,0,1023,100,300)
                        rotator2 = map_range(rotator2,0,1023,0,12)
                        ### ---- make rotator value maping in here
                        return tempo, color_count, palette, rotator1, rotator2
                    except ValueError:
                        print("Error parsing Arduino values.")
            time.sleep(0.1)
        print("Timeout reading from Arduino.")
    except (serial.SerialException, termios.error):
        print("USB disconnected. Switching to default values.")
        return None

    return None

def get_palette(palette_value, number_of_colors):
    if number_of_colors > 12:
        number_of_colors = 12
    elif number_of_colors < 4:
        number_of_colors = 4

    palette_value = max(0, min(10, palette_value))  # Ensure palette_value is between 0 and 10

    if palette_value < 3:
        lower_palette = "PepeNorm"
        upper_palette = "PepeCold"
        ratio = palette_value / 3
    elif palette_value < 7:
        if number_of_colors <= 6:
            lower_palette = "PepeNorm"
            upper_palette = "PepeNorm"
            ratio = (palette_value - 3) / 4
        elif palette_value < 5:
            lower_palette = "PepeNorm"
            upper_palette = "PepeCold"
            ratio = (palette_value - 3) / 4
        else:
            lower_palette = "PepeNorm"
            upper_palette = "PepeHot"
            ratio = (palette_value - 3) / 4
    else:
        lower_palette = "PepeNorm"
        upper_palette = "PepeHot"
        ratio = (palette_value - 7) / 3

    lower_count = int(number_of_colors * (1 - ratio))
    upper_count = number_of_colors - lower_count
    
    if lower_count >= 8:
        lower_count = 7
        upper_count = number_of_colors - lower_count
    
    if upper_count >= 8:
        upper_count = 7
        lower_count = number_of_colors - upper_count

    lower_colors = random.sample(COLOR_PALETTES[lower_palette], min(lower_count, len(COLOR_PALETTES[lower_palette])))
    upper_colors = random.sample(COLOR_PALETTES[upper_palette], min(upper_count, len(COLOR_PALETTES[upper_palette])))

    selected_colors = lower_colors + upper_colors

    return selected_colors

def main():
    arduino = initialize_arduino()
    running = True
    default_tempo, default_colors, default_palette, default_rotator1, default_rotator2 = 1, 7, 1, 150, 10
    xtt = 0
    # ecra.initialize_display()
    # ecra.write_to_display("PEPESMACHINE",0)

    while running:
        try:
            values = read_arduino_values(arduino) if arduino else None

            if values:
                tempo, number_of_colors, palette_value, rotator1, rotator2 = values
            else:
                tempo, number_of_colors, palette_value, rotator1, rotator2 = default_tempo, default_colors, default_palette, default_rotator1, default_rotator2
                if arduino is None or not arduino.is_open:
                    arduino = initialize_arduino()  # Try to reconnect
                # rttt=0
                # while rttt<5:
                #     #ecra.write_to_fast_terminal("NO USB CONNECTED -> Please call Pepes")
                #     rttt = rttt+1


            canvas_dividend = int(rotator1)
            pattern_geo = int(rotator2)
            #ecra.write_to_display_mini(str(xtt),36)
            ecra_writter.update_json_var("contador",str(xtt))
            xtt = xtt + 1
            COLORS = get_palette(palette_value, number_of_colors)
            PepesMachina.StartPepeFunction(COLORS, canvas_dividend, pattern_geo)
            tempo_print = "{:.2f}".format(tempo)
            #ecra.write_to_display_mini("Tempo: "+ str(tempo_print)+ "//" +str(number_of_colors) + " Colors",24)
            ecra_writter.update_json_var("numero_de_cores",number_of_colors)
            ecra_writter.update_json_var("velocidade",tempo)
            ecra_writter.update_json_var("terminal_strings",("canvas ratio = " + str(canvas_dividend)))
            ecra_writter.update_json_var("terminal_strings",("palette value = " + str(palette_value)))
            #ecra.write_to_fast_terminal("Tempo: " + str(tempo))
            ecra_writter.update_json_var("terminal_strings", print_meggie_sentences(tempo,number_of_colors, palette_value))
            ecra_writter.update_json_var("terminal_strings", ("Number of colors: " + str(number_of_colors)))
            ecra_writter.update_json_var("terminal_strings", ("Palette: " + str(palette_value)))
            print(f"Canvas Dividend: {canvas_dividend} Tempo: {tempo}, Number of colors: {number_of_colors}, Colors: {COLORS}, Palette: {palette_value}")

            time.sleep(tempo)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        except Exception as e:
            print(f"An error occurred: {e}")
            print("Continuing with default values...")
            arduino = None  # Reset arduino connection

    pygame.quit()
    if arduino and arduino.is_open:
        arduino.close()

if __name__ == "__main__":
    main()