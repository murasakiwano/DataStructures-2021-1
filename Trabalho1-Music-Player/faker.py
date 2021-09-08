#!/usr/bin/env python
from pprint import pprint
from pathlib import Path
import random, string

def randomword(length):
   letters = string.ascii_letters
   return ''.join(random.choice(letters) for i in range(length))

commands = [
    'play',
    'stop',
    'add',
    'del',
    'next',
    'list',
    'current',
    'undo',
    'ended',
]

# create directory to store fake tests
tests_dir = Path('fake_tests/')
tests_dir.mkdir(exist_ok=True)

for i in range(1, random.randint(50, 1e3)):
    print(f'Fake test #{i:04d}')
    musics = {randomword(random.randint(1, 10)) for _ in range(random.randint(500, 1e3))}
    musics = list(musics)

    with tests_dir.joinpath(f'{i:04d}.in').open('w') as f:
        for i in range(random.randint(10, 1e3)):
            command = random.choice(commands)
            if command in ['add', 'del', 'next']:
                command += ' ' + random.choice(musics)
            elif command == 'undo' and random.randint(0, 1):
                command += ' *'
            command += '\n'
            f.write(command)
        f.write('fight\n')
