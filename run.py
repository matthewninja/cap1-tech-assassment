import os
from code_check import *
import re

def main():
  c = CodeChecker()
  files = os.listdir('input')
  files = filter(python_filter, files) 
  print (files)
  for path in files:
    lines, comment, single_line_comment, comment_in_block, block_comments, todos = c.count_comments('input/' + path)
    print_lines(path,lines, comment, single_line_comment, comment_in_block, block_comments, todos)

def print_lines(path,lines, comment, single_line_comment, comment_in_block, block_comments, todos):
  print("Summary of ", path, ":")
  print("Total # of lines: {}".format(lines))
  print("Total # of comment lines: {}".format(comment))
  print("Total # of single line comments: {}".format(single_line_comment))
  print("Total # of comment lines within block comments: {}".format(comment_in_block))
  print("Total # of block line comments: {}".format(block_comments))
  print("Total # of TODO’s: {}".format(todos))
  print("")

def python_filter(path):
  if path[0] == '.':
    return False
  if len(path) > 3 and path[-3:] == '.py':
    return True
  return False
main()