import re

def open_the_file (filename):
      with open (filename, 'r', encoding = 'Shift-JIS') as openfile:
            raw_txt = openfile.read()
      return raw_txt

def main():
      txt1 = open_the_file('Source_for_research/majutsu.txt')
      print(txt1)

if __name__ == '__main__':
      main()
      

