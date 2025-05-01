class Page:
    def __init__(self):
        self.loaded = False

    def load(self):
        if not self.loaded:
            self.load_page()
            self.loaded = True

    def load_page(self):
        raise NotImplementedError