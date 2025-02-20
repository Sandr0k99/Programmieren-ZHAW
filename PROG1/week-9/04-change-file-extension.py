import os


# Function to change the extension of files in a folder to '.mp3'
def change_file_extensions(path_to_folder):
    # List all files in the given folder
    files = os.listdir(path_to_folder)

    # Loop through each file in the folder
    for file_name in files:
        if file_name.endswith('.mp3'):
            continue

        # Generate the new file name with .mp3 extension (lowercase)
        new_file_name = file_name.rsplit('.', 1)[0] + '.mp3'

        # Full file paths
        old_file_path = os.path.join(path_to_folder, file_name)
        new_file_path = os.path.join(path_to_folder, new_file_name)

        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"Renamed: {file_name} -> {new_file_name}")


# Path to your folder (replace with your actual folder path)
path_to_folder = 'music_extension_example'

# Call the function to change the file extensions
change_file_extensions(path_to_folder)