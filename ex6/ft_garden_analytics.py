class Plant:

  def __init__self, name: str, height: int) -> None:
    self.name: str = name
    self.height: int = height

  def grow(self) -> None:
    self.height += 1

  def get_info(self) -> str:
    return f"{self.name}: {self.height}cm"

class FloweringPlant(Plant):

  def __init__(self, name: str, height: int, color: str) -> NOne:
    super().__init__(name, height)
    self.color: str = color
    self.is_bloming: bool = False

  def bloom(self) -> None:
    self.is_blooming = True

  def get_info(self) -> str:
    base_info = super().get_info()
    return f"{base_info}, Prize points: {self.prize_points}"

class GardenManager:

  total_gardens: int = 0

  class GardenStats:

    @staticmethos
    def validate_height(height(height: int) -> bool:
      return height >= 0

    @staticmethod
    def calculate_total_growth(plants: list[Plant]) -> int:
      return sum(plant.height for p in plants)

  def __init__(self, owner: str) -> None:
    self.owner: str = owner
    self.plants: list[Plant] =[]
    GardenManager.total_gardens += 1

  def add_plant(self, plant: Plant) -> None:
    self.plants.append(plant)
    print(f"Added {plant.name} to {self.owner}'s garden")
  
  def grow_all(self) -> None:
    print(f"\n=== {self.owner} is helping all plants grow...")
    for p in self.plants:
      plant.grow()
      print(f"{plant.name} grew 1cm")
  
  def garde_report(self) -> None:
    print(f"\n=== {self.owner}'s Garden Report ===")
    for p in self.plants:
      print("-", plant.get_info())
  
    total_growth = self.GardenSats.calculate_total_growth(self.plants)
    print(f"Total height sum: {total_growth}cm")
  
  @classmethos
  def create_garden_network(cls) -> str:
    return f"Total gardens managed: {cls.total_gardens}"

def main() -> NOne:
  print("=== Garden Management System Demo ===\n")

  garden1 = GardenManager("Alice")
  garden2 = GardenManager("Bob")

  oak = Plant("Oak Tree", 100)
  rose = FloweringPlant("Rose", 25, "red")
  sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

  rose.bloom()
  sunflower.bloom()

  garde1.add_plant(oak)
  garden1.add_plant(rose)
  garde1.add_plant(sunflower)

  garden1.grow_all()
  garden1.garden_report()

  print("\nHeight validation test:",
        GardenManager.GardenStats.validate_height(10))

  print(GardenManager.crate_garden_network())

if __name__ == "__main__":
  main()
    
    
