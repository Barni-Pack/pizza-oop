from abc import ABC, abstractmethod
import time


class Pizza():
    crust = ''
    sause = ''
    toppings = []
    
    baking_time = 0
    price = 0
    
    def __init__(
        self,
    ) -> None:
        self.assembled = False
        self.baked = False
        self.pieces = 1
        self.packaged = False

    def assemble(self):
        for _ in self.toppings:
            time.sleep(1)
        self.assembled = True

    def bake(self):
        time.sleep(self.baking_time)
        self.baked = True

    def cut(self, pieces=8):
        self.pieces = pieces

    def package(self):
        self.packaged = True
        
    def __str__(self) -> str:
        s = []
        toppings = ', '.join(self.toppings)
        s.append(f'toppings: {toppings}')
        s.append(f'assembled: {self.assembled}')
        s.append(f'baked: {self.baked}')
        s.append(f'pieces: {self.pieces}')
        s.append(f'packaged: {self.packaged}')
        
        return '\n' + '\n'.join(s) + '\n'
