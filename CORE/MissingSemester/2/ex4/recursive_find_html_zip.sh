#!/usr/bin/env bash

# The task it so write a command that recursively finds akk HTML files in the folder and makes a zip with them (as the name of this file might suggest). 
# Extra requirements:
# - should work if the filenames have spaces

# find -print0 will print the exact filenames (quotes, spaces, etc.) and xargs -0 will take them in correctly

# tar --create --file --verbose is same as tar -cvf, -z is for gzip
find . -name "*.html" -print0 | xargs -0 tar -cvzf html.zip
