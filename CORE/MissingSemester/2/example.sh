#!/bin/bash

echo "Starting program at $(date)"

echo "Running program $0 with $# arguments with pid $$"

# $@ expands all the arguments
for file in "$@"; do
	grep foobar "$file" > /dev/null 2> /dev/null
	# when pattern is not found, grep has exit status 1,
	# redirect STDOUT and STDERR to a null register (will be discarded) ::: note 2> is for redirecting STDERR

# if error code is NOT EQUAL to 0:
	if [[ "$?" -ne 0 ]]; then
		echo "File $file does not have any foobar, adding one"
		echo "# foobar" >> "$file"
	fi
done
