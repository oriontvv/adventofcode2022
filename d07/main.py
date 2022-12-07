from __future__ import annotations
from dataclasses import dataclass
from typing import Callable

# File is a Dir without children
@dataclass
class Dir:
    name: str
    size: int
    parent: Dir | None
    children: dict[str, Dir]


def build_tree(lines: list[str]) -> Dir:
    root = Dir(name="/", size=0, parent=None, children={})
    cur_node = None
    for line in lines:
        line = line.strip()
        if line.startswith("$ cd "):
            path = line.split("$ cd ")[-1]
            if path == "/":
                cur_node = root
            elif path == "..":
                cur_node = cur_node.parent
            else:
                cur_node = cur_node.children[path]
            assert cur_node is not None, f"Can't reach path {path}"
        elif line == "$ ls":
            continue
        elif line.startswith("dir"):
            path = line.split()[-1]
            if path not in cur_node.children:
                cur_node.children[path] = Dir(
                    name=path, size=0, parent=cur_node, children={}
                )
        else:
            size, name = line.split()
            if name not in cur_node.children:
                cur_node.children[name] = Dir(
                    name=path, size=int(size), parent=cur_node, children={}
                )
    calc_sizes(root)
    return root


def calc_sizes(node: Dir):
    for child in node.children.values():
        child.size = calc_sizes(child)
        node.size += child.size
    return node.size


def find_nodes(node: Dir, pred: Callable):
    if pred(node):
        yield node
    for child in node.children.values():
        yield from find_nodes(child, pred)


root = build_tree(open("in.txt"))
is_node_at_most_size = lambda node: node.children and node.size <= 100000
is_node_at_least_size = lambda node: node.children and node.size >= root.size - 40000000

print(sum(node.size for node in find_nodes(root, is_node_at_most_size)))
print(min(node.size for node in find_nodes(root, is_node_at_least_size)))
