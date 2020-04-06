library(tidyverse)
df <- readr::read_tsv('https://raw.githubusercontent.com/annaoskina/DH_research_2019-20/master/Files_tsv/wagahaiwa_nekodearu.txt.tsv', col_names = FALSE)

df %>% 
  mutate(id = 1:n(),
         new = str_detect("外", X13),
         new = ifelse(is.na(new), FALSE, new)) %>% 
  filter(new) %>% 
  ggplot() +
  geom_vline(aes(xintercept = id, color = new))
