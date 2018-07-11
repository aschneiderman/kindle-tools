# kindle-tools
Some quick and dirty Pthon scripts for working with a Kindle’s text file of highlights.

## get-highlights.py

Given part of a book title, puts a copy of the highlighted passages and their citation number
into a text file.  To use it:

- connect your Kindle to a computer via a USB cable
- download the My Clippings.txt to your computer into a folder containing the script
- change book_title to part of the title of the book whose highlights you want
- change book_highlights_file to the file name where the highlights should be stored
- run the script 

TO DO:

- Make the script more robust -- eg if the title has parentheses in it, it'll mess up the parsing; check to make sure ot only grabs the highlights from one book (I banged out this script to take care of an immediate need)
- Save the book title and author at the top of the output file
- Create a better but simple UI
- Fix it so Word will read it w/o asking what type of text it is

## Future Scripts

- Flask script that (optionally) walks you through how to download the clippings file, then lets you interactively choose from a list of all the books in the clippings file
