#!/usr/bin/env python3
"""One-line office joke entry for make.fun.

Competition: u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162
Writes a single one-line joke about office life to /output/entry.txt.
The joke was written by the agent in this session (see CANDIDATES.md
in the build workspace for the scored shortlist it was chosen from).
Chosen line (candidate B, 24/25): a concrete everyday setup — a calendar
so full the narrator books a meeting with himself just to eat lunch —
paid off by the surprise deadpan punch "and I declined it", which is
why it won the shortlist over the runner-up on punch and internal logic.

SPDX-License-Identifier: MIT
"""

import os

JOKE = "My calendar is so full I booked a meeting with myself just to eat lunch, and I declined it."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
