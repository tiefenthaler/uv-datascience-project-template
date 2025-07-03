import sys
from pathlib import Path

"""Script to compare configuration files between the root and template directories.

This script checks for consistency between key configuration files in the project's
root directory and those within the `{{cookiecutter.repo_name}}` template directory.
It reports identical, different, and missing files to help maintain synchronization
between the template and the generated projects.
"""

# Define the files to compare
files_to_compare = [
    # ".pre-commit-config.yaml",
]

# Define the root and template directories
root_dir = Path(__file__).parent.parent
template_dir = root_dir / "{{cookiecutter.repo_name}}"

# Store the results of the comparison
results = {"identical": [], "different": [], "missing_in_template": [], "missing_in_root": []}

# Compare the files
for file in files_to_compare:
    root_file = root_dir / file
    template_file = template_dir / file

    if root_file.exists() and template_file.exists():
        if root_file.read_text() == template_file.read_text():
            results["identical"].append(file)
        else:
            results["different"].append(file)
    elif root_file.exists():
        results["missing_in_template"].append(file)
    else:
        results["missing_in_root"].append(file)

# Print the results
print("--- Template Sync Check Results ---")

if results["different"]:
    print("\n❌ Different files:")
    for file in results["different"]:
        print(f"  - {file}")

if results["missing_in_template"]:
    print("\n❌ Files missing in template:")
    for file in results["missing_in_template"]:
        print(f"  - {file}")

if results["missing_in_root"]:
    print("\n❌ Files missing in root:")
    for file in results["missing_in_root"]:
        print(f"  - {file}")

if (
    not results["different"]
    and not results["missing_in_template"]
    and not results["missing_in_root"]
):
    print("\n✅ All files are in sync!")

# Exit with a non-zero status code if there are differences
if results["different"] or results["missing_in_template"] or results["missing_in_root"]:
    sys.exit(1)
