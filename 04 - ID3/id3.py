from collections import Counter
from math import log
from typing import Dict, List

class Node:
    def __init__(self, value: int, children) -> None:
        self._value = value
        self._children = children

    def get_value(self) -> int:
        return self._value

    def get_children(self):
        return self._children

    def check(self, values: List[str]) -> str:
        if values[self.get_value()] in self.get_children():
            return self.get_children()[values[self.get_value()]].check(values)
        classes = [child.check(values) for child in self.get_children().values()]
        return Counter(classes).most_common(1)[0][0]


class Leaf:
    def __init__(self, class_: str) -> None:
        self._class_ = class_

    def get_class(self) -> str:
        return self._class_

    def check(self, values: List[str]) -> str:
        return self.get_class()

class TrainingData:
    def __init__(self, values: List[str], class_: str) -> None:
        self._values = values
        self._class_ = class_

    def get_values(self) -> List[str]:
        return self._values

    def get_class(self) -> str:
        return self._class_


def entropy(training_pairs: List[TrainingData]) -> float:
    classes = [pair.get_class() for pair in training_pairs]
    possible_values = list(set(classes))
    return - sum(classes.count(value) * log(classes.count(value)) for value in possible_values)


def inf(attribute: int, training_pairs: List[TrainingData]) -> float:
    divided_pairs = divide_by_attribute(attribute, training_pairs)
    return sum(len(subset)/len(training_pairs) * entropy(subset) for subset in divided_pairs.values())


def inf_gain(attribute: int, training_pairs: List[TrainingData]) -> float:
    return entropy(training_pairs) - inf(attribute, training_pairs)


def get_most_common_attribute(attributes: List[int], training_pairs: List[TrainingData]) -> int:
    atributes_values = []
    for attribute in attributes:
        atributes_values.append((inf_gain(attribute, training_pairs), attribute))
    return max(atributes_values)[1]


def divide_by_attribute(most_common_attribute: int, training_pairs: List[TrainingData]) -> Dict[str, List[TrainingData]]:
    divided = {}
    for pair in training_pairs:
        divided.setdefault(pair.get_values()[most_common_attribute], []).append(pair)
    return divided


def get_trees(attributes: List[int], most_common_attribute: int, devided_attributes: Dict[str, List[TrainingData]]) -> Node:
    new_attributes = attributes.copy()
    new_attributes.discard(most_common_attribute)
    return Node(most_common_attribute, {attribute: id3(new_pairs, new_attributes) for attribute, new_pairs in devided_attributes.items()})

def id3(training_pairs: List[TrainingData], attributes: List[int]) -> Node:
    classes = {pair.get_class() for pair in training_pairs}

    if len(classes) == 1:
        return Leaf(training_pairs[0].get_class())

    if len(attributes) == 0:
        return Leaf(Counter(classes).most_common(1)[0][0])

    most_common_attribute = get_most_common_attribute(attributes, training_pairs)

    devided_attributes = divide_by_attribute(most_common_attribute, training_pairs)

    return get_trees(attributes, most_common_attribute, devided_attributes)


def main():
    node = id3(
        [
            TrainingData(["A", "1"], "0"),
            TrainingData(["B", "1"], "1"),
            TrainingData(["B", "2"], "1"),
            TrainingData(["B", "2"], "0"),
            TrainingData(["B", "3"], "1"),
        ],
        set((0, 1))
    )

if __name__ == "__main__":
    main()
