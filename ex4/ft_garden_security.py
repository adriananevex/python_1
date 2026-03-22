class SecurePlant:

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self._height: int = 0
        self._age: int = 0

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

    def get_info(self) -> str:
        return f"{self.name} ({self._height}cm, {self._age} days)"


def main() -> None:
    print("=== Garden Security System ===")

    plant = SecurePlant("Rose", 25, 30)

    print("\nInvalid operation attempted:")
    plant.set_height(-5)

    print("\nCurrent plant:")
    print(plant.get_info())


if __name__ == "__main__":
    main()