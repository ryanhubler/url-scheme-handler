import sys
import os
import subprocess
import time

# Define executable path
exe_path = r"C:/Program Files (x86)/myapp/bin/myapp.exe"

# Verify executable exists
if not os.path.exists(exe_path):
    sys.stderr.write(f"Error: Executable not found at {exe_path}\n")
    sys.exit(1)

# Get raw input if provided
raw_input = sys.argv[1] if len(sys.argv) > 1 else ""

try:
    # Remove scheme if present
    if raw_input.startswith("myapp://"):
        scheme_removed = raw_input[len("myapp://"):]
    else:
        scheme_removed = raw_input

    # Convert path to arguments
    path = scheme_removed.replace("/", ",").strip(",")
    arg = [x for x in path.split(",") if x]  # Remove empty strings, create list of all arguments

    # Start process with all available arguments
    command = [exe_path] + arg
    subprocess.check_call(command)

except Exception as e:
    # On any error, log it and run myapp.exe with no arguments
    sys.stderr.write(f"Error processing input: {e}\n")
    try:
        subprocess.check_call([exe_path])
    except subprocess.CalledProcessError as e2:
        sys.stderr.write(f"Error running executable with no arguments: {e2}\n")
        sys.exit(1)
    except Exception as e2:
        sys.stderr.write(f"Unexpected error running executable with no arguments: {e2}\n")
        sys.exit(1)
