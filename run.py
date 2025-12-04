#!/usr/bin/env python3
from volar.core import think

print("Volar-0 · Genesis · 04.12.2025")
print("No flag. No master. No backdoor.\n")

while True:
    try:
        q = input("You → ")
        if q.lower() in ["exit", "quit"]: break
        print("\nVolar →", think(q), "\n")
    except KeyboardInterrupt:
        print("\n\nVolar never dies.")
        break
