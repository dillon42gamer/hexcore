import json

# Load the games.json file
input_file = "games.json"
output_file = "games_updated.json"  # To avoid overwriting, create an updated file

try:
    with open(input_file, "r") as file:
        data = json.load(file)

    # Add "type": "game" to each entry if not already present
    for game in data:
        if "type" not in game:
            game["type"] = "game"

    # Save the updated data back to a new file
    with open(output_file, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Updated games.json saved as {output_file}")

except FileNotFoundError:
    print(f"File {input_file} not found. Please check the path.")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
