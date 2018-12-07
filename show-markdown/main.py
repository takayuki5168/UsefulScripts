#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import markdown
import sys
import subprocess

def main():
    md = markdown.Markdown()
    
    with open(sys.argv[1], "r") as f:
        markdown_text_list = f.readlines()
        
    markdown_text = ""
    for mt in markdown_text_list:
        markdown_text += mt
    
    with open("/tmp/test.html", "w") as f:
        f.write(md.convert(markdown_text))
        
    subprocess.call(["chromium-browser", "/tmp/test.html"])
    subprocess.call(["rm", "/tmp/test.html"])

if __name__ == '__main__':
    main() # 0:today, 1:tommorow
