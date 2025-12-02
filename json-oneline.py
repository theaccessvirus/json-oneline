import json
import sys

def format_max_patch(input_file, output_file=None):
    with open(input_file, 'r') as f:
        patch = json.load(f)
    
    if output_file is None:
        output_file = input_file.replace('.maxpat', '_compact.maxpat')
        if output_file == input_file:
            output_file = input_file + '_compact'
    
    lines = ['{']
    
    keys = list(patch.keys())
    for i, key in enumerate(keys):
        value = patch[key]
        comma = ',' if i < len(keys) - 1 else ''
        
        if key == 'boxes':
            lines.append('  "boxes": [')
            for j, box in enumerate(value):
                box_comma = ',' if j < len(value) - 1 else ''
                lines.append('    ' + json.dumps(box, separators=(',', ':')) + box_comma)
            lines.append('  ]' + comma)
        
        elif key == 'lines':
            lines.append('  "lines": [')
            for j, line in enumerate(value):
                line_comma = ',' if j < len(value) - 1 else ''
                lines.append('    ' + json.dumps(line, separators=(',', ':')) + line_comma)
            lines.append('  ]' + comma)
        
        else:
            lines.append('  ' + json.dumps(key) + ':' + json.dumps(value, separators=(',', ':')) + comma)
    
    lines.append('}')
    
    with open(output_file, 'w') as f:
        f.write('\n'.join(lines))
    
    print(f"Saved to: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python compact_patch.py input.maxpat [output.maxpat]")
    else:
        output = sys.argv[2] if len(sys.argv) > 2 else None
        format_max_patch(sys.argv[1], output)