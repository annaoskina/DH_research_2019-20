import MeCab

m = MeCab.Tagger('C:/Users/annao/test_mecab/UniDic')
#s = '内陣には御主《おんあるじ》耶蘇《ヤソ》基督《キリスト》の画像《ぐわざう》の前に、燐寸'
#result = m.parse(s)
#print(result)

#fw = open("1.txt", "w", encoding = "Shift-JIS")
#fw.write(result.encode('Shift-JIS','surrogateescape').decode('Shift-JIS'))
#fw.close()

with open('01aru_onna_zenpen.txt', 'r', encoding = 'utf-8') as t:
  result = m.parse(t.read())
  
fw = open("1.txt", "w", encoding = "utf-8")
fw.write(result)
fw.close()
