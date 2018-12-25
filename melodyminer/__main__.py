# coding: utf-8

import argparse
import asyncio
import logging
import sys

from melodyminer import __version__, commands

log = logging.getLogger('melodyminer')

parser = argparse.ArgumentParser(
    description='melodyminer is a music organizing app',
    prog='melodyminer'
)

parser.add_argument(
    '-v', '--version',
    action='version',
    version=f'%(prog)s {__version__}'
)

parser.add_argument(
    '-l', '--log-level',
    default='INFO',
    choices=('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'),
    help='Log level (alap: %(default)s)'
)

subparsers = parser.add_subparsers(
    title='Commands',
    dest='command'
)
subparsers.required = True

# setup ------------------------------------------------------------------------
parser_setup = subparsers.add_parser(
    'setup',
    help='Do initial app setup',
)
parser_setup.set_defaults(func=commands.setup)


# start ------------------------------------------------------------------------
parser_start = subparsers.add_parser(
    'start',
    help='Start the melodyminer server'
)
parser_start.set_defaults(func=commands.start)

parser_start.add_argument(
    '-H', '--host',
    help='Server IP to listen on (default: %(default)s)',
    default='0.0.0.0'
)

parser_start.add_argument(
    '-P', '--port',
    help='Server port to listen on (default: %(default)s)',
    type=int,
    default=9001
)


def main():
    args = parser.parse_args()

    stdout_handler = logging.StreamHandler(stream=sys.stdout)
    formatter = logging.Formatter('%(asctime)s | %(relativeCreated)d | %(levelname)-7s | %(message)s')
    stdout_handler.setFormatter(formatter)

    log_level: int = logging.getLevelName(args.log_level)
    log.setLevel(log_level)
    log.addHandler(stdout_handler)

    func = args.func

    if asyncio.iscoroutinefunction(func):
        log.debug('Executing %s in the event loop', func)
        return asyncio.run(func(args), debug=log_level == logging.DEBUG)
    else:
        log.debug('Executing %s', func)
        return func(args)


if __name__ == '__main__':
    sys.exit(main())
