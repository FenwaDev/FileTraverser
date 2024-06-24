#!/usr/bin/env python3

import os
import argparse

def traverse_directory(path, max_files, min_size):
    files = []
    for root, _, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(root, filename)
            size_in_mb = os.path.getsize(filepath) / (1024 * 1024)
            if size_in_mb >= min_size:
                files.append((filepath, size_in_mb))
            if len(files) >= max_files:
                break
        if len(files) >= max_files:
            break

    print(f"Found {len(files)} files:")
    for file, size in files:
        print(f"{file} - {size:.2f} MB")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Traverse directory and list files based on criteria.")
    parser.add_argument("path", help="Path to traverse.")
    parser.add_argument("--max-files", type=int, default=20, help="Maximum number of files to list.")
    parser.add_argument("--min-size", type=float, default=0, help="Minimum file size in MB.")

    args = parser.parse_args()

    traverse_directory(args.path, args.max_files, args.min_size)
