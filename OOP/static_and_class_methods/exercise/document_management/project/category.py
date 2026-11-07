class Category:
    def __init__(self, _id: int, name: str):
        self.name = name
        self.id = _id

    def edit(self, new_name: str) -> None:
        self.name = new_name

    def __repr__(self) -> str:
        return f'Category {self.id}: {self.name}'