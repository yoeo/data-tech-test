#!/usr/bin/env python3

"""Create a segment with fake data"""

from argparse import ArgumentParser
from datetime import datetime
import json
from pathlib import Path
import random


random.seed()

USERS_FILE = 'users.segment'
STREAMS_FILE = 'streams.segment'
NAMES_FILE = 'names.txt'

CUR_DIR = Path(__file__).absolute().parent
DATADIR = CUR_DIR.absolute().parent.joinpath('data')
NAMES = CUR_DIR.joinpath(NAMES_FILE).read_text().lower().split()
LANGUAGES = 'ar en fr pt'.split()
COUNTRIES = 'ES FR GB MA BR'.split()
SERVERS = 'gmail.com hotmail.com yahoo.com'.split()

BASE_DATE = datetime.fromisoformat('2019-06-01T00:00:00+00:00')
BASE_TS = BASE_DATE.timestamp() * 1000
ONE_DAY = 1000 * 60 * 60 * 24
NB_DAYS = 30

NB_ARTISTS = 10


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument(
        '-u',
        dest='users',
        default=100,
        type=int,
        help='number of users to generate',
    )
    parser.add_argument(
        '-a',
        dest='artists',
        default=10,
        type=int,
        help='number of artists streamed',
    )
    parser.add_argument(
        '-s',
        dest='streams',
        default=10000,
        type=int,
        help='max number of streams to generate',
    )
    parser.add_argument(
        'destination',
        default=str(DATADIR),
        help='directory where the generated files will be stored',
    )
    args = parser.parse_args()

    destination = Path(args.destination).absolute()
    user_ids = list(range(1, 1+args.users))
    random.shuffle(user_ids)

    user_reg = {}
    users_path = destination.joinpath(USERS_FILE)
    with users_path.open('w') as output_file:
        for user_id in user_ids:
            name = random.choice(NAMES)
            server = random.choice(SERVERS)
            registration = rand_day()
            user = {
                'user_id': user_id,
                'username': name,
                'language': random.choice(LANGUAGES),
                'country': random.choice(COUNTRIES),
                'email': f'fake.{name}@{server}',
                'consent': random.choice(range(10)) != 0,
                'registration': registration,
            }
            json.dump(user, output_file)
            output_file.write('\n')
            user_reg[user['user_id']] = user['registration']

    streams_path = destination.joinpath(STREAMS_FILE)
    with streams_path.open('w') as output_file:
        for _ in range(1, 1+args.streams):
            user_id = random.randint(1, args.users)
            artist_id = random.randint(1, args.artists)
            stream_time = rand_day() + random.randint(0, ONE_DAY)
            if stream_time < user_reg[user_id]:
                continue

            stream = {
                'user_id': user_id,
                'artist_id': artist_id,
                'stream_time': stream_time,
            }
            json.dump(stream, output_file)
            output_file.write('\n')

    print(f"Done, check: {destination}")


def rand_day():
    return int(BASE_TS+random.randint(0, NB_DAYS)*ONE_DAY)


if __name__ == '__main__':
    main()
