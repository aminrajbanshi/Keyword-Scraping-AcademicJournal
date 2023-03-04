from bs4 import BeautifulSoup
import urllib.request
import re
import pandas as pd
import requests
import csv

# url = 'https://us.sagepub.com/en-us/nam/journal/asia-pacific-journal-public-health#submission-guidelines'
# url = 'https://us.sagepub.com/en-us/nam/cancer-control/journal203425#submission-guidelines'
url = 'https://us.sagepub.com/en-us/nam/health-services-insights/journal202662#submission-guidelines'
req = urllib.request.Request(
    url,
    data=None,
    headers={
    }
)
sauce = urllib.request.urlopen(req).read()
soup = BeautifulSoup(sauce, 'html.parser')

print("Title")
title_output = "'"
pattern_title = re.compile(r'title[\.| ]', re.IGNORECASE)
# Can search for 'Title', 'title.', 'title'  but NOT 'titles'
no_of_words_title = 10
# Determines number of words scraped from each side of the keyword i.e. 'title'
for elem in soup(text=pattern_title):
    stri = elem.parent.text
    list_in = stri.split(' ')
    list_indices = [i for i, x in enumerate(list_in) if re.match(pattern_title, x.strip()+' ')]
    # +' ' to conform with our pattern
    for index in list_indices:
        start = index-no_of_words_title
        end = index+no_of_words_title+1
        if start < 0:
            start = 0
        print(' '.join(list_in[start:end]).strip())
        # Printing all outputs as a list
        title_output = title_output + "-----" + (' '.join(list_in[start:end]).strip())
        # Storing each value of the list as a continuous string for the output
        print()

print("Abstract")
abstract_output = "'"
pattern_abstract = re.compile(r'abstract[\.| ]', re.IGNORECASE)
# Can search for 'Abstract', 'abstract.', 'abstract'  but NOT 'abstracts'
no_of_words_abstract = 10
for elem in soup(text=pattern_abstract):
    stri = elem.parent.text
    list_in = stri.split(' ')
    list_indices = [i for i, x in enumerate(list_in) if re.match(pattern_abstract, x.strip()+' ')]
    # +' ' to conform with our pattern
    for index in list_indices:
        start = index-no_of_words_abstract
        end = index+no_of_words_abstract+1
        if start < 0:
            start = 0
        print(' '.join(list_in[start:end]).strip())
        abstract_output = abstract_output + "-----" + (' '.join(list_in[start:end]).strip())
        # Repeating similar processes
        print()

print("Article")
article_output = "'"
pattern_article = re.compile(r'article[\.| ]', re.IGNORECASE)
no_of_words_article = 10
for elem in soup(text=pattern_article):
    stri = elem.parent.text
    list_in = stri.split(' ')
    list_indices = [i for i, x in enumerate(list_in) if re.match(pattern_article, x.strip()+' ')]
    for index in list_indices:
        start = index-no_of_words_article
        end = index+no_of_words_article+1
        if start < 0:
            start = 0
        print(' '.join(list_in[start:end]).strip())
        article_output = article_output + "-----" + (' '.join(list_in[start:end]).strip())
        print()

print("References")
references_output = "'"
pattern_references = re.compile(r'references[\.| ]', re.IGNORECASE)
no_of_words_references = 10
for elem in soup(text=pattern_references):
    stri = elem.parent.text
    list_in = stri.split(' ')
    list_indices = [i for i, x in enumerate(list_in) if re.match(pattern_references, x.strip()+' ')]
    for index in list_indices:
        start = index-no_of_words_references
        end = index+no_of_words_references+1
        if start < 0:
            start = 0
        print(' '.join(list_in[start:end]).strip())
        references_output = references_output + "-----" + (' '.join(list_in[start:end]).strip())
        print()

print("Figures")
figures_output = "'"
pattern_figures = re.compile(r'figures[\.| ]', re.IGNORECASE)
no_of_words_figures = 10
for elem in soup(text=pattern_figures):
    stri = elem.parent.text
    list_in = stri.split(' ')
    list_indices = [i for i, x in enumerate(list_in) if re.match(pattern_figures, x.strip()+' ')]
    for index in list_indices:
        start = index-no_of_words_figures
        end = index+no_of_words_figures+1
        if start < 0:
            start = 0
        print(' '.join(list_in[start:end]).strip())
        figures_output = figures_output + "-----" + (' '.join(list_in[start:end]).strip())
        print()

print("Tables")
tables_output = "'"
pattern_tables = re.compile(r'tables[\.| ]', re.IGNORECASE)
no_of_words_tables = 10
for elem in soup(text=pattern_tables):
    stri = elem.parent.text
    list_in = stri.split(' ')
    list_indices = [i for i, x in enumerate(list_in) if re.match(pattern_tables, x.strip()+' ')]
    for index in list_indices:
        start = index-no_of_words_tables
        end = index+no_of_words_tables+1
        if start < 0:
            start = 0
        print(' '.join(list_in[start:end]).strip())
        tables_output = tables_output + "-----" + (' '.join(list_in[start:end]).strip())
        print()

# Creating a dataframe to store all the data extracted
data = {'Journal Name': [url]}
df = pd.DataFrame(data)
df['Title'] = title_output
df['Abstract'] = abstract_output
df['Article'] = article_output
df['References'] = references_output
df['Tables'] = tables_output
df['Figures'] = figures_output
df['Journal Link'] = url

# Appending the data into a csv file
# df.to_csv('sage_publishing_asia_pacific_journal_of_public_health_advanced_scrap.csv')
# df.to_csv('sage_pub_cancer_control_journal_keyword_scrape.csv')
df.to_csv('sage_pub_health_services_insight_journal_keyword_scrape.csv')
