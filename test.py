from code_check import *
import unittest

class TestCodeCheck(unittest.TestCase):
  def test_one(self):
    path = 'test_inputs/sample.py'
    lines, comment, single_line_comment, comment_in_block, block_comments, todos = c.count_comments(path)
    # self.print_lines(lines, comment, single_line_comment, comment_in_block, block_comments, todos)
    assert lines == 61, "Should be 61. Instead, got: {}".format(lines)
    assert comment == 27, "Should be 27. Instead, got: {}".format(comment)
    assert single_line_comment == 19
    assert comment_in_block == 8
    assert block_comments == 2
    assert todos == 3

  def test_blank(self):
    path = 'test_inputs/blank.py'
    lines, comment, single_line_comment, comment_in_block, block_comments, todos = c.count_comments(path)
    # self.print_lines(lines, comment, single_line_comment, comment_in_block, block_comments, todos)
    assert lines == 1, "Should be 1. Instead, got: {}".format(lines)
    assert comment == 0
    assert single_line_comment == 0
    assert comment_in_block == 0
    assert block_comments == 0
    assert todos == 0

  def test_edge_case1(self):
    path = 'test_inputs/edge-case.py'
    lines, comment, single_line_comment, comment_in_block, block_comments, todos = c.count_comments(path)
    # self.print_lines(lines, comment, single_line_comment, comment_in_block, block_comments, todos)
    assert lines == 2, "Should be 2. Instead, got: {}".format(lines)
    assert comment == 0, "Should be 0. Instead, got: {}".format(comment)
    assert single_line_comment == 0,"Should be 0. Instead, got: {}".format(single_line_comment)
    assert comment_in_block == 0, "Should be 0. Instead, got: {}".format(comment_in_block)
    assert block_comments == 0,  "Should be 0. Instead, got: {}".format(block_comments)
    assert todos == 0, "Should be 0. Instead, got: {}".format(todos)

  def test_edge_case2(self):
    path = 'test_inputs/edge-case2.py'
    lines, comment, single_line_comment, comment_in_block, block_comments, todos = c.count_comments(path)
    # self.print_lines(lines, comment, single_line_comment, comment_in_block, block_comments, todos)
    assert lines == 3, "Should be 4. Instead, got: {}".format(lines)
    assert comment == 0, "Should be 0. Instead, got: {}".format(comment)
    assert single_line_comment == 0,"Should be 0. Instead, got: {}".format(single_line_comment)
    assert comment_in_block == 0, "Should be 0. Instead, got: {}".format(comment_in_block)
    assert block_comments == 0,  "Should be 0. Instead, got: {}".format(block_comments)
    assert todos == 0, "Should be 0. Instead, got: {}".format(todos)

  def test_edge_case3(self):
    path = 'test_inputs/edge-case3.py'
    lines, comment, single_line_comment, comment_in_block, block_comments, todos = c.count_comments(path)
    # self.print_lines(lines, comment, single_line_comment, comment_in_block, block_comments, todos)
    assert lines == 11, "Should be 11. Instead, got: {}".format(lines)
    assert comment == 9, "Should be 9. Instead, got: {}".format(comment)
    assert single_line_comment == 3,"Should be 3. Instead, got: {}".format(single_line_comment)
    assert comment_in_block == 6, "Should be 6. Instead, got: {}".format(comment_in_block)
    assert block_comments == 3,  "Should be 3. Instead, got: {}".format(block_comments)
    assert todos == 1, "Should be 1. Instead, got: {}".format(todos)

  def print_lines(self,lines, comment, single_line_comment, comment_in_block, block_comments, todos):
    print("Total # of lines: {}".format(lines))
    print("Total # of comment lines: {}".format(comment))
    print("Total # of single line comments: {}".format(single_line_comment))
    print("Total # of comment lines within block comments: {}".format(comment_in_block))
    print("Total # of block line comments: {}".format(block_comments))
    print("Total # of TODO’s: {}".format(todos))

if __name__ == '__main__':
  c = CodeChecker()
  unittest.main()
