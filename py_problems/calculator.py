import abc
from typing import Any, Generator, Iterator, Optional, Tuple, Union

"""
Using lexer and parser, more generic
"""

OPERATORS = {"+", "-", "(", ")"}


class Lexer:
    """Converts string into tokens"""

    def scan(self, text: str) -> Generator[Union[str, int], None, None]:
        i = 0
        n = len(text)
        while i < n:
            if text[i] == " ":
                i += 1
                continue
            if text[i].isdigit():
                num = 0
                while i < n and text[i].isdigit():
                    num = int(text[i]) + num * 10
                    i += 1
                yield num
            elif text[i] in OPERATORS:
                yield text[i]
                i += 1
            else:
                raise ValueError(f"Unexpected text token {text[i]}!")


class Node(abc.ABC):
    def __init__(self, **kwargs: Any) -> None: ...

    @abc.abstractmethod
    def evaluate(self) -> int: ...

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}"


class NumNode(Node):
    def __init__(self, number: int) -> None:
        self.number = number

    def evaluate(self) -> int:
        return self.number

    def __repr__(self) -> str:
        return f"{self.number}"


class BinaryNode(Node, abc.ABC):
    def __init__(self, left: Node, right: Node) -> None:
        self.left = left
        self.right = right


class PlusNode(BinaryNode):
    def evaluate(self) -> int:
        return self.left.evaluate() + self.right.evaluate()

    def __repr__(self) -> str:
        return f"{self.left} + {self.right}"


class UnaryNode(Node, abc.ABC):
    def __init__(self, next_node: Node) -> None:
        self.next_node = next_node


class NegateNode(UnaryNode):
    def evaluate(self) -> int:
        return -self.next_node.evaluate()

    def __repr__(self) -> str:
        return f"-{self.next_node}"


class MinusNode(BinaryNode):
    def evaluate(self) -> int:
        return self.left.evaluate() - self.right.evaluate()

    def __repr__(self) -> str:
        return f"{self.left} - {self.right}"


class GroupNode(Node):
    def __init__(self, root_node: Node) -> None:
        self.root_node = root_node

    def evaluate(self) -> int:
        return self.root_node.evaluate()

    def __repr__(self) -> str:
        return f"({self.root_node})"


class Parser:
    """Parses tokens into tree"""

    def next_node(
        self, lexer_iter: Iterator, last_node: Optional[Node]
    ) -> Optional[Node]:
        token = next(lexer_iter, None)
        if token is None:
            return None
        if isinstance(token, int):
            return NumNode(token)
        elif token == "+":
            return PlusNode(last_node, self.next_node(lexer_iter, None))
        elif token == "-":
            if last_node is not None:
                return MinusNode(last_node, self.next_node(lexer_iter, None))
            else:
                return NegateNode(self.next_node(lexer_iter, None))
        elif token == "(":
            return GroupNode(self.parse(lexer_iter, None))
        elif token == ")":
            return None
        raise ValueError(f"Unexpected {token=}, {last_node=}")

    def parse(self, lexer_iter: Iterator, last_node: Optional[Node]) -> Optional[Node]:
        new_node = self.next_node(lexer_iter, last_node)
        if new_node is None:
            return last_node
        return self.parse(lexer_iter, new_node)


class Intepreter:
    """Evaluate tree"""

    def evaluate(self, tree: Node) -> int:
        return tree.evaluate()


"""
Using Stack and recursion, more efficient
"""


class Solution:
    def update_stack(self, stack: list, num: int, op: str):
        if op == "+":
            stack.append(num)
        if op == "-":
            stack.append(-num)
        if op == "*":
            stack.append(stack.pop() * num)
        if op == "/":
            stack.append(int(stack.pop() / num))

    def efficient_calculate(self, s: str, idx: int) -> Tuple[int, int]:
        n = len(s)
        num = 0
        op = "+"
        sum_stack = []
        while idx < n:
            if s[idx].isdigit():
                num = num * 10 + int(s[idx])
            elif s[idx] in "+-*/":
                self.update_stack(sum_stack, num, op)
                num = 0
                op = s[idx]
            elif s[idx] == "(":
                num, idx = self.efficient_calculate(s, idx + 1)
                idx -= 1
            elif s[idx] == ")":
                self.update_stack(sum_stack, num, op)
                return sum(sum_stack), idx + 1
            idx += 1
        self.update_stack(sum_stack, num, op)
        return sum(sum_stack), idx

    def calculate(self, s: str) -> int:
        """
        Use stack for in order evaluation (left to right)
        whenever we encounter brackets, we will recurse into bracket's expression
        and push to stack afterwards (after eval)
        """
        retval, _ = self.efficient_calculate(s, 0)
        return retval


if __name__ == "__main__":
    # iter_ = Lexer().scan("1+3 -2")
    # tree = Parser().parse(Lexer().scan("(4 -(2 + 3)) + (3 - 2)"), None)
    # print(tree)
    # print(Intepreter().evaluate(tree))

    print(Solution().calculate("1-(     -2)"))
