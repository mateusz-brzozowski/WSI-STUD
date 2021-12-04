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

    def to_dot(self) -> str:
        self_name = f"node_{id(self)}"

        # Create a node for the current node
        x = f'  {self_name} [label="Split on attr {self.get_value()}"];\n'

        # Create all the edges
        for edge_label, child in self.get_children().items():
            # Add dot from the child (to get its definition before inserting the edge)
            x += child.to_dot()

            # Add the edge to the child
            child_name = f"node_{id(child)}"
            escaped_edge_label = edge_label.encode("unicode_escape") \
                                           .decode("ascii") \
                                           .replace('"', r'\"')
            x += f'  {self_name} -> {child_name} [label="{escaped_edge_label}"];\n'

        return x

class Leaf:
    def __init__(self, class_: str) -> None:
        self._class_ = class_

    def get_class(self) -> str:
        return self._class_

    def to_dot(self) -> str:
        class_escaped = self.get_class().encode("unicode_escape") \
                                   .decode("ascii") \
                                   .replace('"', r'\"')
        return f'  node_{id(self)} [shape=box, label="{class_escaped}"];\n'

class TrainingData:
    def __init__(self, values: List[str], class_: str) -> None:
        self._values = values
        self._class_ = class_

    def get_values(self) -> List[str]:
        return self._values

    def get_class(self) -> str:
        return self._class_


def divide(training_pairs: List[TrainingData], attribute: int, value: int) -> List[TrainingData]:
    return [elem for elem in training_pairs if elem.get_values()[attribute] == value]


def entropy(training_pairs: List[TrainingData]) -> float:
    classes = [pair.get_class() for pair in training_pairs]
    possible_values = list(set(classes))
    return - sum(classes.count(value) * log(classes.count(value)) for value in possible_values)


def inf(attribute: int, training_pairs: List[TrainingData]) -> float:
    possible_values = list(set([pair.get_values()[attribute] for pair in training_pairs]))
    divided = [divide(training_pairs, attribute, value) for value in possible_values]
    return sum([(len(subset)/len(training_pairs)) * entropy(subset) for subset in divided])


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

# def get_childrens(devided_attributes, attributes):
#     new_attributes = {}
#     for attribute, new_pairs in devided_attributes.items():
#         new_attributes.setdefault(attribute, []).append(id3(new_pairs, attributes))
#     return new_attributes

def id3(training_pairs: List[TrainingData], attributes: List[int]) -> Node:
    classes = {pair.get_class() for pair in training_pairs}

    if len(classes) == 1:
        return Leaf(training_pairs[0].get_class())

    if len(attributes) == 0:
        return Leaf(Counter(classes).most_common(1)[0][0])

    most_common_attribute = get_most_common_attribute(attributes, training_pairs)

    devided_attributes = divide_by_attribute(most_common_attribute, training_pairs)

    # return Node(most_common_attribute, get_childrens(devided_attributes, new_attributes))
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

    print("digraph {")
    print(node.to_dot())
    print("}")

if __name__ == "__main__":
    main()
