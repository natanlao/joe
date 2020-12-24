import random
import time
from pathlib import Path
from typing import Sequence

from flask import Flask, render_template, request
from jinja2 import StrictUndefined


app = Flask(__name__, static_url_path='')
app.jinja_env.undefined = StrictUndefined
observations_dir = Path(__file__).resolve().parent / 'observations'


@app.context_processor
def available_personas():
    return {
        'personas': [f.stem for f in observations_dir.glob('*.txt')],
        'name': ''  # messy: overriden by render_template
    }


@app.route('/', methods=['GET', 'POST'])
def generate_wisdom():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        name = request.form['name']
        wisdom = curate_wisdom(name, 10)
        # server wait is bad but this is more realistic
        time.sleep(random.randrange(7))
        return render_template('index.html',
                               wisdom=format_wisdom(wisdom, name),
                               name=request.form['name'])


def curate_wisdom(name: str, amount: int) -> str:
    """
    Choose `amount` contiguous lines from f'{name}.txt'
    """
    observations_file = observations_dir / f'{name}.txt'
    if not observations_file.exists():
        raise ValueError(f'No such file {observations_file.as_posix()}')
    else:
        with observations_file.open('r') as fh:
            observations = fh.read().splitlines()
        cutoff = len(observations) - amount
        index = random.randrange(cutoff)
        return observations[index:index + amount]


def format_wisdom(strs: Sequence[str], name: str) -> str:
    return '<br><br>'.join([f'<strong>{name.upper()}</strong>: {s}' for s in strs])

