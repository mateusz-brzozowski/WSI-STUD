from random import uniform
import json

class Node:
    def __init__(self, name, parents = None, probabilities = None):
        self.name = name
        self.parents = parents
        self.probabilities = probabilities

def load_from_json(path_file):
    with open(path_file, 'r') as file_handle:
        data = json.load(file_handle)
    nodes = []
    for json_node in data:
        nodes.append(Node(json_node["Name"], json_node["Parents"], json_node["Probabilities"]))
    return nodes

def generate_and_save(path_file, nodes, number_of_examples):
    with open(path_file, 'w') as file_handle:
        for _ in range(number_of_examples):
            example = {}
            result = ''
            for node in nodes:
                parent_example = ""
                for name in node.parents:
                    parent_example += 'T' if example[name] else 'F'
                example[node.name] = uniform(0, 1) < node.probabilities[parent_example]
                result += f"{example[node.name]},"
            file_handle.write(result[:-1] + '\n')

def main():
    nodes = load_from_json("07 - Bayes Network/input.json")
    generate_and_save("07 - Bayes Network/output.data", nodes, 10000)

if __name__ == "__main__":
    main()