class CodeChecker:
  def count_comments(self, path):
    lines = 1
    single_line_comment = 0
    comment_in_block = 0
    block_comments = 0
    todos = 0
    reading_multiline_single = False
    reading_multiline_double = False
    f = open(path)

    for line in f:
      lines += 1 # increment lines
      if self.has_single_line_comment(line): 
        single_line_comment += 1
      elif self.has_block_comment_in_one_line(line):
        # print("line:", line,"/end line")
        block_comments += 1
        comment_in_block += 1
      elif self.has_multi_line_comment_single(line):
        reading_multiline_single = not reading_multiline_single
        if not reading_multiline_single:
          block_comments += 1
        comment_in_block += 1
      elif self.has_multi_line_comment_double(line):
        reading_multiline_double = not reading_multiline_double
        if not reading_multiline_double:
          block_comments += 1
        comment_in_block += 1
      elif reading_multiline_double:
        comment_in_block += 1
      elif reading_multiline_single:
        comment_in_block += 1
      if self.has_todo(line):
        todos += 1

    f.close()
    comment = single_line_comment + comment_in_block
    return lines, comment ,single_line_comment,comment_in_block,block_comments,todos

  # checks for single line comment, dealing with edge case where # is in a string
  def has_single_line_comment(self, line):
    in_string_single = False
    in_string_double = False
    escaped = False
    for c in line:
      if in_string_double or in_string_single: # escaped character doesn't count for anything
        if c == '\\':
          escaped = True
          continue
      if not escaped and c == '\'' and not in_string_double: # enter/exit a string with single quote
        in_string_single = not in_string_single
      elif not escaped and c == '"' and not in_string_single: # enter/exit a string with double quote
        in_string_double = not in_string_double

      escaped = False
      if c == '#' and not in_string_double and not in_string_single:
        return True

    return False

  # checks for ''', which opens or closes a multi-line comment
  # deals with edge case where ''' is inside a string
  def has_multi_line_comment_single(self, line):
    in_string_double = False
    escaped = False
    for i in range(len(line)):
      if in_string_double: # escaped character doesn't count for anything
        if line[i] == '\\':
          escaped = True
          continue

      if not escaped and line[i] == '"':
        in_string_double = not in_string_double

      escaped = False
      if line[i] == '\'' and not in_string_double and i + 2 < len(line):
        if line[i+1] == '\'' and line[i+2] == '\'':
          return True
    return False

  # checks for """, which opens or closes a multi-line comment
  # deals with edge case where """ is in a string
  def has_multi_line_comment_double(self, line):
    in_string_double = False
    escaped = False
    for i in range(len(line)):
      if in_string_double: # escaped character doesn't count for anything
        if line[i] == '\\':
          escaped = True
          continue
      if not escaped and line[i] == "'":
        in_string_double = not in_string_double

      escaped = False
      if line[i] == '"' and not in_string_double and i + 2 < len(line):
        if line[i+1] == '"' and line[i+2] == '"':
          return True
    return False

  def has_block_comment_in_one_line(self,line):
    # if has ''' twice to open and close comment
    # or if has """ twice to open and close comment
    if self.has_multi_line_comment_double(line):
      trunc = line[line.index('"""')+3:]
      if '"""' in trunc:
        return True
    if self.has_multi_line_comment_single(line):
      trunc = line[line.index("'''")+3:]
      if "'''" in trunc:
        return True
    return False

  # checks for TODO, excludes edge case where TODO is inside a string
  def has_todo(self,line):
    in_string_single = False
    in_string_double = False
    escaped = False
    for i in range(len(line)):
      if in_string_double or in_string_single: # escaped character doesn't count for anything
        if line[i] == '\\':
          escaped = True
          continue
      if not escaped and line[i] == '\'' and not in_string_double: # enter/exit a string with single quote
        in_string_single = not in_string_single
      elif not escaped and line[i] == '"' and not in_string_single: # enter/exit a string with double quote
        in_string_double = not in_string_double

      escaped = False
      if line[i] == 'T' and not in_string_double and not in_string_single and i + 3 < len(line):
        if line[i:i+4] == 'TODO':
          return True

    return False

  def valid_parenthesis(self, s):
    stack = []
    for c in s:
      if c == '(' or c =='[' or c == '{' :
        stack.append(c)
      elif c == ')':
        if not stack:
          return False
        if stack.pop() != '(':
          return False
      elif c == ']':
        if not stack:
          return False
        if stack.pop() != '[':
          return False
      elif c == '}':
        if not stack:
          return False
        if stack.pop() != '{':
          return False
    if stack:
      return False
    return True

