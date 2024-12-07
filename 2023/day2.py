#!/usr/bin/env python3


import string
import aoclib
import re
sum = 0

max_vals = {
    'red': 12,
    'green': 13,
    'blue': 14
    }

args = aoclib.handle_args(description="AOC 2023 day 2")
if args.debug:
    aoclib.debug = True

gamesum = 0

if args.test:
    infilename = f"input/day{args.day}.{args.part}test"
else:
    infilename = f"input/day{args.day}"


def split_game_runs(line):
    game, runs = line.split(':')
    game = game.split()[1]
    runs = runs.split(';')
    return {int(game): [x.strip() for x in runs]}

def check_colorcounter(run):
    pattern = re.compile(r'\s*(\d+)\s(\w+)')
    res = True
    match = pattern.findall(run)
    for m in match:
        if int(m[0]) > max_vals[m[1]]:
            res = False
    return res


def find_highest_color_value(run):
    color_dict = {
    }
    pattern = re.compile(r'\s*(\d+)\s(\w+)')
    match = pattern.findall(run)
    for m in match:
        ccount = color_dict.get(m[1], int(m[0]))
        if int(m[0]) > int(ccount):
            color_dict[m[1]] = int(m[0])
    return color_dict

def product(color_dict):
    ret = 1
    for k in color_dict.keys():
        if color_dict[k] != 0:
            ret *= color_dict[k]
    return ret


if __name__ == "__main__":
    match args.part:
        case "1":
            with open(infilename) as infile:
                for line in infile.readlines():
                    gamecolors = split_game_runs(line.strip())
                    print(gamecolors)
                    for game, runs in gamecolors.items():
                        for run in runs:
                            if(not check_colorcounter(run)):
                                print(f"{run} is False")
                                break
                            print(f"{run} is True")
                        else:
                            print(f"{gamesum} + {game}")
                            gamesum += game
            print(gamesum)

        case "2":
            with open(infilename) as infile:
                for line in infile.readlines():
                    gamecolors = split_game_runs(line.strip())
                    for game, runs in gamecolors.items():
                        for run in runs:
                            colors = find_highest_color_value(run)
                            print(run)
                            print(colors)
                            p = product(colors)
                            print(p)
                            gamesum += p
            print(gamesum)
                            
