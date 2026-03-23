class Plant:

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"\n{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"\nHeight updated: {round(height, 1)}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {age} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> str:
        return f"{self.name}: {self._height}cm, {self._age} days old"


def main() -> None:
    print("=== Garden Security System ===")

    plant = Plant("Rose", 15.0, 10)
    print(f"Plant created: {plant.show()}")

    plant.set_height(25.0)
    plant.set_age(30)

    plant.set_height(-5)
    plant.set_age(-3)

    print(f"\nCurrent state: {plant.show()}")


if __name__ == "__main__":
    main()
