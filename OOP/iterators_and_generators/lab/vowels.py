class vowels:
    vowels_chars = ['a', 'e', 'i', 'u', 'y', 'o']

    def __init__(self, text: str):
        self.text = text
        self.current = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1

        if self.current >= len(self.text):
            raise StopIteration

        if self.text[self.current].lower() in self.vowels_chars:
            return self.text[self.current]

        return self.__next__()



my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)