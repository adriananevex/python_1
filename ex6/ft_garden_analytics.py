# ft_garden_analytics.py

class Plant:

    class Stats:
        def __init__(self):
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self):
            print(
                f"Stats: {self.grow_calls} grow, {self.age_calls} age, "
                f"{self.show_calls} show"
            )

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self._stats = Plant.Stats()

    @staticmethod
    def older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

    def grow(self, amount: float = 8.0):
        self.height += amount
        self._stats.grow_calls += 1

    def age_up(self, days: int):
        self.age += days
        self._stats.age_calls += 1

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        self._stats.show_calls += 1

    def show_stats(self):
        self._stats.display()


class Flower(Plant):

    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self):
        self.bloomed = True
        print(f"{self.name} is blooming beautifully!")

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if not self.bloomed:
            print(f"{self.name} has not bloomed yet")
        else:
            print(f"{self.name} is blooming beautifully!")


class Tree(Plant):

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float,
    ):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade_calls = 0

    def produce_shade(self):
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height}cm long and {self.trunk_diameter}cm wide."
        )
        self.shade_calls += 1

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def show_stats(self):
        super().show_stats()
        print(f"{self.shade_calls} shade")


class Seed(Flower):

    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self):
        super().bloom()
        self.seeds = 42

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")


def display_statistics(plant: Plant):
    print(f"[statistics for {plant.name}]")
    plant.show_stats()


def main():

    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.older_than_year(400)}")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_statistics(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_statistics(rose)

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_statistics(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()

    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age_up(20)
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)

    print("=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    display_statistics(unknown)


if __name__ == "__main__":
    main()
