library(tidyverse)
df <- read_tsv(library(tidyverse))
df <- read_tsv("https://raw.githubusercontent.com/annaoskina/DH_research_2019_20/master/R/Correlation.tsv")
df1 <- read_csv("https://raw.githubusercontent.com/annaoskina/DH_research_2019_20/master/R/Correlation1.csv")
df1 %>%
  select(-Style) %>% 
  na.omit() %>% 
  mutate(Filename = str_c(1:n(), " ", Filename)) %>% 
  as.data.frame() ->
  df1

rownames(df1) <- df1$Writing

df1 %>% 
  select(`katakana_romaji`, `romaji_kanji`, `kanji_katakana`) %>% 
  dist() %>% 
  hclust() %>% 
  plot()

df1 <- read_csv("https://raw.githubusercontent.com/annaoskina/DH_research_2019_20/master/R/Correlation1.csv")

df1 %>% 
  select(-Style) %>% 
  na.omit() %>% 
  ggplot(aes(katakana_romaji, kanji_katakana, color = Author, label = Writing))+
  geom_point()+
  geom_text()

df1 %>% 
  select(-Style) %>%
  na.omit %>% 
  ggplot(aes(fct_reorder(Writing, romaji_kanji), romaji_kanji))+
  #ggplot(aes(Writing, katakana_romaji)) +
  geom_col()+
  coord_flip()
