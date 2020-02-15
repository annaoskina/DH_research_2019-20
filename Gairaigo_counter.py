import MeCab
import os
import re

#def open_all_files (path_to_files):
      lst_of_sources = os.listdir("/home/anna/Documents/DH_research")
      return lst_of_sources

#def open_one_file (lst_of_sources):
      for fl in lst_of_sources:
           if not fl.endswith(".txt"):
                 continue
            with open('/home/anna/Documents/DH_research/{}'.format(fl), 'r', encoding = "shift-jis") as openfile:
                  fls_as_str = openfile.read()
      return fls_as_str #хочу получить список с прочитанными файлами...
            
def open_the_file (path_to_file):
      with open (path_to_file, 'r', encoding = 'shift-jis') as openfile:
            fl_as_str = openfile.read()
      return fl_as_str

def clean_the_file (fl_as_str):
      txt_1 = re.sub ('(-------).+(-------)', '', fl_as_str) #очищаю от условных обозначений в начале
      txt_2 = re.sub ('《.+》', '', txt_1)  #очищаю от фуриганы
      clean_txt = re.sub ('(底本：「).+(ボランティアの皆さんです。)', '', txt_2) #очищаю от метаданных
      return clean_txt

def lemmatize_the_txt (clean_txt):
      m = MeCab.Tagger('-d /home/anna/Documents/UniDic-kindai_1603')
      parsed_txt = m.parse(clean_txt)
      return parsed_txt

def count_gairaigo (parsed_txt):
      return result_gairaigo

def count_romaji (parsed_txt):
      return result_romaji

def count_katakana (parsed_txt):
      return result_katakana

def count_kanji (parced_txt):
      return result_kanji

def combine_results (result_gairaigo, result_romaji, result_katakana, result_kanji):
      return list_of_results

def write_the_file

def main():
      path_to_file = "/home/anna/Documents/DH_research/Source_for_research/majutsu.txt"
      exit_file = open_the_file (path_to_file)
      clean_file = clean_the_file(exit_file)
      parsed_file = lemmatize_the_file (clean_file)
      print(parsed_file)
      

if __name__ == "__main__":
      main()
      
