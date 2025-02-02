import os

def replace_text_in_file(file_path, replacements):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_data = file.read()
        
        # Replace each keyword in the file content
        for old_text, new_text in replacements.items():
            file_data = file_data.replace(old_text, new_text)
        
        # Write the changes back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(file_data)
        print(f"Processed file: {file_path}")
    
    except Exception as e:
        print(f"Could not process file {file_path}: {e}")

def replace_in_directory(directory, replacements):
    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            replace_text_in_file(file_path, replacements)

# Set your directory path here
directory_path = 'C:/Users/scott/Documents/GitHub/PixelPulsefr'

# Define the replacements
replacements = {
    "PixelPulse": "PixelPulse",
    "PixelPulse": "PixelPulse",
    "PixelPulse lite": "PixelPulse",
    "PixelPulse lite": "PixelPulse"
}

# Run the replacement function
replace_in_directory(directory_path, replacements)
