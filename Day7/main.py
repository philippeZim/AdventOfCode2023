with open("input.txt", "r") as f:
    lines = [line.rstrip() for line in f]

card_val = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
            "7": 7, "8": 8, "9": 9, "T": 10, "J": 11,
            "Q": 12, "K": 13, "A": 14}

card_type = {"Five of a kind": 7,
             "Four of a kind": 6,
             "Full house": 5,
             "Three of a kind": 4,
             "Two pair": 3,
             "One pair": 2,
             "High card": 1}


def get_type(hand):
    d = dict()
    for x in hand:
        if x in d:
            d[x] = d[x] + 1
        else:
            d[x] = 1
    dl = len(d)
    if dl == 5:
        return "High card"
    if dl == 4:
        return "One pair"
    if dl == 3:
        for x in d:
            if d[x] == 3:
                return "Three of a kind"
        return "Two pair"
    if dl == 2:
        for x in d:
            if d[x] == 4:
                return "Four of a kind"
        return "Full house"
    return "Five of a kind"


def val_of_hand(hand1):
    res = 0
    no_bet = hand1.split()[0]
    type = card_type[get_type(no_bet)]
    res += type * 10_000_000_000

    cur_ind = 1
    for i in range(5):
        res += cur_ind * card_val[no_bet[-1 - i]]
        cur_ind *= 100
    return res


lines = sorted(lines, key=val_of_hand)
res_part1 = 0
for i in range(len(lines)):
    el = int(lines[i].split()[1])
    res_part1 += (i + 1) * el
print(res_part1)

# Part 2

card_val2 = {"J": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
             "7": 7, "8": 8, "9": 9, "T": 10,
             "Q": 11, "K": 12, "A": 13}


def find_best(hand):
    if hand == "JJJJJ":
        return "AAAAA"
    d = dict()
    for x in hand:
        if x in d:
            d[x] = d[x] + 1
        else:
            d[x] = 1
    max_card = ""
    for x in d:
        if x != "J":
            if d[x] > d.get(max_card, 0):
                max_card = x
    res = ""
    for x in hand:
        if x == "J":
            res += max_card
        else:
            res += x
    return res



def get_type2(hand):
    if "J" in hand:
        hand = find_best(hand)
    d = dict()
    for x in hand:
        if x in d:
            d[x] = d[x] + 1
        else:
            d[x] = 1
    dl = len(d)
    if dl == 5:
        return "High card"
    if dl == 4:
        return "One pair"
    if dl == 3:
        for x in d:
            if d[x] == 3:
                return "Three of a kind"
        return "Two pair"
    if dl == 2:
        for x in d:
            if d[x] == 4:
                return "Four of a kind"
        return "Full house"
    return "Five of a kind"


def val_of_hand2(hand1):
    res = 0
    no_bet = hand1.split()[0]
    type = card_type[get_type2(no_bet)]
    res += type * 10_000_000_000

    cur_ind = 1
    for i in range(5):
        res += cur_ind * card_val2[no_bet[-1 - i]]
        cur_ind *= 100
    return res


with open("input.txt", "r") as f:
    lines = [line.rstrip() for line in f]


lines = sorted(lines, key=val_of_hand2)
res_part2 = 0
for i in range(len(lines)):
    el = int(lines[i].split()[1])
    res_part2 += (i + 1) * el
print(res_part2)