library(tidyverse)
df <- read_csv('https://raw.githubusercontent.com/annaoskina/DH_research_2019-20/master/Results_csv/kokoro.txt.csv', col_names = FALSE)

df %>% 
  select(-X27) %>% 
  pivot_longer(names_to = "cols", values_to = "values", X2:X13) %>% 
  pivot_wider(names_from = X1, values_from = values) %>% 
  select(-cols) %>%
  cor()

df %>% 
  pivot_longer(names_to = "cols", values_to = "values", X2:X50) %>% 
  pivot_wider(names_from = X1, values_from = values) %>% 
  select(-cols) %>% 
  ggplot(aes(katakana, kanji))+
  geom_point()

df %>% 
  pivot_longer(names_to = "cols", values_to = "values", X2:X13) %>% 
  pivot_wider(names_from = X1, values_from = values) %>% 
  select(-cols) %>% 
  mutate(all_gairaigo = mean(katakana:kanji))

