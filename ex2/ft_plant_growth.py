#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_growth.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: horarivo <horarivo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/13 22:59:50 by horarivo            #+#    #+#            #
#   Updated: 2026/05/16 11:52:12 by horarivo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age_day = age

    def grow(self) -> None:
        self.height = round(self.height + 0.8, 1)

    def age(self) -> None:
        self.age_day += 1

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age_day} days old"


def simulate(plant: Plant) -> None:
    print("=== Garden Plant Growth ===")
    print(plant)
    init_height = plant.height
    for day in range(1, 8):
        plant.grow()
        plant.age()
        print(f"=== Day {day} ===")
        print(plant)

    print(f"Growth this week: {round(plant.height - init_height, 1)}cm")


if __name__ == "__main__":
    Rose = Plant("Rose", 25.0, 30)

    simulate(Rose)
