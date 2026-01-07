from pathlib import Path
import datetime as dt
import re

PRINT_PAPER = 40_000
SYMBOLS_PER_A4 = PRINT_PAPER / 24
REQUIRED_PRINT_PAPERS = 4.5
REQUIRED_A4 = REQUIRED_PRINT_PAPERS * 24

EXCLUDE_FILES = ["0_0_abstract.md"]
EXCLUDE_TEX = [
'frac', 'sqrt', 'left', 'right', 'big', 'Big', 'bigg', 'Bigg',
'text', 'mathrm', 'mathbf', 'mathit', 'mathcal', 'mathbb', 'boldsymbol',
'displaystyle', 'scriptstyle', 'scriptscriptstyle', 'limits', 'nolimits',
'operatorname', 'overline', 'underline', 'widehat', 'widetilde',
'quad', 'qquad', 'hspace', 'vspace',
'phantom', 'vphantom', 'hphantom',
'sum', 'int', 'prod', 'nabla', 'partial', 'delta', '{', '}', '\\', '^', '_',
'infty', 'lambda',
'overline', 'underline', 'label', '$$', '$', 'begin', 'aligned', 'left', 'right', 'langle', 'rangle',
'span data-section=',
]
EXCLUDE_RE = [r'>.*?\n']

args = {"path": "./content/"}

def count_symbols(file):
    with open(file, "r") as f:
        mdcontent = f.read()

    for exclude_parts in EXCLUDE_TEX:
        mdcontent = mdcontent.replace(exclude_parts, '')

    for exclude_re in EXCLUDE_RE:
        mdcontent = re.sub(exclude_re, '', mdcontent)
    # print(mdcontent)
    return len(mdcontent)


def count_workdays(start_date, end_date):
    """
    Count the number of workdays (Mon–Fri) between two dates, inclusive.
    """
    if isinstance(start_date, str):
        start_date = dt.datetime.strptime(start_date, "%Y-%m-%d").date()
    if isinstance(end_date, str):
        end_date = dt.datetime.strptime(end_date, "%Y-%m-%d").date()

    if start_date > end_date:
        start_date, end_date = end_date, start_date

    delta_days = (end_date - start_date).days + 1
    return sum((start_date + dt.timedelta(days=i)).weekday() < 5 for i in range(delta_days))


symbols = {file: count_symbols(file) for file in Path(args['path']).rglob("*.md")}
total_symbols = sum(count for file, count in symbols.items() if file.name not in EXCLUDE_FILES)

print(f"""Total {total_symbols} symbols
{total_symbols / SYMBOLS_PER_A4:.1f} / {REQUIRED_A4} pages ({total_symbols / SYMBOLS_PER_A4 / REQUIRED_A4 * 100:.0f}%)
""")

section_count = {}
SECTIONS = {'0_0': ('Annot', 2 * 0.13),
            '0_1': ('Intro', 0.13),
            '1': ('Backg', round(REQUIRED_PRINT_PAPERS * .2, 1)),
            '2': ('PDT m.', 0.6),
            '3': ('BeamSh', 0.8),
            '4': ('CircB', 0.5),
            '5': ('TimeC', 0.7),
            '6': ('Appl', 0.8),
            '7': ('Concl', 0.35),
           }

for file, count in symbols.items():
    for sec_num, v in SECTIONS.items():
        if file.name.startswith(sec_num):
            section_count[sec_num] = section_count.get(sec_num, 0) + count

for sec_num in sorted(section_count.keys()):
    count = section_count[sec_num]
    print(f"{SECTIONS[sec_num][0]}:\t {count / SYMBOLS_PER_A4:.1f} / {SECTIONS[sec_num][1] * 24:.1f} ({count / SYMBOLS_PER_A4 / SECTIONS[sec_num][1] / 24 * 100:.1f}%)")

print(f"""
At least {(REQUIRED_A4 - total_symbols / SYMBOLS_PER_A4) / count_workdays(dt.datetime.now().date(), "2026-01-14"):.1f} pages/day""")
