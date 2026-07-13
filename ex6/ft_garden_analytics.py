#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_analytics.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: horarivo <horarivo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/21 18:41:11 by horarivo            #+#    #+#            #
#   Updated: 2026/06/12 07:14:02 by horarivo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    class _Stats:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def display(self) -> None:
            print(f"Stats: {self._grow_count} grow, "
                  f"{self._age_count} age, "
                  f"{self._show_count} show")

    def __init__(self,
                 name: str,
                 height: float,
                 age_day: int,
                 growth_rate: int = 1
                 ) -> None:
        self._name = name
        self._height = height
        self._age_day = age_day
        self._growth_rate = growth_rate
        self.stats = self._Stats()

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    @property
    def name(self) -> str:
        return self._name

    def set_age(self, age: int) -> None:
        if int(age) > 0:
            self._age_day = age
        else:
            print(f"{self._name}: Error, age can't be negative\n"
                  "Age update rejected")

    def set_height(self, height: float) -> None:
        if float(height) > 0:
            self._height = height
        else:
            print(f"{self._name}: Error, height can't be negative\n"
                  "Height update rejected")

    def get_age(self) -> None:
        print(f"Age updated: {self._age_day} days")

    def get_height(self) -> None:
        print(f"Height updated: {int(self._height)} cm")

    def grow(self) -> None:
        self._height += self._growth_rate
        self.stats._grow_count += 1

    def age(self) -> None:
        self._age_day += 20
        self.stats._age_count += 1

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm, "
              f"{self._age_day} days old")
        self.stats._show_count += 1


class Flower(Plant):
    def __init__(self, name: str,
                 height: float,
                 age_day: int,
                 color: str,
                 growth_rate: int,
                 is_blooming: bool = False,
                 ) -> None:
        super().__init__(name, height, age_day, growth_rate)
        self._is_blooming = is_blooming
        self._color = color

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        self.is_bloomed()

    def age(self) -> None:
        super().age()

    def bloom(self) -> bool:
        self._is_blooming = True
        return self._is_blooming

    def is_bloomed(self) -> None:
        if self._is_blooming:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")

    def flower_color(self) -> None:
        print(f" Color: {self._color}")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age_day: int, diameter: float) -> None:
        super().__init__(name, height, age_day)
        self._diameter = diameter
        self.stats: Tree._TreeStats = self._TreeStats()

    class _TreeStats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count = 0

        def display(self) -> None:
            super().display()
            print(f" {self._shade_count} shade")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._diameter}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {self._name.lower()} to produce shade]")
        print(f"Tree {self._name} now produces a shade of "
              f"{self._height}cm long and {self._diameter}cm wide.")
        self.stats._shade_count += 1


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age_day: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, age_day)
        self._harvest_season = harvest_season
        self._nut_value = 0

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nut_value}")

    def grow(self) -> None:
        super().grow()
        self._nut_value += 20
        print(f"[make {self._name.lower()} grow and age for 20 days]")


class Seed(Flower):
    def __init__(self, name: str, height: float,
                 age_day: int, is_blooming: bool,
                 color: str, seed_count: int, growth_rate: int) -> None:
        super().__init__(name,
                         height,
                         age_day,
                         color,
                         growth_rate,
                         is_blooming
                         )
        self.seed_count = seed_count

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seed_count}")

    def bloom(self) -> bool:
        result = super().bloom()
        return result


def display_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.stats.display()


def main() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red", 8, False)
    rose.show()
    display_stats(rose)
    rose.grow()
    print("[asking the rose to grow and bloom]")
    rose.bloom()
    rose.show()
    display_stats(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_stats(oak)
    oak.produce_shade()
    display_stats(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, False, "yellow", 0, 30)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.seed_count = 42
    sunflower.bloom()
    sunflower.show()
    display_stats(sunflower)

    print("\n=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    display_stats(unknown)


if __name__ == "__main__":
    main()
