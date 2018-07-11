# get-highlights.py: grab the highlights of one Kindle book from your Kindle's My Clippings.txt file

import os, sys
import re

book_title = r"Freedom's Teacher"
book_highlights_file = r'Freedoms Teacher.txt'

book_highlights = open(book_highlights_file, 'w', encoding='utf-8-sig')

with open('My Clippings.txt', 'r', encoding='utf-8-sig') as f:
    contents = f.read().replace(u'\ufeff', '')
    highlights = contents.rsplit('==========')

for highlight in highlights:
    if book_title in highlight:          # Yes, this is a kludge (see below for why)
        # print('\n\n', highlight, '\n\n----------------------------------------\n')

        # Yes, I should use a regular expression to do this, but I kept getting stuck :-)    
        author_title, remainder = highlight.split(')\n- ', 1)
        title, author = author_title.split(' (')
        title = title.strip()
        metadata, quote = remainder.split('\n\n')
        match = re.search(r'(Page.*)\|', metadata, re.IGNORECASE)
        if match:
            page_citation = match.group(1)
        else:
            page_citation = ''
            print('Warning: Missing page citation')
        book_highlights.write('{0} ({1})\n\n'.format(quote.strip(), page_citation.strip()))
        
book_highlights.close()    

print('\n\n', book_title, 'had a total of', len(highlights), 'highlights,'
      '\n which have been copied to', book_highlights_file, '\n\n\n')