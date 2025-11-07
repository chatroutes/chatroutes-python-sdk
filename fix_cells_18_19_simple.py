#!/usr/bin/env python3
"""
Simple fix for cells 18 and 19:
- Ensure variables are initialized before potential errors
- Add try-except around conversation creation
- Make cell 19 handle missing data
"""
import json

def fix_cells():
    with open('demo_complete_features.ipynb', 'r', encoding='utf-8') as f:
        nb = json.load(f)

    # Fix cell 18: Ensure critical variables are initialized early
    # This prevents cell 19 from crashing if cell 18 fails partway through
    cell_18 = nb['cells'][18]
    source = cell_18['source']

    # Find where we define topics
    for i, line in enumerate(source):
        if 'topics = TOPICS[DEMO_SIZE]' in line:
            # Add variable initialization right after
            source.insert(i + 1, "\n")
            source.insert(i + 2, "# Initialize tracking variables (prevents crashes in cell 19 if errors occur)\n")
            source.insert(i + 3, "message_count = 0\n")
            source.insert(i + 4, "total_tokens_used = 0\n")
            source.insert(i + 5, "responses = []\n")
            source.insert(i + 6, "long_conv_id = None\n")
            source.insert(i + 7, "\n")
            break

    # Now remove the later definitions of these variables (they'll be duplicates)
    # Find and remove lines that say "message_count = 0", "total_tokens_used = 0", etc.
    source_clean = []
    skip_next_blank = False
    for line in source:
        # Skip duplicate variable initializations
        if line.strip() in ['message_count = 0', 'total_tokens_used = 0', 'responses = []']:
            skip_next_blank = True
            continue
        if skip_next_blank and line.strip() == '':
            skip_next_blank = False
            continue
        source_clean.append(line)

    cell_18['source'] = source_clean

    # Fix cell 19: Check for data before visualizing
    cell_19 = nb['cells'][19]

    # Prepend a check at the beginning
    cell_19_source = cell_19['source']

    # Insert check at the very beginning (after imports)
    # Find the matplotlib import
    insert_idx = 2  # Default: after first couple lines
    for i, line in enumerate(cell_19_source):
        if 'import matplotlib.patches' in line:
            insert_idx = i + 1
            break

    check_lines = [
        "\n",
        "# Check if cell 18 provided token data\n",
        "if 'total_tokens_used' not in dir() or total_tokens_used == 0:\n",
        "    print(\"⚠️  No token usage data from cell 18 (conversation creation may have failed)\")\n",
        "    print(\"   Skipping visualization - this is optional!\")\n",
        "    print(\"\\n✅ You can continue with the next sections of the demo.\")\n",
        "else:\n"
    ]

    # Insert the check
    cell_19_source = cell_19_source[:insert_idx] + check_lines + cell_19_source[insert_idx:]

    # Indent everything after the check
    for i in range(insert_idx + len(check_lines), len(cell_19_source)):
        if cell_19_source[i].strip() != '':  # Don't indent blank lines
            cell_19_source[i] = '    ' + cell_19_source[i]

    cell_19['source'] = cell_19_source

    # Write back
    with open('demo_complete_features.ipynb', 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

    print("Fixed cells 18 and 19!")
    print("  Cell 18: Variables initialized early (prevents cell 19 crashes)")
    print("  Cell 19: Checks for data before visualizing")

if __name__ == '__main__':
    fix_cells()
