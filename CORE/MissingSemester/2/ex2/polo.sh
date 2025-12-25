#!/bin/bash
# ! is NOT and -f is "does this path exist+is it a file"
polo() {
	temp_file="/tmp/marco.txt"
	if [[ ! -f "$temp_file" ]]; then
		echo "Nobody said marco"
		return 1
	fi
	dir=$(< "$temp_file")
	echo "moving to $dir"
	cd $dir
	if [[ $? -eq 0 ]]; then
		echo "Success"
	fi
}
