class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def grow(self) -> None:
        self.height += 1

    def age_one_day(self) -> None:
        self.age += 1

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


def main() -> None:
    rose = Plant("Rose", 25, 30)

    print("=== Day 1 ===")
    print(rose.get_info())

    for i in range(6):
        rose.grow()
        rose.age_one_day()

    print("=== Day 7 ===")
    print(rose.get_info())
    print("Growth this week: +6cm")


if __name__ == "__main__":
    main()
