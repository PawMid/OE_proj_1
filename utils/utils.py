from typing import (
    List
)


def bin_to_dec(biary: List[bool]) -> int:
    intVal: int = 0
    multiplier: int = 0

    for i in biary:
        intVal += 2 ** multiplier * i
        multiplier += 1

    return intVal