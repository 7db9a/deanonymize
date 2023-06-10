import csv
import fileinput
import os
import argparse

# Create the parser
parser = argparse.ArgumentParser(description='Process a directory and a csv file.')
parser.add_argument('docs_directory', type=str, help='The directory to process')
parser.add_argument('csv_file', type=str, help='The CSV file to use')

# Parse the arguments
args = parser.parse_args()

# Now we use the arguments
csv_file = args.csv_file
docs_directory = args.docs_directory

# First, we need to read the csv file and create a dictionary where the keys are the aliases
# and the values are the names
aliases_to_names = {}
with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        aliases_to_names[row['alias']] = row['name']

# Then, we can iterate over each file in the docs directory
for filename in os.listdir(docs_directory):
    # We'll only process text files
    if filename.endswith('.txt'):
        filepath = os.path.join(docs_directory, filename)
        # We'll use fileinput to process the file in-place
        with fileinput.FileInput(filepath, inplace=True) as file:
            for line in file:
                # For each line in the file, we'll replace each occurrence of an alias with its corresponding name
                for alias, name in aliases_to_names.items():
                    line = line.replace(alias, name)
                # Print the modified line (fileinput redirects this print to the file)
                print(line, end='')