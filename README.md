# Max Patch Formatter

A command-line tool to format Max/MSP/M4L (Max For Live) patch files (.maxpat) or JSON files into a more compact and readable format.
**If you have M4L (Max For Live device) open the patch in max and select all -> copy/paste to any text editor and save as JSON.**

## Features

- Converts Max/MSP patch files to a more readable format
- Creates a new file with "_compact" suffix
- Preserves all functionality of the original patch
- Special handling for "boxes" and "lines" arrays for better readability
- Works with both .maxpat and .json files

## Usage

python format_max_patch.py file1.maxpat file2.maxpat file3.json

## Output

For each input file, a new file will be created with "_compact" added to the filename:
- file1.maxpat → file1_compact.maxpat
- file2.maxpat → file2_compact.maxpat
- file3.json → file3_compact.json
