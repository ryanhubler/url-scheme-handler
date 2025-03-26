import sys, string, os, subprocess, time
# Direct input including the scheme example: myapplication://field1/field2/field3/
raw_input = sys.argv[1]
# Sanitized input removing scheme and leaving "path" example: field1/field2/field3/
scheme_removed = raw_input.strip("myapp://")

# Removes / and replaces it with a ,
string_with_spaces = scheme_removed.replace("/", ",")

# Removes ending / 
finished_input = string_with_spaces.strip("/")

# Converts finished_input to a list arg
arg = finished_input.split(",")

# Starts myapp.exe with arguments of arg[0], arg[1], arg[2] this can be expanded or reduced depending on how many arguments are needed
subprocess.check_call([r"C:/Program Files (x86)/myapp/bin/myapp.exe", arg[0], arg[1], arg[2] ])
