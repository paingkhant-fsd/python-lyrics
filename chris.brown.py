import sys
from rich import print
from time import sleep
import time

def printlyrics():
    lines = [
        ('"Baby, who cares?" ', 0.08),
        ("But I know you care", 0.12),
        ("Bring it over to my place", 0.09),
        ("You don't know what you did       ", 0.06),
        ("did to me", 0.15),
        ("Your body lightweight", 0.09),
        ("speaks to me  ", 0.14),
    ]

    for text, delay in lines:
        for char in text:
            print(f"[#ffce1f]{char}[/#ffce1f]", end="", flush=True)
            time.sleep(delay)
        print()

printlyrics()