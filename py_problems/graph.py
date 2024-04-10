from collections import defaultdict, deque
from typing import Dict, List


class Group:
    def __init__(self) -> None:
        self._dict = defaultdict(dict)
        self._members = set()

    def add_pair(self, a: str, b: str, val: float) -> None:
        self._dict[a][b] = val
        self._dict[b][a] = 1 / val
        self._members.add(a)
        self._members.add(b)

    def has_member(self, a: str) -> bool:
        return a in self._members

    def find_relation(self, a: str, b: str) -> float:
        assert a in self._members and b in self._members
        if a == b:
            return 1.0
        seen = set()
        stack = [(c, val) for c, val in self._dict[a].items()]
        while stack:
            for _ in range(len(stack)):
                c, val = stack.pop()
                if c in seen:
                    continue
                for d, val2 in self._dict[c].items():
                    if d == b:
                        return val * val2
                    else:
                        stack.append((d, val * val2))
                seen.add(c)
        raise "Pair not found?"

    def merge(self, other_group: "Group") -> "Group":
        for a, val_dict in other_group._dict.items():
            for b, val in val_dict.items():
                self.add_pair(a, b, val)
        return self


class Solution:
    """#399"""

    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        groups: Dict[str, Group] = {}

        for (a, b), val in zip(equations, values):
            matching_idices = []
            for idx, group in groups.items():
                if group.has_member(a) or group.has_member(b):
                    group.add_pair(a, b, val)
                    matching_idices.append(idx)
            if len(matching_idices) > 1:
                main_idx = matching_idices[0]
                first_group = groups[main_idx]
                for other_idx in matching_idices[1:]:
                    other_group = groups.pop(other_idx)
                    first_group = first_group.merge(other_group)
                groups[main_idx] = first_group
            elif not matching_idices:
                new_group = Group()
                new_group.add_pair(a, b, val)
                groups[a + b] = new_group
        retval = []
        for a, b in queries:
            has_found = False
            for group in groups.values():
                if group.has_member(a) and group.has_member(b):
                    retval.append(group.find_relation(a, b))
                    has_found = True
                    break
            if not has_found:
                retval.append(-1)
        return retval


class Solution:
    """#433."""

    @staticmethod
    def is_neighbor(a: str, b: str) -> bool:
        diff_cnt = 0
        for i, j in zip(a, b):
            if i == j:
                pass
            elif diff_cnt == 0:
                diff_cnt += 1
            else:
                return False
        return diff_cnt == 1

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # let's build a graph with mappings from one gene to another
        nodes = set([startGene]) | set(bank)
        if endGene not in nodes:
            return -1

        n = len(nodes)
        edges = defaultdict(list)
        nodes_lst = list(nodes)
        for i in range(n):
            for j in range(i + 1, n):
                this, other = nodes_lst[i], nodes_lst[j]
                if self.is_neighbor(this, other):
                    edges[this].append(other)
                    edges[other].append(this)

        # can use dijkt's algo
        # but since edges are unit length, we can simply do bfs till
        # we find the desired end node
        queue = deque([(startGene, 0)])
        seen = set()
        while queue:
            node, dist = queue.popleft()
            print(node, dist)
            seen.add(node)
            if node == endGene:
                return dist
            for next_node in edges[node]:
                if next_node not in seen:
                    queue.append((next_node, dist + 1))
        return -1


if __name__ == "__main__":
    print(
        Solution().minMutation(
            "AAAAAAAA",
            "AAAAACGG",
            ["AAAAAAGA", "AAAAAGGA", "AAAAACGA", "AAAAACGG", "AAAAAAGG", "AAAAAAGC"],
        )
    )
