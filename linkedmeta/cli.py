#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
"""
linkedmeta
"""
import logging
import sys


class Schema:
    @staticmethod
    def load_from_path(path):
        return Schema()


def linkedmeta(*, schema, things):
    """prepare a linked meta-analysis

    Keyword Arguments:
        schema (str): URI or filepath (TODO: or Schema object)
        things (list): list of URIs (TODO: or Thing objects)

    Returns:
        str: ...

    Yields:
        str: ...

    Raises:
        Exception: ...
    """
    return 1


from pathlib import Path


def test_load_from_str():
    schemapath = Path(__file__).parent / "tests" / "schema1.yml"
    output = Schema.load_from_path(schemapath)
    assert output
    assert isinstance(output, Schema)


def test_linkedmeta():
    schema = 'example.org'
    things = ['#thing1', '#thing2']
    output = linkedmeta(schema=schema, things=things)
    assert output


def main(argv=None):
    """
    linkedmeta main() function

    Keyword Arguments:
        argv (list): commandline arguments (e.g. sys.argv[1:])
    Returns:
        int:
    """
    import optparse

    prs = optparse.OptionParser(
        usage="%prog : args")

    prs.add_option('-v', '--verbose',
                   dest='verbose',
                   action='store_true',)
    prs.add_option('-q', '--quiet',
                   dest='quiet',
                   action='store_true',)
    prs.add_option('-t', '--test',
                   dest='run_tests',
                   action='store_true',)


    argv = list(argv) if argv else []
    (opts, args) = prs.parse_args(args=argv)
    loglevel = logging.INFO
    if opts.verbose:
        loglevel = logging.DEBUG
    elif opts.quiet:
        loglevel = logging.ERROR
    logging.basicConfig(level=loglevel)
    log = logging.getLogger('main')
    log.debug('argv: %r', argv)
    log.debug('opts: %r', opts)
    log.debug('args: %r', args)

    if opts.run_tests:
        #sys.argv = [sys.argv[0]] + args
        #return unittest.main()
        import subprocess
        args = [__file__]
        return subprocess.call(['pytest', '-v'] + args)

    EX_OK = 0
    output = linkedmeta(schema, things)
    return EX_OK


if __name__ == "__main__":
    sys.exit(main(argv=sys.argv[1:]))
