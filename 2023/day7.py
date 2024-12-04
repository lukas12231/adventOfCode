from itertools import combinations_with_replacement


def evaluate_card(card: str, c: [str]):
    best = 1
    for check in c:
        count = card.count(check)
        if count == 5:
            best = 7
            break
        if count == 4:
            best = max(best, 6)
        if count == 3:
            if any([True for rem in c if rem != check and card.count(rem) == 2]):
                best = max(best, 5)
            else:
                best = max(best, 4)
        if count == 2:
            if any([True for rem in c if rem != check and card.count(rem) == 2]):
                best = max(best, 3)
            else:
                best = max(best, 2)
    return best

def calc_output(winners: list):
    
    winners = sorted(winners, key=lambda x: x[0])
    idx = len(winners)
    o = 0
    for y in reversed(range(8)):
        tmp  = sorted([x for x in winners if x[0] == y], key=lambda x: x[3])
        for x in tmp:
            o += idx * x[1]
            idx -= 1
    return o

with open("input.txt") as f:
    cards = [x.split(" ") for x in f.readlines()]

# part 1
c = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
winners = []
for card, win in cards:
    best = evaluate_card(card, c)
    winners.append((best, int(win), card, [c.index(x) for x in card]))
print(calc_output(winners))

# part 2
c = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

winners = []
for card, win in cards:
    amt = len([1 for x in card if "J" in x[0]])
    best = 0
    if amt > 0:
        for comb in combinations_with_replacement(c[:-1], amt):
            new_card = card
            for id in range(amt):
                a = new_card.index("J")
                new_card= new_card[:a] + comb[id] + new_card[a+1:]
            best = max(best, evaluate_card(new_card, c))
    else:
        best = evaluate_card(card, c)
    winners.append((best, int(win), card, [c.index(x) for x in card]))

print(calc_output(winners))
