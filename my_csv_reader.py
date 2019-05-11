#!usr/bin/env python

import os


file_path = 'housing.data'


if os.path.isfile(file_path):
    print('I have a valid file!!!')
else:
    print('Invalid file, I\'ll crash')

file = open('housing.data')


for line in file.readlines():
    clean_line = line.replace('  ', ' ').replace('  ', ' ').strip()
    line_values = clean_line.split(' ')

    corrected_line = []
    corrected_file = []

    for value in line_values:

        if value.find('.') != -1:
            corrected_line.append(float(value.strip("'")))
            corrected_file.append(corrected_line)

        else:
            corrected_line.append(int(value.strip()))
            corrected_file.append(corrected_line)



print(corrected_file)

file.close()