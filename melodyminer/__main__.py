# coding: utf-8

import argparse
import asyncio
import logging
import sys
from pathlib import Path

import melodyminer.media.commands
from melodyminer import __version__, commands, db
from melodyminer.conf import settings

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

# media ------------------------------------------------------------------------
parser_media = subparsers.add_parser(
    'media',
    help='CLI tools for media management',
    description='CLI tools for media management'
)
parser_media.set_defaults(func=lambda x: parser_media.print_help())

media_subparsers = parser_media.add_subparsers()

parser_media_import = media_subparsers.add_parser(
    'import',
    help='Import an audio file into the storage'
)
parser_media_import.set_defaults(func=melodyminer.media.commands.import_)

parser_media_import.add_argument(
    'paths',
    help='File path or paths',
    type=Path,
    nargs='+'
)


def main():
    args = parser.parse_args()

    stdout_handler = logging.StreamHandler(stream=sys.stdout)
    formatter = logging.Formatter('%(asctime)s | %(relativeCreated)d | %(levelname)-7s | %(message)s')
    stdout_handler.setFormatter(formatter)

    log_level: int = logging.getLevelName(args.log_level)
    log.setLevel(log_level)
    log.addHandler(stdout_handler)

    func = getattr(args, 'func', None)

    if asyncio.iscoroutinefunction(func):
        log.debug('Executing %s in the event loop', func)

        async def wrapper():
            log.debug('Connecting to the database')
            await db.set_bind(settings.DATABASE_DSN)

            return await func(args)

        return asyncio.run(wrapper(), debug=log_level == logging.DEBUG)

    elif callable(func):
        return func(args)

    else:
        raise NotImplementedError(func)


if __name__ == '__main__':
    sys.exit(main())
