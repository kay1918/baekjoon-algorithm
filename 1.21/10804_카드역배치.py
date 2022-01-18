import sys

section = []
cards = []
for i in range(1,21):
    cards.append(i)

for _ in range(10):
    pair = list(map(int, sys.stdin.readline().split()))
    section.append(pair)

for pair in section:
    cards[pair[0]-1:pair[1]] = list(reversed(cards[pair[0]-1:pair[1]]))

print(*cards)