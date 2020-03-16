sep = ','
with open('parsed.csv') as f:
  lines = f.read()
  lines = lines.split('\n')
  # или:
  # lines = f.readlines()
  for line in lines:
    cells = line.split(sep)
    #print(cells)
for words in cells:
      words = cells[0, 12]
      print(words)
    
#with open ('parsed_by_lines.txt', 'w', encoding='utf-8') as fw:
      #fw.write(cells)
