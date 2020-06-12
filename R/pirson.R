library(tidyverse)
df <- read_tsv(library(tidyverse))
df <- read_tsv("https://raw.githubusercontent.com/annaoskina/DH_research_2019_20/master/R/Correlation.tsv")

df %>%
  select(-Style) %>%   
  na.omit() %>% 
  mutate(Filename = str_c(1:n(), " ", Filename)) %>% 
  as.data.frame() ->
  df

rownames(df) <- df$Filename

df %>% 
  select(`katakana-romaji`, `romaji-kanji`, `kanji-katakana`) %>% 
  dist() %>% 
  hclust() %>% 
  plot()

df %>% 
  na.omit() %>% 
  ggplot(aes('katakana-romaji', 'kanji-katakana', color = 'Name of author'))+
  geom_point()

