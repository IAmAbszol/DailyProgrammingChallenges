import zipfile
import os

while True:
	files = [f for f in os.listdir(".")]
	for file in files:
		if "password" in file:
			with zipfile.ZipFile(file, 'r') as zip_ref:
				zip_ref.extractall(".")

			os.remove(file)
