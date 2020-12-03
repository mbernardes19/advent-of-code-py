from typing import List
from utils import get_entries


def find_entries_that_sum_2020_p1(entries: List[str]):
    minPointer = 1
    maxPointer = int(len(entries) - 1)

    done = False
    while not done:
        total = int(entries[minPointer]) + int(entries[maxPointer])
        if total < 2020:
            minPointer += 1
        elif total > 2020:
            maxPointer -= 1
        else:
            done = True
            return [int(entries[minPointer]), int(entries[maxPointer])]


def find_entries_that_sum_2020_p2(entries: List[str]):
    n = len(entries)
    for i in range(n):
        for j in range(i + 1, n):
            for x in range(j + 1, n):
                if entries[i] != '' and entries[j] != '' and entries[x] != '':
                    if int(entries[i]) + int(entries[j]) + int(entries[x]) == 2020:
                        return [int(entries[i]), int(entries[j]), int(entries[x])]
                    else:
                        pass


def multiply_entries_p1(entries: List[int]):
    return entries[0] * entries[1]


def multiply_entries_p2(entries: List[int]):
    return entries[0] * entries[1] * entries[2]


all_entries = sorted(get_entries(1))
entries_p1 = find_entries_that_sum_2020_p1(all_entries)
prod_entries_p1 = multiply_entries_p1(entries_p1)
entries_p2 = find_entries_that_sum_2020_p2(all_entries)
prod_entries_p2 = multiply_entries_p2(entries_p2)

print(prod_entries_p1)
print(prod_entries_p2)
