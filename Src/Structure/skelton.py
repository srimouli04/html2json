from urllib.parse import urlparse


class Domain:

    def __init__(self, url):
        self.url = url
        self.domain = self.get_domain()
        self.sub_domain = self.get_sub_domain()

    def get_domain(self):
        results = self.get_sub_domain().split('.')
        try:
            return results[-2] + '.' + results[-1]
        except IndexError:
            return False

    def get_sub_domain(self):
        return urlparse(self.url).netloc


class Tag:

    def __init__(self, name):
        self.name = name
        self.content = None
        self.attributes = {}

    def add_content(self, text):
        self.content = ' '.join(text.split())

    def add_attribute(self, key, value):
        if str(type(value)) == "<class 'str'>":
            if len(value) < 1:
                return
        self.attributes[key] = value

    def get_data(self):
        if len(self.attributes) == 0:
            self.attributes = None
        return {
            'name': self.name,
            'content': self.content,
            'attributes': self.attributes
        }
