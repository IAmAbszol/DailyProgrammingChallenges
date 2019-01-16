#!/bin/bash

python unzippy.py

# Rips the xz, bzip2, gzip
while true;
do

	string=`file password*`
	if [[ $string == *"XZ"* ]]; then
		mv password* password.xz
		xz --decompress password.xz
		continue
	fi
	if [[ $string == *"bzip2 compressed data"* ]]; then
		mv password* password.bzip2
		bzip2 --decompress password.bzip2
		continue
	fi
	if [[ $string == *"gzip compressed data"* ]]; then
		mv password* password.gz
		gzip -d password.gz
		continue
	fi
	break

done
