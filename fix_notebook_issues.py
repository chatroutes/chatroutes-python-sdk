#!/usr/bin/env python3
"""
Fix issues in demo_complete_features.ipynb:
1. Remove duplicate summary (cell 35)
2. Renumber Part 5 (Token Savings) to Part 6 (cell 37)
3. Convert cell 38 to markdown if it contains markdown content
4. Renumber Part 6 (Visual Chart) to Part 7 (cell 39)
"""
import json

def fix_notebook():
    # Read notebook
    with open('demo_complete_features.ipynb', 'r', encoding='utf-8') as f:
        nb = json.load(f)

    print(f"Original notebook: {len(nb['cells'])} cells\n")

    # Issue 1: Remove duplicate summary in cell 35
    # Cell 35 is duplicate of cell 41, keep only cell 41
    cell_35_src = nb['cells'][35].get('source', [])
    if isinstance(cell_35_src, list):
        first_line = cell_35_src[0] if cell_35_src else ''
    else:
        first_line = cell_35_src

    # Check if it's the duplicate summary
    if 'CHATROUTES: KEY FEATURES' in first_line:
        print("Issue 1: Found duplicate summary in cell 35")
        print(f"   Removing cell 35 (duplicate summary)")
        del nb['cells'][35]
        print(f"   ✓ Cell 35 removed\n")

        # After removing cell 35, all subsequent cell indices shift down by 1
        # So old cell 36 is now cell 35, old cell 37 is now cell 36, etc.
        # Adjust our references:
        # Old cell 37 (Part 5 Token Savings) → Now cell 36
        # Old cell 38 (code with markdown) → Now cell 37
        # Old cell 39 (Part 6 Visual Chart) → Now cell 38
        cell_37_idx = 36
        cell_38_idx = 37
        cell_39_idx = 38
    else:
        print("Warning: Cell 35 doesn't look like duplicate summary")
        # Keep original indices
        cell_37_idx = 37
        cell_38_idx = 38
        cell_39_idx = 39

    # Issue 2: Renumber Part 5 to Part 6 in cell 37 (now cell 36)
    print(f"Issue 2: Renumbering Part 5 to Part 6 in cell {cell_37_idx}")
    cell_src = nb['cells'][cell_37_idx].get('source', [])
    if isinstance(cell_src, list):
        # Find and replace "Part 5" with "Part 6"
        for i, line in enumerate(cell_src):
            if 'Part 5: Token Savings' in line:
                cell_src[i] = line.replace('Part 5:', 'Part 6:')
                print(f"   ✓ Changed 'Part 5' to 'Part 6'\n")
                break

    # Issue 3: Check cell 38 (now cell 37) - if it's code with markdown, convert it
    print(f"Issue 3: Checking cell {cell_38_idx} for mixed content")
    cell_38 = nb['cells'][cell_38_idx]
    if cell_38.get('cell_type') == 'code':
        src = cell_38.get('source', [])
        if isinstance(src, list) and len(src) > 0:
            first_line = src[0]
            # If it starts with markdown-style heading, it's wrong
            if '##' in first_line and 'Part' in first_line:
                print(f"   Converting cell {cell_38_idx} from code to markdown")
                cell_38['cell_type'] = 'markdown'
                # Remove code-specific fields
                if 'execution_count' in cell_38:
                    del cell_38['execution_count']
                if 'outputs' in cell_38:
                    del cell_38['outputs']
                print(f"   ✓ Converted to markdown\n")

    # Issue 4: Renumber Part 6 to Part 7 in cell 39 (now cell 38)
    print(f"Issue 4: Renumbering Part 6 to Part 7 in cell {cell_39_idx}")
    cell_src = nb['cells'][cell_39_idx].get('source', [])
    if isinstance(cell_src, list):
        for i, line in enumerate(cell_src):
            if 'Part 6: Visual Comparison' in line:
                cell_src[i] = line.replace('Part 6:', 'Part 7:')
                print(f"   ✓ Changed 'Part 6' to 'Part 7'\n")
                break

    # Write fixed notebook
    with open('demo_complete_features.ipynb', 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

    print(f"✓ Fixed notebook saved!")
    print(f"   Original: 44 cells")
    print(f"   Fixed: {len(nb['cells'])} cells")
    print(f"\nChanges:")
    print(f"   1. Removed duplicate summary (cell 35)")
    print(f"   2. Renumbered 'Part 5: Token Savings' → 'Part 6'")
    print(f"   3. Converted mixed content cell to proper type")
    print(f"   4. Renumbered 'Part 6: Visual Chart' → 'Part 7'")

if __name__ == '__main__':
    fix_notebook()
