from urllib.request import urlopen
from bs4 import BeautifulSoup

#specify array of URLs
pages = ['https://priam.umcs.lublin.pl:8443/lib/item?id=chamo:569809',
         'https://priam.umcs.lublin.pl:8443/lib/item?id=chamo:470256',
         'https://priam.umcs.lublin.pl:8443/lib/item?id=chamo:300982',
         'https://priam.umcs.lublin.pl:8443/lib/item?id=chamo:577163'
        ]

library_name = "Biblioteka Główna UMCS"
availability_flag = "Dostępne"

for page in pages:
    
    #query website and return its html
    content = urlopen(page)

    #parse html using beautiful soup
    soup = BeautifulSoup(content, 'html.parser')

    #extract tag with title and make it a bare string 
    book_title = soup.find('h1', attrs={'class': 'title'})
    book_title = book_title.text.strip()

    #extract tag with availability status and make it a bare string
    #assumption: the page exists so at least one 'odd' <tr> exists
    #parse NavigableString into unicode for further processing and to save memory (vide Beautiful Soup documentation) https://www.crummy.com/software/BeautifulSoup/bs4/doc/#navigablestring
    book_column = soup.find('tr', attrs={'class': 'odd'})
    book_status = book_column.find(string=availability_flag)                            

    #print out the availability of the book
    if(book_status == availability_flag):
        print ("AVAILABLE in "+library_name+":\t"+book_title)