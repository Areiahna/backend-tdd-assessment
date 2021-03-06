#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Areiahna Cooks & Demo"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(
        description='Perform transformation on input text.')
    parser.add_argument('text', help='text to be manipulated')
    parser.add_argument('-u', '--upper', action='store_true',
                        help='convert text to uppercase')
    parser.add_argument('-l', '--lower', action='store_true',
                        help='convert text to lowercase')
    parser.add_argument('-t', '--title', action='store_true',
                        help='convert text to titlecase')

    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    ns = parser.parse_args(args)
    msg = ns.text
    if ns.upper:
        msg = msg.upper()
    if ns.lower:
        msg = msg.lower()
    if ns.title:
        msg = msg.title()
    # print(ns)
    print(msg)


if __name__ == '__main__':
    main(sys.argv[1:])
