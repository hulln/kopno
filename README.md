# About the project

## Introduction
Kopno, komentarji političnih novic, is a dataset for a corpus comprised of comments under political articles on four Slovenian news sites: 24ur.com, RTV SLO, Nova24TV and N1. These sites were picked as they are the most popular among people that like to participate in political debates online. 
We aimed to make the dataset balanced with roughly the same number of comments per source. The number of comments on each news site is\
24ur.com – 5144 comments\
RTV SLO – 4489 comments\
Nova24TV – 2539 comments\
N1 – 1863 comments.

Since the dataset has not undergone tokenization or lemmatization, the number of tokens it entails cannot be stated. 

The program that was used to scrape comments from the internet was written by Mojca Brglez, an assistant professor at the Faculty of Arts at the University of Ljubljana. We used articles that were published in the last two months of 2022. The only exception is N1, where articles from the second half of the year were used due to a smaller number of comments. 

After extraction, the data was cleaned, so only relevant data was left: the comment, its author and the date and time of the publication. The author of every comment was anonymised with a Python program. The key by which the usernames are stored is *uporabnik_ime portala_zaporedna številka*.

Every comment also got its unique ID, which was stored using roughly the same key as the username: *ime portala_zaporedna številka komentarja*. If a comment is a reply in a thread, the original comment’s ID is also referenced. A link to the original article is also included in the metadata. We assigned IDs to comments with Brglez’s help. All other programming work was done by the group. 

The last step in this phase of the process was to convert the data into CSV format, which was done using a Python program. The encoding used in this step is utf-8-sig. Some comments in the files contain quotation marks, while others do not. Transformation of comment content into a common form and merging of the separate files into a single larger file was planned for the next phase of corpus development and could also be achieved using a Python program.

The dataset is released under The Creative Commons Attribution-NonCommercial-Share Alike 4.0 International licence agreement (CC BY-NC-SA 4.0).

## The issue with anonymisation 
This corpus is not completely anonymised; only authors of comments are. Following the example of the existing Slovenian corpora, we debated anonymising and replacing all occurrences of names and surnames with a universal identifier that can be found in the register of names and surnames in the Republic of Slovenia. This idea was later rejected, as the subject matter of the comments is political, which means that the names of politicians often appear, which we do not want to obscure, as this would lose the value and sense of the commentary.

Moreover, politicians are public figures (i.e. contemporary figures of interest to the public) who, according to legal theory and the position of the Constitutional Court, can even have their private lives (and even more so their public lives) discussed without their consent, in particular, what is relevant to their character, actions and thoughts concerning their public engagement. The dilemma of simultaneously preserving the mention of public figures in the comments and protecting the personal data of the users of the comments could be solved by using the data in the register of public figures, leaving the appearances in the text and replacing the others. However, this also creates a problem, as it is often ambiguous in the text whether the user is targeting the politician or someone else by mentioning a name. 

An additional issue that can arise with anonymisation is the consideration of only literal occurrences of a particular string. This excludes case-sensitive characters, possible stops, spaces, etc. Therefore, it would be useful to adapt a manual substitution checker to consider a certain degree of deviation from 100 % matching, which could be achieved using certain Python libraries. 
