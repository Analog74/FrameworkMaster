import os
import toml
import json

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
SUMMARY_PATH = os.path.join(PROJECT_ROOT, "SYSTEMS_AND_LIBRARIES.md")

# Helper to find all files matching a pattern

def find_files(root, pattern):
    matches = []
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            if filename == pattern:
                matches.append(os.path.join(dirpath, filename))
    return matches

# Helper to extract info from wally.toml

def parse_wally_toml(path):
    try:
        data = toml.load(path)
        return data
    except Exception:
        return None

# Helper to extract info from README.md

def parse_readme(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        # Get first non-empty line as title, rest as summary
        title = None
        summary = []
        for line in lines:
            if not title and line.strip():
                title = line.strip().lstrip("# ")
            elif title:
                summary.append(line.strip())
        return title, " ".join(summary[:5])
    except Exception:
        return None, None

# Scan for systems (top-level folders in src/ReplicatedStorage)
systems = []
src_rs = os.path.join(PROJECT_ROOT, "src", "ReplicatedStorage")
if os.path.isdir(src_rs):
    for name in os.listdir(src_rs):
        path = os.path.join(src_rs, name)
        if os.path.isdir(path) and name not in ["ThirdParty", "FrameworkModules", "Packages"]:
            systems.append({
                "name": name,
                "path": os.path.relpath(path, PROJECT_ROOT)
            })

# Scan for third-party libraries
third_party = []
tp_dir = os.path.join(src_rs, "ThirdParty")
if os.path.isdir(tp_dir):
    for name in os.listdir(tp_dir):
        lib_path = os.path.join(tp_dir, name)
        if os.path.isdir(lib_path):
            # Try to get info from README.md or wally.toml
            readme = find_files(lib_path, "README.md")
            wally = find_files(lib_path, "wally.toml")
            title, summary = None, None
            if readme:
                title, summary = parse_readme(readme[0])
            wally_info = parse_wally_toml(wally[0]) if wally else None
            third_party.append({
                "name": title or name,
                "path": os.path.relpath(lib_path, PROJECT_ROOT),
                "summary": summary,
                "wally": wally_info
            })
        elif lib_path.endswith(".luau") or lib_path.endswith(".lua"):
            third_party.append({
                "name": name,
                "path": os.path.relpath(lib_path, PROJECT_ROOT),
                "summary": None,
                "wally": None
            })

# Write summary markdown
with open(SUMMARY_PATH, "w", encoding="utf-8") as f:
    f.write("# Project Systems and Libraries Summary\n\n")
    f.write("## Systems\n\n")
    for sys in systems:
        f.write(f"- **{sys['name']}**  \n  Path: `{sys['path']}`\n")
    f.write("\n## Third-Party Libraries\n\n")
    for lib in third_party:
        f.write(f"- **{lib['name']}**  \n  Path: `{lib['path']}`\n")
        if lib['summary']:
            f.write(f"  Summary: {lib['summary']}\n")
        if lib['wally'] is not None:
            f.write(f"  Wally: {json.dumps(lib['wally'])}\n")
        f.write("\n")
    f.write("---\n\nThis file is auto-generated. Run `python generate_systems_summary.py` to update.\n")
