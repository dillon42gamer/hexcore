import os
import re

def add_script_to_html_files(directory):
    # Define the script tag to add
    script_tag = '<script src="authCheck.js"></script>'

    # Walk through all files in the directory and subdirectories
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                
                # Open the file to check its contents
                with open(file_path, 'r+', encoding='utf-8') as f:
                    content = f.read()
                    
                    # Check if the script tag is already in the file
                    if script_tag not in content:
                        # Add the script tag before the closing </body> tag
                        updated_content = re.sub(r'</body>', f'{script_tag}\n</body>', content, flags=re.IGNORECASE)
                        
                        # Move cursor to beginning and overwrite file with updated content
                        f.seek(0)
                        f.write(updated_content)
                        f.truncate()  # Remove any leftover content if script was added at the end

                        print(f"Added script to {file_path}")

# Specify the directory to process
directory_path = "C:/Users/scott/Documents/GitHub/PixelPulsefr"
add_script_to_html_files(directory_path)
