class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 1

    def age_one_day(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


def main() -> None:
    rose = Plant("Rose", 25.0, 30)

    initial_height = rose.height
    print("=== Garden Plant Growth ===")

    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.show()

        if i < 7:
            rose.grow()
            rose.age_one_day()

    growth = rose.height - initial_height
    print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
    main()
