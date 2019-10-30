# Technical Assessment for Capital One
## Usage
You may run the unit tests by running test.py:
`python3 test.py`

You can test the code vs all of your python source files by copying them to the input directory, then running the program:
```sh
cp your_source/* ./input
python3 run.py
```
## Edge cases
There are many edge cases that were handled to produce the correct output:
1. Blank files have one line
2. If the `#` character is inside a string, it should not be counted as a comment
3. Escaped `'` or `"` inside a string should not close the string
4. `TODO` inside a string does not count as a todo
5. Block comments might be opened and closed in one line in one line: `'''hello'''` or `"""hello"""`
## Complexity
This program runs in O(n^6) time complexity. Yes, this isn't ideal. It can be reduced to O(n) by conducting all of the various edge-case checks in one pass. Still, even with a python file of 10,000 lines, it runs in under one second.
