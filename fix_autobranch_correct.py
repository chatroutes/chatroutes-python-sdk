#!/usr/bin/env python3
"""
Correctly fix AutoBranch section ordering.

Current (BROKEN) order:
  Cell 11: Summary markdown
  Cell 12-14: USE autobranch_available (ERROR!)
  Cell 15: DEFINES autobranch_available
  Cell 16: Intro markdown

Correct order should be:
  Cell 11: Intro markdown (Part 2.5)
  Cell 12: Health check (DEFINES autobranch_available)
  Cell 13-15: Pattern detection, hybrid, practical (USE autobranch_available)
  Cell 16: Summary markdown
"""
import json

def fix_autobranch_correct():
    with open('demo_complete_features.ipynb', 'r', encoding='utf-8') as f:
        nb = json.load(f)

    cells = nb['cells']
    autobranch_cells = cells[11:17]  # Extract cells 11-16

    # Current order in autobranch_cells array:
    # [0] = Cell 11 = Summary
    # [1] = Cell 12 = Practical example (uses variable)
    # [2] = Cell 13 = Hybrid detection (uses variable)
    # [3] = Cell 14 = Pattern detection (uses variable)
    # [4] = Cell 15 = Health check (DEFINES variable)
    # [5] = Cell 16 = Intro

    # Correct order should be:
    # Intro → Health check → Pattern → Hybrid → Practical → Summary

    reordered = [
        autobranch_cells[5],  # Intro (was cell 16)
        autobranch_cells[4],  # Health check (was cell 15) - DEFINES variable
        autobranch_cells[3],  # Pattern detection (was cell 14)
        autobranch_cells[2],  # Hybrid detection (was cell 13)
        autobranch_cells[1],  # Practical example (was cell 12)
        autobranch_cells[0],  # Summary (was cell 11)
    ]

    # Rebuild notebook
    nb['cells'] = cells[:11] + reordered + cells[17:]

    # Write fixed notebook
    with open('demo_complete_features.ipynb', 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

    # Verify the fix
    with open('autobranch_fixed.txt', 'w', encoding='utf-8') as out:
        out.write('Fixed AutoBranch section order:\n')
        for idx in range(11, 17):
            cell = nb['cells'][idx]
            cell_type = cell.get('cell_type')
            src = ''.join(cell.get('source', [])) if isinstance(cell.get('source', []), list) else cell.get('source', '')

            defines = 'DEFINES autobranch_available' if 'autobranch_available = ' in src else ''
            uses = 'USES autobranch_available' if ('autobranch_available' in src and 'autobranch_available = ' not in src) else ''
            status = f' -> {defines}{uses}' if (defines or uses) else ''

            first_line = src.split('\n')[0][:60]
            out.write(f'  Cell {idx} ({cell_type}): {first_line}...{status}\n')

    print("Fixed! Check autobranch_fixed.txt for verification")

if __name__ == '__main__':
    fix_autobranch_correct()
