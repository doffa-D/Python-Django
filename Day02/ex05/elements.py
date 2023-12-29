from elem import Elem, Text



"""
    this is double tag   html, head, body, title, table, th, tr, td, ul, ol, li, h1, h2, p, div, span
"""
class Html(Elem):
    def __init__(sefl, content=None, attr=None, tag_type="double"):
        super().__init__(tag="html", content=content, tag_type="double", attr=attr)

class Head(Elem):
    def __init__(sefl, content=None, attr=None, tag_type="double"):
        super().__init__(tag="head", content=content, tag_type="double", attr=attr)

class Body(Elem):
    def __init__(sefl, content=None, attr=None, tag_type="double"):
        super().__init__(tag="body", content=content, tag_type="double", attr=attr)

class Title(Elem):
    def __init__(sefl, content=None, attr=None, tag_type="double"):
        super().__init__(tag="title", content=content, tag_type="double", attr=attr)

class Table(Elem):
    def __init__(sefl, content=None, attr=None, tag_type="double"):
        super().__init__(tag="table", content=content, tag_type="double", attr=attr)

class th(Elem):
    def __init__(sefl, content=None, attr=None, tag_type="double"):
        super().__init__(tag="th", content=content, tag_type="double", attr=attr)

class tr(Elem):
    def __init__(sefl, content=None, attr=None, tag_type="double"):
        super().__init__(tag="tr", content=content, tag_type="double", attr=attr)

class td(Elem):
    def __init__(sefl, content=None, attr=None, tag_type="double"):
        super().__init__(tag="td", content=content, tag_type="double", attr=attr)

class ul(Elem):
    def __init__(sefl, content=None, attr=None, tag_type="double"):
        super().__init__(tag="ul", content=content, tag_type="double", attr=attr)

class ol(Elem):
    def __init__(sefl, content=None, attr=None, tag_type="double"):
        super().__init__(tag="ol", content=content, tag_type="double", attr=attr)

class li(Elem):
    def __init__(sefl, content=None, attr=None, tag_type="double"):
        super().__init__(tag="li", content=content, tag_type="double", attr=attr)

class h1(Elem):
    def __init__(sefl, content=None, attr=None, tag_type="double"):
        super().__init__(tag="h1", content=content, tag_type="double", attr=attr)

class h2(Elem):
    def __init__(sefl, content=None, attr=None, tag_type="double"):
        super().__init__(tag="h2", content=content, tag_type="double", attr=attr)

class p(Elem):
    def __init__(sefl, content=None, attr=None, tag_type="double"):
        super().__init__(tag="p", content=content, tag_type="double", attr=attr)

class div(Elem):
    def __init__(sefl, content=None, attr=None, tag_type="double"):
        super().__init__(tag="div", content=content, tag_type="double", attr=attr)

class span(Elem):
    def __init__(sefl, content=None, attr=None, tag_type="double"):
        super().__init__(tag="span", content=content, tag_type="double", attr=attr)





"""
    this is simple tag meta, img, hr, br
"""


class img(Elem):
    def __init__(sefl, content=None, attr=None, tag_type="simple"):
        super().__init__(tag="img", content=content, tag_type="simple", attr=attr)

class meta(Elem):
    def __init__(sefl, content=None, attr=None, tag_type="simple"):
        super().__init__(tag="meta", content=content, tag_type="simple", attr=attr)

class hr(Elem):
    def __init__(sefl, content=None, attr=None, tag_type="simple"):
        super().__init__(tag="hr", content=content, tag_type="simple", attr=attr)

class br(Elem):
    def __init__(sefl, content=None, attr=None, tag_type="simple"):
        super().__init__(tag="br", content=content, tag_type="simple", attr=attr)




# <html>
#   <head>
#     <title>"Hello ground!"</title>
#   </head>
#   <body>
#     <h1>"Oh no, not again!"</h1>
#     <img src="http://i.imgur.com/pfp3T.jpg" />
#   </body>
# </html>

print(Html([
    Head(
        Title(content = Text('"Hello ground!"'))),
    Body(
        h1(content = Text('"Oh no, not again!"'))),
        img(attr = {"src": "http://i.imgur.com/pfp3T.jpg"})
        ]))
