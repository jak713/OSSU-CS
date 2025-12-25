#!/usr/bin/env bash

count=0

while ./command2debug.sh &>> debug.out; do
	((count++))
done

echo "function ran $count times" >> debug.out
echo "Loop finished"
