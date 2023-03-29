# IRM-2023 Final Project

Abstract:
This research aims to compare the amount of spelling errors made on Dutch Twitter comparing 2011 to 2021. Specifically looking at the usage of "kado" (which is the wrong spelling of the word) and "cadeau" which is the correct spelling. As more Dutch people have become highly-educated compared to the years before (Centraal Bureau voor de Statistiek, 2022), it would be expected that the amount of spelling errors has decreased. Based on that the hypothesis is that "kado" is used less frequently in 2021 compared to 2011. The research will be done by taking at set amount of Dutch tweets from both 2011 and 2021 and then comparing the amount that "kado" and "cadeau" are used in 2011 versus 2021 relatively. For this, a Python program will be created that counts the amount of occurrences of both "kado" and "cadeau" from a file (which will later consist of the Twitter data). The program will then also compare both frequencies of "kado" and "cadeau" to each other and tell us which word was more used with their percentages of the total amount of tweets mentioning either "kado" or "cadeau". Based on that we can conclude whether the hypothesis was correct.

Background information:
Another research done by Lieke Verheijen has looked at whether the usage of Whatsapp has any significant influence on the language proficiency of Dutch young adults and adolescents (specifically in writing). Their research did not seem to have found any direct relation between the usage of Whatsapp and people's language proficiency. Their results did show that spelling errors seem to be more common in adolescents (12-17) than young adults (18-23). For this research we will try to see if this also applies to Twitter specifically looking at one common misspelling.

Method:
Make a Python script that reads the data file and counts every occurence of the word "kado" or "cadeau" and compares both frequencies to the total amount of tweets mentioning either of the two (total occurences of "kado" + total occurences of "cadeau"). Looking at the graph from cbs.nl, their data goes up until 2021. We will therefore take that same year and compare it to exactly a decade ago (2011) as the Twitter data goes back to at most 2010. We'll take a set amount of tweets from both years (as much as possible without the dataframe being too large) and then compare the frequency of both words in % of the total amount of tweets mentioning either "kado" or "cadeau" in each year. The Dutch tweets will be taken from the month of December, as it would be expected that the words "kado" and "cadeau" will be more used during the christmas season.

Sources:
Centraal Bureau voor de Statistiek. (2022, October 17). Meer hoogopgeleiden en beroepsniveau steeg mee. Centraal Bureau Voor De Statistiek. https://www.cbs.nl/nl-nl/nieuws/2022/42/meer-hoogopgeleiden-en-beroepsniveau-steeg-mee

Who’s afraid of Whatsapp?: De invloed van sociale media op schoolse schrijfvaardigheid. (2018). Radboud University Nijmegen. https://repository.ubn.ru.nl/bitstream/handle/2066/235914/upload_in_progress_2066_235914.pdf?sequence=1

WhatsApp with social media slang? Youth language use in Dutch written computer-mediated communication. (2017). Radboud University Nijmegen. https://repository.ubn.ru.nl/bitstream/handle/2066/235915/235915.pdf?sequence=1
