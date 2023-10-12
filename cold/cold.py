"""Kttis coldputer problem.
"""

__author__ = "Ram Basnet"
__date__ = "Oct 10, 2023"


def answer(temps: str) -> int:
    """Finds and returns no. of -ve of temps.

    Args:
        temps (str): temps separated by space

    Returns:
        int: number of hyphens (-ne temps)
    """
    return temps.count('-')


def solve() -> None:
    """_summary_
    """
    _ = input()
    data = input()
    print(answer(data))


if __name__ == "__main__":
    solve()
