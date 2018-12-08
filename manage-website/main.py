#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import subprocess
import os

def main():
    home_path = os.path.expanduser('~')
    
    if len(sys.argv) == 1:
        print("Invalid argments")                
    elif sys.argv[1] == "add":
        with open(home_path + "/.useful_scripts/manage-website/websites.txt", "a") as f:
            f.write("{} {}\n".format(sys.argv[2], sys.argv[3]))
    elif sys.argv[1] == "list":
        with open(home_path + "/.useful_scripts/manage-website/websites.txt", "r") as f:
            contents = f.readlines()
        for content in contents:
            id = content.split(" ")[0]
            url = content.split(" ")[1][:-1]
            print("{} \t {}".format(id, url))
    elif sys.argv[1] == "remove":   # TODO
        pass
    elif sys.argv[1] == "show":
        if len(sys.argv) != 3:
            print("Invalid argments")
            return
        if "https://" in sys.argv[2] or "http://" in sys.argv[2]:
            subprocess.call(["chromium-browser", sys.argv[2]])
        else:
            with open(home_path + "/.useful_scripts/manage-website/websites.txt", "r") as f:
                contents = f.readlines()
            for content in contents:
                id = content.split(" ")[0]
                url = content.split(" ")[1][:-1]
                if id == sys.argv[2]:
                    print(url)
                    subprocess.call(["chromium-browser", url])
                    return
            print("There is no URL of {}".format(sys.argv[2]))
    else:
        print("Invalid argments")        

if __name__ == '__main__':
    main()
