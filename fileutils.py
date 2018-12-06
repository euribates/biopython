#!/usr/bin/env python


def safe_filename(fn):
    fn = fn.replace(' ', '_')
    fn = fn.replace('/', '_')
    fn = fn.replace('\\', '_')
    return fn
