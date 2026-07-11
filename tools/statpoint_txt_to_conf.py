#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# This file is part of Hercules.
# http://herc.ws - http://github.com/HerculesWS/Hercules
#
# Copyright (C) 2026 Hercules Dev Team
#
# Hercules is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Convert legacy plain-text statpoint data to statpoint.conf."""

from __future__ import annotations

import argparse
from pathlib import Path


HEADER = """//================= Hercules Database =====================================
//=       _   _                     _
//=      | | | |                   | |
//=      | |_| | ___ _ __ ___ _   _| | ___  ___
//=      |  _  |/ _ \\ '__/ __| | | | |/ _ \\/ __|
//=      | | | |  __/ | | (__| |_| | |  __/\\__ \\
//=      \\_| |_/\\___|_|  \\___|\\__,_|_|\\___||___/
//================= License ===============================================
//= This file is part of Hercules.
//= http://herc.ws - http://github.com/HerculesWS/Hercules
//=
//= Copyright (C) 2026 Hercules Dev Team
//=
//= Hercules is free software: you can redistribute it and/or modify
//= it under the terms of the GNU General Public License as published by
//= the Free Software Foundation, either version 3 of the License, or
//= (at your option) any later version.
//=
//= This program is distributed in the hope that it will be useful,
//= but WITHOUT ANY WARRANTY; without even the implied warranty of
//= MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//= GNU General Public License for more details.
//=
//= You should have received a copy of the GNU General Public License
//= along with this program.  If not, see <http://www.gnu.org/licenses/>.
//================= Description ===========================================
//= Status point totals by base level.
//=========================================================================

statpoint_db: (
/**************************************************************************
 ************* Entry structure ********************************************
 **************************************************************************
{
	Level:       (int) Base level.
	StatusPoint: (int) Total status points at this base level.
}
**************************************************************************/
"""


def parse_rows(source: Path) -> list[tuple[int, int]]:
    rows: list[tuple[int, int]] = []

    for line_no, line in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
        data = line.split("//", 1)[0].strip()
        if not data:
            continue

        parts = data.replace(",", " ").split()
        if len(parts) != 1:
            raise ValueError(f"{source}:{line_no}: expected one numeric column")

        status_point = int(parts[0])
        rows.append((len(rows) + 1, status_point))

    return rows


def write_conf(rows: list[tuple[int, int]], target: Path) -> None:
    lines = [HEADER]
    for index, (level, status_point) in enumerate(rows):
        closing = "}," if index < len(rows) - 1 else "}"
        lines.extend(
            (
                "{",
                f"\tLevel: {level}",
                f"\tStatusPoint: {status_point}",
                closing,
            )
        )
    lines.append(")\n")
    target.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("target", type=Path)
    args = parser.parse_args()

    write_conf(parse_rows(args.source), args.target)


if __name__ == "__main__":
    main()
