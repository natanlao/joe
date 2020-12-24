"""
Parses a Signal backup CSV, returning message content for a given `ADDRESS`
id.

See https://github.com/xeals/signal-back for help generating a CSV.

Retained for propriety -- this ended up not working nicely since some messages
in a conversation contained both messages sent and received under the same
ADDRESS. See signal_extract.sh for the workaround.
"""
import argparse
import csv
import pathlib
from typing import (
    Sequence,
)


def filter_csv(csvfile: pathlib.Path, target: str, **filters) -> Sequence[str]:
    with csvfile.open('r') as fh:
        reader = csv.DictReader(fh)
        return [row[target] for row in reader
                if filters.items() <= row.items()]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('csv_file',
                        help='Path to CSV dump of Signal backup')
    parser.add_argument('address',
                        help='Value of the ADDRESS column.')
    arguments = parser.parse_args()
    csvfile = pathlib.Path(arguments.csv_file)
    messages = filter_csv(csvfile, 'BODY', ADDRESS=arguments.address)
    print('\n'.join(messages))
