import os
import zipfile
from pathlib import Path

# Patterns to exclude
EXCLUDE_PATTERNS = [
    '.venv',
    '.git',
    '__pycache__',
    '.pyc',
    '.pyo',
    '.DS_Store',
    'project-management',
    'reference',
    'PITCH_SPEECH.md',
    'INTERACTIVITY_STRATEGY.md',
    'SDG_ALTERNATIVES.md',
    'BRANCHING_STRATEGY.md',
    'GOOGLE_DRIVE_BACKUP.md',
    'SUBMISSION_PREP.md',
    'artifacts',
    'scripts',
    '.zip',
]

# Files/folders to include
INCLUDE_PATTERNS = [
    'README.md',
    'SUBMISSION_GUIDE_FOR_JUDGES.txt',
    'notebooks/',
    'data/',
    'visualizations/',
    'presentation/',
    'docs/technical/',
    'docs/guides/SUBMISSION_PACKAGE.md',
    'docs/guides/PRESENTATION_DECK.md',
    'docs/guides/QUESTIONS_ANSWERED.md',
]

def should_exclude(path_str):
    """Check if path should be excluded"""
    for pattern in EXCLUDE_PATTERNS:
        if pattern in path_str:
            return True
    return False

def should_include(rel_path):
    """Check if path should be included"""
    # Root level files
    if rel_path in ['README.md', 'SUBMISSION_GUIDE_FOR_JUDGES.txt']:
        return True
    
    # Check directories - normalize paths
    rel_normalized = rel_path.replace('\\', '/')
    
    for pattern in INCLUDE_PATTERNS:
        # Remove trailing slash for comparison
        pattern_clean = pattern.rstrip('/')
        if rel_normalized.startswith(pattern_clean + '/') or rel_normalized == pattern_clean:
            return True
    
    return False

# Base directory
base_dir = Path(r'C:\Users\USER\Documents\10Alatytics-2025')
output_zip = Path(r'C:\Users\USER\Documents\10Alatytics-2025\artifacts\10Alytics_Basit_Balogun_Working_Files_Submission.zip')

print(f"Creating submission ZIP: {output_zip}")
print(f"Source directory: {base_dir}\n")

# Create ZIP file
with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
    file_count = 0
    total_size = 0
    
    # Walk through directory
    for root, dirs, files in os.walk(base_dir):
        # Get relative path
        rel_root = os.path.relpath(root, base_dir.parent)
        
        # Skip excluded directories
        dirs[:] = [d for d in dirs if not should_exclude(os.path.join(rel_root, d))]
        
        for file in files:
            file_path = Path(root) / file
            rel_path = os.path.relpath(file_path, base_dir.parent)
            
            # Check if should be excluded
            if should_exclude(str(rel_path)):
                continue
            
            # Check if should be included (starts with any include pattern)
            rel_from_base = os.path.relpath(file_path, base_dir)
            if not should_include(rel_from_base):
                continue
            
            # Add to ZIP
            zipf.write(file_path, rel_path)
            file_size = file_path.stat().st_size
            total_size += file_size
            file_count += 1
            print(f"✓ Added: {rel_from_base} ({file_size:,} bytes)")

print(f"\n{'='*60}")
print(f"ZIP creation complete!")
print(f"Total files: {file_count}")
print(f"Total size: {total_size:,} bytes ({total_size / 1024 / 1024:.2f} MB)")
print(f"Output: {output_zip}")
print(f"{'='*60}")
