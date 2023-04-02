from typing import Dict
from collections.abc import Callable, Iterable


def group_by(func: Callable, iterable: Iterable) -> Dict:
    """
    Group the elements of a list based on the result of a function
    this func create a dict with the result of the function as key and the list of elements as value
    :param func: function to apply to each element
    :param iterable: iterable to group by
    :return: dict of grouped elements
    for example:
    # >>> group_by(len, ["hi", "bye", "yo", "try"])
    output: {2: ["hi", "yo"], 3: ["bye", "try"]}
    """
    # using setdefault
    dict_group_by_func: dict = {}
    return dict(
        [dict_group_by_func.setdefault(func(item), []).append(item) or (func(item), dict_group_by_func[func(item)])
         for item in iterable])


if __name__ == '__main__':
    print(group_by(len, ["hi", "bye", "yo", "try"]))
