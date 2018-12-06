#!/usr/bin/python

# CALCULATION OF GC CONTENT (GENES)

import os
import logging
import argparse

import fastalib
from fileutils import safe_filename


def get_option_args():
    args_parser = argparse.ArgumentParser(
        description='Found GC in FASTA files of a directory',
        )
    args_parser.add_argument(
        'path',
        default='.',
        help='Path where look for FASTA files. Default is current working dir',
        )
    args_parser.add_argument(
        '--tron',
        dest='tron',
        action='store_const',
        const=True,
        default=False,
        help='Show trace of activity (Disabled by default)',
        )
    return args_parser.parse_args()


if __name__ == '__main__':
    args = get_option_args()
    genomes = [fn for fn in os.listdir(args.path) if fn.endswith(".faa")]
    for filename in genomes:
        if args.tron:
            logging.info('Processing {}'.format(filename))
        full_name = os.path.join(args.path, filename)
        data = fastalib.read_fasta_file(full_name)
        if args.tron:
            logging.info('Generating output files')
        for key in data:
            lines = data[key]
            filename = safe_filename('result_id_{}.fasta'.format(key))
            with open(filename, 'w') as f1:
                for l in lines:
                    f1.write('{}\n'.format(l))
            g, a, t, c = fastalib.count_nucleotydes_gatc(lines)
            filename = safe_filename('result_GC_{}.fasta'.format(key))
            with open(filename, 'w') as f2:
                f2.write('Guanine:  {:d}\n'.format(g))
                f2.write('Adenine:  {:d}\n'.format(a))
                f2.write('Thymine:  {:d}\n'.format(t))
                f2.write('Cytosine: {:d}\n'.format(c))
                p = round(float(c+g)/(a+c+g+t), 9)
                f2.write('CG proportion: {:9f}\n'.format(p))
        if args.tron:
            logging.info('Finished. {} files processed'.format(len(genomes)))
