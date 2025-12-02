import json
import sys

def format_max_patch(input_file):
    with open(input_file, 'r') as f:
        patch = json.load(f)
    
    if input_file.endswith('.maxpat'):
        output_file = input_file.replace('.maxpat', '_compact.maxpat')
    elif input_file.endswith('.json'):
        output_file = input_file.replace('.json', '_compact.json')
    else:
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

for f in sys.argv[1:]:
    if f.endswith('.maxpat') or f.endswith('.json'):
        format_max_patch(f)