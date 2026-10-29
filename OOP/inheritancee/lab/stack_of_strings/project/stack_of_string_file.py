class Stack:
    def __init__(self):
        self.data: list = []

    def push(self, item: str) -> None:
        self.data.append(item)

    def pop(self) -> None:
        return self.data.pop()

    def top(self) -> None:
        return self.data[-1]

    def is_empty(self) -> bool:
        return not any(self.data)

    def __str__(self):
        return '[' + ', '.join(reversed(self.data)) + ']'

