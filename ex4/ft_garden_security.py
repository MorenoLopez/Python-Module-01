#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_security.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: horarivo <horarivo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/14 12:39:32 by horarivo            #+#    #+#            #
#   Updated: 2026/06/12 06:58:56 by horarivo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def set_age(self, age: int) -> None:
        if int(age) > 0:
            self._age = age
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
        print(f"Age updated: {self._age} days")

    def get_height(self) -> None:
        print(f"Height updated: {int(self._height)}cm")

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm, "
              f"{self._age} days old")


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    rose.set_height(25.0)
    rose.set_age(30)
    print("\n")
    rose.get_height()
    rose.get_age()
    print("\n")
    rose.set_height(-25)
    rose.set_age(-30)
    print("\n")
    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
