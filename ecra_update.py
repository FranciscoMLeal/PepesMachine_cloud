import time
import ecra_writter
import ecra

def display_update_loop(filename='ecra_text.json', interval=5):
    # Initialize previous values
    prev_data = ecra_writter.load_from_json(filename)

    while True:
        # Load current values
        current_data = ecra_writter.load_from_json(filename)

        # Check and update 'contador'
        if (current_data.get('contador') is not None and
            current_data['contador'] != prev_data.get('contador')):
            ecra.write_to_display_mini(current_data['contador'], 36)
        
        # Check and update 'titulo'
        if (current_data.get('titulo') is not None and
            current_data['titulo'] != prev_data.get('titulo')):
            ecra.write_to_display(current_data['titulo'], 0)

        # Check and update 'velocidade' and 'numero_de_cores'
        velocidade = current_data.get('velocidade')
        numero_de_cores = current_data.get('numero_de_cores')
        if (velocidade is not None and numero_de_cores is not None and
            (velocidade != prev_data.get('velocidade') or
             numero_de_cores != prev_data.get('numero_de_cores'))):
            ecra.write_to_display_mini(
                "Tempo: {} // {} Colors".format(velocidade, numero_de_cores), 24
            )

        # Check and update 'terminal_strings'
        current_terminal_strings = current_data.get('terminal_strings', [])
        prev_terminal_strings = prev_data.get('terminal_strings', [])
        
        if current_terminal_strings != prev_terminal_strings:
            for string in current_terminal_strings:
                if string:  # Ensure the string is not empty
                    ecra.write_to_fast_terminal(string)
        
        # Update previous data
        prev_data = current_data

        # Wait for the specified interval
        time.sleep(interval)

if __name__ == "__main__":
    ecra.initialize_display()
    ecra.write_to_display("PEPESMACHINE", 0)
    display_update_loop()
