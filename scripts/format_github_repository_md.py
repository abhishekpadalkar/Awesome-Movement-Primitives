#!/usr/bin/env python3

#Purpose: reformat markdown file github link into awesome format

match_str = 'https://github.com/'

with open('README.md', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if len(line) > len(match_str):
        if match_str in line[:len(match_str)+1]:
            cl_line = line.split('\n')[0]
            authrepo = line.split(match_str)[1].split('\n')[0]
            sg_ico = f"https://img.shields.io/github/stars/{authrepo}?style=social"
            lines[i] = f"[{authrepo}]({cl_line}):  [![GitHub stars]({sg_ico})]({sg_link}/stargazers/)\n"

with open('README.md', 'w') as f:
    f.writelines(lines)
