from __future__ import annotations

from abc import ABC


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor: str | None = None
        self.ram: int | None = None
        self.price: int = 0
        
    @property
    def manufacturer(self):
        return self.__manufacturer
    
    @manufacturer.setter
    def manufacturer(self, value):
        if value.strip() == '':
            raise ValueError('Manufacturer name cannot be empty.')
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip() == '':
            raise ValueError('Model name cannot be empty.')
        self.__model = value

    def configure_computer(self, processor: str, ram: int):
        pass

    def __repr__(self) -> str:
        return f'{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM'

