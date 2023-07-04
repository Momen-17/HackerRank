from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print(f'-> {attr[0]} > {attr[1]}') for attr in attrs]
    def handle_startendtag(self, tag, attrs):
        print(tag)
        [print(f'-> {attr[0]} > {attr[1]}') for attr in attrs]

parser = MyHTMLParser()
[parser.feed(input()) for _ in range(int(input()))]