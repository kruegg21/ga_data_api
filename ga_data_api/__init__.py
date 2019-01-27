# -*- coding: utf-8 -*-

"""Top-level package for GA Data API."""
import logging
import os


__author__ = """yes"""
__email__ = 'Kurt Bergen Ruegg'
__version__ = '0.1.7'


logging.basicConfig(level=logging.DEBUG,
                    filename=os.path.join(os.path.dirname(__file__),
                                          'logs', 'debug.log'),
                    filemode='a+',
                    format='%(asctime)-15s %(levelname)-8s %(message)s')
