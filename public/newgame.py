import os

# Function to remove the URL from a given file
def remove_url_from_file(file_path, url_to_remove):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # If the URL is found in the file, remove it
    if url_to_remove in content:
        content = content.replace(url_to_remove, '')
        
        # Write the updated content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Removed URL from: {file_path}")

# Function to traverse all directories and subdirectories
def remove_url_from_html_files(start_dir, url_to_remove):
    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if file.endswith('.html'):  # Check if the file is an HTML file
                file_path = os.path.join(root, file)
                remove_url_from_file(file_path, url_to_remove)

# Define the URL to be removed
url_to_remove = "https://forpixel.mysynology.net"

# Start directory is the current directory
current_directory = os.getcwd()

# Run the script
remove_url_from_html_files(current_directory, url_to_remove)
