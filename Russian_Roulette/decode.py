import re

# Function to calculate the modulus and replace with ASCII character
def replace_modulus_with_ascii(content):
    pattern = re.compile(r'set (\w+)=([\d]+) %% ([\d]+)')
    matches = pattern.findall(content)
    
    for match in matches:
        var_name = match[0]
        dividend = int(match[1])
        divisor = int(match[2])
        result = dividend % divisor
        ascii_char = chr(result)
        replacement = f'set {var_name}={ascii_char}'
        content = re.sub(rf'set {var_name}={dividend} %% {divisor}', replacement, content)
    
    return content

# Function to replace variable placeholders with their values
def replace_variables(content):
    assignments = re.findall(r'set (\w+)=([^\n]*)', content)
    variables = {var: value for var, value in assignments}

    for var, value in variables.items():
        content = re.sub(rf'%{var}%', value, content)

    return content

# Read the obfuscated.cmd file
with open('script.cmd', 'r') as file:
    content = file.read()

# Replace modulus operations with ASCII characters
content = replace_modulus_with_ascii(content)

# Replace variable placeholders with their values
content = replace_variables(content)

# Write the deobfuscated content to a new file
with open('deobfuscated.cmd', 'w') as file:
    file.write(content)

print("Deobfuscation complete. The deobfuscated file is saved as 'deobfuscated.cmd'.")