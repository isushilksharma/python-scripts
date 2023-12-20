#Python script to execute a shell command and capture its output

import subprocess

def execute_shell_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout, result.stderr

# Example usage:
command_to_run = "ls -l"
output, error = execute_shell_command(command_to_run)
print(f"Output:\n{output}")
print(f"Error:\n{error}")
