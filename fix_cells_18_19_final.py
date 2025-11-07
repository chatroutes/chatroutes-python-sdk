#!/usr/bin/env python3
"""
Fix cells 18 and 19 to handle API errors gracefully.

The issue is that if cell 18's conversation creation fails early,
the variables won't be defined and cell 19 will crash.

Solution:
- Cell 18: Initialize variables at the top
- Cell 19: Check if variables exist before using them
"""
import json

def fix_cells():
    with open('demo_complete_features.ipynb', 'r', encoding='utf-8') as f:
        nb = json.load(f)

    # Cell 18: The issue is that message_count, total_tokens_used, responses
    # are defined AFTER the conversation creation. If that fails, they won't exist.
    # Move them to the beginning.

    cell_18 = nb['cells'][18]
    source = cell_18['source']
    if isinstance(source, str):
        source = [source]

    # Find where topics is defined and add variables right after
    new_source = []
    vars_added = False
    for line in source:
        new_source.append(line)
        if not vars_added and 'topics = TOPICS[DEMO_SIZE]' in line:
            new_source.extend([
                "\n",
                "# Initialize variables early (prevents cell 19 from crashing if errors occur)\n",
                "message_count = 0\n",
                "total_tokens_used = 0\n",
                "responses = []\n",
                "long_conv_id = None\n",
                "\n"
            ])
            vars_added = True

    # Remove duplicate variable definitions later in the cell
    final_source = []
    for line in new_source:
        # Skip lines that are now duplicates
        if line.strip() in ['message_count = 0', 'total_tokens_used = 0', 'responses = []']:
            continue
        final_source.append(line)

    cell_18['source'] = final_source

    # Cell 19: Add check at the beginning
    cell_19 = nb['cells'][19]
    source_19 = cell_19['source']
    if isinstance(source_19, str):
        source_19 = [source_19]

    # Add check before the calculation
    new_source_19 = []
    check_added = False
    indent_level = 0

    for line in source_19:
        if not check_added and 'parts_1_2_estimate = 2000' in line:
            # Add the check before this line
            new_source_19.extend([
                "\n",
                "# Verify we have token data from cell 18\n",
                "if 'total_tokens_used' not in dir() or total_tokens_used == 0:\n",
                "    print(\"⚠️  No token usage data (cell 18 may have encountered errors)\")\n",
                "    print(\"   Skipping visualization - this section is optional!\")\n",
                "    print(\"\\n✅ You can continue with the remaining demos.\")\n",
                "else:\n"
            ])
            check_added = True
            indent_level = 4  # Start indenting

        # Add the line with appropriate indentation
        if indent_level > 0 and line.strip() != '':
            new_source_19.append(' ' * indent_level + line)
        else:
            new_source_19.append(line)

    cell_19['source'] = new_source_19

    # Save
    with open('demo_complete_features.ipynb', 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

    print("Fixed cells 18 and 19!")
    print("   Cell 18: Variables initialized early")
    print("   Cell 19: Checks for data before visualizing")

if __name__ == '__main__':
    fix_cells()
