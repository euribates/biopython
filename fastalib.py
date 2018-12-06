#!/usr/bin/env python

import collections


def read_fasta_file(filename):
    """Read a FASTA file, returns a dictionary.

    Thew content on every key is a list of strings.
    All letters are converted to uppercase.
    """
    result = collections.OrderedDict()
    with open(filename, 'r') as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            if line[0] == '>':
                key = line[1:]  # The > symbols don't add information
                result[key] = list()
            else:
                result[key].append(line.upper())
    return result


def count_nucleotydes_gatc(lines):
    """Read a secuence of nucleotyes and returns
    number of G/T/A/C found.
    """
    s = ''.join(lines)
    counter = collections.Counter(s)
    g = counter['G']
    a = counter['A']
    t = counter['T']
    c = counter['C']
    return (g, a, t, c)
