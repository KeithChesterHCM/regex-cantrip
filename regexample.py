# regexample.py
import sys, re

# Consume parameters
if len(sys.argv) <= 1:
  print "Error: No pattern found."
  print "Usage: python regexample.py <pattern> <optional-buffer>"
  sys.exit(0)

pattern = sys.argv[1]
print pattern

regEx = re.compile(pattern) # create regEx object

# begin parsing from stdin
for i,line in enumerate(sys.stdin):
  # check if this line has the pattern
  if regEx.search(line) != None:
    print str(i) + ': ' + line.strip()
