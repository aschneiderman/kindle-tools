# kindle-tools
Some quick and dirty Pthon scripts for working with a Kindle’s text file of highlights.

## get-highlights.py

Given part of a book title, puts a copy of the highlighted passages and their citation number
into a text file.  To use it:

- connect your Kindle to a computer via a USB cable
- download the My Clippings.txt to your computer into a folder containing the script
- change the title and output name names 
- run the script 

TO DO:

- Make the scriot more robust -- eg if the title has parentheses in it, it'll mess up the parsing; check to make sure ot only grabs the highlights from one book (I banged out this script to take care of an immediate need)
- Save the book title and author at the top of the output file
- Create a better UI
