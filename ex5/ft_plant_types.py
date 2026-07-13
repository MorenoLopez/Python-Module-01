#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_types.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: horarivo <horarivo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/21 09:39:51 by horarivo            #+#    #+#            #
#   Updated: 2026/06/12 07:04:32 by horarivo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float, age_day: int) -> None:
        self.name = name
        self.height = height
        self.age_day = age_day

    def set_age(self, age: int) -> None:
        if int(age) > 0:
            self.age_day = age
        else:
            print(f"{self.name}: Error, age can't be negative\n"
                  "Height update rejected")

    def set_height(self, height: float) -> None:
        if float(height) > 0:
            self.height = height
        else:
            print(f"{self.name}: Error, height can't be negative\n"
                  "Age update rejected")

    def get_age(self) -> None:
        print(f"Age updated: {self.age_day} days")

    def get_height(self) -> None:
        print(f"Height updated: {int(self.height)} cm")

    def grow(self) -> None:
        self.age_day += 20
        self.height += 42

    def age(self) -> None:
        self.age_day += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, "
              f"{self.age_day} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 age_day: int, is_blooming: bool, color: str) -> None:
        super().__init__(name, height, age_day)
        self.is_blooming = is_blooming
        self.color = color

    def _is_bloomed(self) -> None:
        if self.is_blooming:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        self._is_bloomed()

    def age(self) -> None:
        super().age()

    def bloom(self) -> bool:
        print("[asking the rose to bloom]")
        self.is_blooming = True
        return self.is_blooming


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age_day: int, diameter: float) -> None:
        super().__init__(name, height, age_day)
        self.diameter = diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.diameter}cm")

    def produce_shade(self) -> None:
        print("[asking the oak to produce shade]")
        print(f"Tree {self.name} now produces a shade of "
              f"{self.height}cm long and {self.diameter}cm wide.")


class Vegetable(Plant):
    nut_value = 0

    def __init__(self, name: str, height: float, age_day: int) -> None:
        super().__init__(name, height, age_day)

    def show(self) -> None:
        super().show()
        print(" Harvest season: April")
        print(f"Nutritional value: {self.nut_value}")

    def grow(self) -> None:
        super().grow()
        self.nut_value += 20
        print("[make tomato grow and age for 20 days]")


def main() -> None:
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 15.0, 10, False, "red")
    print("=== Flower")
    rose.show()
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10)
    tomato.show()
    tomato.grow()
    tomato.show()


if __name__ == "__main__":
    main()
