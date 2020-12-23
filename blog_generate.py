import time
import argparse
import os

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--md', type=str, default=None)

args = parser.parse_args()
md_path = args.md

blog_name = md_path.split('/')[-1].split('.')[0]
now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

file_header = '''
---
title: %s
date: %s
tags:
---
''' % (blog_name, now)

# 2 add file header
with open(md_path, "r+") as f:
    old = f.read()
    f.seek(0)
    f.write(file_header)
    f.write(old)
