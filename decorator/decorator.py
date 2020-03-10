class TextTag:

    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


class BoldWrapper(TextTag):
    """Wraps a tag in <b>"""

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<b>{}</b>".format(self._wrapped.render())


simple_hello = TextTag("hello, world!")
special_hello = BoldWrapper(simple_hello)

print(simple_hello.render())
print(special_hello.render())
