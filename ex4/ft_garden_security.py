class SecurePlant:

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = 0
        self._age = 0

        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        if height < 0:
            print("Security: Negative height rejected")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm [OK]")

    def set_age(self, age: int) -> None:
        if age < 0:
            print("Security: Negative age rejected")
        else:
            self._age = age
            print(f"Age updated: {self._age} days [OK]")

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> str:
        return f"{self.name} ({self._height}cm, {self._age} days old)"


def main() -> None:
    print("=== Garden Security System ===")

    plant = SecurePlant("Rose", 25.0, 30)
    print("Plant created: ", show(plant))

    print("\nInvalid operation attempted:")
    plant.set_height(-5)

    print("\nCurrent plant:")
    print(plant.show())


if __name__ == "__main__":
    main()