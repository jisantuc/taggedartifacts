#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `pyrepro` package."""

import glob
import os

import unittest

from pyrepro import Artifact


@Artifact('outpath')
def func(outpath):
    with open(outpath, 'w') as outf:
        outf.write('good job')


@Artifact('lol')
def func2(outpath):
    with open(outpath, 'w') as outf:
        outf.write('good job')


class TestPyrepro(unittest.TestCase):
    """Tests for `pyrepro` package."""

    def setUp(self):
        files = glob.glob('foo*.txt')
        for f in files:
            os.remove(f)

    def tearDown(self):
        files = glob.glob('foo*.txt')
        for f in files:
            os.remove(f)

    def test_create_file(self):
        func(outpath='foo.txt')
        files = glob.glob('foo*.txt')
        assert len(files) == 1
        assert 'foo.txt' not in files

    def test_assert_for_bad_keyword(self):
        with self.assertRaises(KeyError):
            func2(outpath='foo.txt')
