import sys

if len(sys.argv) < 2:
  print("Help: python3 add_blank_lines.py path_to_the_file\n")

path = sys.argv[1]
file = open(path)
lines = file.readlines()
file.close()

# add blank lines
ret = ""
for i in range(len(lines)):
  if i < len(lines)-1 and len(lines[i])!=1 and len(lines[i+1])!=1:
    ret += lines[i] + "\n"
  else:
    ret += lines[i]

print(ret)

file = open(path, 'w')
file.write(ret)
file.close()
