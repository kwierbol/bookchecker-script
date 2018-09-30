# BookChecker Script - check books' availability
______________________________________________________________

## General purpose
This script was created to help with the problem of checking availability of the books which are popular and borrowed out very often. Instead of visiting your library website over and over, just simply run the script.

## Technologies
Created with Python 3.6 and Beautiful Soup 4.6.3

## Usage
__v 1.0__ - The script only works with a specific kind of library web app since its work is based on the HTML structure. Add URLs of the pages of books you're interested in to the __pages__ array like this:
```
#specify array of URLs
pages = ['https://priam.umcs.lublin.pl:8443/lib/item?id=chamo:569809',
         'https://priam.umcs.lublin.pl:8443/lib/item?id=chamo:470256',
         'https://priam.umcs.lublin.pl:8443/lib/item?id=chamo:300982',
        ]
```
Once the array is set with URLs, you're good to go.
The script looks for the data about availability in Polish language.


## TODO
 - handle unexisting books
 - handle rows of class 'even' and their possible absence
 - handle multiple rows of classes both 'even' and 'odd'
 - REGEXP ("Dost*")
 - extract library name from html (info in header?)
 - only set as available if it's available to take home
 - extract the link under 'zamow' button and use it to order the book
 - *documentation*: describe how to automate script execution itself -> run it automatically every some time and tell user when the book is available