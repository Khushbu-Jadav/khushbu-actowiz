from lxml import html
from rich import print

with open(r'C:\python practice\day11\book_to_scrap.html','r',encoding='utf-8')as f:
    data = f.read()

tree=html.fromstring(data)
book_data=[]
books=tree.xpath("//article")


book_title=tree.xpath("//article//h3//a/@title")
book_price=tree.xpath("//article//div//p[@class='price_color']/text()")  

book_data.append({
        "book_title":book_title,
        "book_price":book_price
} )
    
print(book_data)



# <!-- <bookstore> (root element node)
# <author>J K. Rowling</author> (element node)
# lang="en" (attribute node) 
# atomic values:
# J K. Rowling
# "en"
# nodename :	Selects all nodes with the name "nodename"
# -->

# / :	Selects from the root node
# full path: html/body/header/div/div/div/a/text()
# // :	Selects nodes in the document from the current node that match the selection no matter where they are
# direct path: //header//a/text()
# .	: Selects the current node
# //ul/.
# //ul 
# both are same
# ..	: Selects the parent of the current node
# //article//.. : it'll select article's parent node <li>
# @	: Selects attributes
# //@role : we'll get it's value "alert"
# //ul[@class="breadcrumb"]//li[1] : select the first li
# (//div[@class="side_categories"]//ul//li//a)[last()] : last book category
# (//div[@class="side_categories"]//ul//li//a)[last()-1] : second last book category
# (//div[@class="side_categories"]//ul//li//a)[position()<3] : first 2 book category
# //title[@lang] : Selects all the title elements that have an attribute named lang
# //title[@lang='en'] : Selects all the title elements that have a "lang" attribute with a value of "en"
# *	Matches any element node
# /bookstore/* : Selects all the child element nodes of the bookstore element
# @* Matches any attribute node
# //title[@*]	Selects all title elements which have at least one attribute of any kind
# //*	Selects all elements in the document
# node() Matches any node of any kind
# //book/title | //book/price	Selects all the title AND price elements of all book elements
# //title | //price	Selects all the title AND price elements in the document
# /bookstore/book/title | //price	Selects all the title elements of the book element of the bookstore element AND all the price elements in the document

# child::book	Selects all book nodes that are children of the current node
# attribute::lang	Selects the lang attribute of the current node
# child::*	Selects all element children of the current node
# attribute::*	Selects all attributes of the current node
# child::text()	Selects all text node children of the current node
# child::node()	Selects all children of the current node
# descendant::book	Selects all book descendants of the current node
# ancestor::book	Selects all book ancestors of the current node
# ancestor-or-self::book	Selects all book ancestors of the current node - and the current as well if it is a book node
# child::*/child::price	    Selects all price grandchildren of the current node

# |	Computes two node-sets	//book | //cd
# +	Addition	6 + 4
# -	Subtraction	6 - 4
# *	Multiplication	6 * 4
# div	Division	8 div 4
# =	Equal	price=9.80
# !=	Not equal	price!=9.80
# <	Less than	price<9.80
# <=	Less than or equal to	price<=9.80
# >	Greater than	price>9.80
# >=	Greater than or equal to	price>=9.80
# or	or	price=9.80 or price=9.70
# and	and	price>9.00 and price<9.90
# mod	Modulus (division remainder)	5 mod 2
