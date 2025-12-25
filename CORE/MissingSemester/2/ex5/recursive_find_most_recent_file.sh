#!/usr/bin/env bash

# Task it to write a command/script to recursively (directory, in directory, in directory) find the most recenetly modified file in a directory. More generally, can you list all files by recency?
# I do believe listing all files by recency was part of ex1.

find . -type f -printf "%T@ %t %p\n" | sort -n | tail -1

# %T@ time in seconds since Jan 1 1970
# %t last modification in time in ctime
# %p file name

# sort -n is numerical sort, always ascending, so we're after the last file (tail -1)

