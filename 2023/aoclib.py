import argparse
import sys

debug = False

def handle_args(description):
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--day", "-d", help="day of aoc", required=True)
    parser.add_argument("--part", "-p", help="part", required=True)
    parser.add_argument("--test", "-t", default=False, action="store_true")
    parser.add_argument("--debug", "-D", default=False, action="store_true")
    args = parser.parse_args()
    return args

def debugprint(msg):
    if debug:
        sys.stdout.write(f"DEBUG: {msg}\n")


words2digit = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
    }
words2teens = {
    "ten": "10",
    "eleven": "11",
    "twelve": "12",
    "thirteen": "13",
    "fourteen": "14",
    "fifteen": "15",
    "sixteen": "16",
    "seventeen": "17",
    "eighteen": "18",
    "nineteen": "19"
    }
        
if __name__ == "__main__":
    pass
