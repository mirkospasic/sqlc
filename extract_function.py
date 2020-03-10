#!/usr/bin/python
import sys
import re

if len(sys.argv) != 2:
    exit("usage: " + sys.argv[0] + " new_file")

try:
    f = open(sys.argv[1], "r")
    content = f.read()
    f.close()
except IOError:
    exit("Greska pri otvaranju fajla")
  
type = r"int[*]?"
args = type + r"\s+[*]*[a-zA-Z_]\w*" + r"(\s*[,]\s+" + type + r"\s+[*]*[a-zA-Z_]\w*)*"
function_pattern  = r"^" + "(" + type + "|void)" + r"\s+" + r"([a-z])" + r"\s*[(](" + args + r")\s*[)]\s*[{]\s*"
function_pattern += r"(\n|.)*?^[}]"
    
p1 = re.search(function_pattern, content, re.M)
fn1 = p1.group()

print fn1
