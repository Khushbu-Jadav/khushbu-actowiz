from parsel import Selector

html_content = """
<html>
    <body>
        <div class="content">
            <h1>Title: Extracting text using Xpath</h1>
            <p class="description">This is a description.</p>
        </div>
        <ul>
            <li>Geek 1</li>
            <li>Geek 2</li>
            <li>Geek 3</li>
        </ul>
        <a href="http://example.com/"></a>
    </body>
</html>
"""

selector = Selector(text=html_content)

title = selector.xpath('//h1/text()').get()
print(title)

description = selector.css('p.description::text').get()
print(description)

items = selector.xpath('//li/text()').getall()
print(items)

items = selector.css('li::text').getall()
print(items)

link = selector.css('a::attr(href)').get()
print(link) 

#div.content bcz content is a class
div_text = selector.css('div.content').css('h1::text').get()
print(div_text)