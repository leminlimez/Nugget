class NuggetException(Exception):
    def __init__(self, message: str, detailed_text: str | None = None):
        self.message = message
        self.detailed_text = detailed_text
        super().__init__(self.message)
        
    def __str__(self):
        return self.message