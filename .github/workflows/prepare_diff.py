#!/usr/bin/python
import sys
import re

if len(sys.argv) != 3:
    exit("usage: " + sys.argv[0] + " new_file old_file")

try:
    f = open(sys.argv[1], "r")
    content = f.read()
    f.close()
    f = open(sys.argv[2], "r")
    content_old = f.read()
    f.close()
except IOError:
    exit("Greska pri otvaranju fajla")
  
type = r"int[*]?"
args = type + r"\s+[*]*[a-zA-Z_]\w*" + r"(\s*[,]\s+" + type + r"\s+[*]*[a-zA-Z_]\w*)*"
function_pattern  = r"^" + "(" + type + "|void)" + r"\s+" + r"([a-z])" + r"\s*[(](" + args + r")\s*[)]\s*[{]\s*"
function_pattern += r"(\n|.)*?^[}]"
    
p1 = re.search(function_pattern, content, re.M)
p2 = re.search(function_pattern, content_old, re.M)
fn1 = p1.group()
fn2 = p2.group()
fn2 = fn2.replace(p2.group(2), chr(ord(p1.group(2))+1), 1)

new_content = content.replace(fn1, fn1 + "\n\n" + fn2, 1)
print new_content
