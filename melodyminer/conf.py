# coding: utf-8

import os
import importlib

os.environ.setdefault('MELODYMINER_SETTINGS', 'settings')
settings = importlib.import_module(os.environ['MELODYMINER_SETTINGS'])
