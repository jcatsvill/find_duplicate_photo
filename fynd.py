import os
import sys
from hashlib import md5
from collections import defaultdict

def find_duplicates(work_dir):
    duplicates = defaultdict(list)
    for root, _, files in os.walk(work_dir):
        for f in files:
            f_name = os.path.join(root, f)
            f_hash = md5(open(f_name, 'rb').read()).hexdigest()
            duplicates[f_hash].append(f_name)
    return duplicates

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Example: python find.py /paht/to/work/dir")
        sys.exit(0)

    work_dir = sys.argv[1]
    duplicates = find_duplicates(work_dir)

    for f_hash, f_names in duplicates.items():
        if len(f_names) > 1:
            print(f_hash)
            for f_name in f_names:
                print(f"  -->{f_name}")
