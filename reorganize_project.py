import os
import shutil
import json
from datetime import datetime

# Project root (destination)
root = "/Users/analog/Documents/Roblox/_Projects/FrameworkRestructure"

# Source folder for FrameworkModules and other files
source_dir = "/Users/analog/Documents/Roblox/_Projects/FrameworkModules/FrameworkModules"

# Duplicates to archive
duplicates = [
    ("SpellCombatSystem.markdown", "duplicates/archive/2025-07-03/SpellCombatSystem_1.markdown"),
    ("SpellCombatSystem_2.markdown", "duplicates/archive/2025-07-03/SpellCombatSystem_2.markdown"),
    ("SpellCombatSystem_GUI_Integration.markdown", "duplicates/archive/2025-07-03/SpellCombatSystem_GUI_Integration_1.markdown"),
    ("SpellCombatSystem_GUI_Integration_2.markdown", "duplicates/archive/2025-07-03/SpellCombatSystem_GUI_Integration_2.markdown"),
    ("spell_database.lua", "duplicates/archive/2025-07-03/spell_database.lua"),
    ("FX_System.markdown", "duplicates/archive/2025-07-03/FX_System.markdown")
]

# Documentation files to merge/copy
consolidated_docs = {
    "README.md": "docs/README.md",
    "GUI_Integration.md": "docs/GUI_Integration.md",
    "FX_System.md": "docs/FX_System.md",
    "SETUP.md": "docs/SETUP.md"
}

# Root-level files to copy
root_files = ["default.project.json", "spells.json", "generate_lua.py", "reorganize_project.py"]

# Helper: Recursively copy all files/folders except those in skip_list
skip_list = set([src for src, _ in duplicates])
def recursive_copy(src_dir, dst_dir, skip_list):
    for rootdir, dirs, files in os.walk(src_dir):
        rel_dir = os.path.relpath(rootdir, src_dir)
        # Compute destination directory
        if rel_dir == ".":
            dest_dir = dst_dir
        else:
            dest_dir = os.path.join(dst_dir, rel_dir)
        os.makedirs(dest_dir, exist_ok=True)
        for file in files:
            if file in skip_list:
                continue
            src_file = os.path.join(rootdir, file)
            dst_file = os.path.join(dest_dir, file)
            if not os.path.exists(dst_file):
                shutil.copy2(src_file, dst_file)
                print(f"Copied {src_file} to {dst_file}")
            else:
                print(f"Skipped (already exists): {dst_file}")

# 1. Create all needed directories
folders = [
    "duplicates/archive/2025-07-03",
    "docs",
    "src/ReplicatedStorage/SpellCombatSystem/Scripts",
    "src/ReplicatedStorage/SpellCombatSystem/Spells",
    "src/ReplicatedStorage/SpellCombatSystem/MovementConfigs",
    "src/ReplicatedStorage/SpellCombatSystem/EffectConfigs",
    "src/ReplicatedStorage/SpellCombatSystem/GUIConfigs",
    "src/ReplicatedStorage/FrameworkModules",
    "src/ReplicatedStorage/ThirdParty/ZonePlus",
    "src/ReplicatedStorage/ThirdParty/Roact",
    "src/ReplicatedStorage/ThirdParty/RoactRadial",
    "src/ReplicatedStorage/ThirdParty/Iris",
    "src/ReplicatedStorage/ThirdParty/RbxGuiLib",
    "src/ReplicatedStorage/Assets/GUIGraphics/Images",
    "src/ReplicatedStorage/Assets/GUIGraphics/Templates",
    "src/ReplicatedStorage/Assets/GUIGraphics/Animations",
    "src/ServerScriptService/Tools",
    "src/StarterPlayer/StarterPlayerScripts/SpellCombatSystemClient",
    "src/ServerStorage/Plugins"
]
for d in folders:
    os.makedirs(os.path.join(root, d), exist_ok=True)

# 2. Archive duplicates
for src, dst in duplicates:
    src_path = os.path.join(source_dir, src)
    dst_path = os.path.join(root, dst)
    if os.path.exists(src_path):
        shutil.move(src_path, dst_path)
        print(f"Archived {src} to {dst}")
    else:
        print(f"Warning: {src} not found for archiving")

# 3. Copy root-level files
for file in root_files:
    src_path = os.path.join(source_dir, file)
    dst_path = os.path.join(root, file)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path)
        print(f"Copied {file} to project root")
    else:
        print(f"Warning: {file} not found in source root")

# 4. Copy/merge documentation
for src, dst in consolidated_docs.items():
    src_path = os.path.join(source_dir, src)
    dst_path = os.path.join(root, dst)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path)
        print(f"Copied {src} to {dst}")
    else:
        print(f"Warning: {src} not found for docs")

# 5. Recursively copy all remaining files/folders (except archived/handled above)
recursive_copy(source_dir, os.path.join(root, "src/ReplicatedStorage/FrameworkModules"), skip_list)

# 6. Create ProgressTracking.json
progress_tracking = {
    "milestones": [
        {"phase": "Core Setup", "status": "Pending", "date": "2025-07-03"},
        {"phase": "GUI Integration", "status": "Pending", "date": "2025-07-03"},
        {"phase": "Optimization", "status": "Pending", "date": "2025-07-03"},
        {"phase": "Iteration", "status": "Pending", "date": "2025-07-03"}
    ]
}
with open(os.path.join(root, "src/ServerStorage/ProgressTracking.json"), "w") as f:
    json.dump(progress_tracking, f, indent=2)
print("Created: src/ServerStorage/ProgressTracking.json")

print("Reorganization complete. Run 'python3 generate_lua.py' to generate spell modules and tooling.")
