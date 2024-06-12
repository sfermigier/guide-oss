#!/usr/bin/env python3

import os
from pathlib import Path

for source in Path('source').rglob('*.md'):
    target = source.with_suffix('.rst')
    if target.exists():
        if target.stat().st_mtime > source.stat().st_mtime:
            print("Skipping", source)
            continue

    print("Transforming", source)
    os.system(f"pandoc {source} -o {target}")
