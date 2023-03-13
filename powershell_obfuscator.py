import random
import string

# Specify the path to your PowerShell script
powershell_script_path = 'SharpHound.ps1'

# Read in the PowerShell script
with open(powershell_script_path, 'r') as f:
    powershell_script = f.read()

# Obfuscate the PowerShell script
obfuscated_script = ""
for line in powershell_script.splitlines():
    obfuscated_line = ""
    for char in line:
        if char in string.ascii_letters:
            if random.randint(0,1) == 0:
                obfuscated_line += char.lower()
            else:
                obfuscated_line += char.upper()
        elif char.isdigit():
            obfuscated_line += char
        else:
            obfuscated_line += char.encode('utf-16')[2:].decode('utf-8')
    obfuscated_script += obfuscated_line + "\n"

# Write the obfuscated PowerShell script to a new file
obfuscated_script_path = 'Obfuscated.ps1'
with open(obfuscated_script_path, 'w') as f:
    f.write(obfuscated_script)
