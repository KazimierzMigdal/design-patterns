class SpanishLocalizer:
    def __init__(self):
        self.translations = {"dog": "perro", "cat": "gato"}

    def localize(self, msg):
        return self.translations.get(msg, msg)


class EnglishLocalizer:
    def localize(self, msg):
        return msg


def get_localizer(language="English"):
    localizers = {
        "English": EnglishLocalizer,
        "Spanish": SpanishLocalizer,
    }
    return localizers[language]()



def main():
    e, s = get_localizer(language="English"), get_localizer(language="Spanish")
    for msg in "dog parrot cat bear".split():
        print(e.localize(msg), s.localize(msg))

main()

