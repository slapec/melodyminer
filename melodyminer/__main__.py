# coding: utf-8

import argparse
import sys

from aiohttp import web

from melodyminer.web.app import app

parser = argparse.ArgumentParser(
    description='melodyminer is a music organizing app'
)


def main():
    args = parser.parse_args()

    web.run_app(app)


if __name__ == '__main__':
    sys.exit(main())
