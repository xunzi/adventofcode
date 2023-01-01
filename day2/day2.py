#!/usr/bin/env python3

# each choice only loses against its immediate successor

sum_overall = 0

rps = {
    "A": {"name": "rock", "points": 1, "loseagainst": "Y"},
    "B": {"name": "paper", "points": 2, "loseagainst": "Z"},
    "C": {"name": "scissors", "points": 3, "loseagainst": "X"},
    "X": {"name": "rock", "points": 1},
    "Y": {"name": "paper", "points": 2},
    "Z": {"name": "scissors", "points": 3},
}

rps2 = {
    "A": {"name": "rock", "points": 1, "loseagainst": "B"},
    "B": {"name": "paper", "points": 2, "loseagainst": "C"},
    "C": {"name": "scissors", "points": 3, "loseagainst": "A"},
    "X": 0,
    "Y": 3,
    "Z": 6,
}


sample_input = (["A", "Y"], ["B", "X"], ["C", "Z"])


def eval_choices(first, second):
    #
    if rps[first]["name"] == rps[second]["name"]:
        print(f"""{rps[first]['name']} is equal to {rps[second]['name']}""")
        return 3 + rps[second]["points"]
    elif rps[first]["loseagainst"] == second:
        print(f"""{rps[first]['name']} loses to {rps[second]['name']}""")
        return 6 + rps[second]["points"]
    else:
        print(f"""{rps[first]['name']} wins against {rps[second]['name']}""")
        return rps[second]["points"]


def find_loser(winner):
    for k in ["A", "B", "C"]:
        if rps2[k]["loseagainst"] == winner:
            return k


def eval2(first, second):
    if second == "Y":
        # print(f"""draw, {first}  equal to {first}""")
        return rps2[first]["points"] + rps2[second]
    elif second == "Z":
        loser = rps2[first]["loseagainst"]
        # print(f"""lose, {loser} loses against {first}""")
        return rps2[loser]["points"] + rps2[second]
    else:  # second is Z
        loser = find_loser(first)
        # print(f"""win, {first} wins against {loser}""")
        return rps2[loser]["points"] + rps2[second]


if __name__ == "__main__":
    for s in sample_input:
        sum_overall += eval_choices(s[0], s[1])
    # print(sum_overall)
    sum_overall = 0
    with open("day2-input.txt") as input:
        for line in input.readlines():
            line = line.strip()
            first, second = line.split()
            # print(first, second)
            i = eval_choices(first, second)
            # print(i)
            sum_overall += i
    print("Part1: ", sum_overall)
    sum2 = 0
    for s in sample_input:
        sum2 += eval2(s[0], s[1])
    # print("part2: ", sum2)
    sum2 = 0
    with open("day2-input.txt") as input:
        for line in input.readlines():
            line = line.strip()
            first, second = line.split()
            i = eval2(first, second)
            # print(i)
            sum2 += i

    print("Part2: ", sum2)
