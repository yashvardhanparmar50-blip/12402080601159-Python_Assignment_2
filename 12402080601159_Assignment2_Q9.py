"""Q9: OOP Inventory Merger with Operator Overloading
Student: Yashvardhansinh Parmar | Enrollment: 12402080601159
"""
from dataclasses import dataclass, field

@dataclass
class Inventory:
    stock: dict = field(default_factory=dict)

    def __add__(self, other):
        merged = dict(self.stock)
        for item, quantity in other.stock.items():
            merged[item] = merged.get(item, 0) + quantity
        return Inventory(merged)

    def __getitem__(self, item):
        return self.stock[item]

    def __str__(self):
        return "\n".join(f"{item}: {qty}" for item, qty in sorted(self.stock.items()))

if __name__ == "__main__":
    store_a = Inventory({"pen": 10, "notebook": 4})
    store_b = Inventory({"pen": 5, "eraser": 8})
    print(store_a + store_b)
