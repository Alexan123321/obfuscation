import os
import random
import base64

# Define the path to the batch file to be obfuscated
batch_file_path = "path/to/batch/script.bat"

# Define a list of characters to be used in the obfuscated file
char_list = "abcdefghijklmnopqrstuvwxyz0123456789"

# Define a function to generate a random string of specified length
def generate_random_string(length):
    return ''.join(random.choice(char_list) for i in range(length))

# Read the contents of the batch file
with open(batch_file_path, "r") as batch_file:
    batch_content = batch_file.read()

# Split the batch content into lines
batch_lines = batch_content.splitlines()

# Define a list to hold the obfuscated lines
obfuscated_lines = []

# Obfuscate each line
for line in batch_lines:
    # Replace all characters in the line with random characters
    obfuscated_line = generate_random_string(len(line))
    
    # Replace the REM keyword with a random string
    obfuscated_line = obfuscated_line.replace("REM", generate_random_string(3))
    
    # Replace the CALL keyword with a random string
    obfuscated_line = obfuscated_line.replace("CALL", generate_random_string(4))
    
    # Append the obfuscated line to the list
    obfuscated_lines.append(obfuscated_line)
    
# Join the obfuscated lines back into a single string
obfuscated_content = "\n".join(obfuscated_lines)

# Encode the obfuscated content using Base64 encoding
encoded_content = base64.b64encode(obfuscated_content.encode("utf-8")).decode("utf-8")

# Write the obfuscated content to a new file
with open("obfuscated_script.bat", "w") as obfuscated_file:
    obfuscated_file.write(":: Obfuscated content\n")
    obfuscated_file.write("certutil -decode \"%~f0\" \"%temp%\\obfuscated_script.bat\" >nul\n")
    obfuscated_file.write("start \"\" \"%temp%\\obfuscated_script.bat\"\n")
    obfuscated_file.write(encoded_content)
    obfuscated_file.write("\n:: End of obfuscated content")

# Display the path to the obfuscated file
print("Obfuscated script saved to: " + os.path.abspath("obfuscated_script.bat"))
