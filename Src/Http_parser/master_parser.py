from bs4 import BeautifulSoup
from Src.Structure.skelton import Tag
from urllib.request import Request, urlopen
from Src.file_ops.general import *
import json

def write_json(file_name, data):
    with open(file_name, 'w') as f:
        json.dump(data, f)

class WebPageParser:

    def __init__(self, html_string):
        self.soup = BeautifulSoup(html_string, 'html.parser')
        self.html = self.soup.find('html')
        self.all_tags = self.parse()

    def parse(self):
        results = []
        for x, tag in enumerate(self.html.descendants):
            print(self.html.descendants)

            if str(type(tag)) == "<class 'bs4.element.Tag'>":
                print(str(type(tag)))
                if tag.name == 'script':
                    continue

                # Find tags with no children (base tags)
                if tag.contents:
                    if sum(1 for _ in tag.descendants) == 1:
                        t = Tag(tag.name.lower())

                        # Because it might be None (<i class="fa fa-icon"></i>)
                        if tag.string:
                            t.add_content(tag.string)

                        if tag.attrs:
                            for a in tag.attrs:
                                t.add_attribute(a, tag[a])

                        results.append(t.get_data())

                # Self enclosed tags (hr, meta, img, etc...)
                else:
                    t = Tag(tag.name.lower())
                    m = []
                    
                    if tag.attrs:
                        for a in tag.attrs:
                            t.add_attribute(a, tag[a])
                            m.append(a)
                    results.append(t.get_data())
        print(m)
        return results

    
class ResponseParser:

    def __init__(self, response):
        self.response = response
        self.headers = self.parse()

    def parse(self):
        results = {}
        header_info = str(self.response.info()).split('\n')
        for item in header_info:
            row = item.split(':', 1)
            try:
                key = ' '.join(row[0].split())
                value = ' '.join(row[1].split())
                results[key] = value
            except IndexError:
                pass
        return results

class Jsonbuild:

    @staticmethod
    def parse(url, output_dir, output_file):
        print('Crawling ' + url)
        resp = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}))
        resp_bytes = resp.read()
        resp_parser = ResponseParser(resp)
        try:
            page_parser = WebPageParser(resp_bytes.decode('utf-8'))
        except UnicodeDecodeError:
            return
        json_results = {
            'url': url,
            'status': resp.getcode(),
            'headers': resp_parser.headers,
            'tags': page_parser.all_tags
        }
        write_json(output_dir + '/' + output_file + '.json', json_results)
