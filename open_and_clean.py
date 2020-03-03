import re
import MeCab

def open_the_file(filename):
      with open (filename, 'r', encoding = 'Shift-JIS') as openfile:
            raw_txt = openfile.read()
      return raw_txt

def clean_the_file(raw_file):
      step_1 = re.sub ('(----------).+(---------)', '', raw_file, flags=re.DOTALL) #очищаю от условных обозначений в начале
      step_2 = re.sub ('《.+》', '', step_1)  #очищаю от фуриганы
      clean_txt = re.sub ('(底本：「).+?(ボランティアの皆さんです。)', '', step_2, flags=re.DOTALL) #очищаю от метаданных
      return clean_txt

def lemmatize_the_txt(clean_file):
      m = MeCab.Tagger('-d /home/anna/Documents/UniDic-kindai_1603')
      parsed_txt = m.parse(clean_file)
      return parsed_txt

def count_all_words(parsed_text):
      list_of_everything = parsed_text.split('\n')
      count_all_words = len(list_of_everything)
      return count_all_words

def count_all_gairaigo(parsed_text):
      list_of_everything = parsed_text.split('\n')
      list_of_gairaigo = []
      for i, gairaigo in enumerate(list_of_everything):
            if '外' in gairaigo:
                  list_of_gairaigo.append(gairaigo)
      number_of_gairaigo = len(list_of_gairaigo)
      return number_of_gairaigo

def main():
      raw_file = open_the_file('Source_for_research/majutsu.txt')
      clean_file = clean_the_file(raw_file)
      parsed_text = lemmatize_the_txt(clean_file)
      #number_of_words = count_all_words(parsed_text)
      number_of_gairaigo = count_all_gairaigo(parsed_text)
      print(number_of_gairaigo)

if __name__ == '__main__':
      main()
      

