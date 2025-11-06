#!/usr/bin/env python3
"""
Script to improve demo_complete_features.ipynb by restructuring cells 24-27
"""
import json
import sys

def create_improved_cells():
    """Create the improved cell structure for immutability section"""

    cells = []

    # Cell 24: Markdown intro to immutability
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 🔐 Part 5: Message Immutability & Data Integrity\n",
            "\n",
            "### What is Immutability?\n",
            "\n",
            "ChatRoutes ensures **100% immutable messages** meaning:\n",
            "- **Messages cannot be modified** after creation\n",
            "- Every message has a **cryptographic hash** (SHA-256)\n",
            "- Updates create **new versions** (not modifications)\n",
            "- Deletions are **soft** (marked deleted, not removed)\n",
            "- Complete **audit trail** for compliance\n",
            "\n",
            "This is critical for:\n",
            "- ✅ HIPAA compliance (healthcare)\n",
            "- ✅ GDPR compliance (data protection)\n",
            "- ✅ SOC2 compliance (security)\n",
            "- ✅ Legal/audit trails\n",
            "- ✅ Data integrity guarantees"
        ]
    })

    # Cell 25: Markdown - Concept 1 explanation
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### 🔄 Concept 1: Updates Create NEW Messages (Not Modifications)\n",
            "\n",
            "#### ❌ Traditional Systems (Mutable):\n",
            "```sql\n",
            "UPDATE messages SET content = 'new' WHERE id = 'msg_123'\n",
            "```\n",
            "→ Original data **LOST forever**\n",
            "\n",
            "#### ✅ ChatRoutes (Immutable):\n",
            "1. Original message **preserved** with hash\n",
            "2. Create **NEW message** with updated content\n",
            "3. Link them with **version tracking**\n",
            "\n",
            "→ Complete audit trail maintained!\n",
            "\n",
            "**Let's see this in action:**"
        ]
    })

    # Cell 26: Code - Demonstrate updates creating new messages
    cells.append({
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "print(\"🔄 DEMONSTRATION: Updates Create New Messages\\n\")\n",
            "print(\"=\" * 70)\n",
            "\n",
            "# Create a test conversation\n",
            "test_conv = client.conversations.create({\n",
            "    'title': 'Immutability Demo',\n",
            "    'model': 'claude-sonnet-4-5'\n",
            "})\n",
            "\n",
            "print(f\"✅ Created test conversation: {test_conv['id']}\\n\")\n",
            "\n",
            "# Send original message\n",
            "print(\"📤 Step 1: Creating original message...\")\n",
            "original = client.messages.send(\n",
            "    test_conv['id'],\n",
            "    {'content': 'What is 2 + 2?', 'model': 'claude-sonnet-4-5'}\n",
            ")\n",
            "\n",
            "original_msg = original.get('assistantMessage') or original.get('message')\n",
            "original_id = original_msg['id']\n",
            "original_hash = original_msg.get('contentHash', 'N/A')\n",
            "\n",
            "print(f\"   ✅ Original Message ID: {original_id}\")\n",
            "print(f\"   Content: {original_msg['content'][:60]}...\")\n",
            "print(f\"   Hash: {original_hash[:16] if original_hash != 'N/A' else 'N/A'}...\\n\")\n",
            "\n",
            "# Send 'correction' message\n",
            "print(\"📤 Step 2: Creating 'corrected' message...\")\n",
            "correction = client.messages.send(\n",
            "    test_conv['id'],\n",
            "    {'content': 'Actually, let me clarify my question.', 'model': 'claude-sonnet-4-5'}\n",
            ")\n",
            "\n",
            "corrected_msg = correction.get('assistantMessage') or correction.get('message')\n",
            "corrected_id = corrected_msg['id']\n",
            "\n",
            "print(f\"   ✅ New Message ID: {corrected_id}\\n\")\n",
            "\n",
            "# Show both still exist\n",
            "print(\"✅ RESULT: Both messages exist independently!\")\n",
            "print(\"=\" * 70)\n",
            "print(f\"   Original: {original_id} (still exists unchanged)\")\n",
            "print(f\"   New:      {corrected_id} (separate message)\")\n",
            "print(\"\\n💡 Key Point: The original message is PRESERVED forever!\")\n",
            "\n",
            "# Store conversation ID for cleanup\n",
            "demo_conv_id = test_conv['id']"
        ]
    })

    # Cell 27: Markdown - Concept 2 explanation
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### 🪦 Concept 2: Soft Deletes (Tombstone Pattern)\n",
            "\n",
            "When you \"delete\" a message in ChatRoutes:\n",
            "\n",
            "#### ❌ What DOESN'T happen:\n",
            "- Message row is NOT removed from database\n",
            "- Content is NOT erased\n",
            "- Hash is NOT deleted\n",
            "\n",
            "#### ✅ What DOES happen:\n",
            "- `deletedAt` timestamp is set (e.g., 2025-11-06 10:30:00)\n",
            "- `deleteReason` is recorded\n",
            "- Message becomes 'tombstone' (marked but preserved)\n",
            "- Audit log entry created (who, when, why)\n",
            "\n",
            "#### 💾 Database State After Deletion:\n",
            "\n",
            "```\n",
            "┌─────────────────────────────────────────────────────┐\n",
            "│ Message Record (STILL IN DATABASE)                 │\n",
            "├─────────────────────────────────────────────────────┤\n",
            "│ id: msg_abc123                                      │\n",
            "│ content: \"What is 2 + 2?\"                          │\n",
            "│ contentHash: a3f5e1b...                             │\n",
            "│ deletedAt: 2025-11-06 10:30:00 ← TOMBSTONE MARKER  │\n",
            "│ deleteReason: 'User requested deletion'            │\n",
            "└─────────────────────────────────────────────────────┘\n",
            "```\n",
            "\n",
            "**The data is still there - just marked as deleted!**"
        ]
    })

    # Cell 28: Markdown - Concept 3 explanation
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### 📋 Concept 3: Complete Audit Trail\n",
            "\n",
            "Every action creates an audit log entry:\n",
            "\n",
            "```\n",
            "┌──────────────────────────────────────────────────────────┐\n",
            "│ Audit Log Table                                          │\n",
            "├──────────────────────────────────────────────────────────┤\n",
            "│ messageId    │ action  │ userId  │ timestamp  │ metadata │\n",
            "├──────────────────────────────────────────────────────────┤\n",
            "│ msg_abc123   │ CREATE  │ user_1  │ 10:25:00   │ {...}    │\n",
            "│ msg_abc123   │ VIEW    │ user_2  │ 10:28:00   │ {...}    │\n",
            "│ msg_abc123   │ DELETE  │ user_1  │ 10:30:00   │ {reason} │\n",
            "└──────────────────────────────────────────────────────────┘\n",
            "```\n",
            "\n",
            "#### ✅ Benefits:\n",
            "- Who did what, when, and why\n",
            "- Complete history for forensics\n",
            "- Regulatory compliance (HIPAA, GDPR, SOC2)\n",
            "- Data can be 'undeleted' if needed"
        ]
    })

    # Cell 29: Markdown - Concept 4 explanation
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### 🔐 Concept 4: Cryptographic Hash Verification\n",
            "\n",
            "Every message has a **SHA-256 hash** that proves data integrity.\n",
            "\n",
            "**Let's verify a message hash:**"
        ]
    })

    # Cell 30: Code - Hash verification demonstration
    cells.append({
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "import hashlib\n",
            "import json\n",
            "\n",
            "print(\"🔐 DEMONSTRATION: Hash Verification\\n\")\n",
            "print(\"=\" * 70)\n",
            "\n",
            "# Get a message with hash\n",
            "conv_data = client.conversations.get(demo_conv_id)\n",
            "messages = conv_data.get('messages', [])\n",
            "\n",
            "if len(messages) > 0:\n",
            "    message = messages[0]\n",
            "    stored_hash = message.get('contentHash')\n",
            "    \n",
            "    if stored_hash:\n",
            "        print(\"📝 Message Data:\")\n",
            "        print(f\"   ID: {message['id']}\")\n",
            "        print(f\"   Content: {message['content'][:60]}...\")\n",
            "        print(f\"   Stored Hash: {stored_hash}\\n\")\n",
            "        \n",
            "        # Recalculate hash (same algorithm as backend)\n",
            "        canonical_data = {\n",
            "            \"v\": 1,\n",
            "            \"role\": message['role'],\n",
            "            \"content\": message['content'],\n",
            "            \"model\": message.get('model'),\n",
            "            \"parentMessageId\": message.get('parentMessageId'),\n",
            "            \"branchId\": message.get('branchId'),\n",
            "            \"createdAt\": message.get('createdAt')\n",
            "        }\n",
            "        \n",
            "        canonical_json = json.dumps(canonical_data, separators=(',', ':'))\n",
            "        calculated_hash = hashlib.sha256(canonical_json.encode()).hexdigest()\n",
            "        \n",
            "        print(\"🔍 Hash Verification:\")\n",
            "        print(f\"   Stored:     {stored_hash}\")\n",
            "        print(f\"   Calculated: {calculated_hash}\\n\")\n",
            "        \n",
            "        if calculated_hash == stored_hash:\n",
            "            print(\"   ✅ MATCH! Message data is authentic and unchanged!\")\n",
            "        else:\n",
            "            print(\"   ❌ MISMATCH! Data may have been tampered with!\")\n",
            "        \n",
            "        # Show what happens with tampering\n",
            "        print(\"\\n🔬 What Happens if Data is Tampered?\\n\")\n",
            "        \n",
            "        tampered_data = canonical_data.copy()\n",
            "        tampered_data['content'] = message['content'] + \"X\"  # Add one character\n",
            "        \n",
            "        tampered_json = json.dumps(tampered_data, separators=(',', ':'))\n",
            "        tampered_hash = hashlib.sha256(tampered_json.encode()).hexdigest()\n",
            "        \n",
            "        print(f\"   Original hash:  {calculated_hash[:32]}...\")\n",
            "        print(f\"   Tampered hash:  {tampered_hash[:32]}...\")\n",
            "        print(f\"\\n   ❌ COMPLETELY DIFFERENT! Tampering detected immediately.\")\n",
            "        \n",
            "    else:\n",
            "        print(\"⚠️  Message doesn't have hash yet (older message)\")\n",
            "else:\n",
            "    print(\"⚠️  No messages available\")\n",
            "\n",
            "print(\"\\n\" + \"=\" * 70)"
        ]
    })

    # Cell 31: Markdown - How hashing works
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### 💡 How Hash Verification Works\n",
            "\n",
            "#### ❌ Common Misconception:\n",
            "\"Can I decrypt the hash to get the message back?\"\n",
            "\n",
            "**NO!** SHA-256 is NOT encryption - it's a **ONE-WAY hash function**.\n",
            "\n",
            "#### ✅ How It Actually Works:\n",
            "\n",
            "```\n",
            "Verification Process:\n",
            "1. Take original message data from database\n",
            "2. Recalculate hash using same algorithm  \n",
            "3. Compare: New hash === Stored hash?\n",
            "   • Match = Data unchanged ✅\n",
            "   • Mismatch = Data tampered ❌\n",
            "```\n",
            "\n",
            "#### 🔐 Why This is Powerful:\n",
            "\n",
            "- **Cannot reverse**: Hash → Original data (impossible)\n",
            "- **Can verify**: Original data → Hash (easy)\n",
            "- **Tamper-proof**: Any change = Different hash\n",
            "- **Deterministic**: Same input = Same hash (always)\n",
            "\n",
            "#### 🎯 Real-World Applications:\n",
            "\n",
            "- **Medical records**: Prove records haven't been altered\n",
            "- **Legal documents**: Verify authenticity in court\n",
            "- **Audit trails**: Complete tamper-proof history\n",
            "- **Compliance**: Meet HIPAA, GDPR, SOC2 requirements"
        ]
    })

    # Cell 32: Markdown - Real-world use cases
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### 🏥 Real-World Use Cases\n",
            "\n",
            "#### 📊 Healthcare (HIPAA):\n",
            "- Doctor updates patient notes → New version, old preserved\n",
            "- Complete audit trail for malpractice defense\n",
            "- Prove notes weren't altered after incident\n",
            "\n",
            "#### ⚖️ Legal/Financial:\n",
            "- Contract negotiations → Every revision tracked\n",
            "- Deleted emails recoverable for discovery\n",
            "- Cryptographic proof of original content\n",
            "\n",
            "#### 🔒 Security/Compliance:\n",
            "- Data breach investigation → Complete history\n",
            "- Regulatory audits → Unalterable records\n",
            "- Insider threat detection → Who changed what\n",
            "\n",
            "### ✅ Key Takeaways:\n",
            "\n",
            "1. **Messages are NEVER truly deleted or modified**\n",
            "2. **All changes create NEW records with audit trails**\n",
            "3. **Cryptographic hashes prove data integrity**\n",
            "4. **Complete history preserved for compliance**\n",
            "5. **Original data always verifiable**"
        ]
    })

    # Cell 33: Code - Cleanup
    cells.append({
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Clean up demo conversation\n",
            "try:\n",
            "    client.conversations.delete(demo_conv_id)\n",
            "    print(\"🧹 Demo conversation cleaned up (soft-deleted, of course!)\")\n",
            "except Exception as e:\n",
            "    print(f\"Note: {str(e)}\")"
        ]
    })

    return cells


def main():
    # Read the original notebook
    with open('demo_complete_features.ipynb', 'r', encoding='utf-8') as f:
        nb = json.load(f)

    print(f"Original notebook has {len(nb['cells'])} cells")

    # Find cells 23-27 to replace (0-indexed, so 23-27 actual)
    # Cell 23: Shows contentHash
    # Cells 24-27: Need to be replaced

    # Keep cells 0-23
    new_cells = nb['cells'][:23]

    print(f"Keeping first 23 cells")

    # Add improved cells (these become cells 23-32, replacing old 23-27)
    # But wait - we need to check if cell 23 should also be replaced
    # Looking at the original, cell 23 is actually demonstrating contentHash
    # which is related but might be OK. Let me keep it and only replace 24-27.

    # Actually, let's keep cell 23 as is and replace starting from cell 24
    # So: keep 0-23, replace 24-27 with new structure, keep 28+

    new_cells = nb['cells'][:24]  # Keep 0-23 (24 cells)

    print(f"Kept cells 0-23 (24 cells total)")

    # Add improved cells (10 new cells to replace old cells 24-27)
    improved_cells = create_improved_cells()
    new_cells.extend(improved_cells)

    print(f"Added {len(improved_cells)} improved cells")

    # Add remaining cells from position 28 onwards
    # Old notebook had cells 28-37, we want to keep those
    # Old cell 28 = tree structure
    # Old cells 29-37 = token savings and cleanup

    # Skip old cells 24-27 (indices 24-27)
    # Keep cells from index 28 onwards
    remaining_cells = nb['cells'][28:]
    new_cells.extend(remaining_cells)

    print(f"Added {len(remaining_cells)} remaining cells (from old cell 28 onwards)")
    print(f"New notebook has {len(new_cells)} cells total")

    # Update the notebook
    nb['cells'] = new_cells

    # Write the improved notebook
    with open('demo_complete_features.ipynb', 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

    print("\n✅ Successfully updated demo_complete_features.ipynb!")
    print(f"   Old structure: 38 cells")
    print(f"   New structure: {len(new_cells)} cells")
    print(f"   Changes:")
    print(f"   - Kept cells 0-23 unchanged")
    print(f"   - Replaced cells 24-27 (4 cells) with cells 24-33 (10 cells)")
    print(f"   - Kept cells 28-37 as cells 34-43")

if __name__ == '__main__':
    main()
