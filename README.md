#BookChecker Script - check books' availability

##General purpose
This script was created to help with the problem of checking availability of the books that are popular and borrowed out very often.
Instead of visiting your library website over and over, just simply run the script.

##Usage:
v. 1.0 - Make sure your library's website uses *this kind of software*. Add URLs of the pages with books you're interested in to the            'pages' array. The script looks for the data in Polish language.

##How does it work:
... created with Python 3.6 and Beautiful Soup 4.6.3

##TODO:
 - handle unexisting books
 - handle rows of class 'even' and their possible absence
 - handle multiple rows of classes both 'even' and 'odd'
 - REGEXP ("Dost*")
 - extract library name from html (info in header?)
 - only set as available if it's available to take home
 - extract the link under 'zamow' button and use it to order the book
 - [documentation]: describe how to automate script execution itself -> run it automatically every some time and tell user when the      book is available