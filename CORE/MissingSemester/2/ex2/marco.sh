#!/bin/bash
marco() {
	temp_file="/tmp/marco.txt"
	dir=$(pwd)
	pwd > ${temp_file}

	echo "Marco has spoken: Saved $dir to $temp_file." 
	echo "Say polo to get back there."
}
