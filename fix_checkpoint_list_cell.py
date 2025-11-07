#!/usr/bin/env python3
"""
Fix checkpoint listing cell (cell 22) to add robust error handling.
"""
import json

def fix_checkpoint_list_cell():
    with open('demo_complete_features.ipynb', 'r', encoding='utf-8') as f:
        nb = json.load(f)

    # Find cell 22 (checkpoint listing)
    cell_22 = nb['cells'][22]

    # New cell content with error handling
    new_source = [
        "print(\"Listing all checkpoints for this conversation...\\n\")\n",
        "\n",
        "try:\n",
        "    checkpoints = client.checkpoints.list(long_conv_id)\n",
        "    \n",
        "    print(f\"✅ Found {len(checkpoints)} checkpoint(s)\\n\")\n",
        "    \n",
        "    for i, cp in enumerate(checkpoints, 1):\n",
        "        token_count = cp.get('tokenCount') or cp.get('token_count')\n",
        "        created_at = cp.get('createdAt') or cp.get('created_at')\n",
        "        \n",
        "        print(f\"Checkpoint {i}:\")\n",
        "        print(f\"   ID: {cp['id'][:16]}...\")\n",
        "        print(f\"   Tokens: {token_count}\")\n",
        "        print(f\"   Created: {created_at}\")\n",
        "        print(f\"   Summary: {cp['summary'][:100]}...\")\n",
        "        print()\n",
        "        \n",
        "except Exception as e:\n",
        "    error_msg = str(e)\n",
        "    print(f\"❌ Error listing checkpoints: {error_msg}\")\n",
        "    print(f\"\\n💡 Troubleshooting:\")\n",
        "    \n",
        "    if 'Invalid JSON' in error_msg:\n",
        "        print(\"   • API returned malformed response - likely a temporary server issue\")\n",
        "        print(\"   • Try running this cell again in a few moments\")\n",
        "        print(\"   • This is optional - you can skip to the next section\")\n",
        "    elif 'not found' in error_msg.lower():\n",
        "        print(\"   • The conversation may have been deleted\")\n",
        "        print(\"   • No checkpoints exist yet (cell 21 may have failed)\")\n",
        "    else:\n",
        "        print(\"   • Check your internet connection\")\n",
        "        print(\"   • Verify the conversation still exists\")\n",
        "    \n",
        "    print(\"\\n✅ This is just a review step - you can continue with the demo!\")"
    ]

    # Update the cell
    cell_22['source'] = new_source

    # Write back to notebook
    with open('demo_complete_features.ipynb', 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

    print("Fixed checkpoint listing cell!")
    print("  - Added comprehensive error handling")
    print("  - Added helpful troubleshooting messages")
    print("  - Notebook will continue gracefully even if API fails")

if __name__ == '__main__':
    fix_checkpoint_list_cell()
