import json

def update_json_var(var_name, new_value, filename='ecra_text.json'):
    try:
        # Read the existing data from the file
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        # If the file does not exist, initialize with default values
        data = {
            "titulo": "",
            "contador": 0,
            "numero_de_cores": 0,
            "velocidade": 0,
            "terminal_strings": []
        }
    
    # Update the specified variable with the new value
    if var_name == "terminal_strings":
        # If the list already has 6 items, remove the first item (oldest)
        if len(data["terminal_strings"]) >= 6:
            data["terminal_strings"].pop(0)
        # Add the new string to the end of the list
        data["terminal_strings"].append(new_value)
    elif var_name in data:
        data[var_name] = new_value
    else:
        raise KeyError(f"Variable '{var_name}' does not exist in the JSON data.")
    
    # Write the updated data back to the file
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def load_from_json(filename='ecra_text.json'):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# Example usage:
if __name__ == "__main__":
    update_json_var("titulo", "New Title for E-ink Display")
    update_json_var("contador", 100)
    update_json_var("numero_de_cores", 4)
    update_json_var("velocidade", 1200)
    update_json_var("terminal_strings", "First string")
    update_json_var("terminal_strings", "Second string")
    update_json_var("terminal_strings", "Third string")
    update_json_var("terminal_strings", "Fourth string")
    update_json_var("terminal_strings", "Fifth string")
    update_json_var("terminal_strings", "Sixth string")
    update_json_var("terminal_strings", "Seventh string")
    update_json_var("terminal_strings", "Eighth string")

    data = load_from_json()
    print(f"Titulo: {data['titulo']}")
    print(f"Contador: {data['contador']}")
    print(f"Numero de Cores: {data['numero_de_cores']}")
    print(f"Velocidade: {data['velocidade']}")
    print(f"Terminal Strings: {data['terminal_strings']}")
