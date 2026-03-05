class Plant:

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_basic_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days"


class Flower(Plant):

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> str:
        return f"{self.name} is blooming beautifully!"


class Tree(Plant):

    def __init__(self, name: str, height: int, age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self) -> str:
        shade_area = self.trunk_diameter * 1.5
        return f"{self.name} provides {shade_area} square metters of shade"


class Vegetable(Plant):

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str,
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value


def main() -> None:
    print("=== Garden Plant Types ===\n")
    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 20, 25, "yellow")

    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 400, 1500, 40)

    tomato = Vegetable("Tomato", 80, 90, "summer", "Vitamin C")
    carrot = Vegetable("Carrot", 30, 70, "winter", "Beta-carotene")

    plants = [rose, tulip, oak, pine, tomato, carrot]

    for p in plants:
        print(p.get_basic_info())

    print("\nSpecial Actions:")
    print(rose.bloom())
    print(oak.produce_shade())


if __name__ == "__main__":
    main()
