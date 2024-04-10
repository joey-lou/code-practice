"""
A six-sided die is a small cube with a different number of pips on each face (side), ranging from 1 to 6.
On any two opposite side of the cube, the number of pips adds up to 7; that is, there are three pairs of opposite sides: 1 and 6, 2 and 5, and 3 and 4.
There are N dice lying on a table, each showing the pips on its top face. In one move, you can take one die and rotate it to an adjacent face.
For example, you can rotate a die that shows 1 s that it shows 2, 3, 4 or 5. However, it cannot show 6 in a single move, because the faces with one pip and six pips visible are opposite sides rather than adjacent.
You want to show the same number of pips on the top face of all N dice. Given that each of the dice can be moved multiple times, count the minimum number of moves needed to get equal faces.

Write a function that, given an array A consisting of N integers describing the number of pips (from 1 to 6) shown on each die's top face, returns the minimum number of moves necessary for each die show the same number of pips.
"""

import collections


def moves(A):
    minimum = float("INFINITY")
    for i in range(1, 7):
        temp = 0
        for x in A:
            temp += ((x + i) % 7 == 0) + 1 - (x == i)
        if temp < minimum:
            print("Minimum:", i)
            minimum = temp
    return minimum


# or think about each target dice number, to roll to the number
# itself needs 0 move
# its complement needs 2 moves
# others needs 1 move


def moves(A):
    cnt = collections.Counter(A)
    return min(cnt[7 - i] + len(A) - cnt[i] for i in range(1, 7))


A = [1, 2, 3]
print(moves(A))
A = [1, 1, 6]
print(moves(A))
A = [1, 6, 2, 3]
print(moves(A))
